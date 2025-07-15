# Programme qui demande une liste d’entiers à l’utilisateur (saisie séparée par des espaces),
# puis calculer la somme des nombres pairs uniquement.

# Données
entree = input("Entrez des nombres séparés par des espaces : ")
liste = [int(x) for x in entree.split()]

# Initialisation
somme_pairs = 0

# Résultat
for nombre in liste:
    if nombre % 2 == 0:
        somme_pairs += nombre

# Affichage
print(f"\nsomme des nombres pairs {somme_pairs}")
