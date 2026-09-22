print("--- OUTIL DE CHIFFREMENT DE CESAR ---")

mode = input("Voulez-vous (1) Chiffrer ou (2) Déchiffrer ? : ")
message = input("Entrez votre message (sans accents) : ")
cle = int(input("Entrez la clé de décalage (un nombre, ex: 3) : "))

if mode == "2":
    cle = -cle # Pour déchiffrer, on décale dans le sens inverse

message_final = ""

for lettre in message:
    if lettre.isalpha(): # On ne chiffre que les lettres
        base = ord('a') if lettre.islower() else ord('A')
        # Calcul du décalage circulaire dans l'alphabet
        nouvelle_lettre = chr((ord(lettre) - base + cle) % 26 + base)
        message_final += nouvelle_lettre
    else:
        message_final += lettre # On garde les espaces et symboles intacts

print(f"\nRésultat : {message_final}")

