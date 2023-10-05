##
## Algo1 sur les listes : dans un fichier listes.py
##
## Ecrire une fonction qui prend un tableau en paramètre et vérifie que la liste ne contient que des entiers:
##   - Paramètres : une liste
##   - retour : un boolean, True si la liste ne contient que des int, False sinon
## -> écrire le code de la fonction, mais aussi la fonction "proprement" (un nom compréhensible, la docstring, une belle indentation)
##
## Ecrire une fonction qui prend en paramètre une liste, qui vérifie si la liste ne contient bien que des int, et renvoie :
##   - 0 si la liste contient autre chose que des entiers
##   - la valeure maximale de la liste
##

def neContientQueDesInt(l):
    """
    Cette fonction contrôle une liste et vérifie qu'elle ne contient que des valeurs de type int
    :param l: la liste que l'on veut controler
    :return: True si la liste ne contient que des int ou est vide, False sinon
    """
    for elt in l:
        if type(elt) != type(1):
            return False
    return True

def indexListe(l,eltATrouver):
    """
    Recherche l'index d'un élement dans la liste
    :param l: la liste dans laquelle on cherche
    :param elt: l'élement que l'on cherche
    :return: l'index de l'élément recherché, ou -1 si il n'est pas trouvé
    """
    index = 0
    for elt in l:
        if elt == eltATrouver:
            return index
        index = index + 1
    return -1

def maxListe(l):
    """
    Cette fonction renvoie le plus grand élément de la liste, si cette dernière ne contient que des int.
    Si un élement n'est pas int, la fonction renvoie 0.
    Si la liste est vide, la fonction renvoie 0.

    :param l: la liste où chercher le maximum
    :return: le plus grand élément de la liste si elle ne contient que des int, 0 sinon
    """
    if len(l) == 0:
        return 0
    if not neContientQueDesInt(l):
        return 0
    # Si on arrive ici, c'est que la liste ne contient que des int
    max = l[0]
    for elt in l:
        if elt > max:
            max = elt
    return max


def tests():
    testsTrue = [
        [1,2,3,4,5,6,7],
        [234, 43, 5, 6466, 2, 244, 2, 65, 23],
        []
    ]
    testsFalse = [
        ["h", "l", "u", "g"],
        [1, 2, 3, "g"],
        [1, 2, 3, ","]
    ]


    for jeuTest in testsTrue:
        if not neContientQueDesInt(jeuTest):
            print("Un test ne passe pas: ",jeuTest)

    for jeuTest in testsFalse:
        if neContientQueDesInt(jeuTest):
            print("Un test ne passe pas: ",jeuTest)


    tests = [
        [ [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10],
        [ [1, 21, 3, 4, 5, 6, 7, 8, 9, 10], 21],
        [ ["1", 21, 3, 4, 5, 6, 7, 8, 9, 10], 0],
        [ [-21, -3, -4, -5, -6, -7, -8, -9, -10], -3],
        [ [], 0]
    ]

    for jeuTest in tests:
        liste = jeuTest[0]
        resultatAttendu = jeuTest[1]
        resultat = maxListe(liste)
        if resultat != resultatAttendu:
            print("Erreur sur le tests avec ",liste, "attendu",resultatAttendu, "obtenu", resultat)

    print("Fin des tests !")