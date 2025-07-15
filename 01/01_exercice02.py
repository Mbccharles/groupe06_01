# mini "fiche produit" qui contient : nom, prix, stock, remise

# Définition des variables
nom_produit = "Ballon de foot"
prix= 20
stock= 100
remise= 0.1 # 15%
# calcul du prix final
prix_final =prix * (1 - remise)

# Affichage
print (f"Produit : {nom_produit}")
print (f"Prix initial : {prix} $")
print (f"Remise: {remise* 100}%")
print (f"Prix final : {prix_final: .2f} $")
print(f"Stock disponible: {stock}")