from django.shortcuts import render
from django.http import HttpResponse


def about(request):
    return render(request, 'generator/about.html')


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    list('abcdefghijklmnopqrstuvwxyz')
    return render(request, 'generator/password.html')
