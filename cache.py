import asyncio

from api import get_pokemon_data


async def test_cache():
    print("\nPremière requête : récupération de Pikachu 📡")
    start = asyncio.get_event_loop().time()
    data1 = await get_pokemon_data("pikachu")
    print(f"Temps d’exécution : {asyncio.get_event_loop().time() - start:.2f} secondes\n")

    print("Deuxième requête : récupération de Pikachu depuis le cache ⚡")
    start = asyncio.get_event_loop().time()
    data2 = await get_pokemon_data("pikachu")
    print(f"Temps d’exécution : {asyncio.get_event_loop().time() - start:.2f} secondes\n")

    print(f"Les données sont-elles identiques ? {'✅ Oui' if data1 == data2 else '❌ Non'}")

