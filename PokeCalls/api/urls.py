from django.urls import path
from . import views

urlpatterns = [
    path('guess-pokemon/', views.guess_pokemon, name='guess-pokemon'),
    path('guess-move/', views.guess_move, name='guess-move'),
]