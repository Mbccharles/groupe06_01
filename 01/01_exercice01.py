# programme qui demande le prénom, l’âge, la ville et le métier d’un utilisateur, puis
# affiche un mini profil structuré.

# Demande d'informations à L'utilisateur
prenom = input ("Entrez votre prénom : ")
age = int (input ( "Entrez votre âge : "))
ville = input ("Entrez votre ville : ")
metier = input ("Entrez votre métier : ")

# Approximation des jours vécus
jours_vécus = age* 365

# Affichage formaté
print ("\n=== PROFIL UTILISATEUR ===" )
print (f"Prénom: {prenom}")
print (f"Âge : {age} ans ({jours_vécus} jours vécus environ)")
print (f"Ville : {ville}")
print (f"Métier: {metier}")