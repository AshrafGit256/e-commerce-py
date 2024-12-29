from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User 


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"", "class": "form-control"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"", "class": "form-control"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"", "class": "form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"", "class": "form-control"}))
    
    class Meta:
        model = User
        fields = ['username', 'email']