from django.shortcuts import render,redirect
from .forms import ImageUploadForm,ProfileEditForm
from django.http import HttpResponse,HttpResponseRedirect
from .models import Image,Profile,Comment
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def welcome(request):
    images = Image.objects.all()
    return render(request,'welcome.html'{'images':images})

def home(request):
    images = Image.objects.all()
    return render(request,'home.html'{'images':images})

@login_required    
def profile(request):
    current_user = request.user
    profile = Profile.objects.get(user = current_user)
    images = Image.get_images(current_user)
    return render(request,'profile.html',{'profile':profile,'images':images})

