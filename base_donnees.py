import sqlite3
from datetime import datetime

# 1. Connexion ou création automatique du fichier de base de données
connexion = sqlite3.connect("messages_secrets.db")
curseur = connexion.cursor()

# 2. Création de la table pour stocker les messages
curseur.execute("""
CREATE TABLE IF NOT EXISTS archives (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date_creation TEXT,
    message_original TEXT,
    message_code TEXT,
    cle_utilisee INTEGER
)
""")
connexion.commit()

print("--- BASE DE DONNEES ASSOCIEE ---")
print("1. Sauvegarder un message")
print("2. Voir l'historique des messages")
choix = input("Votre choix (1-2) : ")

if choix == "1":
    orig = input("Message d'origine : ")
    code = input("Message chiffré : ")
    cle = int(input("Clé utilisée : "))
    date_actuelle = str(datetime.now())

    # Insertion sécurisée des données
    curseur.execute("INSERT INTO archives (date_creation, message_original, message_code, cle_utilisee) VALUES (?, ?, ?, ?)", 
                   (date_actuelle, orig, code, cle))
    connexion.commit()
    print("✅ Entrée sauvegardée avec succès.")

elif choix == "2":
    curseur.execute("SELECT * FROM archives")
    lignes = curseur.fetchall()
    print("\n--- HISTORIQUE DES ARCHIVES ---")
    for ligne in lignes:
        print(f"ID: {ligne[0]} | Date: {ligne[1]}")
        print(f"   Original : {ligne[2]}")
        print(f"   Chiffré  : {ligne[3]} (Clé: {ligne[4]})\n")

connexion.close()
