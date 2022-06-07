print("Calcul d'un prêt immobilier ou d'un crédit à la consommations.")
s = int(input("Entrer le montant du prêt ou crédit: "))       #somme prêt
t = int(input("Entrer le taux annuel en %: "))    ###taux annuel
n = int(input("Entrer le nombre d'années: "))   #nombre années
tm = t/100/12                                    #taux mensuel
a = (1+tm)**(12*n)
m = s*tm*a/(a-1)                                #mensualité avec intérêts


print("La mensualité avec intérêts est de ", m, "euros.")
print("Le montant des intérêts remboursés sont de", a, "euros.")
print("Le taux mensuel est de ", tm)
print("")
print("")
print("")
print("Tableau d'amortissement")
for i in range(1, s+1):
    ,vvofpjopj