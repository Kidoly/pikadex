from django.urls import path
from .views import pokemon_view, autocomplete_pokemon, pokemon_list, get_team, add_pokemon, remove_pokemon


urlpatterns = [
    path("<int:pokemon_id>/", pokemon_view, name="pokemon_detail"),
    path("autocomplete_pokemon/", autocomplete_pokemon, name="autocomplete_pokemon"),
    path("", pokemon_list, name="pokemon_list"),
    path("get_team/<str:token>/", get_team, name="get_team"),
    path("add_to_team/", add_pokemon, name="add_pokemon"),
    path("remove_from_team/", remove_pokemon, name="remove_pokemon"),
]
