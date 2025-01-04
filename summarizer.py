import os
import openai
from dotenv import load_dotenv

load_dotenv()  # Charger la clé depuis le fichier .env
openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_text(text):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",  # Ou un autre modèle comme gpt-4 si tu veux
        messages=[
            {"role": "system", "content": "Tu es un assistant qui résume des textes."},
            {"role": "user", "content": f"Voici un texte : {text}. Résume-le en 5 phrases."}
        ]
    )
    return response.choices[0].message.content.strip()

# Exemple d'utilisation
if __name__ == "__main__":
    example_text = "Ceci est un exemple de texte à résumer."
    print(summarize_text(example_text))
