print("Hello World!")

# Déclaration de variables
nomVariable = 2  # nomVariable est un entier
nomVariable = "Bonjour"  # nomVariable est une chaine de caractères
nomVariable = "2"

# Nom des variables
adlh2sgsfgj = 2 # A ne pas faire : mettre des noms qui signifient quelque chose
# 2 bonnes pratiques pour nommer les variables:
uneVariableQuiSertAQuelqueChose = 2  # CamelCase
une_variable_qui_sert_a_quelque_chose = 3  # avec des _

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

if b < 5:
    print("b < 5")
print("fin du if")

if b < 5:
    print("b < 5")
else:
    print("b >= 5 (via else)")

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

# Gestion des inputs : attention à convertir en entier avec int() si besoin d'un type numérique
#userInput = int(input("entrez la valeur de départ (entier):"))
#print(userInput + 3)


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



sapin(3)
sapin(10)

# 50 = 4*11 + 6
print(50 // 11) # 4
print(50 % 11)  # 6

# 10 = 2*5 + 0
print(10 // 5)
print(10 % 5)


# Les modules
# lien vers la doc python : https://docs.python.org/
# Aller dans "Library" et chercher ce qui vous interesse