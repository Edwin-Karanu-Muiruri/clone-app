from  django.forms import ModelForm
from .models import Image,Profile

class ImageUploadForm(ModelForm):
    class Meta:
        model = Image
        exclude = ['comments','likes','profile']

class ProfileEditForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_photo','bio']