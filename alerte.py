import os

print("Exécution de l'action principale...")

# Commande native via Termux:API pour envoyer une notification avec le paramètre sonore d'Android
titre = "Notification Expert"
contenu = "L'opération s'est déroulée avec succès !"
os.system(f'termux-notification --title "{titre}" --content "{contenu}" --sound')

print("🔊 Alerte système déclenchée !")
