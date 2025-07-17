# Exercice 2 — Vérifier un email
email = input("Entrez votre email ")
if email.endswith("@gmail.com"):
    print("Email valide (Gmail).")
else:
    print("Email invalide ou non Gmail.")
