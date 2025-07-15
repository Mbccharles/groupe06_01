# Programme qui demande une note sur 1️00 et attribue une mention :
# • ≥ 90 : Excellent
# • ≥ 75️ : Très Bien
# • ≥ 60 : Bien
# • ≥ 5️0 : Passable
# • < 50 : Insuffisant

# Données
note = float(input("Entrez votre note sur 100 : "))

# Conditions
if note >= 90:
    print("Mention : Excellent")
elif note >= 75:
    print("Mention : Très bien")
elif note >= 60:
    print("Mention : Bien")
elif note >= 50:
    print("Mention : Passable")
else:
    print("Mention : Insuffisant")
