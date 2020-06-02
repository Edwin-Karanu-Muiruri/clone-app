from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    
    profile_photo = models.ImageField(upload_to = 'images/',null = True,blank = True)
    bio = models.TextField()




class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length = 50)
    caption = models.TextField()
    profile = models.ForeignKey(User,on_delete = models.CASCADE)
    likes = models.ManyToManyField(User,related_name='posts')


class Comment(models.Model):
    image = models.ForeignKey(Image,on_delete = models.CASCADE,related_name='comments')
    review = models.TextField()
    date_pub = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)