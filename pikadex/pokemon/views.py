from django.shortcuts import render
from .utils import pokemon_creation

def pokemon_view(request, pokemon_id):
    pokemon = pokemon_creation(pokemon_id)  # Fetch Pokémon by ID
    if not pokemon:
        return render(request, "not_found.html", {"id": pokemon_id})
    
    return render(request, "detail.html", {"pokemon": pokemon})
