# Exercice 5 — Extraire éléments pairs d’une liste
entree = input("Entrez des nombres séparés par des espaces :")
liste = entree.split()
elements_pairs = liste[::2]
print(f"Éléments aux indices pairs {elements_pairs}")
