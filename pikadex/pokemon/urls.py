from django.urls import path
from .views import pokemon_view, autocomplete_pokemon, pokemon_list, get_team, add_pokemon, remove_pokemon

"""
URLs de l'application pokemon
Les URLs de l'application pokemon sont accessibles depuis le chemin /pokemon/

pokemon/ : Liste des pokémons
pokemon/<int:pokemon_id>/ : Détails d'un pokémon
pokemon/autocomplete_pokemon/ : Autocomplétion de la recherche de pokémon
pokemon/get_team/<str:token>/ : Récupération de l'équipe d'un joueur
pokemon/add_to_team/ : Ajout d'un pokémon à l'équipe
pokemon/remove_from_team/ : Retrait d'un pokémon de l'équipe
"""
urlpatterns = [
    path("<int:pokemon_id>/", pokemon_view, name="pokemon_detail"),
    path("autocomplete_pokemon/", autocomplete_pokemon, name="autocomplete_pokemon"),
    path("", pokemon_list, name="pokemon_list"),
    path("get_team/<str:token>/", get_team, name="get_team"),
    path("add_to_team/", add_pokemon, name="add_pokemon"),
    path("remove_from_team/", remove_pokemon, name="remove_pokemon"),
]
