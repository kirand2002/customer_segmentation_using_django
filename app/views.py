from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Signup, AdminLogin, FAQ

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

def predict(request):
    return render(request, 'predict.html')


def user_view_faq(request):
    faqs = FAQ.objects.all()
    return render(request, 'userviewfaq.html', {'faqs': faqs})


