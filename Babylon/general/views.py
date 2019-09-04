from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):  # can change into class view later
    return render(request, 'general/index.html')

def team(request):
    return render(request, 'general/team.html')

def games(request):
    return render(request, 'general/game-page.html')

def waves(request):
    return render(request, 'general/waves.html')
