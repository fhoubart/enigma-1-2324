print("Hello World!")

# Déclaration de variables
nomVariable = 2  # nomVariable est un entier
nomVariable = "Bonjour"  # nomVariable est une chaine de caractères
nomVariable = "2"
variableBool = True # Type boolean

# Conversion de types
variableInt = int("2") # variableInt est un entier
print(variableInt * 2)  # -> 4
variableStr = str(2)
print(variableStr * 2) # -> 22

# Nom des variables
adlh2sgsfgj = 2 # A ne pas faire : mettre des noms qui signifient quelque chose
# 2 bonnes pratiques pour nommer les variables:
uneVariableQuiSertAQuelqueChose = 2  # CamelCase
une_variable_qui_sert_a_quelque_chose = 3  # avec des _
NOMBRE_DE_JOUEURS = 3 # constante en majuscule

print(nomVariable)
print(adlh2sgsfgj)
print(uneVariableQuiSertAQuelqueChose)
print(une_variable_qui_sert_a_quelque_chose)

# Opérateur +
# entre deux int : addition
# entre deux str : concatenation
a = nomVariable + "5"
b = uneVariableQuiSertAQuelqueChose + 5
print(a)
print(b)

# Opérateurs numériques
# + : addition
# - : soustraction
# * : multiplication
# / : division
# // : quotion de la division euclidienne
# % : modulo = reste de la division euclidienne, revient à compter en boucle
# ** : puissance

# Opérateurs chaines de caractères / listes :
# + : concaténation
# * : répétition de chaine

# Autres opérations numériques
print("Autres opérations numériques")
print(b * 4) # multiplication
print(b - 1) # soustraction
print(b / 2) # division
print(b ** 3) # puissance trois

# Opérateurs sur les str
print("Opérateurs sur les str (a=\"25\")")
print(a * 4) # Concaténation 4 fois de a
print(a+"4") # Concaténation


# Instructions conditionnelles
print ("Instructions conditionnelles")
print(b)

if b > 5:
    # Corps du if indenté
    print("b > 5")
# fin de l'indentation, on n'est plus dans le if

# If basic
if b < 5:
    print("b < 5")
print("fin du if")

# if else
if b < 5:
    print("b < 5")
else:
    print("b >= 5 (via else)")

# if avec plusieurs conditions
if b > 5:
    print("b>5")
elif b > 3:
    print("b est compris entre 3 et 5 (3 non inclus)")
else:
    print("b est inferieur ou égal à 3")


# Opérateurs de comparaison
print("Opérateurs de comparaison")
print(b == 7) # egalité
print(b > 7) # supérieur strict
print(b >= 7) # supérieur ou égale
print(b < 7)
print(b <= 7)
print(b != 7) # différent

print( b < 10 and b != 8)
print( b < 10 and b != 7)
print( b > 10 or b == 7)
print(b > 3 and (b > 10 or b == 7))

# Entrée/sortie

print("un message text") # afficher une chaine de caractère
print(b) # affiche une variable, en gérant le type de la variable (si b est un int, il sera converti automatiquement en str)
print(b, a, "du text")  # print affiche successivement ses différents paramètres séparés par un espace
print("La variable b est inférieur à 10 (b=" + str(b) + ")")
print(f'La vaiable b est inférieur à 10 ({b})') # formattage de chaine de caractères

# Gestion des inputs : attention à convertir en entier avec int() si besoin d'un type numérique
userInput = int(input("entrez la valeur de départ (entier):"))
print(userInput + 3)


# Boucle
print("Boucles")

print("boucle while")
b = 7
while(b > 3):
    print(b)
    b = b - 1
print("La boucle est finie")

print("boucle for")
for fruit in ['Banane', 'Pomme', 'Poire']:
    print(fruit)


# Bouclage avec un index
# On veut :
"""
Iteration 1
Iteration 2
Iteration 3
Iteration 4
Iteration 5
"""
i = 1
while(i <= 5):
    print("Iteration "+str(i))
    i = i + 1

for i in [1, 2, 3, 4, 5]:
    print("Iteration " + str(i))

for i in range(1,5):
    print("Iteration " + str(i))

range(5,1,-1) # Range décroissant : 5, 4, 3, 2
range(1,5,2)  # Range par pas de deux : 1, 3
range(5, 1, -2) # range décroissant par pas de deux : 5, 3

# Procédure : un ensemble d'instructions à exécuter en blocs
# Fonctions : renvoie une valeur
def sapin(n):
    for i in range(1, n + 1):
        print("*" * i)


def factorielle(n):
    """
    Factorielle(n) = n * (n-1) * (n-2) * ... * 4 * 3 * 2 * 1
    :param n: le nombre dont on veut calculer la factorielle
    :return: La factorielle du nombre passé en paramètre
    """
    # docstring
    f = 1
    for i in range(1,n+1):
        f = f * i

    return f


def factorielleRecursif(n):
    if n <= 1:
        return 1
    else:
        return n*factorielleRecursif(n-1)


def estPair(x):
    #if x % 2 == 0:
    #    return True
    #else
    #    return False
    return x % 2 == 0

def max(a,b):
    """
    Calcule le maximum entre les deux paramètres du même type
    :param a: la première valeur à comparer, peut importe le type
    :param b: La deuxième valeur à comparer, qui doit être du même type que a
    :return: Le max des deux valeurs
    """
    if a < b:
        return b
    else:
        return a

max(2,3)
a = 5
b = 8
x = 2
y = 3
c = max(x,y)

def tousLesPairs(x):
    for i in range(0, x+1):
        if estPair(i):
            print(i)

def tousLesPairs2(x):
    # On avance par pas de 2, donc tous les i sont pairs
    for i in range(0,x+1,2):
        print(i)



###########################
## Liste
###########################
# Documentation : https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range

tableau = ['Pomme', 'Banane', 'Poire', 3, 7]

# accède via des indexes des éléments
print(tableau[2])  # -> Poire
print(tableau[0])  # -> Pomme

# Parcourir tout le tableau
for i in tableau:
    print(i) # Pomme, puis Banane, puis Poire, puis 3, puis 7

print(tableau)
print(tableau[0:2])
print(tableau[0:3])
print(tableau[0:3:2])

tableau[4] = 'Cerise'
print(tableau)
#tableau[5] = 'Fraise' # ne fait rien, le tableau n'a pas d'élément d'index 5
#print(tableau)

tableau.append("Fraise")
print(tableau)

# Utiliser les tableau comme des stacks (piles)
print(tableau.pop())
print(tableau)


if 'Banane' in tableau:
    print("Il y a une banane dans le tableau, elle se trouve à l'index:")
    print(tableau.index('Banane'))

chaine = "Hello World"
print(chaine[1]) # e
print(chaine[0:5]) # Hello
# La chaine étant un tableau de lettres, on peut boucler dessus
for i in chaine:
    print(i)

tableauEntier = [1, 5, 2, 8, 4, 7, 6]
tableauEntier.sort()
print(tableauEntier)

# lien vers la doc python : https://docs.python.org/
# Aller dans "Library" et chercher ce qui vous interesse




