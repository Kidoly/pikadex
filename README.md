# Pikadex

Pikadex - Projet Python utilisant le framework Django
![alt text](https://pngimg.com/uploads/pokemon/pokemon_PNG107.png "Logo Title Text 1")

## Description

Ce projet est une application web construite avec Django et permet d'afficher les 151 premiers pokemon. Il permet également de rechercher et afficher les caractéristiques d'un pokemon en particulier et de creer des équipes.

## Détails techniques

### Backend

- **Framework** : Django
- **Routes disponibles** :
  - `pokemon/` : Liste des Pokémon
  - `pokemon/<int:pokemon_id>/` : Détails d'un Pokémon
  - `pokemon/autocomplete_pokemon/` : Autocomplétion de la recherche de Pokémon
  - `pokemon/get_team/<str:token>/` : Récupération de l'équipe d'un joueur
  - `pokemon/add_to_team/` : Ajout d'un Pokémon à l'équipe
  - `pokemon/remove_from_team/` : Retrait d'un Pokémon de l'équipe

### Frontend

- **Technologies** : HTML, CSS (Tailwind), JavaScript

### API

- **Source des données** : [PokéAPI](https://pokeapi.co/)

## Installation

1. Cloner le dépôt Git :
```sh
git clone https://github.com/Kidoly/pikadex.git
```

2. Aller dans le dossier du projet :
```sh
cd pikadex
```

3. Créer un environnement virtuel
```sh
python -m venv env
```

4.Activer l'environnement virtuel :

Linux/macOS :
```sh
source env/bin/activate
```
Windows (PowerShell) :
```sh
.\env\Scripts\Activate.ps1
```

5. Installer les dépendances :
```sh
pip install -r requirements.txt
```

6. Lancer le serveur Django :
```sh
python manage.py runserver
```

7. Accéder à l'application via l'URL :
```sh
http://127.0.0.1:8000/pokemon/
```

## Utilisation

- **Page d'accueil** :  
  Explorez la liste des Pokémon et ajoutez-les à votre équipe.

- **Page des détails** :  
  Consultez les caractéristiques d’un Pokémon : stats, capacités et types.

