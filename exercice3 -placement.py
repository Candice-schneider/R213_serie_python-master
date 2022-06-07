print("Calcul d'intérêt annuel sur un placement.")
base = int(input("Entrez le capital de base du placement: "))
t = float(input("Entrez le taux d'intérêt en pourcentage: "))
n = int(input("Entrez le nombre d'année prévu pour le placement: "))
placement = int(input("Entrez le montant du placement mensuel: "))
if placement < 45:
    print("Le placement doit être au minimum de 45€/ mois. Veulliez entrer un nouveau montant.")
    placement = int(input("Entrez le montant du placement mensuel: "))

somme = 0
choix = str(input("choisissez le type d'intérêts sur votre placement(entrez: a pour annuel ou m pour mensuel): "))
if choix == "a":
    somme = base
    for i in range(0, n):
        somme = (somme + 12 * placement) * (1 + t/100)
        print("la somme total du capital à l'année ", i, " est de", round(somme, 2), "€.")
else:
    somme = base
    n = n * 12
    for i in range(0, n):
        somme = (somme + placement) * (1 + t/100/12)
        print("la somme total du capital au mois ", i, " est de", round(somme, 2), "€.")
