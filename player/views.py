# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from gameplay.models import Game


def home(request):
    my_games = Game.objects.games_for_user(request.user)
    active_games = my_games.active()

    return render(request, "player/home.html",
                  {'games': active_games})
