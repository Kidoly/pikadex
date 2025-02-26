import requests

pokeApiUrl = "https://pokeapi.co/api/v2/pokemon/"

class Pokemon():
    def __init__(self, name, id, image, height, weight, types, abilities, stats):
        self.name = name
        self.id = id
        self.image = image
        self.height = height
        self.weight = weight
        self.types = types
        self.abilities = abilities
        self.stats = stats

class Ability():
    def __init__(self, name, value, effort, url):
        self.name = name
        self.value = value
        self.effort = effort
        self.url = url

class Stat():
    def __init__(self, name, base_stat, effort, url):
        self.name = name
        self.base_stat = base_stat
        self.effort = effort
        self.url = url

class Type():
    def __init__(self, name, slot, url):
        self.name = name
        self.slot = slot
        self.url = url

def pokemon_creation(identifier):
    response = requests.get(f"{pokeApiUrl}{identifier}")
    if response.status_code == 200:
        data = response.json()
        return Pokemon(
            data["forms"][0]["name"],
            data["id"],
            data["sprites"]["other"]["official-artwork"]["front_default"],
            data["height"] / 10,
            data["weight"] / 10,
            [Type(t["type"]["name"], t["slot"], t["type"]["url"]) for t in data["types"]],
            [Ability(a["ability"]["name"], a["is_hidden"], a["slot"], a["ability"]["url"]) for a in data["abilities"]],
            [Stat(s["stat"]["name"], s["base_stat"], s["effort"], s["stat"]["url"]) for s in data["stats"]]
        )
    return None

def search_pokemon(query):
    """ Returns a list of matching Pokémon names and images based on user input. """
    response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")  
    if response.status_code == 200:
        data = response.json()
        matched_pokemons = [
            {
                "id": i + 1,
                "name": p["name"].capitalize(),
                "image": pokemon_creation(p["name"]).image
            }
            for i, p in enumerate(data["results"]) if query.lower() in p["name"]
        ]
        return matched_pokemons
    return []