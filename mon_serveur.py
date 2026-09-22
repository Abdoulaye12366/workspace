from flask import Flask, jsonify

app = Flask(__name__)

# 1. Route principale qui affiche un message texte
@app.route('/')
def accueil():
    return "<h1>Bienvenue sur le serveur de Habi !</h1><p>Statut : Expert Independent en cours de deploiement.</p>"

# 2. Une route API qui distribue des donnees au format de developpement (JSON)
@app.route('/api/statut')
def api_statut():
    donnees = {
        "nom": "Habi",
        "role": "Expert Independent",
        "outils_prets": ["Git", "Python", "Web Scraper", "Port Scanner"]
    }
    return jsonify(donnees)

if __name__ == '__main__':
    # Lance le serveur localement sur le port 5000
    app.run(host='0.0.0.0', port=5000)
