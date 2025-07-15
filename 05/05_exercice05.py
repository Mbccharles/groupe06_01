# Programme qui demande une liste de mots à l’utilisateur (saisie séparée par des espaces),
# Compte le nombre total de voyelles dans tous les mots.

# Données
mots = input("Entrez des mots séparés par des espaces :").split()
voyelles = "aeiouyAEIOUY"
total_voyelles = 0

# Processus
for mot in mots:
    for lettre in mot:
        if lettre in voyelles:
            total_voyelles += 1

# Affichage
print(f"Nombre total de voyelles : {total_voyelles}")
