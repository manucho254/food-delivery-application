from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.models import auth
from django.contrib import messages


class HomeView(View):
    def get(self,  request, *args, **kwargs):
        return render(request,  'index.html',  {})
    
class RegisterView(View):
    def get(self, request, *args, **kwargs):
        pass
    def post(self, request, *args, **kwargs):
        pass
    
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