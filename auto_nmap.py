import subprocess

print("--- ROBOT D'AUTOMATISATION NMAP ---")
cible = "scanme.nmap.org"

print(f"Lancement d'un scan rapide sur {cible}...")

# Exécute la commande système nmap -F (scan rapide des 100 ports principaux)
commande = subprocess.run(["nmap", "-F", cible], capture_output=True, text=True)

# Récupération du résultat texte
resultat_scan = commande.stdout

# Affichage dans la console
print("\n[Rapport du Scan] :")
print(resultat_scan)

# Sauvegarde automatique dans un fichier texte
with open("rapport_nmap.txt", "w", encoding="utf-8") as fichier:
    fichier.write(resultat_scan)

print("✅ Rapport enregistré avec succès dans 'rapport_nmap.txt'")
