from django.shortcuts import render
from .utils import pokemon_creation, search_pokemon
from django.http import JsonResponse

def pokemon_view(request, pokemon_id):
    pokemon = pokemon_creation(pokemon_id)
    if not pokemon:
        return render(request, "not_found.html", {"id": pokemon_id})
    
    return render(request, "detail.html", {"pokemon": pokemon})

def autocomplete_pokemon(request):
    query = request.GET.get('q', '')
    if query:
        matched_pokemons = search_pokemon(query)
        return JsonResponse(matched_pokemons, safe=False)
    return JsonResponse([], safe=False)