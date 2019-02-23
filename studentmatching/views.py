from django.shortcuts import render
from django.contrib.auth import logout as auth_logout

def index(request):
    return render(request, 'studentmatching/index.html')

def login(request):
    return render(request, 'studentmatching/login.html')

def logout(request):
    auth_logout(request)
    return render(request, 'studentmatching/logout.html')
