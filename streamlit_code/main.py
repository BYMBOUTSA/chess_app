# Script principal pour exécuter l'application

import streamlit as st
import pandas as pd

st.write("Hello world !")

player_name = st.text_input("Quel est votre nom ?", "Saisissez votre nom ici ...")

if st.button("value"):
    st.success(player_name)

# Faire appel à l'API lichess pour recevoir des données sur les 50 dernières partie d'échecs du joueur.
