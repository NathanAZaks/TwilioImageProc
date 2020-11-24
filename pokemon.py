import requests

def get_pokemon_name(pokemon_number):
    api_endpoint = 'https://pokeapi.co/api/v2/pokemon/'

    # pokemon_number = '123'

    pokemon_response = requests.get(api_endpoint + pokemon_number).json()

    pokemon_name = pokemon_response['species']['name']

    return pokemon_name
