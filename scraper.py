import requests
from bs4 import BeautifulSoup

def get_clean_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for script in soup(["script", "style"]):
        script.decompose()
    return " ".join(soup.get_text().split())

# Exemple d'utilisation
if __name__ == "__main__":
    print(get_clean_text("https://royalcanin.com"))
