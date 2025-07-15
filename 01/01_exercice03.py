# script qui convertit une durée en secondes (entrée sous forme d'heures, minutes,
# secondes).

# Entrée utilisateur
heures= int (input ("Nombre d'heures : "))
minutes = int (input ("Nombre de minutes : "))
secondes= int (input ("Nombre de secondes : "))

# Conversion
total_secondes = heures * 3600 + minutes * 60 + secondes

# Résultat
print (f"\nDurée totale = {total_secondes} secondes.")