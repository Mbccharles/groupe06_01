# Écrire un convertisseur de devises qui convertit un montant en dollars vers euros,
# francs CFA, et livres sterling.
# Taux : 1️ USD → 0,857 EUR, 1️ USD → 651️ CFA, 1️ USD → 0,743 GBP.

# Conversion
usd = float(input("Montant en USD : "))
eur = usd * 0.857
cfa = usd * 561
gbp = usd * 0.743

# Affichage
print(f"{usd} USD = {eur:.2f} EUR")
print(f"{usd}USD = {cfa:.2f} CFA")
print(f"{usd} USD {gbp:.2f} GBP")