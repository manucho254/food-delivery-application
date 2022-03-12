from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth.models import auth
from django.contrib import messages
from .forms import RegisterForm


class HomeView(View):
    def get(self,  request, *args, **kwargs):
        return render(request,  'index.html',  {})
    
class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        context = {
            'form':form
        }
        return render(request,  'register.html', context)
        
    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('verify')
    
class LoginView(View):
    def get(self, request, *args, **kwargs):
        pass
    def post(self, request, *args, **kwargs):
        pass
    
class LogoutView(View):
    def get(self, request, *args, **kwargs):
        pass
    def post(self, request, *args, **kwargs):
        pass