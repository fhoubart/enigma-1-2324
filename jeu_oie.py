#import du package random pour la génération des nombres aléatoires
# On utilise ici import random pour importer tout le module random dans l'espace de nom et utiliser ensuite les
# fonctions du packages sous la forme random.randint.
# On aurai aussi pu faire "from random import randint" et appeler directement randint dans le code
import random
import math

########
# Modélisation du jeu
########

# Un Plateau, pour stocker où sont les cases particulières sous forme de tableau.
# Les joueurs ne sont pas stockées sur le plateau mais dans un tableau à part qui indique leur position
# Le plateau est un tableau d'entier, l'entier indique ce qu'il se passe sur les cases :
#  0 : case normale, rien de spécial
#  1 : case "oie", avancer une deuxième fois du même nombre de cases que ce qui vient d'être joué
#  2 : reculer de 5 cases
#  3 : case de fin, victoire

# Un tableau de joueurs
# Il stocke le numéro de case de chaque joueurs


def initialiserPlateau(nombresDeCases):
    """
    Initialise un plateau avec un nombre de case prédéfinie. Cela crée le tableau et met les bonnes valeurs pour
    les cases en fonction du type de case. Cette fonction met des cases oie toutes les 9 cases exceptée la première,
    et sur les autres aléatoirement avec une chance sur 10 une case pénalite
    :param nombresDeCases:
    :return:
    """
    plateau = []
    # Créer toutes les cases du plateau comme des cases simples
    for i in range(nombresDeCases):
        # Choix du type de case : on met 0 par défaut, et on test si il faut mettre une case spéciale
        typeDeCase = 0 # Case simple par défaut
        # Test si case oie
        if i%9 == 0 and i > 0:
            typeDeCase = 1
        else: # Si pas une case oie, une chance sur 10 d'être une case pénalité
            if random.randint(1,10) == 10:
                typeDeCase = 2

        # Ajout de la case dans le plateau
        plateau.append(typeDeCase)

    # Ajout de la case de fin
    plateau.append(3)
    return plateau


def initialiserJoueurs(nbJoueurs):
    """
    Initialise le tableau de joueurs
    :param nbJoueurs: le nombre de joueurs
    :return: le tableau initialisé avec les joueurs sur la case 0
    """
    joueurs = []
    for i in range(nbJoueurs):
        joueurs.append(0) # 0 car les joueurs commencent sur la case 0

    return joueurs


def lancerDe():
    """
    Renvoie un nombre aléatoire entre 1 et 6
    :return: un nombre aléatoire entre 1 et 6
    """
    return random.randint(1,6)

def lancerDeuxDe():
    """
    Lance deux dés
    :return: un nombre entier entre 2 et 12
    """
    return lancerDe() + lancerDe()


def avancer(plateau, joueurs, joueurQuiJoue, nbCases):
    """
    Fait avancer un joueur sur le plateau d'un nombre de case défini. Cette fonction s'occupe de vérifier si la case
    est spécial et de faire ce qui correspond.
    :param plateau: la plateau de jeu avec les positions des cases spéciales
    :param joueurs: Le tableau de joueurs
    :param joueurQuiJoue: L'index du joueur qui joue
    :param nbCases: Le nombre de case de combien il faut avancer le joueur qui joue
    :return: Rien, le tableau de joueurs est modifier en conséquences
    """
    positionJoueur = joueurs[joueurQuiJoue]
    nouvellePosition = positionJoueur + nbCases

    # Si le joueur dépasse la fin du plateau, il revient sur ses pas
    if nouvellePosition >= len(plateau):
        nouvellePosition = len(plateau)-1 - (nbCases - (len(plateau)-1-positionJoueur))

    # Si le joueur se retrouve avant le début, on le remet sur la première case
    if nouvellePosition < 0:
        nouvellePosition = 0

    joueurs[joueurQuiJoue] = nouvellePosition

    # Vérification si on est sur la même case qu'un autre joueur, si oui remettre l'autre joueur au début
    for i in range(0,len(joueurs)):
        # Le joueur qui joue est forcement sur la même case que lui même... On ignore ce cas
        if i != joueurQuiJoue:
            # On compare la position du joueur i (différent du joueur qui joue) avec la nouvelle position du joueur,
            # si c'est la même on met le joueur i au début
            if joueurs[i] == nouvellePosition:
                joueurs[i] = 0

    # Vérification des cases spéciales
    if plateau[nouvellePosition] == 1:
        # Case oie, on avance à nouveau du même nombre de cases
        avancer(plateau, joueurs, joueurQuiJoue, nbCases)
    elif plateau[nouvellePosition] == 2:
        # Case pénalité, on recule de 5 cases
        avancer(plateau, joueurs, joueurQuiJoue, -5)

    return

def partieTermine(plateau,joueurs):
    """
    Vérifie si la partie est terminée
    :param plateau: le plateau de jeu
    :param joueurs: le tableau des joueurs qui contient les positions
    :return: True si la partie est terminée, False sinon
    """
    for i in range(len(joueurs)):
        # On vérifie si le joueur est sur une case de type 3
        if plateau[joueurs[i]] == 3:
            return True
    # Si on arrive ici, aucun joueur n'a gagné
    return False

def quiAGagne(plateau, joueurs):
    """
    Vérifie si un joueur a gagné la partie
    :param plateau: le plateau de jeu
    :param joueurs: le tableau de joueurs qui contient les positions
    :return: -1 si aucun joueur n'a gagné, l'index du joueur qui a gagné si l'un deux à gagné
    """
    for i in range(len(joueurs)):
        if plateau[joueurs[i]] == 3:
            return i
    # Si on arrive ici, aucun joueur n'a gagné
    return -1

def indexJoueurSurUneCase(joueurs,case):
    """
    Cherche l'index du premier joueur présent sur une case
    :param joueurs: le tableau de joueurs
    :param case: la case sur laquelle on cherche un joueur
    :return: l'index du joueur sur la case s'il y en a un, -1 sinon
    """
    for i in range(len(joueurs)):
        if joueurs[i] == case:
            return i
    # Si on arrive ici, aucun joueur n'a gagné
    return -1


def afficherPlateau(plateau,joueurs):
    """
    Affiche le plateau en linéaire sous la forme :
    +---+---+---+---+---+---+---+
    |   | ! |   | O | 1 |   | 2 |
    +---+---+---+---+---+---+---+
    Avec :
      - ! pour les cases pénalité
      - O pour les cases oie
      - n pour le joueur n
    :param plateau: Le plateau de jeu
    :param joueurs: Le tableau de joueurs qui contient les positions
    :return: rien
    """

    # AFfichage de la première rangée de +---+---+---
    for i in range(len(plateau)):
        print("+---",end="")
    print("+")

    # Affichage du contenu des cases
    for case in range(len(plateau)):
        indexJoueurSurLaCase = indexJoueurSurUneCase(joueurs,case)
        if indexJoueurSurLaCase >= 0:
            # Il y a quelqu'un sur la case, on l'affiche
            print("| "+str(indexJoueurSurLaCase+1)+" ",end="")
        else:
            # Pas de joueur sur la case, on affiche le type de case
            if plateau[case] == 0:
                print("|   ",end="")
            elif plateau[case] == 1:
                print("| O ",end="")
            elif plateau[case] == 2:
                print("| ! ",end="")
            elif plateau[case] == 3:
                print("| V ",end="")

    print("|")

    # Affichage de la dernière rangée de "+---+---+---+---"
    for i in range(len(plateau)):
        print("+---", end="")
    print("+")


def afficherPlateauCarre(plateau,joueur,nbCasesParLignes):
    """
    Cette fonction affiche le plateau en carré en parcourant du bas en haut, de gauche à droite puis au dessus de
    droite à gauche et ainsi de suite
                +---+---+
                | 16| 15|
    +---+---+---+---+---+
    | 10| 11| 12| 13| 14|
    +---+---+---+---+---+
    | 9 | 8 | 7 | 6 | 5 |
    +---+---+---+---+---+
    | 0 | 1 | 2 | 3 | 4 |
    +---+---+---+---+---+
    La complexité réside dans le parcours en zigzag, et l'affichage de la première ligne qui n'est pas forcement
    complète.
    Le plateau étant stocké dans un tableau simple, il suffit pour chaque case de calculer les coordonnées dans le
    tableau plateau qui correspond. En sachant qu'on parcours du haut en bas (donc avec un numéro de ligne décroissant)
    et de gauche à droite (donc un numéro de colonne croissant). Le numéro de ligne modulo 2 donne si il faut compter
    en incrémentant ou en décrémentant.

    Pour la première ligne, il faut tester le numéro de la case pour savoir si on affiche une case ou un blanc.

    :param plateau: Le plateau de jeu
    :param joueur: Le tableau de joueurs qui contient leurs positions sur le plateau
    :return: rien
    """

    # Calcul du nombre de lignes nécessaire à l'affichage du plateau
    nbLignesNecessaires = math.ceil(len(plateau)/nbCasesParLignes)

    # On compte en décroissant, du nombre de lignes nécessaires à 0
    for ligneCourante in range(nbLignesNecessaires-1,-1,-1):

        # AFfichage de la première ligne de +----
        for rangeeCourante in range(nbCasesParLignes):

            # Caclul du numéro de la case dans plateau correspondant
            if ligneCourante % 2 == 0:
                # On va de gauche à droite
                case = ligneCourante*nbLignesNecessaires+rangeeCourante
            else:
                # On va de droite à gauche
                case = (ligneCourante+1)*(nbCasesParLignes)-1-rangeeCourante

            # On affiche des blancs et pas une case si on est en dehors du plateau
            if case == len(plateau):
                if ligneCourante % 2 == 0:
                    print("+   ",end="") # Caractère de fin de la case précédente (on va de gauche à droite)
                else:
                    print("    ",end="") # On va de droite à gauche => rien à gauche
            elif case > len(plateau):
                print("    ",end="")
            else:
                print("+---", end="")

        # A la fin de la boucle, on affiche le dernier caractère, qui peut être un blanc si on est en dehors du plateau
        if case < len(plateau):
            print("+")
        else:
            print("")

        # Affiche des cases
        for rangeeCourante in range(nbCasesParLignes):
            # La variable case contient les coordonnées dans le plateau
            if ligneCourante % 2 == 0:
                # On va de gauche à droite
                case = ligneCourante*nbLignesNecessaires+rangeeCourante
            else:
                # On va de droite à gauche
                case = (ligneCourante+1)*(nbCasesParLignes)-1-rangeeCourante

            # Si on est en dehors du plateau, on n'affiche rien
            if case == len(plateau):
                if ligneCourante % 2 == 0:
                    print("|   ", end="")  # Caractère de fin de la case précédente (on va de gauche à droite)
                else:
                    print("    ", end="")  # On va de droite à gauche => rien à gauche
            elif case > len(plateau):
                print("    ",end="")
            else:
                # Vérification de la présence d'un joueur sur la case => on affiche le numéro du joueur
                indexJoueurSurLaCase = indexJoueurSurUneCase(joueurs, case)
                if indexJoueurSurLaCase >= 0:
                    # Il y a quelqu'un sur la case, on l'affiche
                    print("| " + str(indexJoueurSurLaCase + 1) + " ", end="")
                else:
                    # Pas de joueur sur la case, on affiche le type de case
                    if plateau[case] == 0:
                        print("|   ", end="")
                    elif plateau[case] == 1:
                        print("| O ", end="")
                    elif plateau[case] == 2:
                        print("| ! ", end="")
                    elif plateau[case] == 3:
                        print("| V ", end="")

        # Affichage de la barre en fin de ligne, qui peut être blanche si on est en dehors du plateau
        if case < len(plateau):
            print("|")
        else:
            print("")

    # AFfichage de la dernière ligne de +----, avec les mêmes tests que la première (cas où il n'y a qu'une ligne
    # non complète
    for rangeeCourante in range(nbCasesParLignes):

        # Caclul du numéro de la case dans plateau correspondant
        if ligneCourante % 2 == 0:
            # On va de gauche à droite
            case = ligneCourante * nbLignesNecessaires + rangeeCourante
        else:
            # On va de droite à gauche
            case = (ligneCourante + 1) * (nbCasesParLignes) - 1 - rangeeCourante

        # On affiche des blancs et pas une case si on est en dehors du plateau
        if case == len(plateau):
            print("+   ", end="")
        elif case > len(plateau):
            print("    ", end="")
        else:
            print("+---", end="")

    # A la fin de la boucle, on affiche le dernier caractère, qui peut être un blanc si on est en dehors du plateau
    if case < len(plateau):
        print("+")
    else:
        print("")


##################
# programme main
##################

nbCases = int(input("Combien de cases sur le plateau ? "))
nbJoueurs = int(input("Combien de joueurs ? "))

plateau = initialiserPlateau(nbCases)
joueurs = initialiserJoueurs(nbJoueurs)

joueurCourant = 0

while not partieTermine(plateau,joueurs):
    print("###########################")
    print(f"##   Tour du joueur {joueurCourant+1}")
    print("###########################")

    afficherPlateauCarre(plateau,joueurs,5)

    print()

    resultatLancerDe = lancerDeuxDe()

    print(f"Le joueur {joueurCourant+1} a fait {resultatLancerDe}")
    input("Appuyer sur entrée pour continuer")

    avancer(plateau, joueurs, joueurCourant, resultatLancerDe)
    afficherPlateau(plateau,joueurs)

    input("Appuyer sur entrée pour passer au joueur suivant")

    joueurCourant = (joueurCourant + 1)%nbJoueurs

# Lorsqu'on sort de la boucle, la partie est terminée
print(f'Le joueur {(quiAGagne(plateau,joueurs)+1)} a gagné')
