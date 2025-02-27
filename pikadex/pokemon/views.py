from django.shortcuts import render
from .utils import pokemon_creation, search_pokemon, get_pokemons
from django.http import JsonResponse
from django.shortcuts import redirect
import uuid

TEAMS = {}

def pokemon_view(request, pokemon_id):
    if "user_token" not in request.session:
        request.session["user_token"] = str(uuid.uuid4())

    user_token = request.session["user_token"]
    team_pokemon_ids = TEAMS.get(user_token, [])
    team = [pokemon_creation(pokemon_id) for pokemon_id in team_pokemon_ids]

    pokemon = pokemon_creation(pokemon_id)
    if not pokemon:
        return render(request, "404.html", {"id": pokemon_id})

    return render(request, "detail.html", {"pokemon": pokemon, "team": team, "user_token": user_token})


def autocomplete_pokemon(request):
    query = request.GET.get('q', '')
    if query:
        matched_pokemons = search_pokemon(query)
        return JsonResponse(matched_pokemons, safe=False)
    return JsonResponse([], safe=False)

def pokemon_list(request):
    if "user_token" not in request.session:
        request.session["user_token"] = str(uuid.uuid4())

    user_token = request.session["user_token"]
    pokemons = get_pokemons()
    team_pokemon_ids = TEAMS.get(user_token, [])

    team = [pokemon_creation(pokemon_id) for pokemon_id in team_pokemon_ids]

    return render(request, 'home.html', {'pokemons': pokemons, 'user_token': user_token, 'team': team})


def add_pokemon(request):
    token = request.POST.get('token')
    pokemon_id = request.POST.get('pokemon_id')

    if not token or not pokemon_id:
        return redirect('/pokemon/')

    if token not in TEAMS:
        TEAMS[token] = []

    if len(TEAMS[token]) >= 5:
        return redirect('/pokemon/')

    TEAMS[token].append(pokemon_id)

    return redirect('/pokemon/') 

def remove_pokemon(request):
    token = request.POST.get('token')
    pokemon_id = request.POST.get('pokemon_id')

    if not token or not pokemon_id:
        print("no token or pokemon_id")
        return redirect('/pokemon/')

    if token not in TEAMS:
        print("no token in TEAMS")
        return redirect('/pokemon/')

    if pokemon_id in TEAMS[token]:
        print("removing pokemon")
        TEAMS[token].remove(pokemon_id)

    return redirect('/pokemon/')

def get_team(request, token):
    team = TEAMS.get(token, [])
    return JsonResponse({"team": team})

