'''
        Auteur : Joël Dendaletche
        But : tracé une figure géométrique à l'aide de la bibliothèque Turtle
        Le projet utilise l'objet file pour itérer le calcul de chaque nouveau point
        Les coordonnées des points d'un polygone sont placés dans une file
        l'algorithme consiste à calculer les coordonnées d'un point pour tracer une droite qui part du premier points
        de la file et passe par le deuxième en prolongeant le segment d'une fraction déterminée de la longueur entre les
        deux points. Le deuxième point est remplacé par le nouveau. A la prochaine itération, le segment va partir du
        nouveau point pour passer par le suivant dans la file, qui sera remplacé par le nouveau point et ainsi de
        suite.
'''
import turtle

board = turtle.Turtle()

listePoints = [(0,0),(10,0),(5, int(10*75**.5)]
print(listePoints)
for x, y in listePoints :
    board.goto(x, y)

turtle.done()