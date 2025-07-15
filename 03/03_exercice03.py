# Programme qui demande la valeur d'un panier. Si le montant est :
# • ≥ 1️00 $ → Livraison gratuite.
# • Entre 5️0 $ et 99.99 $ → Livraison 5️ $.
# • < 5️0 $ → Livraison 1️0 $.

# Données
panier = float(input("Montant du panier ($) : "))

# Conditions
if panier >= 100:
    frais = 0
elif panier >= 50:
    frais = 5
else:
    frais = 10

# Affichage
total= panier + frais
print(f"Frais de livraison : {frais} $")
print(f"Total à payer : {total:.2f} $")