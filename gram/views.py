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
    return render(request,'welcome.html',{'images':images})

def home(request):
    images = Image.objects.all()
    return render(request,'home.html',{'images':images})

@login_required    
def profile(request):
    current_user = request.user
    profile = Profile.objects.get(user = current_user)
    images = Image.get_images(current_user)
    return render(request,'profile.html',{'profile':profile,'images':images})

@login_required
def update_profile(request):
    current_user = request.user
    if request.method == "POST":
        form = EditProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile_photo = form.cleaned_data['profile_photo']
            bio  = form.cleaned_data['bio']
            updated_profile = Profile.objects.get(user= current_user)
            updated_profile.profile_photo = profile_photo
            updated_profile.bio = bio
            updated_profile.save()
        return redirect('profile')
    else:
        form = EditProfileForm()
    return render(request, 'update_profile.html', {"form": form})


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
        return redirect('/home/')
    else:
        form = ImageUploadForm()
    return render(request,'upload.html',{'form':form})

@login_required
def get_images(request,id):
    image = Image.objects.get(pk=id)
    comments = Comment.get_image_comment(image)
    total_likes = image.likes_count()
    liked = False
    if image.likes.filter(id = request.user.id).exists():
        liked = True
    return render(request,'post.html',{'image':image,'comments':comments,'total_likes':total_likes,'liked':liked})    


@login_required
def like_image(request,id):
    image = Image.objects.get(pk=id)
    liked = False
    if image.likes.filter(id=request.user.id).exists():
        image.likes.remove(request.user)
        liked = False
    else:
        image.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('get_images',args=[int(image.id)]))

@login_required
def search_results(request):
    if 'user' in request.GET and request.GET['user']:
        searched_term = request.GET.get('user')
        profiles = Profile.search_user(searched_term)
        message = f"{searched_term}"
        return render(request, 'search.html', {'message':message,'profiles':profiles})
    else:
        message = "Enter something to search"
        return render(request, 'search.html',{'message':message})
