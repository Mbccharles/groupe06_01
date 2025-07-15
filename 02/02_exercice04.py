# Programme qui demande trois notes (sur 2️0), calcule la moyenne et dit si l’étudiant
# est reçu (moyenne ≥ 1️0) ou non.

# Données
note1 = float(input("Première note : "))
note2 = float(input("Deuxième note : "))
note3 = float(input("Troisième note : "))

# Calcul de la moyenne
moyenne = (note1 + note2 + note3) / 3
print(f"Moyenne {moyenne:.2f}")

# Condition
if moyenne>= 10:
    print("L'étudiant est reçu.")
else :
    print("L'étudiant n'est pas reçu." )