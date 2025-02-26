from django.urls import path
from .views import pokemon_view

urlpatterns = [
    path("<int:pokemon_id>/", pokemon_view, name="pokemon_detail"),
]
