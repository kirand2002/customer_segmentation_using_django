from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Signup, AdminLogin, FAQ
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64
from sklearn.tree import DecisionTreeRegressor
from sklearn.cluster import KMeans
from django.contrib import messages
from django.core.files.storage import default_storage

def index(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'aboutus.html')

def contact(request):
    return render(request, 'contact.html')

def signup(request):
    
    if request.method == 'POST':
        uname = request.POST.get('uname')
        uphone = request.POST.get('uphone')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        if uname and uphone and username and password:
            Signup.objects.create(uname=uname, uphone=uphone, username=username, password=password)
            messages.success(request, ("Your Account Have Been Created Succesfully  ..!"))
            redirect('index')
        else:
            messages.success(request, ("Sorry Somthing Went Worng  ..!"))
            
    return render(request, 'signup.html', {})

def user_login(request):
   
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = Signup.objects.filter(username=username, password=password).first()
        if user:
            request.session['username'] = username
            messages.success(request, ("You Have Been Logged In Succesfully  ..!"))

            return redirect('userhome')
        else:
            messages.success(request, ("Sorry Invalid Username or Password ..!"))
    return render(request, 'userlogin.html', {})

def admin_login(request):
    
    if request.method == 'POST':
        ausername = request.POST.get('ausername')
        apassword = request.POST.get('apassword')
        admin = AdminLogin.objects.filter(ausername=ausername, apassword=apassword).first()
        if admin:
            request.session['admin'] = ausername
            messages.success(request, ("You Have Been Logged In Succesfully  ..!"))
            
            return redirect('adminhome')
        else:
            messages.success(request, ("Sorry Invalid Username or Password ..!"))
    return render(request, 'adminlogin.html', {})

def user_home(request):
    return render(request, 'userhome.html')

def admin_home(request):
    return render(request, 'adminhome.html')

def admin_view_users(request):
    users = Signup.objects.all()
    return render(request, 'adminviewusers.html', {'users': users})

def admin_view_faq(request):
    faqs = FAQ.objects.all()
    return render(request, 'adminviewfaq.html', {'faqs': faqs})

def add_faq(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        answer = request.POST.get('answer')
        FAQ.objects.create(question=question, answer=answer)
        return redirect('adminviewfaq')
    return render(request, 'addfaq.html')

def logout_view(request):
    logout(request)
    messages.success(request, ("You Have Been Succesfully Logged Out ..!"))
    return redirect('index')


def user_view_faq(request):
    faqs = FAQ.objects.all()
    return render(request, 'userviewfaq.html', {'faqs': faqs})



def segmentation(request):
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        df = pd.read_csv(uploaded_file)

        main_col = request.POST.get('main_col')
        index_col = request.POST.get('index_col')

        # Validate Columns
        if main_col not in df.columns or index_col not in df.columns:
            return render(request, 'segmentation.html', {'error': 'Invalid column names provided.'})

        # Convert non-numeric columns to NaN and drop rows with NaN
        df = df.apply(pd.to_numeric, errors='coerce')
        df.dropna(inplace=True)

        # Ensure DataFrame is not empty after cleaning
        if df.empty:
            return render(request, 'segmentation.html', {'error': 'No valid numeric data available after cleaning.'})

        # Select numeric features only
        features = [col for col in df.columns if col not in [index_col, main_col]]

        # Ensure at least one feature exists
        if not features:
            return render(request, 'segmentation.html', {'error': 'Not enough numeric features for segmentation.'})

        # Train Decision Tree Regressor
        estimator = DecisionTreeRegressor().fit(df[features], df[main_col])
        feature_importance = {feature: round(importance, 4) for feature, importance in zip(features, estimator.feature_importances_)}

        # Apply KMeans Clustering
        df['cluster'] = KMeans(n_clusters=4, random_state=42).fit_predict(df[features])

        # Generate Feature Importance Plot
       
        plt.figure(figsize=(10, 5))  # Increase figure size
        sns.barplot(x=list(feature_importance.keys()), y=list(feature_importance.values()), palette='coolwarm')

        plt.xlabel("Features")
        plt.ylabel("Importance Score")
        plt.title("Feature Importance")

        plt.xticks(rotation=45, ha="right")  # Rotate and align labels
        plt.tight_layout()  # Adjust layout to prevent cutoff

        buf = BytesIO()
        plt.savefig(buf, format="png", bbox_inches="tight")  # Ensures labels fit
        buf.seek(0)
        feature_importance_plot = base64.b64encode(buf.getvalue()).decode("utf-8")
        buf.close()
        plt.close()

        # Generate Clustering Scatter Plot (Only if at least 2 features)
        cluster_plot = None
        if len(features) >= 2:
            plt.figure(figsize=(8, 5))
            sns.scatterplot(x=df[features[0]], y=df[features[1]], hue=df['cluster'], palette='viridis', s=100)
            plt.xlabel(features[0])
            plt.ylabel(features[1])
            plt.title("Customer Segmentation Clusters")
            buf = BytesIO()
            plt.savefig(buf, format="png")
            buf.seek(0)
            cluster_plot = base64.b64encode(buf.getvalue()).decode("utf-8")
            buf.close()
            plt.close()

        # Store results in session and redirect
        request.session['feature_importance_plot'] = feature_importance_plot
        request.session['cluster_plot'] = cluster_plot
        request.session['feature_importance'] = feature_importance

        return redirect('segmentationresults')  # Redirect to new results page

    return render(request, 'segmentation.html')


def segmentationresults(request):
    # Retrieve stored session data
    feature_importance_plot = request.session.get('feature_importance_plot')
    cluster_plot = request.session.get('cluster_plot')
    feature_importance = request.session.get('feature_importance')

    if not feature_importance_plot or not cluster_plot:
        return redirect('segmentation')

    return render(request, 'segmentationresults.html', {
        'feature_importance_plot': feature_importance_plot,
        'cluster_plot': cluster_plot,
        'feature_importance': feature_importance
    })



def segmentation_cols(request):
    
    columns = []  # Initialize empty list for dropdowns

    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        df = pd.read_csv(uploaded_file)

        # Extract column names for dropdown
        columns = list(df.columns)

        main_col = request.POST.get('main_col')
        index_col = request.POST.get('index_col')

        # Validate Columns
        if main_col not in df.columns or index_col not in df.columns:
            return render(request, 'segmentation.html', {'error': 'Invalid column names provided.', 'columns': columns})

        # Convert non-numeric columns to NaN and drop rows with NaN
        df = df.apply(pd.to_numeric, errors='coerce')
        df.dropna(inplace=True)

        # Ensure DataFrame is not empty after cleaning
        if df.empty:
            return render(request, 'segmentation.html', {'error': 'No valid numeric data available after cleaning.', 'columns': columns})

        # Select numeric features only
        features = [col for col in df.columns if col not in [index_col, main_col]]

        # Ensure at least one feature exists
        if not features:
            return render(request, 'segmentation.html', {'error': 'Not enough numeric features for segmentation.', 'columns': columns})

        # Store columns in session for pre-filling dropdowns
        request.session['columns'] = columns

        # Pass columns back to the template for re-selection
        return render(request, 'segmentation.html', {'columns': columns})

    return render(request, 'segmentation.html', {'columns': columns})





