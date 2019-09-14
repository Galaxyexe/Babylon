from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import datetime
from Babylon import settings
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        upload_to='profile_pics', default='default.jpg')
    description = models.CharField(max_length=300, default='')
    phone = models.IntegerField(default=0)
