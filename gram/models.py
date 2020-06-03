from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
    profile_photo = CloudinaryField('image')
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
        instance.Profile.save()


class Image(models.Model):
    image = CloudinaryField('image')
    image_name = models.CharField(max_length = 50)
    caption = models.TextField()
    profile = models.ForeignKey(User,on_delete = models.CASCADE)
    likes = models.ManyToManyField(User,related_name='posts')
    comment = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.image_name
    
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def likes_counter(self):
        return self.likes.count()

    @classmethod
    def update_caption(cls,id,caption):
        cls.objects.filter(id=id).update(caption=caption)
        updated_caption = cls.objects.get(id=id)
        return updated_caption

    @classmethod
    def get_images(cls,profile):
        return cls.objects.filter(profile=profile)


class Comment(models.Model):
    image = models.ForeignKey(Image,on_delete = models.CASCADE,related_name='comments')
    review = models.TextField()
    date_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    @classmethod
    def get_image_comment(cls,image):
        return cls.objects.filter(image =image)