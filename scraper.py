import requests
from bs4 import BeautifulSoup

print("--- ROBOT DE SCRAPING AVANCE ---")
url = "https://google.com"

print(f"Connexion au site {url}...")
html_recupere = requests.get(url)
analyse = BeautifulSoup(html_recupere.text, 'html.parser')

balise_h1 = analyse.find('h1')
titre_onglet = analyse.title.text if analyse.title else "Aucun titre"

# Préparation du texte à sauvegarder
donnees_a_enregistrer = f"Résultats du scraping pour {url} :\n"
donnees_a_enregistrer += f"- Titre de l'onglet : {titre_onglet}\n"

if balise_h1:
    donnees_a_enregistrer += f"- Titre h1 : {balise_h1.text}\n"
else:
    donnees_a_enregistrer += "- Titre h1 : Aucun h1 trouvé sur cette page\n"

# Écriture automatique dans un fichier texte
with open("resultats.txt", "w", encoding="utf-8") as fichier:
    fichier.write(donnees_a_enregistrer)

print("\n✅ Extraction réussie ! Les données ont été sauvegardées dans 'resultats.txt'.")
