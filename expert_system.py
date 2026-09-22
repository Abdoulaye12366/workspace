import sqlite3
import os
from datetime import datetime

print("--- SYSTEME DE SÉCURITÉ DE HABI ---")
message = input("Entrez le message à chiffrer : ")
cle = 5  # Clé fixe pour notre automatisation

# 1. Chiffrement (César)
message_chiffre = ""
for lettre in message:
    if lettre.isalpha():
        base = ord('a') if lettre.islower() else ord('A')
        message_chiffre += chr((ord(lettre) - base + cle) % 26 + base)
    else:
        message_chiffre += lettre

print(f"\nRésultat du chiffrement : {message_chiffre}")

# 2. Sauvegarde automatique dans SQLite
connexion = sqlite3.connect("messages_secrets.db")
curseur = connexion.cursor()
curseur.execute("""
CREATE TABLE IF NOT EXISTS archives (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date_creation TEXT,
    message_original TEXT,
    message_code TEXT,
    cle_utilisee INTEGER
)
""")
curseur.execute("INSERT INTO archives (date_creation, message_original, message_code, cle_utilisee) VALUES (?, ?, ?, ?)", 
               (str(datetime.now()), message, message_chiffre, cle))
connexion.commit()
connexion.close()
print("💾 Données archivées dans SQLite.")

# 3. Notification sonore de succès
os.system('termux-notification --title "Système Habi" --content "Chiffrement et archivage réussis !" --sound')
print("🔊 Notification système envoyée.")
