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

@login_required
def comment(request,id):
    image = Image.objects.get(pk=id)
    review = request.GET.get('comment')
    user = request.user
    comment = Comment(image = image, review = review,user = user)
    comment.save_comment()
    return redirect(get_images,id=id)

@login_required
def image_upload(request):
    if request.method == "POST":
        form = ImageUploadForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.profile = request.user
            image.save()
        return redirect('home')
    else:
        form.ImageUploadForm()
    return render(request,'upload.html',{'form':form})
    
