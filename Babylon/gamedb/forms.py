from django import forms
from .models import Game

class UserRegisterForm():
    title = forms.CharField()
    genre = forms.CharField()
    points = forms.IntegerField()
    desc = forms.TextField()
    image = forms.ImageField()

    class Meta:
        model = Game
        fields = ['username', 'email', 'number', 'password1', 'password2']
