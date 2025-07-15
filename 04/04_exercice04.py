# Demander l’ancienneté (années) et la performance (note 1️ à 5️).
# • Si ancienneté ≥ 5️ ans →
#       Si performance ≥ 4️ → prime 2️000 €.
#       Sinon → prime 1️000 €.
# • Si ancienneté < 5️ ans →
#       Si performance ≥ 4️ → prime 5️00 €.
#       Sinon → pas de prime.

# Données
anciennete = int(input("Années d'ancienneté : "))
note = int(input("Note de performance (1-5) : "))
if anciennete >= 5:
    if note >= 4:
        prime = 2000
    else:
        prime = 1000
else:
    if note >= 4:
        prime = 500
    else:
        prime = 0
print(f"Prime attribuée {prime} $.")
