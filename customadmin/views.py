from django.shortcuts import render
from django.contrib .auth.models import User
from django.contrib.auth import authenticate, login, logout 

# Create your views here.

def admin_login(request):
    
    return render(request, 'customadmin/adminlogin.html')