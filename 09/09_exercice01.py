# Exercice 1 — Nettoyer un texte utilisateur
texte = input("Entrez un texte :")
texte = texte.strip().lower().replace(".", "!")
print(f"Texte nettoyé : {texte}")
