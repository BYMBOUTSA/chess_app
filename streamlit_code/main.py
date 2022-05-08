# Script principal pour exécuter l'application

import streamlit as st
import pandas as pd

# Our imports
from lichess_api.games_data import get_games_from_player

st.write("Hello world !")

player_name = st.text_input("Quel est votre nom ?", "Saisissez votre nom ici ...")

if st.button("value"):
    st.success(player_name)

    # Faire appel à l'API lichess pour recevoir des données sur les 50 dernières partie d'échecs du joueur.
    df = get_games_from_player(player_name, 50)

    # Show the result
    st.dataframe(df)

