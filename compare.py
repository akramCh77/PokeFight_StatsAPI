import asyncio
from api import get_pokemon_data
import requests

async def comparaison(pokemon1,pokemon2):
    # Exécuter les deux requêtes en parallèle
    p1, p2 = await asyncio.gather(get_pokemon_data(pokemon1), get_pokemon_data(pokemon2))

    if not p1 or not p2 :
        return None
    stronger = p1['name'] if p1['attack'] > p2['attack'] else p2['name']

    return{         
        'pokemon1_name': p1['name'],
        'pokemon2_name': p2['name'],
        'pokemon1_hp': p1['hp'],
        'pokemon2_hp': p2['hp'],
        'pokemon1_attack': p1['attack'],
        'pokemon2_attack': p2['attack'],
        'stronger': stronger,
        'pokemon1_sprite':p1['sprite'],
        'pokemon2_sprite':p2['sprite']

    }

