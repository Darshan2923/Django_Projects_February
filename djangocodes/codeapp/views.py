from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
# Create your views here.

# blogs
def index(request):
    posts = BlogPost.objects.all()
    posts = BlogPost.objects.filter().order_by('-datetime')
    context={'posts':posts}
    return render(request,'codeapp/index.html',context)

@login_required(login_url='/login')
def add_blogs(request):
    form=BlogPostForm()
    if request.method=='POST':
        form = BlogPostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            blogpost = form.save(commit=False)
            blogpost.author = request.user
            blogpost.save()
            return redirect('/')
        else:
            form=BlogPostForm()
    return render(request,'codeapp/add_blogs.html',{'form':form})

@login_required(login_url='/login')
def delete_blogs(request,slug):
    posts=BlogPost.objects.get(slug=slug)
    if request.method=='POST':
        posts.delete()
        return redirect('/')
    return render(request,'codeapp/delete.html',{'posts':posts})

def blogs_comments(request, slug):
    # Fetch the BlogPost object based on the provided slug
    post = BlogPost.objects.filter(slug=slug).first()
    # Fetch all comments associated with the retrieved blog post
    comments = Comment.objects.filter(blog=post)
    # Check if the incoming request method is POST
    if request.method == 'POST':
        # If it is a POST request, extract the user and comment content from the form
        user = request.user
        content = request.POST.get('content', '')
        # Create a new Comment object with the extracted user, content, and associated blog post
        comment = Comment(user=user, content=content, blog=post)   
        # Save the new comment to the database
        comment.save()
    # Render the 'blog_comments.html' template with the comments and the retrieved blog post
    return render(request, 'codeapp/blog_comments.html', {'comments': comments, 'post': post})


# Profile pages
def profile_page(request):
    return render(request,'profile_page.html')

def edit_profile(request):
    form=None
    try:
        profile=request.user.profile
        form=ProfileForm()
    except:
        profile=Profile(user=request.user)
    if request.method=='POST':
        form=ProfileForm(data=request.POST,files=request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            alert=True
            return render(request,'codeapp/edit_profile.html',{'alert':alert})
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'codeapp/edit_profile.html', {'form': form})


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

