from django.shortcuts import render
from django import forms
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')
def home(request):
    return render(request,'home.html')
def profile(request):
    return render(request,'profile.html')

