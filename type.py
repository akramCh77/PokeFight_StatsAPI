import asyncio
import aiohttp
import requests

from ERROR import gestion_erreur
from api import get_pokemon_data


async def Ptype(pokemon_type):
    url = f"https://pokeapi.co/api/v2/type/{pokemon_type.lower()}"
    async with aiohttp.ClientSession() as session:
        data= await gestion_erreur(session,url)
        if not data:
         return None
        
        pokemon_list=data['pokemon']
        total_hp=0
        count=len(pokemon_list)

        pokemon_name=[p['pokemon']['name'] for p in pokemon_list]
        pokemon_data= await asyncio.gather(*(get_pokemon_data(name)for name in pokemon_name))
        total_hp=sum(m['hp'] for m in pokemon_data if m is not None)
    
        avr_hp= total_hp / count if count > 0 else 0
        return{
           'count':count,
           'avr_hp':avr_hp

        }