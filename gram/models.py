from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'images/',null = True,blank = True)
    bio = models.TextField()

    def __str__(self):
        return self.user.username

    @classmethod
    def search_user(cls,search_term):
        return User.objects.filter(username__icontains=search_term)

    @receiver(post_save, sender=User)
    def create_profile(sender,instance,created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    
    @receiver(post_save,sender=User)
    def save_profile(sender,instance, **kwargs):
        instance.profile.save()




class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length = 50)
    caption = models.TextField()
    profile = models.ForeignKey(User,on_delete = models.CASCADE)
    likes = models.ManyToManyField(User,related_name='posts')
    comment = models.TextField(null=True,blank=True)

class Comment(models.Model):
    image = models.ForeignKey(Image,on_delete = models.CASCADE,related_name='comments')
    review = models.TextField()
    date_pub = models.DateTimeField(auto_now_add=True)
