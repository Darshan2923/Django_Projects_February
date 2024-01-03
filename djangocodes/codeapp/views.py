from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import *
# Create your views here.
def index(request):
    posts = BlogPost.objects.all()
    posts = BlogPost.objects.filter().order_by('-datetime')
    context={'posts':posts}
    return render(request,'codeapp/index.html',context)

# User authentication
def register_page(request):
    if request.method=="POST":   
        username = request.POST['username']
        email = request.POST['email']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if User.objects.filter(username = username).first():
            messages.error(request, "This username is already taken")
            return redirect('index')
        
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('/register')
        
        user = User.objects.create_user(username, email, password1)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return render(request, 'codeapp/login_page.html')   
    return render(request,'codeapp/register_page.html')


def login_page(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("/")
        else:
            messages.error(request, "Invalid Credentials")
        return render(request, 'codeapp/index.html')  
    return render(request,'codeapp/login_page.html')


def logout_user(request):
    logout(request)
    return redirect('/login/')

