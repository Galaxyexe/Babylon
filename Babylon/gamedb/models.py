from django.db import models
from django.utils import timezone
# communications between users and poster
from django.contrib.auth.models import User
from django.urls import reverse


class Game(models.Model):  # goes off of database of people?
    title = models.CharField(max_length=100)
    creator = models.TextField()
    image = models.ImageField(default='default.jpg', upload_to='game_pics')
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return(self.title)

    def get_absolute_url(self):
        # don't have to put in link, reverse goes to area
        return reverse('post-detail', kwargs={'pk': self.pk})
