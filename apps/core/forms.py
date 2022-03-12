from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label='', max_length=100,required = True,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),)
    password1 = forms.CharField(label='',required = True,widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),)
    password2 = forms.CharField(label='',required = True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}),)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']