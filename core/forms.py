from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
    
    }))
    
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Enter Email Address',
    
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
    'placeholder': 'Choose Password',
    
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
    'placeholder': 'Repeat Password',
    
    }))