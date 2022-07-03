from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .forms import BlogPostForm, ProfileForm

from .models import *



# Create your views here.
def blog_post(request):
    posts=BlogPost.objects.all()
    posts=BlogPost.objects.filter().order_by('-dateTime')

    return render(request,'blog.html',{'posts':posts})

def blog_comments(request,slug):
    post=BlogPost.objects.filter(slug=slug).first()
    comments=Comment.objects.filter(blog=post)
    if request.method=="POST":
        user=request.user
        content=request.POST.get('content','')
        blog_id=request.POST.get('blog_id','')
        comment=Comment(user=user,content=content,blog=post)
        comment.save()
    return render(request,'comment_blog.html',{'post':post,'comments':comments})

def add_post(request,):
    if request.method=='POST':
        form=BlogPostForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            blogpost=form.save(commit=False)
            blogpost.author=request.user
            blogpost.save()
            obj=form.instance
            alert=True
            return render(request,'add_blog.html',{'obj':obj},{'alert':alert})
        else:
            return render(request,'add_blog.html',{'form':form})



def delete_post(request,slug):
    posts=BlogPost.objects.get(slug=slug)
    if request.method=='POST':
        posts.delete()
        return redirect('/')
    return render(request,'delete_blog.html',{'posts':posts})

def search(request):
    if request.method=='POST':
        searched=request.POST['searched']
        blogs=BlogPost.objects.filter(title__contains=searched)
        return render(request,'search.html',{'blogs':blogs})

    else:
        return render(request,'search.html',{})

def user_posts(request,myid):
    posts=BlogPost.objects.filter(id=myid)
    return render(request,'user_posts.html',{'posts':posts})

def profile(request):
    return render(request,'profile.html')


def edit_profile(request):
    try:
        profile=request.user.profile
    except:
        profile=Profile(user=request.user)
    if request.method=='POST':
        form=ProfileForm(data=request.POST,files=request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            alert=True
            return render(request,'edit_profile.html',{'alert':alert})
        else:
            form=ProfileForm(instance=profile)
        
        return render(request,'edit_profile.html',{'form':form})

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1 != password2:
            messages.error(request,'Pasword missmatch')
            return redirect('/register')
        user=User.objects.create_user(username,email,password1)
        user.first_name=first_name
        user.last_name=last_name
        user.saver()
        return render(request,'login.html')

    return render(request,'register.html')

def login_user(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not  None:
            login(request,user)
            messages.success(request,'Logged in Successfully')
            return redirect('/')
        else:
            messages.error(request,'Invalid Credentials')
        return render(request,'login.html')

def logout_user(request):
    logout(request)
    messages.success(request, "Logged out Successfully")
    return redirect('/login')





    


