# Programme qui demande un mot de passe, vérifie :
# • ≥ 8 caractères
# • Contient au moins un chiffre
# • Contient au moins une majuscule

# Données
mdp = input("Entrez un mot de passe : ")

# Conditions
if len(mdp) >= 8 and any(c.isdigit() for c in mdp) and any (c.isupper() for c in mdp):
    print("Mot de passe valide.")
else :
    print ("Mot de passe invalide." )