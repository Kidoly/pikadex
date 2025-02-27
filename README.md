# pikadex

Pikadex - Projet python utilisant le framework Django

Description :

Ce projet est une application web construite avec
Django et permet d'afficher les 151 premiers pokemon.
Ainsi que de rechercher et afficher les caractéristiques 
d'un pokemon en particulier et de creer des équipes.

Détails techniques : 

 - Backend : 
    
        - Django en framework web.
        - Les router contiennent :
            - pokemon/ : Liste des pokémons
            - pokemon/<int:pokemon_id>/ : Détails d'un pokémon
            - pokemon/autocomplete_pokemon/ : Autocomplétion de la recherche de pokémon
            - pokemon/get_team/<str:token>/ : Récupération de l'équipe d'un joueur
            - pokemon/add_to_team/ : Ajout d'un pokémon à l'équipe
            - pokemon/remove_from_team/ : Retrait d'un pokémon de l'équipe

 - Frontend : 

        - HTML/CSS (Tailwind) et javascript

 - API : 
    
     - Les données sont récupérées sur l'API : https://pokeapi.co/

Installation : 

1. Pour utiliser l'application il faut clonner le git : 
git clone https://github.com/Kidoly/pikadex.git

2. Aller dans le dossier pikadex :
cd pikadex

3. La meilleur pratique est de créer un environnement virtuel :
python -m venv env

4. Puis l'activer :
linux :
source env/bin/activate

Windows :
./Scripts/activate.ps1

5. On installe les prérequis :
pip install -r requirements.txt

6. On change de dossier :
cd pikadex

7. et on lance le serveur :
python manage.py runserver

8. Pour voir l'application on doit aller sur l'URL suivante :
http://127.0.0.1:8000/pokemon/


Utilisation : 

    1. Page d'acceuil :

        - Permet de parcourir les pokemons et de les ajouter a son équipe.


    2. Page des détails :

        - Affiche les détails d'un pokemon avec ses stats, ses capacitées et ses types.











