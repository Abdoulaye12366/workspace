import requests
from bs4 import BeautifulSoup

print("--- ROBOT D'EXPLORATION DE LIENS ---")
url = "https://example.com"  # Vous pouvez changer pour un autre site

print(f"Connexion et analyse de {url}...")
html_recupere = requests.get(url)
analyse = BeautifulSoup(html_recupere.text, 'html.parser')

# Trouver toutes les balises de liens <a>
liens = analyse.find_all('a')

print(f"\n✅ {len(liens)} lien(s) détecté(s) sur la page :\n")

# Boucle pour afficher et stocker chaque lien trouvé
liste_liens = ""
for index, lien in enumerate(liens, start=1):
    adresse = lien.get('href')
    texte = lien.text.strip() if lien.text else "Texte vide"
    
    ligne = f"{index}. [{texte}] -> {adresse}\n"
    print(ligne, end="")
    liste_liens += ligne

# Sauvegarde des liens dans le fichier texte
with open("resultats.txt", "w", encoding="utf-8") as fichier:
    fichier.write(f"Liens extraits de {url} :\n" + liste_liens)

print("\n💾 Tous les liens ont été enregistrés dans 'resultats.txt'.")
