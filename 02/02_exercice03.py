# Petit "calculateur de factures" qui demande à l’utilisateur un montant HT et un taux
# de TVA, calculer et afficher le montant TTC.

# Données
montant_ht = float(input ("Montant HT ($) : "))
taux_tva = float (input ("Taux de TVA(%) : "))

# conversion en coefficient multiplicateur
taux_coef = taux_tva / 100

# Calcul TTC
montant_ttc = montant_ht * (1 + taux_coef)

# Affiche
print (f"\nMontant TTC {montant_ttc:.2f} $")