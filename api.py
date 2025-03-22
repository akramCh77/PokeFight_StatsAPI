import pprint
import aiohttp
import requests
import asyncio
from aiocache import Cache,cached 
from ERROR import gestion_erreur


@cached(ttl=3600, cache=Cache.MEMORY)  # Cache les résultats pendant 1 heure


async def get_pokemon_data(pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon.lower()}"  # Utilise pokemon au lieu de id
    async with aiohttp.ClientSession() as session:
         data= await gestion_erreur(session,url)
         if not data or 'stats' not in data:
            print(f"❌ Erreur : Impossible de récupérer les stats de {pokemon}.")
            return None
         stats = {stat['stat']['name']: stat['base_stat'] for stat in data['stats']}
         sprite_url = data['sprites']['front_default'] if 'sprites' in data and 'front_default' in data['sprites'] else None
         return {'name': data.get('name'),
                'hp':stats.get('hp',0),
                'attack':stats.get('attack',0),
                'defense':stats.get('defense'),
                 'speed':stats.get('speed'),
                 'sprite': sprite_url }
        
