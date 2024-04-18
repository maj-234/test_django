from django.shortcuts import render, HttpResponse, redirect
from .forms import CreateUser, LoginForm, CreateBlog
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.
from django.views import View
from .models import Blog


class login_page(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'auth_page/login.html', {'form' : form})
    
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            passwd = form.cleaned_data['password']
            user = authenticate(username=username, password=passwd)
            login(request, user)
            return redirect('/auth/blog/')
        else:
            form = LoginForm()
            return render(request, 'auth_page/login.html', {'form' : form})
        
    

class logout_page(View):
    def get(self, request):
        logout(request.user)
        return redirect('login')


class register_page(View):
    def get(self, request):
        form = CreateUser()
        return render(request, 'auth_page/register.html', {'form' : form})
    
    def post(self, request):
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = CreateUser()
            return render(request, 'auth_page/register.html', {'form' : form})      


class blog_page(View):
    def get(self, request):
        if request.user.is_authenticated:
            blogs = Blog.objects.all()
            return render(request, 'auth_page/blog.html', {'blogs' : blogs})
        return redirect('login')
    
class create_blog(View):
    def get(self, request):
        form = CreateBlog()
        return render(request, 'auth_page/create.html', {'form' : form})
    
    def post(self, request):
        form = CreateBlog(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/auth/blog/')
        else:
            form = CreateBlog()
            return render(request, 'auth_page/create.html', {'form' : form})
        