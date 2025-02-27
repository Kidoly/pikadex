from django.shortcuts import render
from .utils import pokemon_creation, search_pokemon, get_pokemons
from django.http import JsonResponse
from django.shortcuts import redirect
import uuid

TEAMS = {}

def pokemon_view(request, pokemon_id):
    """
    Fonction qui affiche les détails d'un pokémon

    Args:
        request (HttpRequest): Requête HTTP avec des données de session (si il y en a)
        pokemon_id (int): ID du pokémon
    
    Returns:
        HttpResponse: Page HTML avec les détails du pokémon
    """
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
    """
    Fonction qui renvoie une liste de pokémons correspondant à la recherche
    """
    query = request.GET.get('q', '')
    if query:
        matched_pokemons = search_pokemon(query)
        return JsonResponse(matched_pokemons, safe=False)
    return JsonResponse([], safe=False)

def pokemon_list(request):
    """
    Fonction qui affiche la liste des pokémons

    Args:
        request (HttpRequest): Requête HTTP avec des données de session (si il y en a)

    Returns:
        HttpResponse: Page HTML avec la liste des pokémons et l'équipe du joueur
    """
    if "user_token" not in request.session:
        request.session["user_token"] = str(uuid.uuid4())

    user_token = request.session["user_token"]
    pokemons = get_pokemons()
    team_pokemon_ids = TEAMS.get(user_token, [])

    team = [pokemon_creation(pokemon_id) for pokemon_id in team_pokemon_ids]

    return render(request, 'home.html', {'pokemons': pokemons, 'user_token': user_token, 'team': team})


def add_pokemon(request):
    """
    Fonction qui ajoute un pokémon à l'équipe du joueur

    Args:
        request (HttpRequest): Requête HTTP avec les données du pokémon à ajouter et le token du joueur

    Returns:
        HttpResponse: Redirige vers la page de la liste des pokémons (et ajoute le pokémon à l'équipe si il y a de la place)
    """
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
    """
    Fonction qui retire un pokémon de l'équipe du joueur

    Args:
        request (HttpRequest): Requête HTTP avec les données du pokémon à retirer et le token du joueur

    Returns:
        HttpResponse: Redirige vers la page de la liste des pokémons (et retire le pokémon de l'équipe si il y est)
    """
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

def get_team(token):
    """
    Fonction qui renvoie l'équipe du joueur

    Args:
        token (str): Token du joueur
    
    Returns:
        JsonResponse: Liste des pokémons de l'équipe du joueur
    """
    team = TEAMS.get(token, [])
    return JsonResponse({"team": team})

