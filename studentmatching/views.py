from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the student matching index.")

def login(request):
    return HttpResponse("This is the login page.")
