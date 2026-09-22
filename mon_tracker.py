import requests
import sqlite3
from datetime import datetime

print("--- GEOLOCALISATEUR IP & ARCHIVAGE ---")
cible = input("Entrez l'adresse IP à localiser (ou Entrée pour votre IP) : ").strip()

url = f"http://ip-api.com{cible}"

try:
    print(f"Recherche des informations sur le serveur...")
    reponse = requests.get(url).json()

    if reponse.get("status") == "success":
        ip = reponse.get('query')
        pays = reponse.get('country')
        ville = reponse.get('city')
        isp = reponse.get('isp')

        print("\n=== INFORMATIONS LOCALISÉES ===")
        print(f"📍 Adresse IP  : {ip}")
        print(f"🌍 Pays        : {pays}")
        print(f"City: {ville}")
        print(f"🏢 Fournisseur : {isp}")

        # --- SAUVEGARDE AUTOMATIQUE DANS SQLITE ---
        connexion = sqlite3.connect("messages_secrets.db")
        curseur = connexion.cursor()

        # Création de la table si elle n'existe pas
        curseur.execute("""
        CREATE TABLE IF NOT EXISTS historique_ip (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date_recherche TEXT,
            ip TEXT,
            pays TEXT,
            ville TEXT,
            fournisseur TEXT
        )
        """)

        # Insertion des données de géolocalisation
        curseur.execute("""
        INSERT INTO historique_ip (date_recherche, ip, pays, ville, fournisseur) 
        VALUES (?, ?, ?, ?, ?)
        """, (str(datetime.now()), ip, pays, ville, isp))

        connexion.commit()
        connexion.close()
        print("\n💾 Recherche enregistrée avec succès dans la base de données.")

    else:
        print(f"\n❌ Erreur : Impossible de localiser cette cible ({reponse.get('message')})")

except Exception as e:
    print(f"\n❌ Erreur de connexion réseau : {e}")
