from django.urls import path
from .views import pokemon_view, autocomplete_pokemon, pokemon_list


urlpatterns = [
    path("<int:pokemon_id>/", pokemon_view, name="pokemon_detail"),
    path("autocomplete_pokemon/", autocomplete_pokemon, name="autocomplete_pokemon"),
    path("", pokemon_list, name="pokemon_list"),
]
