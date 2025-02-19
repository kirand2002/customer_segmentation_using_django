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
def index(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'aboutus.html')

def contact(request):
    return render(request, 'contact.html')

def signup(request):
    msg = None
    if request.method == 'POST':
        uname = request.POST.get('uname')
        uphone = request.POST.get('uphone')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        if uname and uphone and username and password:
            Signup.objects.create(uname=uname, uphone=uphone, username=username, password=password)
            msg = "Your account is created"
        else:
            msg = "Something went wrong"
    return render(request, 'signup.html', {'msg': msg})

def user_login(request):
    msg = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = Signup.objects.filter(username=username, password=password).first()
        if user:
            request.session['username'] = username
            return redirect('userhome')
        else:
            msg = "Invalid username or password"
    return render(request, 'userlogin.html', {'msg': msg})

def admin_login(request):
    msg = None
    if request.method == 'POST':
        ausername = request.POST.get('ausername')
        apassword = request.POST.get('apassword')
        admin = AdminLogin.objects.filter(ausername=ausername, apassword=apassword).first()
        if admin:
            request.session['admin'] = ausername
            return redirect('adminhome')
        else:
            msg = "Invalid username or password"
    return render(request, 'adminlogin.html', {'msg': msg})

def user_home(request):
    return render(request, 'userhome.html')

def admin_home(request):
    return render(request, 'adminhome.html')

def logout_view(request):
    request.session.flush()
    return redirect('index')


def admin_login_next(request):
    msg = None
    if request.method == 'POST':
        ausername = request.POST.get('ausername')
        apassword = request.POST.get('apassword')
        
        print(f"Received: {ausername}, {apassword}")  # Debugging output
        
        admin = AdminLogin.objects.filter(ausername=ausername, apassword=apassword).first()

        if admin:
            print("Login successful!")  # Debugging output
            request.session['admin'] = ausername  # Store session
            return redirect('adminhome')  # Redirect to admin dashboard
        else:
            print("Login failed!")  # Debugging output
            msg = "Invalid username or password"

    return render(request, 'adminlogin.html', {'msg': msg})  # Reloads login page if invalid

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
    return redirect('index')


def user_view_faq(request):
    faqs = FAQ.objects.all()
    return render(request, 'userviewfaq.html', {'faqs': faqs})


# import pandas as pd
# from django.shortcuts import render
# from sklearn.tree import DecisionTreeRegressor
# from sklearn.cluster import KMeans

# def segmentation(request):
#     if request.method == 'POST' and request.FILES.get('file'):
#         uploaded_file = request.FILES['file']
#         df = pd.read_csv(uploaded_file)

#         main_col = request.POST.get('main_col')
#         index_col = request.POST.get('index_col')

#         # Validate Columns
#         if main_col not in df.columns or index_col not in df.columns:
#             return render(request, 'segmentation.html', {'error': 'Invalid column names provided.'})

#         # Convert all non-numeric columns except main_col to numeric
#         df = df.apply(pd.to_numeric, errors='coerce')

#         # Drop rows with NaN values that couldn't be converted
#         df.dropna(inplace=True)

#         # Select numeric features only
#         features = [col for col in df.columns if col not in [index_col, main_col]]

#         # Ensure at least one feature exists
#         if not features:
#             return render(request, 'segmentation.html', {'error': 'Not enough numeric features for segmentation.'})

#         # Train Decision Tree Regressor
#         estimator = DecisionTreeRegressor().fit(df[features], df[main_col])
#         feature_importance = {feature: round(importance, 4) for feature, importance in zip(features, estimator.feature_importances_)}

#         # Apply KMeans Clustering
#         df['cluster'] = KMeans(n_clusters=4, random_state=42).fit_predict(df[features])

#         # Convert results to JSON-friendly format
#         cluster_assignments = df[['cluster']].to_dict(orient='records')

#         return render(request, 'segmentation.html', {
#             'feature_importance': feature_importance,
#             'cluster_assignments': cluster_assignments
#         })

#     return render(request, 'segmentation.html')


# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# from io import BytesIO
# import base64
# from django.shortcuts import render
# from sklearn.tree import DecisionTreeRegressor
# from sklearn.cluster import KMeans

# def segmentation(request):
#     if request.method == 'POST' and request.FILES.get('file'):
#         uploaded_file = request.FILES['file']
#         df = pd.read_csv(uploaded_file)

#         main_col = request.POST.get('main_col')
#         index_col = request.POST.get('index_col')

#         # Validate Columns
#         if main_col not in df.columns or index_col not in df.columns:
#             return render(request, 'segmentation.html', {'error': 'Invalid column names provided.'})

#         # Convert non-numeric columns to NaN and drop rows with NaN
#         df = df.apply(pd.to_numeric, errors='coerce')
#         df.dropna(inplace=True)

#         # Ensure DataFrame is not empty after cleaning
#         if df.empty:
#             return render(request, 'segmentation.html', {'error': 'No valid numeric data available after cleaning.'})

#         # Select numeric features only
#         features = [col for col in df.columns if col not in [index_col, main_col]]

#         # Ensure at least one feature exists
#         if not features:
#             return render(request, 'segmentation.html', {'error': 'Not enough numeric features for segmentation.'})

#         # Train Decision Tree Regressor
#         estimator = DecisionTreeRegressor().fit(df[features], df[main_col])
#         feature_importance = {feature: round(importance, 4) for feature, importance in zip(features, estimator.feature_importances_)}

#         # Apply KMeans Clustering
#         df['cluster'] = KMeans(n_clusters=4, random_state=42).fit_predict(df[features])

#         # **Generate Feature Importance Plot**
#         plt.figure(figsize=(8, 5))
#         sns.barplot(x=list(feature_importance.keys()), y=list(feature_importance.values()), palette='coolwarm')
#         plt.xlabel("Features")
#         plt.ylabel("Importance Score")
#         plt.title("Feature Importance")
#         plt.xticks(rotation=45)
#         buf = BytesIO()
#         plt.savefig(buf, format="png")
#         buf.seek(0)
#         feature_importance_plot = base64.b64encode(buf.getvalue()).decode("utf-8")
#         buf.close()
#         plt.close()

#         # **Generate Clustering Scatter Plot (Only if at least 2 features)**
#         cluster_plot = None
#         if len(features) >= 2:
#             plt.figure(figsize=(8, 5))
#             sns.scatterplot(x=df[features[0]], y=df[features[1]], hue=df['cluster'], palette='viridis', s=100)
#             plt.xlabel(features[0])
#             plt.ylabel(features[1])
#             plt.title("Customer Segmentation Clusters")
#             buf = BytesIO()
#             plt.savefig(buf, format="png")
#             buf.seek(0)
#             cluster_plot = base64.b64encode(buf.getvalue()).decode("utf-8")
#             buf.close()
#             plt.close()

#         return render(request, 'segmentation.html', {
#             'feature_importance_plot': feature_importance_plot,
#             'cluster_plot': cluster_plot
#         })

#     return render(request, 'segmentation.html')


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64
from django.shortcuts import render, redirect
from sklearn.tree import DecisionTreeRegressor
from sklearn.cluster import KMeans

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
        plt.figure(figsize=(8, 5))
        sns.barplot(x=list(feature_importance.keys()), y=list(feature_importance.values()), palette='coolwarm')
        plt.xlabel("Features")
        plt.ylabel("Importance Score")
        plt.title("Feature Importance")
        plt.xticks(rotation=45)
        buf = BytesIO()
        plt.savefig(buf, format="png")
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




