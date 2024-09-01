import requests

base_url = "https://pokeapi.co/api/v2/"
is_running = True

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"

    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data {response.status_code}")

def display_pokemon_details(pokemon):
    print()
    print(f"ID     : {pokemon["id"]}")
    print(f"Name   : {pokemon["name"].capitalize()}")
    print(f"Height : {pokemon["height"] / 10:.2f}cm")
    print(f"Weight : {pokemon["weight"] / 10:.2f}kg")
    print(f"EXP    : {pokemon["base_experience"]}")
    print()
    for stat in pokemon["stats"]:
        print(f"{stat.get("stat").get("name").capitalize():16}: {stat.get("base_stat")}")
    print()

while is_running:
    pokemon_name = input("> Enter pokemon name: ").lower()
    
    if pokemon_name:
        pokemon_info = get_pokemon_info(pokemon_name)

    if pokemon_info:
        display_pokemon_details(pokemon_info)