from django.urls import path
from . import views

urlpatterns = [
    path('', views.game, name="game"),
    path('game', views.checkans, name="check"),
    path('games', views.next, name="next"),
   
]
