from flask import Flask, render_template, request
from scraper import get_clean_text
from summarizer import summarize_text

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')  # Récupère l'URL soumise par l'utilisateur
        if url:  # Vérifie que l'URL n'est pas vide
            try:
                clean_text = get_clean_text(url)  # Scraping du texte
                summary = summarize_text(clean_text)  # Résumé du texte
                return render_template('index.html', summary=summary, url=url)  # Affiche le résumé dans le template
            except Exception as e:
                return f"Une erreur est survenue lors du scraping ou du résumé : {e}"
        else:
            return "Veuillez entrer une URL valide."

    return render_template('index.html')  # Affiche le formulaire vide si la méthode est GET

if __name__ == "__main__":
    app.run(debug=True)
