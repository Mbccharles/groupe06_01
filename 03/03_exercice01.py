# Programme qui demande l'âge et le pays d'une personne, vérifie si elle peut s’inscrire à un programme

# Demande d'informations
age =int(input("Entrez votre âge : "))
pays =input("Entrez votre pays: ").lower()

# Condition
if age >= 18 and (pays=="congo" or pays=="cameroun"):
    print("Inscription autorisée.")
elif age < 18:
    print("Vous êtes trop jeune pour vous inscrire.")
else:
    print("Désolé, programme réservé aux ressortissants du Congo ou Cameroun.")