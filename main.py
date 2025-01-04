from scraper import get_clean_text
from summarizer import summarize_text

def summarize_website(url):
    print("Extraction du contenu du site...")
    text = get_clean_text(url)
    print("Résumé du contenu...")
    summary = summarize_text(text)
    return summary

# Exemple d'utilisation
if __name__ == "__main__":
    website_url = input("Entrez l'URL du site web à résumer : ")
    print("Résumé du site web :\n")
    print(summarize_website(website_url))
