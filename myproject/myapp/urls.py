from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('game/', views.heads_tails, name='heads_tails'),
    path('cube/', views.cube, name='cube'),
    path('rnd/', views.rnd, name='rnd'),
]

