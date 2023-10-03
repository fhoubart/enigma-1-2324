# Developper une petite calculatrice :
"""
Entrer le premier nombre : _
Entrer le deuxième nombre : _
Entrer l'opérateur (+, -, * ou /) : _
Le résultat de 2 + 3 est 5
"""
variable1 = int(input("Entrer le premier nombre : "))
variable2 = int(input("Entrer le deuxième nombre : "))
operator = input("Entrer l'opérateur (+, -, * ou /) : ")
operatorValide = True;

if operator == "+":
    resultat = variable1 + variable2
elif operator == "-":
    resultat = variable1 - variable2
elif operator == "*":
    resultat = variable1 * variable2
elif operator == "/":
    resultat = variable1 / variable2
else:
    print("L'opérateur n'est pas valide")
    operatorValide = False

if(operatorValide):
    print("Le résultat de " + str(variable1) + " " + operator + " " + str(variable2) + " est " + str(resultat))