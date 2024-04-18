from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Blog


class CreateUser(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')



class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class CreateBlog(forms.ModelForm):
    username = forms.CharField(max_length=100)
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.TextInput(attrs={'style' : 'width: 80%; height : 70%; margin: 10%;'}))
    
    class Meta:
        model = Blog
        exclude = ('user',)
