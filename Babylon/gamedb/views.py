from django.shortcuts import render
from .models import Game
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic.base import TemplateView

from django.views.generic import (
    DetailView, CreateView
)


class game_page(DetailView):
    model = Game

@staff_member_required
def game_creation(request):
    print(request.body)
    if(request.method == "post"):
        print("we be posting")
    test_game = Game()
    return render(request, 'games/game_creation.html')

def games(request):
    # get a list of games then pass it in
    all_games = Game.objects.all()
    return render(request, 'games/game-page.html')