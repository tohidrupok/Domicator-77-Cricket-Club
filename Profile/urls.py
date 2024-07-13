from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('players/<slug:slug>/', views.player_detail, name='player_detail'),
    path('about/', views.about, name='about'),
    path('vlog/', views.vlog, name='vlog'),
]
    
