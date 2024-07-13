from django.shortcuts import render, get_object_or_404
from .models import Player,Home

def home(request):
    home = Home.objects.first()  
    return render(request, 'home.html', {'home': home})

def profile(request):
    captains = Player.objects.all()[:2]
    players = Player.objects.all()[2:] 
    home = Home.objects.first()  
    return render(request, 'players.html', {'players': players, 'captains':captains,'home':home})


def player_detail(request, slug):
    player = get_object_or_404(Player, slug=slug) 
    return render(request, 'plater_details.html', {'player': player}) 

def about(request):
    about = Home.objects.first()  
    return render(request, 'about.html', {'about': about})