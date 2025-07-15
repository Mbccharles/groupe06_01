# Programme qui demande l’âge et la situation (étudiant, salarié, retraité).
# Détermine le tarif :
# • Moins de 1️8 ans → 5️ $
# • 18-2️5️ ans → étudiant : 6 $, salarié : 8 $
# • Plus de 2️5️ ans → retraité : 7 $, sinon 1️0 $

# Données
age = int(input("Âge : "))
statut = input("Statut (étudiant/salarié/retraité) : ").lower()

# Conditions
if age < 18:
    tarif = 5
else:
    if 18 <= age <= 25:
        if statut == "étudiant":
            tarif = 6
        elif statut == "salarié":
            tarif = 8
        else:
            tarif = 10  # cas inattendu
    else:
        if statut == "retraité":
            tarif = 7
        else:
            tarif = 10

# Affichage
print(f"Votre tarif est de {tarif} $.")
