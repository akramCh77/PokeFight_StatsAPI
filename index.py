# Fichier frontend index.py
import streamlit as st
import asyncio
from api import get_pokemon_data
from compare import comparaison
from combat import simulate_combat

st.title("Pokémon API Explorer")

st.header("Rechercher un Pokémon")
pokemon_name = st.text_input("Entrez le nom d'un Pokémon")
pokemon_data = asyncio.run(get_pokemon_data(pokemon_name))
if st.button("Rechercher"):
    
    if pokemon_data:
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(pokemon_data['sprite'], caption=pokemon_data['name'], width=150)
        with col2:
            st.write(f"**Nom**: {pokemon_data['name']}")
            st.write(f"**HP**: {pokemon_data['hp']}")
            st.write(f"**Attack**: {pokemon_data['attack']}")
            st.write(f"**Defense**: {pokemon_data['defense']}")
            st.write(f"**Speed**: {pokemon_data['speed']}")
    else:
        st.error("Pokémon non trouvé !")

st.header("Comparaison de Pokémon")
col1, col2 = st.columns(2)
with col1:
    pokemon1 = st.text_input("Pokémon 1")
with col2:
    pokemon2 = st.text_input("Pokémon 2")
if st.button("Comparer"):
    comparison = asyncio.run(comparaison(pokemon1, pokemon2))
    if comparison:
        col1, col2 = st.columns(2)
        with col1:
            st.image(comparison['pokemon1_sprite'], caption=comparison['pokemon1_name'], width=150)
                # if comparison.get('pokemon1_sprite') else st.write('Image non disponible')
            st.write(f"{comparison['pokemon1_name']}")
            st.write(f"HP: {comparison['pokemon1_hp']}")
            st.write(f"Attack: {comparison['pokemon1_attack']}")
        with col2:
            
            st.image(comparison['pokemon2_sprite'], caption=comparison['pokemon2_name'], width=150)
            st.write(f"{comparison['pokemon2_name']}")
            st.write(f"HP: {comparison['pokemon2_hp']}")
            st.write(f"Attack: {comparison['pokemon2_attack']}")
        st.success(f"Le Pokémon le plus fort est : {comparison['stronger']}")
      
    else:
        st.error("Comparaison impossible.")

st.header("Simuler un Combat")
if st.button("Lancer le combat"):
    battle_result = asyncio.run(simulate_combat(pokemon1, pokemon2))
    if battle_result:
        col1, col2 = st.columns(2)

        with col1:
         st.image(battle_result['combatant1_sprite'], caption=battle_result['pokemon1'], width=150)
         st.write(f"{battle_result['pokemon1']} inflige {battle_result['p1_damage']} dégâts en 5 tours.")
        
        with col2:
         st.image(battle_result['combatant2_sprite'], caption=battle_result['pokemon2'], width=150)
         st.write(f"{battle_result['pokemon2']} inflige {battle_result['p2_damage']} dégâts en 5 tours.")

        st.success(f"Le vainqueur est : {battle_result['winner']} !")
    else:
        st.error("Impossible de lancer le combat. Vérifiez les noms des Pokémon.")
