from random import *
from listes import indexListe,tests

repas = [ 'Kebab', 'Pizza', 'Sandwitch', 'Rien', 'Burger']

print("Le Sandwitch est à l'index "+str(indexListe(repas,'Sandwitch')))


repasDuJour = choice(repas)
print("Ajourd'hui on mange : "+repasDuJour)

de = randint(1,6)
print("Lancé de dé " + str(de))


##
## Utiliser le module random et le module statistics
## Ecrire :
##   - Une fonction lancerDe() -> renvoie un entier entre 1 et 6
##   - Une fonction LancerDeMultiple(n) -> renvoie un tableau de n éléments, chacuns étant un entier entre 1 et 6
##      indice : pensez à utiliser liste.append() pour ajouter un elt à une liste
##   - controleDe qui va lancer le dé 1000 fois et afficher la valeur moyenne obtenue
##      indice : lisez la doc ! https://docs.python.org/3/library/statistics.html
##