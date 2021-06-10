import os   
import django
import  requests
import json
import random
import urllib.request
import wget
import shutil



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pokemon_tcg.settings')
django.setup()

from card_game.models import *




# # Gets a list of all the pokemon in ruby and saphier 
# response = requests.get('https://pokeapi.co/api/v2/pokedex/4/')
# li = []
# for i in response.json()['pokemon_entries']:
#     li.append(i['pokemon_species']['name'])
# print(li)







# i = li[20]
# response = requests.get(f'https://pokeapi.co/api/v2/pokemon-species/{i}/')
# response = response.json()
# name = i
# # pokemon_id = requests.get(f'https://pokeapi.co/api/v2/pokedex/{i}/').json()['PokemonEntry']['entry_number']
# capture_rate = response['capture_rate']
# is_legendary = response['is_legendary']
# description = 'null'
# # type = requests.get(f'https://pokeapi.co/api/v2/pokemon/{i}/').json()['types']
# # for i in type:
# #     print(i)
# #     # print([i]['type']['name'])
# print(name)
# # print(pokemon_id)
# print(capture_rate)
# print(is_legendary)
# print(description)
# # print(type)



# Populates database with cards
pokedex_url = 'https://pokeapi.co/api/v2/pokedex/4/'
pokemons = requests.get(pokedex_url).json()['pokemon_entries']
# print(pokemons)

for entry in pokemons:
    species_data = requests.get(entry['pokemon_species']['url']).json()
    # print(species_data)
    poke_data = requests.get(f'https://pokeapi.co/api/v2/pokemon/{species_data["name"]}/').json()
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon-species/{poke_data["name"]}/').json()   
    

    card = requests.get(f"https://api.pokemontcg.io/v2/cards?q=name:{poke_data['name']}", headers={'X-Api-Key':'a373cfc1-3b13-46c2-bc19-fc3b7e152fb8'}).json()
    image = card['data'][1]['images']['large']





    pokemon = Card.objects.create(
        name=poke_data['name'], 
        pokemon_id=poke_data['id'],
        is_legendary = response['is_legendary'],
        capture_rate = response['capture_rate'],
        image = image)

    for type_dict in poke_data['types']:
        print(type_dict['type']['name'])
        ptype = PokemonType.objects.get_or_create(ptype=type_dict['type']['name'])
        print(ptype[0]) 
        pokemon.ptype.add(ptype[0])
    
    print(poke_data['name'])
    



        
# Dowloads and saves images

# card = requests.get("https://api.pokemontcg.io/v2/cards?q=name:mudkip", headers={'X-Api-Key':'a373cfc1-3b13-46c2-bc19-fc3b7e152fb8'}).json()
# image = card['data'][1]['images']['large']
# file = "/Users/shmuel/Library/Mobile Documents/com~apple~CloudDocs/Documents/Education /Coding/DI_Bootcamp/Weeks 8-12/Week10/Day 1 - 3/TCG/pokemon_tcg/media/cards/mudkip.png"

# r = requests.get(image, stream=True)
# if r.status_code == 200:
#     r.raw.decode_content = True
#     with open(file,'wb') as f:
#         shutil.copyfileobj(r.raw, f)
#         print('Image sucessfully Downloaded')