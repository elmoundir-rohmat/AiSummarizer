import streamlit as st
from scraper import get_clean_text
from summarizer import summarize_text

# Interface Streamlit
st.title("Web Scraper et Résumeur")

# Saisie de l'URL par l'utilisateur
url = st.text_input("Entrez l'URL du site :")

if url:
    try:
        clean_text = get_clean_text(url)  # Scraping du site
        summary = summarize_text(clean_text)  # Résumé du texte
        st.subheader("Résumé du texte")
        st.write(summary)  # Affichage du résumé
    except Exception as e:
        st.error(f"Une erreur est survenue : {e}")
