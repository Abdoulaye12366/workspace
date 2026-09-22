from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

print("--- GENERATEUR DE RAPPORT PDF ---")
nom_fichier = "Rapport_Expert.pdf"

# Création du document PDF
pdf = canvas.Canvas(nom_fichier, pagesize=letter)
pdf.setTitle("Rapport d'Expert Indépendant")

# Écriture du contenu textuel graphique
pdf.setFont("Helvetica-Bold", 20)
pdf.drawString(100, 700, "RAPPORT D'AUDIT TECHNIQUE")

pdf.setFont("Helvetica", 12)
pdf.drawString(100, 650, "Créateur : Habi - Expert Indépendant")
pdf.drawString(100, 630, "Statut du système : Totalement opérationnel et sécurisé.")
pdf.drawString(100, 610, "Outils validés : Python, Git, SQLite, Nmap, Flask.")

# Sauvegarde du fichier sur le disque
pdf.save()
print(f"✅ Fichier '{nom_fichier}' généré avec succès !")
