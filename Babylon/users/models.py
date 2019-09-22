from django.db import models
#from django.contrib.auth.models import User
from PIL import Image
import datetime
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone = models.CharField(max_length=11, default="")

from Babylon import settings
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        upload_to='profile_pics', default='default.jpg')
    description = models.CharField(max_length=300, default='')
