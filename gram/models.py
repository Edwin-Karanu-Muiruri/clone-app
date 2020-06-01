from django.db import models

# Create your models here.
class Image(models.Model):
    image_name = models.CharField(max_length = 50)
    image_caption = models.CharField(max_length = 50)
    comments = models.CharField(max_length = 50)

class Profile(models.Model):
    bio = models.CharField(max_length = 50)
