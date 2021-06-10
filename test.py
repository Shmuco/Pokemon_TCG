# from pokemontcgsdk import Set
# from pokemontcgsdk import Card
# from pokemontcgsdk import RestClient
# RestClient.configure('a373cfc1-3b13-46c2-bc19-fc3b7e152fb8')

# card = Card.find('xy1-1').nationalPokedexNumbers

# cards = Card.where(q='nationalPokedexNumbers:1')[0].images
# print(card)


import requests
import json
card = requests.get("https://api.pokemontcg.io/v2/cards?q=name:mudkip", headers={'X-Api-Key':'a373cfc1-3b13-46c2-bc19-fc3b7e152fb8'}).json()

image = card['data'][1]['images']['large']


print(image)