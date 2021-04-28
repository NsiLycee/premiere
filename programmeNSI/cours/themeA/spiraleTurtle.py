""" auteur: Thierry Massart
    date : 10 avril 2018
    but du programme : trace avec turtle des spirales
"""

import turtle

def spirale(couleur, largeur, tours):
    """ Dessine avec turtle une spirale
    paramètres :
    - couleur : la couleur à utiliser
    - largeur : la largeur du tracé"""

    turtle.color(couleur)
    turtle.width(largeur)
    for i in range(4 * tours):
        turtle.circle(i*(largeur/2),90)

compteur = 1
sortir = False
while not sortir:
    turtle.reset()
    turtle.speed(0)
    spirale('red', 10, compteur)
    compteur += 2
    if compteur > 50 : sortir = True