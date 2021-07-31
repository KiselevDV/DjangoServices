from django.shortcuts import render, redirect
from django.views.generic.base import View

from .forms import GameForm
from .service import Game


class GameAPI(View):
    def get(self, request):
        return render(request, 'game/index.html', {'form': GameForm()})

    def post(self, request):
        form = GameForm(request.POST)
        if form.is_valid():
            damage = form.cleaned_data['damage']
            game = Game()
            i_get_damage, i_set_damage = game.set_damage(damage)
        context = {
            'form': GameForm(),
            'i_get_damage': i_get_damage,
            'i_set_damage': i_set_damage,
        }
        return render(request, 'game/index.html', context)
