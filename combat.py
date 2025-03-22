import asyncio

from api import get_pokemon_data


async def simulate_combat(pokemon1,pokemon2):
    p1,p2= await asyncio.gather(get_pokemon_data(pokemon1),get_pokemon_data(pokemon2))
    if not p1 or not p2:
        return None
    p1_damage=p1['attack'] *5
    p2_damage=p2['attack']*5

    winner= p1['name'] if p1_damage > p2_damage else p2['name']
    return {
        'pokemon1': p1['name'], 'pokemon2': p2['name'],
        'p1_damage': p1_damage, 'p2_damage': p2_damage,
        'winner': winner,
        'combatant1_sprite':p1['sprite'],
        'combatant2_sprite':p2['sprite']

    }

     