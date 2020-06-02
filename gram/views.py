from django.shortcuts import render,redirect
from django import forms
from django.http import HttpResponse,HttpResponseRedirect
from .models import Image,Profile,Comment
from django.urls import reverse

# Create your views here.
def welcome(request):
    images = Image
    return render(request,'welcome.html')
def home(request):
    return render(request,'home.html')
def profile(request):
    return render(request,'profile.html')

