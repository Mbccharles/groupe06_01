# Programme qui demande une chaîne à l’utilisateur et construit une nouvelle chaîne inversée
# à l’aide d’une boucle for.

# Données
texte = input("Entrez une chaîne : ")
inverse = ""

for char in texte:
    inverse = char + inverse  # On ajoute chaque caractère devant
print(f"chaîne inversée : {inverse} ")
