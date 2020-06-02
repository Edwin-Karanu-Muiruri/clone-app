from  django.forms import ModelForm
from .models import Image,Profile

class ImageUploadForm(ModelForm):
    class Meta:
        model = Image
        exclude = ['comments',]

class ProfileEditForm(ModelForm):
    class Meta:
        model = Profile
        