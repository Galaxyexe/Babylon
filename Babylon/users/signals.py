from django.db.models.signals import post_save  # fired once user is saved
#from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, User


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):  # kwargs any additional
    if(created):
        e = Profile.objects.create(user=instance)
        e.save()
