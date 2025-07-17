# Exercice 2 — Conversion sûre
valeur = input("Entrez un entier :")
try:
    entier = int(valeur)
except ValueError:
    print("Erreur : Ce n'est pas un entier valide.")
else:
    print(f"Vous avez entré l'entier {entier}")
