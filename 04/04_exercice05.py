# Demander le type de plat (viande, poisson, végétarien).
# Si viande → demander cuisson (saignant, à point, bien cuit).
# Si poisson → demander sauce (citron, beurre).
# Si végétarien → proposer salade ou pâtes.

# Données
plat = input("choisissez un plat (viande/poisson/végétarien) : ").lower()

# Conditions
if plat == "viande":
    cuisson = input("cuisson (saignant/à point/bien cuit) : ").lower()
    print(f"Vous avez choisi une viande {cuisson} .")
elif plat == "poisson":
    sauce = input("Sauce (citron/beurre) : ").lower()
    print(f"Vous avez choisi un poisson sauce {sauce} .")
elif plat == "végétarien":
    choix = input("souhaitez-vous une salade ou des pâtes? : ").lower()
    print (f"Vous avez choisi: {choix} .")
else:
    print("choix invalide.")
