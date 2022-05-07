# Script principal pour exécuter l'application

import streamlit as st

st.write("Hello world !")

player_name = st.text_input("Quel est votre nom ?", "Saisissez votre nom ici ...")

if st.button("value"):
    st.success(player_name)