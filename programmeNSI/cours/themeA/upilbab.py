"""

        Corrigés d'Upilab

"""
motClefsPython = ["False", "None", "True", "and", "as", "assert", "async", "await", "break", "class",
                  "continue", "def", "del", "elif", "else", "except", "finally", "for", "from", "global",
                  "if", "import", "in", "is", "lambda", "nonlocal", "not", "or", "pass", "raise", "return",
                  "try", "while", "with", "yield"]
def VF( booleen : bool) -> bool :
    "traduction en mots de la valeur d'un booléen."
    return "vrai" if booleen else "faux"

def upilab4_3_5 () :
    """4.3.5. Exercice UpyLaB 4.2 - Parcours vert bleu rouge
Attention : cet exercice est composé de l'exercice UpyLaB 4.2.a suivi en dessous de l'exercice UpyLaB 4.2.b.
Le Petit Prince vient de débarquer sur la planète U357, et il apprend qu'il peut y voir de belles aurores boréales !
La planète U357 a deux soleils : les étoiles E1515 et E666.  C'est pour cela que les tempêtes magnétiques sont
permanentes, ce qui est excellent pour avoir des aurores boréales.
Par contre, il y fait souvent jour, sauf bien évidemment quand les deux soleils sont couchés en même temps.
Heureusement pour nous, une journée U357 s'écoule sur 24 heures comme sur notre Terre, et pour simplifier, nous ne
prendrons pas en compte les minutes (on ne donne que les heures avec des valeurs entières entre 0 et 23).
Nous vous demandons d'aider le Petit Prince à déterminer les périodes de jour et de nuit.
UPYLAB 4.2A
Pour cela, vous allez dans un premier temps écrire une fonction soleil_leve qui, pour un soleil particulier, reçoit
trois valeurs entières en argument pour la planète :
     - l'heure de lever du soleil (entre 0 et 23)
     - l'heure du coucher du soleil (entre 0 et 23)
     - l'heure actuelle (entre 0 et 23)
et qui renvoie une valeur booléenne vraie si le soleil est levé sur la planète à l'heure donnée en troisième argument
et fausse, s'il est couché.
On supposera que chacun des soleils ne se lève et ne se couche au plus qu'une seule fois par jour.
Il est toutefois possible que le lever ait lieu après l'heure du coucher, ce qui signifie dans ce cas que le soleil est
levé au début de la journée, puis qu'il se couche, puis qu'il se lève à nouveau plus tard dans la journée.
Enfin, si l'heure du lever est la même que l'heure du coucher :
     - soit toutes deux valent 12, cela signifie que le soleil ne se lève pas de la journée,
     - soit toutes les deux valent 0, cela signifie que le soleil ne se couche pas de la journée.

Exemple 1 : L'appel suivant de la fonction : soleil_leve(6, 18, 10) doit retourner True
Exemple 2 : L'appel suivant de la fonction : soleil_leve(15, 8, 12) doit retourner False
Exemple 3 : L'appel suivant de la fonction : soleil_leve(12, 12, 10) doit retourner False
Exemple 4 : L'appel suivant de la fonction : soleil_leve(0, 0, 22) doit retourner True
"""
    def soleil_leve(lever, coucher, heure) :
        if lever <= heure < coucher:
            return True
        elif (heure < lever or heure >= coucher) and coucher > lever:
            return False
        elif lever == coucher and lever == 0:
            return True
        elif lever == coucher:
            return False
        elif heure >= lever > coucher:
            return True
        elif heure < coucher < lever:
            return True
        else:
            return False
    print("Soleil levé : ",VF(soleil_leve(6, 18, 10)))
    try :
        assert soleil_leve(6, 18, 10)  == True
        print("1 soleil_leve(6, 18, 10)  a retourné True")
        assert soleil_leve(15, 8, 12)  == False
        print("2 soleil_leve(15, 18, 12)  a retourné False")
        assert soleil_leve(12, 12, 10) == False
        print("3 soleil_leve(12, 12, 10)  a retourné False")
        assert soleil_leve(0, 0, 10)   == True
        print("4 soleil_leve(0, 0, 10)  a retourné  True")
        assert soleil_leve(15, 8, 6)   == True
        print("5) soleil_leve(15, 8, 6) a retourné  True")
        assert soleil_leve(16, 10, 23) == True
        print("6) soleil_leve(16, 10, 23) a retourné True")
        assert soleil_leve(15, 8, 15)  == True
        print("7) soleil_leve(15, 8, 15) a retourné True")
    except :
        print("Fonction à parfaire !")

    def upilab4_2B () :
        """ Il vous faut maintenant écrire un programme qui lit en entrée :
. l'heure de lever du soleil E1515
. l'heure du coucher du soleil E1515
. l'heure de lever du soleil E666
. l'heure du coucher du soleil E666
et qui utilise la fonction soleil_leve pour afficher ligne par ligne chacune des heures de la journée, depuis 0 jusqu'à
23, suivies d'une espace et d'une astérisque s'il fait nuit à cette heure.
Attention, il ne fera nuit que si E1515 et E666 sont tous deux couchés.
Exemple 1 : Avec les données lues suivantes :
6
18
10
21
le résultat à imprimer vaudra donc
0 *     1 *   2 *   3 *    4 *    5 *   6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21 *   22 *  23 *
Exemple 2 :
Avec les données lues suivantes :
15
8
6
17
le résultat à imprimer vaudra donc
0  à 23 nuit"""
    leverE1515 = int(input("heure de levé de l'étoile E1515 :"))
    coucherE1515 = int(input("heure de couché de l'étoile E1515 :"))
    leverE666 = int(input("heure de levé de l'étoile E666 :"))
    coucherE666 = int(input("heure de couché de l'étoile E666 :"))

    for h in range(24):
        if soleil_leve(leverE1515, coucherE1515, h) or soleil_leve(leverE666, coucherE666, h):
            print(h)
        else:
            print(h, "*")

def upilab4_3_4 () :
    """
    ÉNONCÉ DE L'EXERCICE UPYLAB 4.1
    Écrire une fonction deux_egaux(a, b, c) qui reçoit trois nombres en paramètre et qui renvoie la valeur booléenne
    True si au moins deux de ces nombres ont la même valeur, et la valeur booléenne False sinon.
Ensuite, écrire un programme qui lit trois données de type int, x, y et z, et affiche le résultat de l’exécution de
deux_egaux(x, y, z).
Exemple 1
Avec les données lues suivantes :
1
2
3
le résultat à imprimer vaudra donc False
    """
    def deux_egaux(x, y, z):
        if x == y or x == z or y == z:
            return True
        return False

    x = int(input("Deux égaux au moins :\nDonner un nombre entier :"))
    y = int(input("Donner un deuxième nombre entier :"))
    z = int(input("Donner un troisième nombre entier :"))
    print("Dire qu'au moins deux des nombres suivant (",x,",",y,",",z,") sont égaux est ", VF(deux_egaux(x, y, z)))

def upilab3_5_14 () :
    """Écrire un programme qui lit un nombre entier strictement positif n et imprime une pyramide de chiffres de
    hauteur n (sur n lignes complètes, c'est-à-dire toutes terminées par une fin de ligne).
    La première ligne imprime un “1” (au milieu de la pyramide).
    La ligne i commence par le chiffre i % 10 et tant que l’on n’est pas au milieu, le chiffre suivant a la valeur suivante ((i+1) % 10).
    Après le milieu de la ligne, les chiffres vont en décroissant modulo 10 (symétriquement au début de la ligne).
Notons qu’à la dernière ligne, aucune espace n’est imprimée avant d’écrire les chiffres 0123....
Exemple 1
Avec la donnée lue suivante :     1
le résultat à imprimer vaudra :   1
Exemple 2
Avec la donnée lue suivante :     2
le résultat à imprimer vaudra :   1
                                 232
    :return:
    """
    n = int(input("donner le nombre de lignes :"))
    for li in range(1,n+1) :
        texte = (n - li) * "-"    # remplacer le symbole "-" par un espace " "
        compteur = 0
        for col in range( n - li , n ) :
            texte += str(( li + compteur ) % 10)
            compteur += 1
        compteur = li-1
        for col in range(n, n -li+1, -1) :
            compteur -= 1
            texte += str(( li + compteur ) % 10)
        print(texte)
########################################################################################################################
def quiz4_2_5 () :
    """ Ceci est le docstring c'est à dire l'aide qui s'affichera sur cette fonction si on exécute la fonction
    help(quiz4_2_5)
    Quiz sur la nommenclature des éléments d'un code python
    """
    introduction = "Avant d’examiner de plus près les possibilités et le fonctionnement des fonctions Python, ce quiz \
va vous aider à vérifier que vous avez bien assimilé ce que nous avons vu jusqu’ici.\n\n\
def pgcd(x, y):\n    ''' Calcule le pgcd de 2 nombres entiers positifs '''\n    while (y > 0):\n\
x, y  =  y, x % y\n    return x\n\n\
print('le pgcd de 112 et de 30 vaut : ', pgcd(112,30))\na = int(input('a = '))\nif pgcd(2*a, 6) == 2:\
    print('pgcd(a,12) : ', pgcd(a,12))\nelse:\n    print('pgcd(2*a, 6) différent de 2')"
    print (introduction + 50*"--")
    questions = ["","\"def\" est :", "\"pgcd\" est :",
                 "\"x\" est :","\"\"\" calcule le pgcd de 2 nombres entiers positifs \"\"\" est :",
                 "\"while\" est :", "\"%\" est :","\"return\" est :"]
    listeOptions = ["","Un mot-clé",
                    "Un nom de variable",
                    "Un nom de fonction",
                    "Un docstring",
                    "Un commentaire",
                    "Un autre élément"]
    correction = ["",
                  "La liste des mots clefs ou mots réservés de python est : "+str(motClefsPython),
                  "Le nom d'une fonction peut être écrit par concaténation de plusieurs mots,"+
        "en suivant de préférence les conventions Camel Case (cf. wiki), mais doit être différents des "+
        "mots clefs de python. (rèf : https://fr.wikipedia.org/wiki/Camel_case)",
                  "Le nom d'une variable (comme pour une fonction) peut être écrit par concaténation de"+
      " plusieurs mots, en suivant de préférence les conventions Camel Case (cf. wiki), mais doit être "+
      "différents des mots clefs de python ; le caractère '_' peut aussi être utilisé."+
        " (rèf : https://fr.wikipedia.org/wiki/Camel_case)",
                  "Le Docstring est un commentaire spécial qui est défini en début de fonction, "+
        "il est visible lorsque l'on utilise la fonction help (nom_fontion).",
                  "La liste des mots clefs ou mots réservés de python est : " + str(motClefsPython),
                  "% est un opérateur tout comme +,-,*,/,//,~,^,|,& et permet de réaliser un calcul sur des opérandes."+
        "(référence : https://fr.wikibooks.org/wiki/Programmation_Python/Op%C3%A9rateurs)",
                  "La liste des mots clefs ou mots réservés de python est : "+str(motClefsPython),
                  ]

    NLO = len(listeOptions) - 1     # nombre d'éléments de la liste des options de réponse
    # liste des numéros de bonnes réponses
    rep = [-1, 1, 3, 2, 4, 1, 6, 1]     # -1 ne sert qu'à occuper la position 0 (index 0)
    N = len(questions) - 1  # nombre de questions du quiz
    score = 0
    texteOptions = "Choisissez une réponse parmi :\n"
    for i in range(1,NLO+1) :
        texteOptions += str(i) + ") " + listeOptions [i] + "\n"

    for n in range(1, N + 1):
        print("\nQuestion n° "+ str(n) + " : " + questions[n])
        reponse = int(input(texteOptions+"\nVotre choix : ? "))
        if reponse == rep[n]:
            print("\n------------------------------------------------------------\nC'est bien ça !")
            score += 1
        else:
            print("\n------------------------------------------------------------\nEt non ! réfléchissez ...")
            print(correction[n]+"\n\n------------------------------------------------------------\n")

    print("Votre score est de ", score / N * 100, "% sur ", N, " questions.")




def quiz3_6_2 () :
    introduction = "Pour chacun des codes des questions suivantes, répondez 1 pour Vrai pour ceux qui produisent\n\
l'affichage suivant (et 0 pour Faux si ce n'est pas le cas) :\n2\n4\n6\n8\n"
    print (introduction + 50*"--")

    codes = ["", "for ma_variable_de_controle in range(2,10,2):\n    print(ma_variable_de_controle)",
             "i = 0\n\nwhile i < 8:\n    i = i + 2\n    print(i)",
             "for j in range(7):\n    if j % 2 == 0:        print(j+2)",
             "i = 2\n\nwhile i < 10:\n    print(i)\n    i = i + 2",
             "for i in range(4):\n    print(i * 2 + 2)",
             "j = 2\n\nfor i in range(4):\n    print(i)\n    j = j + 2"]
    rep = [0,1,1,1,1,1,0]
    N = len(codes)-1            # nombre de questions du quiz
    alternative = "\n   1 pour Vrai\n   0 pour Faux :"
    score = 0

    for n in range(1,N+1) :
        print("\n\n" + codes[n])
        reponse = int(input(alternative))
        if reponse == rep[n] :
            print ("\n------------------------------------------------------------\nC'est bien ça !")
            score += 1
        else : print ("\n------------------------------------------------------------\nEt non ! réfléchissez ...")

    print("Votre score est de ", score / N *100, "% sur ", N, " problèmes.")


def upilab3_5_13 () :
    """
On peut calculer approximativement le sinus d’un nombre x en effectuant la sommation des premiers termes de la série
(une série est une somme infinie) :
sin(x) = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + ...
où x est exprimé en radians et 3! désigne la factorielle de 3.
Écrire un programme qui lit une valeur flottante x en entrée et imprime une approximation de sin(x)
Cette approximation sera obtenue en additionnant successivement les différents termes de la série jusqu’à ce que la
 valeur du terme devienne inférieure (en valeur absolue) à une constante \epsilon que l’on fixera à 10^{-6}.
Exemple 1
Avec les données lues suivantes : 0.8
le résultat à imprimer vaudra  : 0.7173557231746032
"""
    x = float(input("Donner x, pour approximer sin(x) :"))
    terme = x
    somme = 0
    n = 1
    while abs(terme) > 1e-6 :
        somme += terme
        terme = (-1)**n * x**(2*n+1) / factoriel(2*n+1)
        print("sin(",x,") = ", somme, " terme = ", terme, "  ",2*n+1,"! = ", factoriel(2*n+1))
        n += 1;
    print(somme)

def factoriel( n : int ) -> int :
    """
    forme non récursive de factoriel
    :param n: entier positif
    :return: factoriel n
    """
    fact = 1
    for i in range(1,n+1) :
        fact *= i
    return fact

def upilab3_5_12 () :
    """
Écrivez un code qui lit un nombre entier strictement positif n et affiche sur n lignes une table de multiplication de
taille  n x n, avec, pour i entre 1 et n,  les n premières valeurs multiples de i strictement positives sur la ième
ligne.
Ainsi, les n premiers multiples de 1 strictement positifs (0 non compris) sont affichés sur la première ligne, les n
premiers multiples de 2 sur la deuxième, et cætera.
Exemple 1
Avec la valeur lue suivante : 3
le résultat à afficher sera :
1   2   3
2   4   6
3   6   9
    """
    n = int(input("Entrer un nombre entier > 1 : "))
    for li in range(1,n+1) :
        texte = ""
        for col in range(1, n+1) :
            texte += " " + str(li*col)
        print(texte)

def upilab3_15 () -> None:
    """Comme mes écureuils s’ennuyaient, je leur ai fabriqué une roue avec des barreaux pour qu’ils puissent faire de
    l’exercice. La roue fait 100 barreaux. Pour m’y retrouver, je les numérote de 0 à 99.
    Très vite je me suis rendu compte que chacun utilisait la roue en sautant toujours le même nombre de barreaux
    (Up saute 7 barreaux à chaque fois, Py en saute 9, LaB en saute 13, …).
Je mets une noisette sur un des barreaux de la roue. Aidez-moi à savoir si un de mes écureuils va l’attraper sachant
que je vais mettre l’écureuil qui fait le test, par exemple Up, sur le barreau 0 et que je connais son comportement
(Up saute toujours 7 barreaux à la fois) et le numéro de barreau, différent de 0, où se trouve la noisette (Up n’aura
donc pas la noisette au départ).
Écrire un programme qui teste si, pour une configuration donnée, un écureuil va ou non atteindre la noisette. Il reçoit
deux valeurs entières en entrée, une valeur saut et une valeur position_cible, toutes deux entre 1 et 99.

Le programme va calculer une valeur position_courante, initialement la valeur 0, et vérifier si en calculant de façon
répétitive la valeur position_courante, celle-ci aboutira un moment à la valeur position_cible.

Notez que pour calculer la valeur suivante de position_courante (initialement mise à 0), il faut incrémenter la valeur
 actuelle de position_courante de la valeur saut et ensuite, si le résultat est plus grand ou égal à 100, calculer la
 position en faisant un modulo 100 de la valeur obtenue (ce qui donne à chaque fois une valeur position_courante entre
 0 et 99). (Notez que l’on peut systématiquement faire le modulo 100 du résultat sans tester si position_courante est
 ou non supérieure à 100 pour obtenir sa bonne valeur).

Notez également, pour ne pas épuiser mon écureuil sans fin, que s’il atteint à nouveau la barreau 0, j’arrête
l’expérience sachant qu’il prendra toujours les mêmes barreaux sans jamais atteindre position_cible (la noisette).

À la fin votre programme dira si oui ou non la noisette a été atteinte ou non.

En pratique, après avoir lu les deux valeurs saut et position_cible, votre programme affichera chaque valeur de
position_courante sur une ligne différente à partir de la seconde valeur (sauf la position_courante initiale qui vaut
toujours 0). La dernière position_courante affichée sera soit 0 soit la dernière valeur de position_courante avant
qu’elle n’aie la valeur de position_cible, si l’écureuil trouve la noisette. Votre programme terminera en affichant,
sur une nouvelle ligne, le message donnant le résultat :

    "Cible atteinte" si l’écureuil a trouvé la noisette,

    "Pas trouvé" si l’écureuil est revenu en position 0 sans trouver la noisette.

Vous pouvez supposer que les valeurs lues sont bien des entiers qui respectent les consignes."""
    saut = int(input("Donner une valeur entre 1 et 99 (valeur du saut de l'écureuil) :"))
    position_cible = int(input("Donner une valeur entre 1 et 99 pour la position de la noisette :"))
    position_courante = -1
    trouve = False
    while position_courante != 0 and not trouve:
        if position_courante == -1: position_courante = 0

        if position_courante % 100 == position_cible:
            print("Cible atteinte")
            trouve = True
        else:
            position_courante += saut
            position_courante %= 100
            if position_courante != position_cible:
                print(position_courante)

    if not trouve: print("Pas trouvé")

def upilab3_10 () :
    """
    Écrire un programme qui calcule la taille moyenne (en nombre de salariés) des Petites et Moyennes Entreprises de
    la région.

Les tailles seront données en entrée, chacune sur sa propre ligne, et la fin des données sera signalée par la
valeur sentinelle -1. Cette valeur n’est pas à comptabiliser pour le calcul de la moyenne, mais indique que l’ensemble
des valeurs a été donné.

Après l’entrée de cette valeur sentinelle -1, le programme affiche la valeur de la moyenne arithmétique calculée.

On suppose que la suite des tailles contient toujours au moins un élément avant la valeur sentinelle -1, et que toutes
ces valeurs sont positives ou nulles.
    """
    somme, valeur, n = 0, 0, -1
    while valeur >= 0:
        n += 1
        somme += valeur
        valeur = int(input())

    print(somme / n)

def upilab3_13 () :
    """
    Écrire un programme qui additionne des valeurs naturelles lues sur entrée et affiche le résultat.
    La première donnée lue ne fait pas partie des valeurs à sommer. Elle détermine si la liste contient
    un nombre déterminé à l’avance de valeurs à lire ou non :

    si cette valeur est un nombre positif ou nul, elle donne le nombre de valeurs à lire et à sommer ;

    si elle est négative, cela signifie qu’elle est suivie d’une liste de données à lire qui sera terminée
    par le caractère "F" signifiant que la liste est terminée.
    """
    choix = int(input())
    somme, donnee = 0, 0
    if choix == -1:
        while donnee != 'F':
            donnee = input()
            if donnee != 'F':
                somme += int(donnee)
    else:
        for i in range(choix):
            somme += int(input())

    print(somme)
def upilab3_14 () :
    """
    Dans cet exercice, nous revenons sur le petit jeu de devinette.

    Écrire un programme qui génère de manière (pseudo) aléatoire un entier (nombre secret) compris entre 0 et 100.
     Ensuite, le joueur doit deviner ce nombre en utilisant le moins d’essais possible.

    À chaque tour, le joueur est invité à proposer un nombre et le programme doit donner une réponse parmi les
    suivantes :

    « Trop grand » : si le nombre secret est plus petit que la proposition et qu’on n’est pas au maximum d’essais

    « Trop petit » : si le nombre secret est plus grand que la proposition et qu’on n’est pas au maximum d’essais

    « Gagné en n essais ! » : si le nombre secret est trouvé

    « Perdu ! Le secret était nombre » : si le joueur a utilisé six essais sans trouver le nombre secret.
    """
    import random
    NB_ESSAIS_MAX = 6
    secret = random.randint(0, 100)
    n, rep, gagne = 0, -1, False
    while rep != secret and n < 6:
        rep = int(input())
        n += 1

        if rep == secret:
            print("Gagné en ", n, " essais !")
            gagne = True
        elif rep > secret and n < 6:
            print("Trop grand")
        elif rep < secret and n < 6:
            print("Trop petit")
        elif n == 6 and rep != secret:
            print("Perdu ! Le secret était", secret)

def upilab13_11et12 () :
    """
Cet exercice propose une variante de l’exercice précédent sur le carré de X.

Écrire un programme qui lit en entrée une valeur naturelle n et qui affiche à l’écran un triangle supérieur droit formé de X (voir exemples plus bas).
Exemple 1

Avec la donnée lue suivante : 6

le résultat à imprimer vaudra :
XXXXXX
 XXXXX
  XXXX
   XXX
    XX
     X
    """
    sortie = False
    while not sortie :
        choix = int(input("1) tracé d'un carré\n2) tracé d'un triangle décroissant vers la droite\n\
3) tracé d'un triangle décroissant vers la gauche\n4) tracé d'un triangle croissant vers la gauche\n\
5) tracé d'un triangle croissant vers la droite\n6 et plus) quitter\nchoix ? :"))
        if choix < 6 :
            n = int(input("Taille du coté :"))
        if choix == 1 :
            for i in range(n):
                print(n * 'X')
        elif choix == 2 :
            k = -1
            for i in range(n):
                k += 1
                print(k * ' ' + (n - k) * 'X')
        elif choix == 3:
            k = -1
            for i in range(n):
                k += 1
                print((n - k) * 'X' + k * ' ')
        elif choix == 4:
            k = n
            for i in range(n):
                k -= 1
                print( k * ' ' + (n - k) * 'X')
        elif choix == 5:
            k = n
            for i in range(n):
                k -= 1
                print((n - k) * 'X' + k * ' ')
        else :
            sortie = True
def upilab4_3_6 () :
    """L’exercice 4.3 d’UpyLaB vous propose une fonction assez classique à rédiger, qui teste si un nombre n , reçu en 
    paramètre, est premier.
Par définition, un nombre entier naturel est premier s’il est divisible (entièrement) uniquement par deux nombres 
différents, par 1 et par lui-même. 1 n’est pas premier. Le plus petit nombre premier est 2. Tous les nombres premiers 
suivants sont impairs puisque tous les nombres pairs sont divisibles par 2.
Il faut rédiger une fonction booléenne (dont le résultat est True ou False), qui reçoit un entier positif et renvoie 
True si et seulement si n est un nombre premier.
L’exercice n’a pas d’applications pratiques dans ce cours, mais comme le problème est assez simple, c’est l’occasion 
d’essayer d’être le plus succinct possible. L’extrait de code suivant peut servir de base. Il vous reste à compléter le 
corps de la fonction premier.
def premier(n):
    ''' renvoie vrai si n est un nombre premier'''
    ...
    return res
# code principal
print("liste des nombres premiers jusqu'à 100")
for i in range(100):
    if premier(i):
        print(i)
MODULO
Dans la fonction premier, il faut vérifier que n n’est divisible par aucun des nombres entiers à partir de 2 et 
strictement inférieurs à lui-même. Pour cela, notons que l’opérateur modulo peut être utile : le test n % i == 0 est 
vrai si i divise n entièrement.

NB : Il est toutefois intéressant de constater qu’il n’est en fait nécessaire de vérifier cette condition que pour les 
nombres entiers qui sont inférieurs ou égaux à la racine carrée du nombre n. Si vous souhaitez rendre votre code plus 
efficace en réduisant le nombre d’instructions exécutées, la fonction sqrt du module math s’avèrera utile ici.
ÉNONCÉ EXERCICE UPYLAB 4.3
Rédigez dans un script Python une fonction premier qui réalise le traitement expliqué précédemment, et le code qui
l’appelle. Ensuite, pour valider votre solution, modifiez votre code pour répondre à l’exercice 4.3 d’UpyLaB, dont voici
l'énoncé :
Écrire une fonction booléenne premier(n) qui reçoit un nombre entier positif n et qui renvoie True si n est un nombre 
premier, et False sinon.
Ensuite, écrire un programme qui lit une valeur entière x et affiche, grâce à des appels à la fonction premier, tous 
les nombres premiers strictement inférieurs à x, chacun sur sa propre ligne.
Exemple 1 : Avec la donnée lue suivante : 7
le résultat à imprimer vaudra donc 2
3
5
Consignes :
    Dans cet exercice, il vous est demandé d’écrire une fonction, puis un programme appelant cette fonction. Notez
    qu’UpyLaB testera ces deux points, en exécutant le programme entier mais aussi en appelant directement la fonction 
    avec les arguments de son choix.
    Plus précisément UpyLaB testera d'abord l'existence d'une définition de la fonction premier avec le bon nombre de
    paramètres.  Si la fonction existe bien, UpyLaB testera un programme qui réalise 2 appels à la fonction et réalise 
    deux print ; ceci pour vérifier que celle-ci n'effectue aucun print.  C'est en effet à votre programme d'effectuer 
    les print demandés. Ensuite différents tests de votre programme complet et de la fonction seront effectués par 
    UpyLaB.
    Il n’est pas demandé que la fonction premier teste le type du paramètre reçu, ni si sa valeur est bien positive ou 
    nulle.
    """
    listePremier = set()    # un set est un ensemble, c'est à dire un eliste sans doublon
    def premier(n : int) -> bool :
        """ teste si un nombre n est premier """
        if n < 2: return False
        if n in listePremier : return  True
        for i in range (2, int(n**0.5)+1) :
            if n % i == 0 : return False
        listePremier.add(n)
        return True

    n = int(input())
    for i in range(2,n):
        if premier(i):
            print(i)
def quiz4_4_1 () :
    """4.4.1. Quiz - Testez vos connaissances !
Dans cette section, avant de parler de règles de bonnes pratiques pour écrire nos codes Python, réalisons un petit quiz
sur ce que nous avons vu jusqu'ici dans ce module.  Qu'impriment les codes suivants ?
(Attention : un seul essai.)    """
    listeOptions = ["","2","4","8","16", "2 4", "4 8", "8 4", "4 2"]
    codes = ["def foo_1(x) :\n    print(2*x)\na = 4\nfoo_1(2*a)",
             "def foo_2(x) :\n    x = 2*x\na = 4\nfoo_2(2*a)\nprint(a)",
             "def foo_3(x) :\n    x = 2*x\nx = 4\nfoo_3(2*x)\nprint(x)",
             "def foo_4(x, y) :\n    x, y = y, x\na = 4\nb = 8\nfoo_4(a, b)\nprint(a, b)",
             "def foo_5(x, y) :\n    return  y, x\na = 4\nb = 8\na, b = foo_5(a, b)\nprint(a, b)",
             "def foo_6(x, y) :\n    return  y, x\na = 4\nb = 8\nfoo_6(a, b)\nprint(a, b)"
             ]
    reponses = [4,2,2,6,7,6]
    correction = [
        "a vaut initialement 4. foo_1 est appelée avec la valeur 8, x vaut donc 8 et 2*x, c'est-à-dire 16, est imprimé dans la fonction.",
        "Initialement la variable globale a vaut 4. foo_2 est appelée avec la valeur 8, la variable locale x "+
"à l'instance de foo_2 vaut donc 8 puis 2*x, c'est-à-dire 16. À la fin de l'exécution de foo_2, la variable locale x "+
"est détruite et il ne reste plus que la variable globale a qui vaut toujours 4.",
        "Initialement la variable globale x vaut 4. foo_3 est appelée avec la valeur 8, la variable locale x à "+
    "l'instance de foo_3 vaut donc 8 puis 2*x, c'est-à-dire 16. À la fin de l'exécution de foo_2, la variable locale x"+
"est détruite et il ne reste plus que la variable globale x qui vaut toujours 4.",
        "Initialement les variables globales a et b valent respectivement 4 et 8. foo_3 est appelée avec les valeurs "+
"4 et 8, les variables x et y, locales à l'instance de foo_4, valent donc respectivement 4 et 8. Ensuite l'exécution "+
"de foo_4 modifie les variables locales x et y mais pas les variables globales a et b qui donc restent avec les valeurs"+
" initiales 4 et 8 qui sont imprimées.",
        "Initialement les variables globales a et b valent respectivement 4 et 8. foo_5 est appelée avec les valeurs 4"+
" et 8. foo_5 renvoie le couple de valeurs 8 et 4. a reçoit la première valeur, c'est-à-dire 8, et b la seconde, soit "+
"4. Ensuite les nouvelles valeurs de a et de b sont imprimées, soit 8 et 4.",
        "Initialement les variables globales a et b valent respectivement 4 et 8. foo_6 est appelée avec les valeurs "+
"4 et 8. foo_6 renvoie le couple de valeurs 8 et 4, mais ces valeurs ne sont pas assignées à des variables par le code"+
" appelant. a et b restent inchangées et le print(a, b) imprime donc les valeurs 4 et 8."
    ]
    N = len(codes)



def upilab4_5_5() -> None :
    """
    ÉNONCÉ DE L'EXERCICE UPYLAB 4.4
Écrire une fonction alea_dice(s) qui génère trois nombres (pseudo) aléatoires à l’aide de la fonction randint du module
random, représentant trois dés (à six faces avec les valeurs de 1 à 6), et qui renvoie la valeur booléenne True si les
dés forment un 421, et la valeur booléenne False sinon.
Le paramètre s de la fonction est un nombre entier, qui sera passé en argument à la fonction random.seed au début du
code de la fonction. Cela permettra de générer la même suite de nombres aléatoires à chaque appel de la fonction, et
ainsi de pouvoir tester son fonctionnement.
Exemple 1 : L’appel suivant de la fonction : alea_dice(1) doit retourner : False
Exemple 2 : L’appel suivant de la fonction : alea_dice(25)doit retourner : True
    :return: rien
    """
    import random

    # tirage de trois dés à 6 faces
    def alea_dice(s):
        random.seed(s) # choix d'une série aléatoire déterminée
        tirage = []
        # trois tirages
        for i in range(3):
            tirage.append(random.randint(1, 6))
        tirage.sort()
        if tirage == [1, 2, 4]: return True
        return False

def upilab4_5_6 () -> None :
    """Note pour réaliser les exercices qui suivent
Certains exercices dont l’exercice UpyLaB suivant utilisent des valeurs de type tuple. Les tuples sont des séquences de
données qui seront étudiées en détail au module suivant. Pour réaliser les exercices de ce présent module, ayant des
valeurs v1 et v2 (par exemple int ou float), il faut juste savoir que :
    tuple() : renvoie un tuple vide
    (v1, ) : renvoie un tuple avec une composante de valeur v1
    (v1, v2) : renvoie un tuple avec les deux valeurs v1 et v2.
    …
Ainsi (2, 3, 5, 7, 11) est un 5-tuple (contient 5 valeurs).
ÉNONCÉ DE L'EXERCICE UPYLAB 4.5
-------------------------------
Considérons les billets et pièces de valeurs suivantes : 20 euros, 10 euros, 5 euros, 2 euros et 1 euro.
Écrire une fonction rendre_monnaie qui reçoit en paramètre un entier prix et cinq valeurs entières x20, x10, x5, x2 et
x1, qui représentent le nombre de billets ou de pièces de chaque valeur que donne un client pour l’achat d’un objet
dont le prix est mentionné.
La fonction doit renvoyer cinq valeurs, représentant le nombre de billets et pièces de chaque sorte qu’il faut rendre
au client, dans le même ordre que précédemment. Cette décomposition doit être faite en rendant le plus possible de
billets et pièces de grosses valeurs.
Si la somme d’argent avancée par le client n’est pas suffisante pour effectuer l’achat, la fonction retournera cinq
valeurs None.
Exemple 1 : L’appel suivant de la fonction : rendre_monnaie(38, 1, 1, 1, 1, 1) doit retourner : (0, 0, 0, 0, 0)
Exemple 2 : L’appel suivant de la fonction : rendre_monnaie(56, 5, 0, 0, 0, 0) doit retourner : (2, 0, 0, 2, 0)
Exemple 3 : L’appel suivant de la fonction :rendre_monnaie(80, 2, 2, 2, 3, 3) doit retourner : (None, None, None, None,
None)
    :return: rien
    """
    def rendre_monnaie(prix, x20, x10, x5, x2 , x1) :
        a_rendre = x20*20+x10*10+x5*5+x2*2+x1 - prix
        if a_rendre < 0 : return (None, None, None, None, None)
        else :
            y20 = a_rendre // 20
            a_rendre %= 20
            y10 = a_rendre // 10
            a_rendre %= 10
            y5 = a_rendre  // 5
            a_rendre %= 5
            y2 = a_rendre // 2
            y1 = a_rendre % 2

            return (y20, y10, y5, y2, y1)

def upilab4_5_7 () -> None :
    """Dans cet exercice, nous allons mettre en pratique la notion de valeur par défaut des paramètres d’une fonction.
Écrire une fonction somme(a, b) qui retourne la somme de deux valeurs entières a et b. Par défaut, la valeur de a est 0
et la valeur de b est 1.
Exemple 1 : L’appel suivant de la fonction : somme(24, 18) doit retourner : 42
Exemple 2 : L’appel suivant de la fonction : somme(4)      doit retourner :  5
Exemple 3 : L’appel suivant de la fonction : somme()       doit retourner :  1
    :return: rien
    """
    def somme (a =0, b=1) : return a+b

def upilab4_5_8 () -> None :
    """4.5.8. Exercice UpyLaB 4.7 - Parcours bleu rouge
Écrire une fonction rac_eq_2nd_deg(a, b, c) qui reçoit trois paramètres de type float correspondant aux trois
coefficients de l’équation du second degré ax^2 + bx + c = 0, et qui renvoie la ou les solutions s’il y en a, sous
forme d’un tuple.
Exemple 1 : l’appel suivant de la fonction : rac_eq_2nd_deg(1.0,-4.0,4.0) doit retourner : (2.0,)
Exemple 2 : L’appel suivant de la fonction : rac_eq_2nd_deg(1.0,1.0,-2.0) doit retourner : (-2.0, 1.0)
Exemple 3 : L’appel suivant de la fonction : rac_eq_2nd_deg(1.0,1.0,1.0)  doit retourner : ()
    :return: rien    """

    def rac_eq_2nd_deg(a : float, b: float, c: float) -> tuple :
        """        calcule les racines réelles de l'équation, si elles existent
        :param a: : float
        :param b: : float
        :param c: : float
        :return: tuple
        """
        det = b**2 - 4*a*c
        if det < 0      : solution = ()
        elif det == 0   : solution = (-b/2/a,)
        else            : solution = ((-b-det**0.5)/2/a , (-b+det**0.5)/2/a)
        return solution

def upilab4_5_9 () -> None :
    """4.5.9. Exercice UpyLaB 4.8 - Parcours bleu rouge
De Wikipedia (5 février 2019) :
En mathématiques, et plus particulièrement en combinatoire, les nombres de Catalan forment une suite d’entiers naturels
utilisée dans divers problèmes de dénombrement.
Ils sont nommés ainsi en l’honneur du mathématicien belge Eugène Charles Catalan (1814-1894).
Les dix premiers nombres de Catalan (pour n de 0 à 9) sont :
1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862.
Le nombre de Catalan d’indice n, appelé n-ième nombre de Catalan, est défini par :
C_n = \frac{(2n)!}{(n+1)!n!}
où n! désigne la factorielle de la valeur entière n :
n! = n(n-1)(n-2)...1
Par exemple, 5! = 5.4.3.2.1 = 120 et
C_4 = \frac{8!}{5! 4!} = 14
Le nombre de chemins sous-diagonaux les plus courts dans une grille de taille {n}\times{n}, le nombre de façons de
découper en triangles un polygone convexe à n+2 côtés, ou encore le nombre de configurations possibles d’expressions
avec n paires de parenthèses, appelé également mot de Dyck de longueur 2n, sont des exemples dont le résultat est donné
par le nombre de Catalan C_n.

Exemples d’applications de \mathbf{C_n} (ici, n = 4)
    Nombre de chemins sous-diagonaux les plus courts dans une grille de taille {n}\times{n}
https://studio.fun-mooc.fr/asset-v1:ulb+44013+session03+type@asset+block/chemins.jpg
    Nombre de façons de découper en triangles un polygone convexe de taille n + 2
https://studio.fun-mooc.fr/asset-v1:ulb+44013+session03+type@asset+block/catalan_hexagone.jpg
    Nombre de parenthésages possibles (mots de Dyck)
(((())))
((()()))
((())())
(()(()))
()((()))
(()()())
((()))()
()(()())
(())(())
(()())()
(())()()
()(())()
()()(())
()()()()
Nous vous demandons d’écrire une fonction catalan(n), où n est un nombre entier positif ou nul, qui renvoie la valeur
du  n-ième nombre de Catalan.
Exemple 1 : L'appel suivant de la fonction : catalan(5) doit retourner 42
Exemple 2 : L'appel suivant de la fonction : catalan(0) doit retourner  1
"""
    def catalan(n : int) ->int :
        """
        Calcul le nombre de Catalan pour n
        (n+2)*(n+3)* ... * 2n / (2 * 3 * ... * n)
        :param n:
        :return:
        """
        p = 1
        for x in range(n+2, 2*n+1) :
            p *= x
        for x in range(2,n+1) :
            p/= x
        return p

    for i in range(1,8) :
        print(i, "  ", catalan(i))

def upilab4_5_1 () :
    """4.5.10. Exercice UpyLaB 4.9 - Parcours bleu rouge
Cet exercice et le suivant vous demandent de programmer le petit jeu appelé « Pierre-feuille-ciseaux » ou
« Pierre-papier-ciseaux » (et qui porte encore d’autres noms comme indiqué dans la page Pierre-papier-ciseaux sur
 Wikipedia que nous utilisons pour rédiger l’énoncé ci-dessous).
Pierre-feuille-ciseaux est un jeu effectué avec les mains et opposant un ou plusieurs joueurs. Ici nous nous
supposerons qu’il y a deux joueurs : l’ordinateur et le joueur lui-même.
Déroulement du jeu
Les deux joueurs choisissent simultanément un des trois coups possibles en le symbolisant de la main :
    poing fermé : Pierre ;
    main ouverte, doigts collés les uns aux autres : Feuille ;
    main avec pouce, annulaire et auriculaire fermé, index et majeur ouvert en forme de V : Ciseaux.
Résultat du jeu :
    la pierre bat les ciseaux (en les émoussant),
    les ciseaux battent la feuille (en la coupant),
    la feuille bat la pierre (en l’enveloppant).
Ainsi chaque coup bat un autre coup, fait match nul contre le deuxième (son homologue) et est battu par le troisième.
Écrire une fonction bat(joueur_1, joueur_2) où joueur_1 et joueur_2 ont chacun une valeur entière 0, 1 ou 2, qui encode
ce que le joueur a fait comme coup (0 : PIERRE, 1 : FEUILLE, 2 : CISEAUX) qui renvoie un résultat booléen :
    vrai si joueur_1 bat le joueur_2 :
    faux si joueur_2 bat joueur_1 ou fait match nul contre lui.
Exemple 1 : L’appel suivant de la fonction : bat(0, 0) doit retourner : False
Exemple 2 : L’appel suivant de la fonction : bat(0, 1) doit retourner : False
Exemple 3 : L’appel suivant de la fonction : bat(2, 1) doit retourner True"""
    def bat(coup1, coup2) :
        """
        :param coup1:    0 Pierre >  2 ciseaux
        :param coup2:    2 > 1 feuille
        :return:
        """
        Pierre  = 0
        Feuille = 1
        Ciseaux = 2
        joueur1Gagne = False # si ex aequo   ou   2 < 0 ou 1 < 2 ou  0 < 1
        if (coup1 == Pierre  and coup2 == Ciseaux) or\
           (coup1 == Ciseaux and coup2 == Feuille) or\
           (coup1 == Feuille and coup2 == Pierre)      : joueur1Gagne = True
        return joueur1Gagne

def upilab4_5_11 () :
    """4.5.11. Exercice UpyLaB 4.10 - Parcours bleu rouge
Pierre-feuille-ciseaux (voir Pierre-papier-ciseaux sur Wikipedia) est un jeu effectué avec les mains et opposant un ou
plusieurs joueurs.
Déroulement du jeu : Les deux joueurs choisissent simultanément un des trois coups possibles en le symbolisant de la
main :
    poing fermé                                                                             : Pierre    = 0 ;
    main ouverte, doigts collés les uns aux autres                                          : Feuille   = 1 ;
    main avec pouce, annulaire et auriculaire fermé, index et majeur ouvert en forme de V   : Ciseaux = 2.
La pierre bat les ciseaux (en les émoussant), les ciseaux battent la feuille (en la coupant), la feuille bat la pierre
(en l’enveloppant). Ainsi chaque coup bat un autre coup, fait match nul contre le deuxième (son homologue) et est battu
 par le troisième.
Écrire un programme qui réalise 5 manches du jeu Pierre-feuille-ciseaux entre l’ordinateur et le joueur. Chaque manche
va consister en :
    la génération (pseudo) aléatoire d’un nombre entre 0 et 2 compris, à l’aide de la fonction randint du module random,
    qui va représenter le coup de l’ordinateur (0 valant Pierre, 1, Feuille et 2, Ciseaux) ;
    la lecture en entrée (input) d’une valeur entière entre 0 et 2 compris qui représente le coup du joueur ;
    l’affichage du résultat sous une des formes :

        coup_o bat coup_j : points
        coup_o est battu par coup_j : points
        coup_o annule coup_j : points
    où
        coup_o et coup_j sont respectivement le coup de l’ordinateur et du joueur : "Pierre" s’il a joué 0, "Feuille"
        s’il a joué 1 et "Ciseaux" s’il a joué 2.
        points donne le résultat des manches jusqu’à présent sachant que le compteur points part de zéro, et est
        incrémenté de un chaque fois que le joueur gagne une manche, et décrémenté de un chaque fois que l’ordinateur
        gagne une manche (les match nuls ne modifiant pas le compteur points).
À la fin des cinq manches, votre programme affichera : Perdu, Nul ou Gagné suivant que le compteur est négatif, nul ou
strictement positif.
Pour plus de clarté dans votre code, nous vous conseillons de définir les trois constantes symboliques :
PIERRE = 0
FEUILLE = 1
CISEAUX = 2
Par ailleurs, votre code doit importer le module random et, avant de commencer les manches, pour permettre à UpyLaB de
valider les résultats, il doit d’abord lire une valeur entière s et appeler la fonction random.seed(s). Vous devez donc
intégrer le code suivant :
import random
PIERRE = 0
FEUILLE = 1
CISEAUX = 2
...

s = int(input())
random.seed(s)

Votre code fera donc un appel à random.seed suivi de cinq appels à random.randint, un par manche. Aucun autre appel à
une fonction de random ne pourra être effectué.

Vous pouvez bien sûr utiliser la fonction bat de l’exercice 4.9 mais nous vous conseillons vivement de définir aussi
d’autres fonctions (par exemple , une fonction qui réalise une manche et imprime la ligne de message) pour structurer
votre code.
---------------------------------------------------
Exemple 1 : Sachant que le code suivant :
random.seed(65)
for i in range(5):
    print(random.randint(0,2))
donne le résultat : 1 1 1 2 0
l’exécution du code avec les entrées :65 0 1 2 1 0
doit afficher :
Feuille bat Pierre : -1
Feuille annule Feuille : -1
Feuille est battu par Ciseaux : 0
Ciseaux bat Feuille : -1
Pierre annule Pierre : -1
Perdu
---------------------------------------------------
Exemple 2 : Sachant que le code suivant :
random.seed(1515)
for i in range(5):
    print(random.randint(0,2))
------------------
donne le résultat : 2 1 0 2 2
l’exécution du code avec les entrées :1515 0 1 2 1 0
doit afficher :
Ciseaux est battu par Pierre : 1
Feuille annule Feuille : 1
Pierre bat Ciseaux : 0
Ciseaux bat Feuille : -1
Ciseaux est battu par Pierre : 0
Nul
--------------------------------------------------
Exemple 3 :
Sachant que le code suivant :
random.seed(2001)
for i in range(5):
    print(random.randint(0,2))
donne le résultat : 2 0 1 0 0
l’exécution du code avec les entrées :2001 0 1 2 1 0
doit afficher :
Ciseaux est battu par Pierre : 1
Pierre est battu par Feuille : 2
Feuille est battu par Ciseaux : 3
Pierre est battu par Feuille : 4
Pierre annule Pierre : 4
Gagné
"""
    def bat(coup1, coup2) :
        """
        :param coup1:    0 Pierre >  2 ciseaux
        :param coup2:    2 > 1 feuille
        :return:
        """
        Pierre  = 0
        Feuille = 1
        Ciseaux = 2

        gain = 0 # si ex aequo = 0  ou   2 < 0 ou 1 < 2 ou  0 < 1
        if (coup1 == Pierre  and coup2 == Ciseaux) or\
           (coup1 == Ciseaux and coup2 == Feuille) or\
           (coup1 == Feuille and coup2 == Pierre)      : gain =  1
        elif coup1 == coup2                            : gain =  0
        else                                           : gain = -1
        return gain
    def lien(gain) :
        """ renvoie le texte de liaison lié au gain """
        if   gain == 0    : texte = " annule "
        elif gain == 1    : texte = " bat "
        else              : texte = " est battu par "
        return texte

    import random

    Nom = ["Pierre", "Feuille", "Ciseaux"]
    seed = int(input())
    coupJ1 = []
    random.seed(seed)
    for i in range(5) :
        coupJ1.append(random.randint(0, 2))
    coupJ2 = []
    for i in range(5) :
        coupJ2.append(int(input()))

    score = 0
    for i in range(5) :
        gain = bat(coupJ1[i],coupJ2[i])
        score -= gain
        print(Nom[coupJ1[i]] + lien(gain) + Nom[coupJ2[i]] + " : " + str(score))

    if score == 0   : print("Nul")
    elif score > 0  : print("Gagné")
    else            : print("Perdu")
########################################################################################################################



def upilab5_1_6() -> None  :
    """5.1.6. Mise en pratique des séquences : exercice UpyLaB 5.1 - Parcours vert bleu rouge
Comme mise en bouche autonome pour ce module, faites l’exercice 5.1 d’UpyLaB. Cet exercice vous demande de mettre en
pratique la manipulation simple de tuples, dans ce cas des couples représentant des noms et prénoms.
Dans ce cours, nous dirons couple pour parler d’un tuple à deux composantes.
Notez que dans le projet, nous utiliserons des couples, c’est-à-dire des tuples à deux valeurs, pour représenter des
coordonnées de points dans un espace à deux dimensions.
ÉNONCÉ DE L’EXERCICE UPYLAB 5.1
Écrire une fonction signature qui reçoit un paramètre identite . Ce paramètre est un couple (tuple de deux composantes)
 dont la première composante représente un nom et la seconde un prénom.
Cette fonction doit retourner la chaîne de caractères formée du prénom suivi du nom, séparés par une espace.
Exemple : L’appel suivant de la fonction : signature(('de Saint-Exupéry', 'Antoine'))
doit retourner : 'Antoine de Saint-Exupéry'   """
    def signature(tuple : tuple) -> str :
        """ manipulation de tuple """
        nom, prenom = tuple
        return prenom + " " + nom
########################################################################################################################
def upilab5_1_7 () :
    """5.1.7. Exercice UpyLaB 5.2 - Parcours vert bleu rouge
On représente un brin d’ADN par une chaîne de caractères dont les caractères sont parmi les quatre suivants : 'A'
(Adénine), 'C' (Cytosine), 'G' (Guanine) et 'T' (Thymine).
Écrire une fonction est_adn qui reçoit une chaîne de caractères en paramètre et qui retourne True si cette chaîne de
caractères n'est pas vide et peut représenter un brin d’ADN, False sinon.
Exemple 1 : L’appel suivant de la fonction : est_adn("ATGGT") doit retourner : True
Exemple 2 : L’appel suivant de la fonction : est_adn("ISA")   doit retourner : False
Exemple 3 : L’appel suivant de la fonction : est_adn("CTaG")  doit retourner : False
"""
    ADN = "ATGC"

    def est_adn(sequence):
        if sequence == "": return False
        for car in sequence:
            if car not in ADN: return False
        return True
########################################################################################################################
def upilab5_1_8 () :
    """5.1.8. Exercice UpyLaB 5.3 - Parcours vert bleu rouge
Écrire une fonction duree qui reçoit deux paramètres debut et fin. Ces derniers sont des couples (tuples de deux
composantes) dont la première composante représente une heure et la seconde les minutes.
Cette fonction doit calculer la durée qui s’est écoulée entre ces deux instants. Le résultat sera donné sous la forme
d’un tuple (heure, minutes).
Exemple 1 L’appel suivant de la fonction : duree ((14, 39), (18, 45)) doit retourner : (4, 6)
Exemple 2 L’appel suivant de la fonction : duree ((6, 0), (5, 15))    doit retourner : (23, 15)
"""
    def duree(debut, fin) :
        h1, m1 = debut
        h2, m2 = fin
        heure1 = h1*60 + m1
        heure2 = h2*60 + m2
        if heure1 > heure2 : heure2 += 24*60
        intervalle = heure2 - heure1
        #h = intervalle // 60
        #m = intervalle % 60
        return intervalle // 60, intervalle % 60
########################################################################################################################
def upilab5_1_9() :
    """5.1.9. Exercice UpyLaB 5.4 - Parcours vert bleu rouge
Écrire une fonction distance_points() qui reçoit en paramètres deux tuples de deux composantes représentant les
coordonnées de deux points et qui retourne la distance euclidienne séparant ces deux points.
Pour rappel, la distance euclidienne entre les points (x_1, y_1) et (x_2, y_2) se calcule grâce à la formule :
dist = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}
où, si a désigne un nombre positif, \sqrt{a} désigne la racine carrée de a et correspond à a^{\frac{1}{2}}.
Exemple 1 : L’appel suivant de la fonction : distance_points((1.0, 1.0), (2.0, 1.0)) doit retourner : 1.0
Exemple 2 : L’appel suivant de la fonction : distance_points((-1.0, 0.5), (2.0, 1.0))
doit retourner (approximativement) :3.0413812651491097
"""
    def distance_points(p1, p2) :
        """ calcul de la distance entre deux points sur un plan z = 0 """
        x_1, y_1 = p1
        x_2, y_2 = p2
        return ((x_1 - x_2)**2 + (y_1 - y_2)**2)**0.5

########################################################################################################################
def upilab5_1_11() :
    """5.1.11. Exercice UpyLaB 5.5 - Parcours bleu rouge
Écrire une fonction longueur(*points) qui reçoit en paramètres un nombre arbitraire de points (tuples de deux
composantes), et retourne la longueur de la ligne brisée correspondante.
Cette longueur se calcule en additionnant les longueurs des segments formés par deux points consécutifs.
Exemple 1 : L’appel suivant de la fonction : longueur((1.0, 1.0), (2.0, 1.0), (3.0, 1.0))
doit retourner : 2.0
Exemple 2 : L’appel suivant de la fonction : longueur((0.5, 1.0), (2.0, 1.0), (2.5, -0.5), (-1.5, -1.0))
doit retourner (approximativement) : 7.1122677042334645
"""
    def distance_points(p1, p2) :
        """ calcul de la distance entre deux points sur un plan z = 0 """
        x_1, y_1 = p1
        x_2, y_2 = p2
        return ((x_1 - x_2)**2 + (y_1 - y_2)**2)**0.5

    def longueur (*points) :
        N = len(points)
        if N < 1 : l = 0
        else :
            l = 0
            p1 = points[0]
            for n in range(1,N) :
                l += distance_points(p1, points[n])
                p1 = points[n]
        return l


    print(longueur((0.5, 1.0), (2.0, 1.0), (2.5, -0.5), (-1.5, -1.0)) ," = ?", 7.1122677042334645)


########################################################################################################################
def upilab5_6 () :
    """ÉNONCÉ DE L’EXERCICE UPYLAB 5.6
Écrire une fonction transcription_arn(brin) qui reçoit une chaîne de caractères en paramètre, correspondant à un brin
d'ADN, et qui retourne une chaîne de caractère correspondant à la transcription ARN de ce brin.

Nous rappelons qu'un brin d'ADN peut être modélisé par une chaîne de caractères, dont les caractères sont pris parmi
les quatre suivants  : 'A'(Adénine), 'C' (Cytosine),'G' (Guanine) et 'T' (Thymine).
La transcription en ARN se traduit par le remplacement des nucléotides de Thymine par des nucléotides d'Uracile, que
l'on représentera par le caractère 'U'.
Exemple :L’appel suivant de la fonction : transcription_arn('AGTCTTACCGATCCAT')
doit retourner : 'AGUCUUACCGAUCCAU'               """
    def transcription_arn(brin) :
        transcrit = ""
        for car in brin :
            if car == 'T' :
                transcrit += 'U'
            else :
                transcrit += car
        return transcrit

########################################################################################################################
def upilab5_7 () :
    """5.2.6. Exercice UpyLaB 5.7 - Parcours vert bleu rouge
Écrire une fonction plus_grand_bord(w) qui reçoit un mot w et retourne le plus grand bord de ce mot.
On dit qu’un mot u est un bord du mot w si u est à la fois un préfixe strict et un suffixe strict de w, c’est-à-dire
qu’on retrouve le mot u au début et à la fin du mot w, sans que u soit égal à w lui-même.
Exemples : 'a' et 'abda' sont des bords de 'abdabda'. En effet, 'abdabda' commence et se termine par 'a', ainsi que par
'abda'. Le plus grand bord de 'abdabda' est 'abda'.

Si w n’a pas de bord, la fonction retourne la chaîne de caractères vide.
Exemple 1 : L’appel suivant de la fonction : plus_grand_bord('abdabda') doit retourner : 'abda'
Remarque : Notez que les apostrophes indiquent ici que l'objet retourné est de type str. Ces apostrophes ne font pas
partie de la chaîne de caractères elle-même.
Exemple 2 : L’appel suivant de la fonction : plus_grand_bord('abcabd') doit retourner : ''
Exemple 3 : L’appel suivant de la fonction : plus_grand_bord('abcba') doit retourner : 'a'
Exemple 4 : L’appel suivant de la fonction : plus_grand_bord('aaaaa') doit retourner : 'aaaa'
"""
    def plus_grand_bord( w ) :
        """ retourne le plus grand bord de ce mot w """
        bord = ""
        N = len(w)
        print("pour " + w)
        for i in range(1,N) :
            if w[:i] == w[N-i:N] :
                bord = w[:i]
            print("i = ", i, "N = ", N, "w[:i] =", w[:i], "w[N-i:N] = ", w[N - i:N])
        return "|" + bord + "|"

    print(plus_grand_bord('abdabda'), " est ce 'abda' ? ")
    print(plus_grand_bord('abcabd'), " est ce '' ? ")
    print(plus_grand_bord('abcba'), " est ce 'a' ? ")
    print(plus_grand_bord('aaaaa'), " est ce 'aaaa' ? ")
########################################################################################################################
def upilab5_2_7 () :
    """5.2.7. Exercice UpyLaB 5.8 - Parcours vert bleu rouge
Écrire une fonction prime_numbers qui reçoit comme paramètre un nombre entier nb et qui renvoie la liste des nb premiers
nombres premiers.
Si le paramètre n’est pas du type attendu, ou ne correspond pas à un nombre entier positif ou nul, la fonction renvoie None.
Exemple 1 : L’appel suivant de la fonction : prime_numbers(4) doit retourner : [2, 3, 5, 7]
Exemple 2 : L’appel suivant de la fonction : prime_numbers(-2)doit retourner : None
"""
    def prime_numbers(n) :
        """ renvoie les n premiers nombres premiers """
        if type(n) is not int or n < 0 : return None
        def isPremier (n) :
            premier = True
            for i in range (2, int(n**.5)+1) :
                if n % i == 0 : premier = False
            return premier
        listePremier = []
        compte = 0
        nb = 2
        while compte != n :
            if nb not in listePremier and isPremier(nb) :
                print("li = ", listePremier, "nb = ", nb)
                compte += 1
                listePremier.append(nb)
            nb += 1

        return listePremier

    print(4, "   ",prime_numbers(4))
    print(8, "   ",prime_numbers(8))

########################################################################################################################
def upilab5_4_5() :
    """5.4.5. Mise en pratique avec ou sans méthodes : exercice UpylaB 5.9 - Parcours vert bleu rouge
Une anagramme d’un mot v est un mot w qui comprend les mêmes lettres que le mot initial v, en même quantité, mais non
nécessairement dans le même ordre (par exemple, « marion » et « romina » sont des anagrammes). Notez que anagramme est
un mot féminin.
Écrire une fonction anagrammes(v, w) qui renvoie la valeur booléenne True si les mots v et w sont des anagrammes.
La fonction retourne la valeur booléenne False dans le cas contraire.
Exemple 1 : L’appel suivant de la fonction : anagrammes('marion', 'romina')     doit retourner : True
Exemple 2 : L’appel suivant de la fonction : anagrammes('bonjour', 'jour')      doit retourner : False
Exemple 3 : L’appel suivant de la fonction : anagrammes('pate', 'patte')        doit retourner : False
"""
    def palindromes (mot1, mot2) :
        """compare deux mots et renvoie vrai s'ils sont le palindrome l'un de l'autre"""
        n1, n2 = len(mot1), len(mot2)
        if n1 == n2 :
            i, rep = 0, True
            while rep and i < n1 -1 : # dès que rep est faux c'est fini !
                print(i, "  ", mot1[i] ,"  ", mot2[n1-i-1])
                i += 1
                if mot1[i] != mot2[n1-i-1] : rep = False
        else : rep = False
        return rep

    def anagrammes (mot1, mot2) :
        """compare deux mots et renvoie vrai s'ils sont l'anagramme l'un de l'autre"""
        n1, n2 = len(mot1), len(mot2)
        if n1 == n2 :
            i, rep = 0, True
            mot = []
            print("pour ", mot1, " et ", mot2)
            for car in mot2 : mot.append(car)
            while rep and i < n1 : # dès que rep est faux c'est fini !
                #print(i, "  ", mot1[i] ,"  ", mot2[n1-i-1])
                print("mot1[",i,"]", mot1[i])
                if mot1[i] not in mot : rep = False
                else :
                    del mot[mot.index(mot1[i])]
                    print("mot = ", mot)
                i += 1
        else : rep = False
        return rep

    print("palindromes('marion', 'romina') = ", palindromes('marion', 'noiram'))
    print("anagrammes('marion', 'romina') = ", anagrammes('marion', 'romina'))
    print("anagrammes('bonjour', 'jour')  = ", anagrammes('bonjour', 'jour') )
    print("anagrammes('bonjour', 'jour')  = ", anagrammes('bonjour', 'jour') )
########################################################################################################################
def upilab5_4_6 () :
    """5.4.6. Exercice UpyLaB 5.10 - Parcours vert bleu rouge
Écrire une fonction dupliques qui reçoit une séquence en paramètre.
La fonction doit renvoyer la valeur booléenne True si la séquence passée en paramètre contient des éléments dupliqués,
et la valeur booléenne False sinon.
Exemple 1 : L’appel suivant de la fonction : dupliques([1, 2, 3, 4]) doit retourner : False
Exemple 2 : L’appel suivant de la fonction : dupliques(['a', 'b', 'c', 'a']) doit retourner : True
Exemple 3 : L’appel suivant de la fonction : dupliques('abcda') doit retourner :True
"""
    def dupliques( sequence ) :
        """ détecte un élément redondant """
        liste = []
        rep, i, n = False, 0, len(sequence)
        while i < n and not rep:
            if sequence[i] in liste : rep = True
            else : liste.append(sequence[i])
            i += 1
        return rep

    print("dupliques([1, 2, 3, 4]) = "          , dupliques([1, 2, 3, 4]))
    print("dupliques(['a', 'b', 'c', 'a']) = "  , dupliques(['a', 'b', 'c', 'a']))
    print("dupliques('abcda') = "               , dupliques('abcda'))
########################################################################################################################
def upilab5_4_7 () :
    """5.4.7. Exercice UpyLaB 5.11 - Parcours bleu rouge
Écrire une fonction intersection(v, w) qui calcule l’intersection entre deux chaînes de caractères v et w.
On définit l’intersection de deux mots comme étant la plus grande partie commune à ces deux mots. Par exemple,
l’intersection de « programme » et « grammaire » est « gramm ».
Si les deux chaînes n’ont aucun caractère en commun, la fonction retourne la chaîne vide, ''.
Si plusieurs solutions sont possibles, la fonction retournera la sous-chaîne d’indice minimal dans v. Par exemple,
intersection('bbaacc', 'aabb') renvoie 'bb'.
Exemple 1 : L’appel suivant de la fonction : intersection('programme', 'grammaire') doit retourner : 'gramm'
Exemple 2 : L’appel suivant de la fonction : intersection('salut', 'merci') doit retourner : ''
Exemple 3 : L’appel suivant de la fonction : intersection('merci', 'adieu') doit retourner : 'e'
"""
    def intersection (seq1, seq2) :
        """ renvoie la partie commune ou intersection de deux séquences """
        inter = ''
        i, n, jMax = 0, len(seq1), 0
        while i < n :
            if seq1[i] in seq2 :
                j = 1
                poursui = True
                while i + jMax < n and poursui :
                    if seq1[i:i+jMax+1] not in seq2 :
                        poursui = False
                    else :
                        inter = seq1[i:i+jMax+1]
                        jMax  = j
                        #print("i = ", i, "j = ", j, "inter = ", inter)
                    j += 1
            i += 1
        return inter

    print("intersection('programme', 'grammaire') = ", intersection('programme', 'grammaire'))
########################################################################################################################
def upilab5_4_8 () :
    """5.4.8. Exercice UpyLaB 5.12 - Parcours bleu rouge
Écrire une fonction my_insert qui reçoit comme premier paramètre une liste d’entiers relatifs triée par ordre croissant
et comme deuxième paramètre un entier relatif n, et qui renvoie une liste correspondant à la liste reçue, mais dans
laquelle le nombre n a été inséré à la bonne place.
La liste donnée en paramètre ne doit pas être modifiée par votre fonction.
Vous pouvez supposer que le premier paramètre sera bien une liste triée d’entiers, mais si le deuxième paramètre n’est
pas du bon type, la fonction retourne None.
Exemple 1 : L’appel suivant de la fonction : my_insert([1, 3, 5], 4)   doit retourner : [1, 3, 4, 5]
Exemple 2 : L’appel suivant de la fonction : my_insert([2, 3, 5], 1)   doit retourner : [1, 2, 3, 5]
Exemple 3 : L’appel suivant de la fonction : my_insert([2, 3, 5], 0.5) doit retourner : None"""
    def my_insert0(liste, elt) :
        """ insert à la bonne place un nombre (elt) dans une liste triée de nombres (liste) """
        res = liste[:]            # copie
        n = len(res)
        if type(elt) is int :
            i = 0
            while i <n and liste[i] < elt :
                i += 1
            res = res[0:i] + [elt] + res[i:]
        else :
            res = None
        return res

    test = [
        ("my_insert0([1, 3, 5], 4)"  , [1, 3, 4, 5] ),
        ("my_insert0([2, 3, 5], 1)"  , [1, 2, 3, 5] ),
        ("my_insert0([2, 3, 5], 0.5)", None),
        ("my_insert0([2, 3, 5], 6)", [2, 3, 5, 6])
         ]
    for (t, r) in test :
        print (t, " = ", eval(t), " devrait donner ", r )
        print("Test réussi ? : ", eval(t) == r )

    def my_insert ( liste, nombre ) :  # variante de la précédente
        """
L’exercice est le même que le précédent, mais ici, si les paramètres ont le type attendu, la fonction modifie la liste
en place et ne retourne rien. Si les paramètres ne sont pas valides, une erreur se produit à l’exécution.
Exemple 1 : L’exécution du code suivant :
l = [1, 3, 5]
my_insert(l, 4)
print(l)
doit afficher : [1, 3, 4, 5]
Exemple 2 : L’exécution du code suivant :
l = [1, 3, 5]
my_insert(l, 'a')
print(l)
doit provoquer une exception Python, par exemple : AssertionError
"""
        assert type(nombre) is int
        assert type(liste)  is list
        assert isinstance(nombre, int), "teste si nombre est de type int"

        n = len(liste)
        i = 0
        while i < n and liste[i] < nombre:
            i += 1
        liste = liste[0:i] + [nombre] + liste[i:]
        return liste  # None

    l = [[1, 5, 78],[2, 3, 5],[2, 3, 5],[2, 3, 5]]
    elt = [-1,1,6,0.5]
    print("\n\nvariante\n--------")
    test = [
        (0,"my_insert([1, 5, 78], -1)"  , [-1, 1, 5, 78] ),
        (1,"my_insert([2, 3, 5], 1)"  , [1, 2, 3, 5] ),
        (2,"my_insert([2, 3, 5], 6)", [2, 3, 5, 6]),
        (3,"my_insert([2, 3, 5], 0.5)", None)
         ]
    for (i, t, r) in test :
        print (t, " = ", eval(t), " devrait donner ", my_insert0(l[i],elt[i]) )
        print("Test réussi ? : ", eval(t) == r )

########################################################################################################################
def upilab5_4_10et11 () :
    """5.4.10. Exercice UpyLaB 5.14 - Parcours vert bleu rouge
(D’après une idée de Jacky Trinh - 11/02/2018)
Nous pouvons définir la distance entre deux mots de même longueur (c’est-à-dire ayant le même nombre de lettres) mot_1 
et mot_2 comme le nombre minimum de fois où il faut modifier une lettre de mot_1 pour obtenir mot_2 (distance de 
Hamming).
Par exemple, les mots « lire » et « bise » sont à une distance de 2, puisqu’il faut changer le “l” et le “r” du mot 
« lire » pour obtenir « bise ».
Écrire une fonction distance_mots(mot_1, mot_2) qui retourne la distance entre deux mots.
Vous pouvez supposer que les deux mots sont de même longueur, et sont écrits sans accents.
Exemple 1 : L’appel suivant de la fonction : distance_mots("lire", "bise")                      doit retourner : 2
Exemple 2 : L’appel suivant de la fonction :distance_mots("Python", "Python")                   doit retourner : 0
Exemple 3 : L’appel suivant de la fonction :distadistance_mots("nce_mots("merci", "adieu")      doit retourner : 5
"""
    def distance_mots(m1, m2):
        """ calcul de la 'distance' entre deux mots """
        distance = len(m1)
        if len(m2) != distance :
            distance = None
        else :
            i = 0
            for c1 in m1:
                if c1 == m2[i]: distance -= 1
                i += 1
        return distance

    test = [('distance_mots("lire", "bise")', 2),('distance_mots("Python", "Python")',0),
            ('distance_mots("merci", "adieu")', 5)]
    for (t, r) in test :
        print (t, " devrait donner ", r, " et donne ", eval(t) )
        print("Test réussi ? : ", eval(t) == r )

    """5.4.11. Exercice UpyLaB 5.15 - Parcours rouge
(D’après une idée de Jacky Trinh - 11/02/2018)
Joao vient d’arriver dans notre pays depuis le Portugal. Il a encore du mal avec la langue française. Malgré ses efforts
considérables, il fait une faute d’orthographe quasi à chaque mot. Son souci est qu’il n’arrive pas toujours à écrire un
mot correctement sans se tromper à une lettre près. Ainsi pour écrire « bonjour », il peut écrire « binjour ». Pour 
remédier à ce problème, Joao utilise un correcteur orthographique. Malheureusement, Joao a un examen aujourd’hui et il 
a oublié son petit correcteur.
Afin de l’aider, nous vous demandons d’écrire une fonction correcteur(mot, liste_mots) où mot est le mot que Joao écrit 
et liste_mots est une liste qui contient les mots (ayant la bonne orthographe) que Joao est susceptible d’utiliser.

Cette fonction doit retourner le mot dont l’orthographe a été corrigée.
Exemple 1 : L’appel suivant de la fonction :
correcteur("bonvour", ["chien", "chat", "train", "voiture", "bonjour", "merci"]) doit retourner : "bonjour"
Exemple 2 : L’appel suivant de la fonction : 
correcteur("chat", ["chien", "chat", "train", "voiture", "bonjour", "merci"])    doit retourner : "chat"
"""
    def correcteur(mot1, listeMots):
        """ cherche dans la liste le mot qui ne diffère que d'un caractère du mot en entrée et renvoie ce mot """
        n = len(mot1)
        motCorrige = n * '*'

        if mot1 in listeMots:
            motCorrige = mot1
        else:
            dMax = 1
            while motCorrige == n * '*' :
                for mot2 in listeMots :
                    d = distance_mots(mot1, mot2)
                    if d != None :
                        if d == dMax:
                            motCorrige = mot2
                dMax += 1
        return motCorrige

    degradeDeMot = ['intrus', 'intris', 'invris', 'invrie', 'cnvrie']
    for mot in degradeDeMot :
        print(mot, " correpsond à ",
          correcteur(mot, ['angle', 'armoire', 'banc', 'bureau', 'carreau', 'chaise', 'dossier', 'escalier', 'lavabo',
                            'lecture', 'marche', 'matelas', 'maternelle', 'meuble', 'mousse', 'peluche', 'placard',
                            'plafond', 'portemanteau', 'poubelle', 'radiateur', 'rampe', 'rideau', 'robinet', 'savon',
                            'serrure', 'serviette', 'sieste', 'silence', 'sommeil', 'sonnette', 'sortie', 'table',
                            'tableau', 'tabouret', 'tapis', 'tiroir', 'toilette', 'aller', 'amener', 'apporter',
                            'appuyer', 'attendre', 'dormir', 'emmener', 'endormir', 'ennuyer', 'entrer', 'fermer',
                            'frapper', 'installer', 'lever', 'ouvrir', 'presser', 'rentrer', 'reposer', 'rester',
                            'sonner', 'tricher', 'venir', 'bonjour', 'crayon', 'stylo', 'pointe', 'mine', 'dessin',
                            'coloriage', 'rayure', 'peinture', 'pinceau', 'couleur', 'craie', 'papier', 'feuille',
                            'carnet', 'carton', 'ciseaux', 'découpage', 'pliage', 'pli', 'colle', 'affaire', 'caisse',
                            'trousse', 'cartable', 'jouet', 'jeu', 'pion', 'domino', 'puzzle', 'cube', 'perle', 'chose',
                            'forme', 'rond', 'tampon', 'livre', 'histoire', 'image', 'album', 'dictionnaire',
                            'magazine', 'catalogue', 'page', 'enveloppe', 'carte', 'affiche', 'alphabet', 'appareil',
                            'cassette', 'chanson', 'chiffre', 'contraire', 'doigt', 'film', 'instrument', 'intrus',
                            'lettre', 'main', 'micro', 'musique', 'nom', 'nombre', 'orchestre', 'ordinateur', 'photo',
                            'pouce', 'question', 'radio', 'sens', 'tambour', 'trompette', 'voix', 'xylophone']))
########################################################################################################################
def comprehensionDeListe () :
    """ quelques exemple de comprehension de liste """
    squares = [x ** 2 for x in range(10)]
    print("squares = [x**2 for x in range(10)] donne ", squares)

    m = [(x, y) for x in range(1, 4) for y in range(1, 4) if x != y]
    print("m = [(x, y) for x in range(1, 4) for y in range(1, 4) if x != y] donne ", m )

    m2 = []
    for x in range(1, 4):
        for y in range(1, 4):
            if x != y:
                m2.append((x, y))

    if (m2 == m) : print("Yes !")

    texte = '1 2 3 4 5 6 7 8'    #input('liste de valeurs')
    ma_liste = texte.split()  # découpe le texte en parties
    # séparées d'au moins une espace
    ma_liste = [int(i) for i in ma_liste]  # crée la liste
    # en traduisant chaque partie en entier
    print("Pour texte = ", texte, " [int(i) for i in ma_liste] donne ", ma_liste)
    liste = [int(i,36) for i in input("Donner SVP une liste des valeurs :").split()]
    print('[int(i) for i in input(\"liste des valeurs\").split()] donne ', liste)

    def keep_alnum_2(s):
        """Nettoie s en lui retirant les caractères non alphanumériques."""

        return "".join([i for i in s if i.isalnum()])

    print("keep_alnum_2('C'est mieux sans 4 espaces') donne ", keep_alnum_2("C'est mieux sans 4 espaces"))
########################################################################################################################
def upilab5_6_3 () :
    """5.6.3. Exercice UpyLaB 5.16 - Parcours vert bleu rouge
AVEC OU SANS COMPRÉHENSION
Les exercices UpyLaB suivants peuvent aussi se résoudre sans utiliser la technique de compréhension de liste. Mais les
solutions sont beaucoup plus courtes avec cette technique ! Nous vous demandons donc si possible de les réaliser avec
du code utilisant des compréhensions de liste.
ÉNONCÉ DE L’EXERCICE UPYLAB 5.16
Écrire une fonction my_pow qui prend comme paramètres un nombre entier m et un nombre flottant b, et qui renvoie une
liste contenant les m premières puissances de b, c’est-à-dire une liste contenant les nombres allant de b^0 à b^{m - 1}.
Si le type des paramètres n’est pas celui attendu, la fonction retournera la valeur None.
Exemple 1 : L’appel suivant de la fonction : my_pow(3, 5.0) doit retourner : [1.0, 5.0, 25.0]
Exemple 2 : L’appel suivant de la fonction : my_pow(3.0, 5.0) doit retourner : None
Exemple 3 : L’appel suivant de la fonction : my_pow('a', 'b') doit retourner : None
"""
    def my_pow(m, nb) :
        if isinstance(n, int) and isinstance(nb, float) :
            return [nb**i for i in range(m)]
        else : return None
########################################################################################################################
def upilab5_6_4 () :
    """5.6.4. Exercice UpyLaB 5.17 - Parcours bleu rouge
On considère une liste qui décrit une séquence t. Chaque élément de cette liste est un tuple de deux composantes : le
nombre de répétitions successives de l’élément x dans la séquence t, et l’élément x lui-même.
Par exemple, la liste [(1, 'He'), (2, 'l'), (1,'o')] décrit la séquence "Hello".
Écrire une fonction decompresse qui reçoit une telle liste en paramètre et renvoie la séquence t sous forme d’une
nouvelle liste.
Exemple : L’appel suivant de la fonction : decompresse([(4, 1), (0, 2), (2, 'test'), (3, 3), (1, 'bonjour')])
doit retourner : [1, 1, 1, 1, 'test', 'test', 3, 3, 3, 'bonjour']
"""
    def decompresse(listeTuple) :
        return [ elt for (n,elt) in listeTuple for i in range(n)]

    print("decompresse([(4, 1), (0, 2), (2, 'test'), (3, 3), (1, 'bonjour')]) doit retourner : \
[1, 1, 1, 1, 'test', 'test', 3, 3, 3, 'bonjour'] et retourne",
          decompresse([(4, 1), (0, 2), (2, 'test'), (3, 3), (1, 'bonjour')]) )

########################################################################################################################
def upilab5_6_5 () :
    """5.6.5. Exercice UpyLaB 5.18 - Parcours rouge
Écrire une fonction my_filter qui reçoit une liste lst et une fonction booléenne f en paramètres et renvoie une nouvelle
liste constituée des éléments de lst pour lesquels la fonction f renvoie True.
Exemples : Pour tester dans votre IDE (Thonny ou PyCharm par exemple) la fonction my_filter, vous allez devoir définir
une fonction booléenne f et la passer en argument à la fonction my_filter.
Vous pourrez donc d’abord définir la fonction f à l’aide du mot-clé def, mais sachez que l’on peut aussi définir
directement la fonction f lors de l’appel à la fonction my_filter en utilisant ce qu’on appelle une fonction lambda.
Il s’agit de fonctions anonymes que l’on peut utiliser au moment même.
Exemple d’une fonction lambda : lambda x : isinstance(x, int)
Cette fonction testera si l’objet x qu’on lui passe est de type int et fait le même travail que la fonction is_int plus
classiquement définie ci-dessous :
def is_int(x):
    return isinstance(x, int)
On pourra alors appeler la fonction my_filter des deux manières suivantes :
my_filter(lst, lambda x : isinstance(x, int))
my_filter(lst, is_int)
La seule différence, c’est que dans le deuxième cas, il faut avoir défini la fonction is_int au préalable (mais
l’avantage, c’est qu’on pourrait la réutiliser dans la suite du code, contrairement à la fonction lambda).
Notez qu’UpyLaB utilisera ces fonctions lambda dans ses tests.
Exemple 1 : L’appel suivant de la fonction : my_filter(['hello', 666, 42, 'Thierry', 1.5], lambda x : isinstance(x, int))
doit retourner : [666, 42]
Exemple 2 : L’appel suivant de la fonction : my_filter([-2, 0, 4, -5, -6], lambda x : x < 0)
doit retourner : [-2, -5, -6]
"""
    def my_filter(liste, fonctionLogique) :
        return [elt for elt in liste if fonctionLogique(elt)]

    test = [(['hello', 666, 42, 'Thierry', 1.5], "lambda x : isinstance(x, int)"),
            ([-2, 0, 4, -5, -6], "lambda x : x < 0")
            ]
    for arg in test :
        print("my_filter(",arg[0],",",arg[1],") donne ", my_filter(arg[0], eval(arg[1])))
########################################################################################################################
def rechercheMotsSansE () :
    """recherche dans le fichier des mots de la langue française tous les mots sans la lettre e
        écrit un fichier des mots sans e appelé : motsSansE.txt
        renvoie la liste de ces mots"""
    #import os
    #os.chdir('C:\Users\Violette\Documents\NSI\Terminale\LectureDecodageFichier')
    # dossier actuel ('C:/Users/Violette/SitesWeb/programmeNSI/cours/themeA')
    # odssier pour lire/écrire les fichiers de mots C:\Users\Violette\Documents\NSI\NSI Terminale\LectureDecodageFichier
    # lecture et recherche des mots sans E et construction d'une liste
    with open('motsFr.txt', encoding="utf-8") as listeMots :
        listeMSE = []
        for mot in listeMots :
            if not('e' in mot) :
                listeMSE.append(mot)
    with open('motsSansE.txt', "wt", encoding="utf-8") as listeMotsSansE :
        for mot in listeMSE :
            listeMotsSansE.write(mot)

########################################################################################################################
def manipulationDeFichiers () :
    """MANIPULATIONS STANDARD DE FICHIERS TEXTE
La liste des méthodes standard sur les fichiers est la suivante :
Instruction                                     Effet
f=open(“fichier”) :                         ouvre “fichier” en lecture
f=open(“fichier”,”w”) :                     ouvre “fichier” en écriture
f=open(“fichier”,”a”) :                    	ouvre “fichier” en écriture en rajoutant après les données déjà présentes
f.read() :	                                 retourne le contenu du fichier f
f.readline() :	                             lit une ligne
f.readlines() :             	             renvoie la liste des lignes de f
f.write(s) :                                 écrit la chaîne de caractères s dans le fichier f
f.close() :             	                 ferme f"""
    pass
########################################################################################################################
def upilab5_8_5 () :
    """ÉNONCÉ DE L’EXERCICE UPYLAB 5.19
D’après Wikipedia, un acrostiche est un poème, une strophe ou une série de strophes fondé sur une forme poétique
consistant en ce que, lues verticalement de haut en bas, la première lettre ou, parfois, les premiers mots d’une suite
de vers composent un mot ou une expression en lien avec le poème.
Écrire une fonction acrostiche qui reçoit en paramètre le nom d’un fichier et qui retourne la chaîne de caractères
formée par les premières lettres de chaque ligne du fichier.
Exemple : Sachant que le fichier Apollinaire.txt contient le texte :
Mon aimée adorée avant que je m'en aille
Avant que notre amour triste défaille
Râle et meure ô m'amie une fois
Il faut nous promener tous les deux seuls dans les bois
Alors je m'en irai plus heureux que les rois.
l’appel suivant de la fonction :acrostiche('Apollinaire.txt') doit retourner : 'MARIA'
"""
    def acrostiche(nomFichier) :
        """lit le fichier nomFichier et collecte les initiales de chaque ligne pour en tirer l'acrostiche ..."""
        with open(nomFichier, 'r', encoding="utf-8") as fichier :
            acro = ""
            for ligne in fichier :
                acro += ligne[0]
        return acro

    test = ['acro1.txt','acro2.txt','acro3.txt']
    for t in test :
        print(acrostiche(t))
########################################################################################################################
def afficheContenuFichier ( nomFichier : str ) -> None :
    """ Affiche le contenu text d'un fichier """
    with open(nomFichier, 'r', encoding="utf-8") as fich :
        for ligne in fich :
            print(ligne)

def upilab5_8_6 () :
    """5.8.6. Exercice UpyLaB 5.20 - Parcours vert bleu rouge
Écrire une fonction nouveaux_heros dont le but consiste à remplacer les héros d'une histoire.
La fonction acceptera deux paramètres :
    le premier sera une chaîne de caractères précisant le nom du fichier contenant l'histoire initiale ;
    le deuxième sera une chaîne de caractères précisant le nom du fichier dans lequel sera sauvegardée l'histoire
    modifiée comme précisé ci-dessous.
Dans l'histoire initiale, présente dans le fichier dont le nom est donné en premier argument, trois protagonistes
interviennent : Pierre, Paul et Jacqueline.
La fonction devra remplacer ces trois héros par, respectivement, Paul, Tom et Mathilde.
Le texte ainsi modifié sera alors stocké dans le fichier dont le nom est donné en deuxième argument.
Aucune autre modification ne sera apportée au texte initial.
Exemple : Sachant que le fichier histoire_1.txt contient le texte :
Si Pierre est le fils de Paul, et si Paul est le frère de Jacqueline, qui est Pierre pour Jacqueline ?
après l'appel suivant de la fonction : nouveaux_heros("histoire_1.txt", "nouvelle_histoire_1.txt")
le fichier dont le nom est nouvelle_histoire_1.txt doit contenir le texte :
Si Paul est le fils de Tom, et si Tom est le frère de Mathilde, qui est Paul pour Mathilde ?
"""
    def nouveaux_heros(nomFichier, nouveauFichier) :
        """ remplace dans nomFichier Pierre, Paul et Jacqueline par  Paul, Tom et Mathilde"""
        listeNomInit = ['Pierre', 'Paul', 'Jacqueline']
        inter = ['***', '---', '+++']
        listeNouveauxNoms =  ['Paul', 'Tom','Mathilde']
        with open(nomFichier, 'r', encoding="utf-8") as fich :
            with open(nouveauFichier, 'w', encoding="utf-8") as fich2:
                for ligne in fich :
                    #print(ligne)
                    for i,nom in enumerate(listeNomInit) :
                        #print(i, nom, " remplacé par ", inter[i] )
                        ligne = ligne.replace(nom, inter[i])
                    #print(ligne)
                    for i,nom in enumerate(inter) :
                        #print(i, nom, " remplacé par ", listeNouveauxNoms[i] )
                        ligne = ligne.replace(nom, listeNouveauxNoms[i])
                    #print(ligne)
                    fich2.write(ligne)

    test = ['histoire_1.txt', 'histoire_2.txt']
    for t in test :
        n = len(t)
        nF = 'nouvelle_histoire_' + t[n-5:n-4] + '.txt'
        afficheContenuFichier(t)
        print( "\n\n est devenu : \n\n")
        nouveaux_heros(t, nF)
        afficheContenuFichier (nF)

def upilab5_8_7 () :
    """5.8.7. Exercice UpyLaB 5.21 - Parcours bleu rouge
Écrire une fonction liste_des_mots qui reçoit en paramètre le nom d’un fichier texte, que la fonction doit ouvrir, et
qui renvoie la liste des mots contenus dans le fichier.
Consignes :On peut supposer que le fichier est présent et dans le bon format en encodage UTF-8.

    Les mots dans la liste seront écrits en minuscule et triés dans l’ordre donné par la codification UTF-8
    (en utilisant la méthode sort par exemple), les accents n’étant pas gérés de façon spécifique (« a » et « à » sont
    deux mots différents).

    Un même mot ne peut pas se trouver deux fois dans la liste.

    Dans le fichier source, les mots peuvent être séparés par des caractères blancs habituels (caractère espace,
    tabulation, passage à la ligne), ou par n’importe quel caractère parmi les suivants :
        - ' " ? ! : ; . , * = ( ) 1 2 3 4 5 6 7 8 9 0
    Certains des fichiers utilisés par UpyLaB pour tester la fonction sont accessibles aux adresses suivantes :
            https://upylab.ulb.ac.be/pub/data/Zola.txt
            https://upylab.ulb.ac.be/pub/data/le-petit-prince.txt
Notez que le fichier le-petit-prince.txt est libre de droit d’auteur sauf en France
(voir https://fr.wikipedia.org/wiki/Le_Petit_Prince). Si vous habitez en France, vous ne pouvez donc légalement le
télécharger, mais aucun souci ailleurs dans le monde.
"""
    listeAutresCar = ['-', '\'', "\"", "?", "!", ":", ";", ".", ",", "=", "(", ")", "1", "2", "3", "4", "5", "6",
                      "7", "8", "9", "0", "+", "-", "/", "*", "%" ]
    def liste_des_mots ( nomFichier ) :
        """ renvoie l'ensemble des mots contenus dans le fichier, dans l'ordre alpha et sous forme de liste """
        texte = []
        with open (nomFichier, 'r', encoding="utf-8") as fich :
            for ligne in fich :
                for carSpe in listeAutresCar :
                    ligne = ligne.replace(carSpe, ' ')
                texte += ligne.split()

        listeMots = []
        for mot in texte :
            if mot.lower() not in listeMots : # évite de passer par un set
                listeMots.append(mot.lower())
                #print(listeMots)

        listeMots.sort()
        return listeMots

    test = ['histoire_1.txt','Zola.txt', 'le-petit-prince.txt']
    for t in test :
        print("Nom du fichier : ", t)
        print("-----------------"+ len(t)*'-')
        afficheContenuFichier  ( t )
        print ( liste_des_mots ( t ) )
        input("suivant ? taper entrée :")

########################################################################################################################
def upilab5_8_8 () :
    """5.8.8. Exercice UpyLaB 5.22 - Parcours rouge
Écrire une fonction wc(nomFichier) qui ouvre le fichier en question et renvoie un tuple de trois nombres :
le nombre de caractères (y compris les caractères de retour à la ligne)
le nombre de mots
le nombre de lignes.
Consignes :
Nous définissons ici un mot comme étant une chaîne de caractères alphanumériques, c’est-à-dire répondant True à la
méthode isalnum(), et maximale, c’est-à-dire entourée d’espaces ou de séparateurs ou de caractères de fin de phrase.
Les fichiers utilisés par UpyLaB pour tester la fonction sont accessibles aux adresses suivantes :
https://upylab.ulb.ac.be/pub/data/wc1.txt
https://upylab.ulb.ac.be/pub/data/Zola.txt
https://upylab.ulb.ac.be/pub/data/le-petit-prince.txt
Pour information, le premier fichier contient les caractères a2x!§t5\n (\n désignant le caractère de fin de ligne).
L’appel de la fonction sur ce fichier retourne donc le tuple (8, 2, 1), les deux mots étant a2x et t5.
Notez que le fichier le-petit-prince.txt est libre de droit d’auteur sauf en France (voir
https://fr.wikipedia.org/wiki/Le_Petit_Prince). Si vous habitez en France, vous ne pouvez donc légalement le télécharger
, mais aucun souci ailleurs dans le monde.
Vous pourriez être tenté d’utiliser la méthode split. Ce n’est peut-être pas une très bonne idée, car la liste des
séparateurs est ici très longue. Par exemple, le fichier pourrait contenir la chaîne
"a$€αω$BOjJOurα"
"""
    def wc(nomFichier) :
        """ compte le nombre de 'mots' composés de caractères alphanumériques ; le nombre de caractères, le nombre de
        lignes du fichier. """
        with open(nomFichier, 'r', encoding="utf-8") as fich:
            nLi, nMots, nCar = 0, 0, 0
            for ligne in fich:
                nLi += 1
                dansMot = False
                for car in ligne :
                    nCar += 1
                    if car.isalnum() and not dansMot :
                        dansMot = True  # début du mot
                        nMots += 1
                    elif not car.isalnum() and dansMot :
                        dansMot = not dansMot  #fin du mot

        return nCar, nMots, nLi

    test = [
        ('histoire_1.txt',(88, 17, 3)),
        ('Zola.txt',(1356, 219, 1)),
        ('le-petit-prince.txt',(82650, 15317, 1550)),
        ('wc1.txt',(8, 2, 1))
    ]
    for t, r in test :
        print("Nom du fichier : ", t)
        print("-----------------"+ len(t)*'-')
        afficheContenuFichier  ( t )
        reponse = wc           ( t )
        print ( reponse )
        print("test réussi ? : ", reponse == r)
        input("suivant ? taper entrée :")
########################################################################################################################
def lire_matrice(fichier_encodage):
    """ lit les données matricielles dans un fichier."""
    with open(fichier_encodage, encoding='utf-8') as fichier_in:
        return [[int(colonne) for colonne in ligne.split()] for ligne in fichier_in]

def printMatrice (matrice : list, marge = 3 )  -> None:
    """ imprime les valeurs d'une matrice """
    if len(matrice) == 0 :    # ou if matrice == []
        print("Matrice vide")
    else :
        for ligne in matrice :
            ligneAffichee = " " * marge + "║"
            for val in ligne :
                ligneAffichee += " " * marge + str(val)
            ligneAffichee += marge * " " + "║"
            print(ligneAffichee)

########################################################################################################################
I3 = [ [ 1, 0, 0 ] , [ 0, 1, 0 ] , [ 0, 0, 1 ] ]
matTexte = [['H','E'],['L','L'],['O',' '],['W','O'],['R','L'],['D','!']]
matHello = [['H','E','L','L','O'],['W','O','R','L','D']]

def init_mat(li, co):
    """ initialise la matrice li x co avec des zéro
    :param li:
    :param co:
    :return:  matrices de 0
    """
    return [[0 for i in range(co)] for j in range(li)]

def matIdentite ( n : int ) -> list :
    """ renvoie la matrice identité carrée de taille n x n avec des zéro sauf
        sur la diagonale qui va d'en haut à gauche vers en bas à droite """
    mat = init_mat(n, n)
    for i in range(n) :
        mat[i][i] = 1
    return mat

def cours5_9_2Matrices () :
    """ cours sur la manipulation des matrices """
    test = ['sudoku1.txt']
    printMatrice(lire_matrice(test[0]))
    print(5*"\n")
    printMatrice(I3)
    n = int(input("Saisir la taille n de la matrice identité à construire :"))
    print(5*"\n")
    printMatrice(matIdentite(n), 10)
    print(5*"\n")
    printMatrice(matTexte)
    print(5*"\n")
    mat = eval(input())
    printMatrice(mat)

########################################################################################################################
def upilab5_9_3 () :
    """ÉNONCÉ DE L’EXERCICE UPYLAB 5.23
Écrire une fonction init_mat(m, n) qui construit et renvoie une matrice d’entiers initialisée à la matrice nulle et de
dimension m x n.
Exemple 1 : L’appel suivant de la fonction : init_mat(2, 3) doit retourner : [[0, 0, 0], [0, 0, 0]]
Exemple 2 : L’appel suivant de la fonction :bit_mat(0, 0) doit retourner : []
"""
    try :
        li = int(input("Nombre de lignes   de la matrice :"))
        co = int(input("Nombre de colonnes de la matrice :"))
        mat = init_mat(li, co)
        print("Matrice nulle de {}} lignes et {}} colonnes".format(li, co))
        printMatrice(mat)
    except :
        print("Erreur de saisie, recommencer !")


########################################################################################################################
def upilab5_9_4 () :
    """ impression d'une matrice à l'écran """
    def print_mat(matrice : list) -> None:
        texte = ""
        c, n = 0, len(matrice)
        if len(matrice) == 0 or type(matrice[0]) != list :
            print("erreur de saisie : une matrice est une liste de listes !")
            return None
        for li, ligne in enumerate(matrice) :
            for val in ligne:
                texte += str(val) + ' '
            if li != n-1 : texte += "\n"
        print(texte)
    try :
        ma_matrice = list(eval(input("entrer une matrice (ou liste de listes) : ")))
        print_mat(ma_matrice)
    except : print("Erreur de saisie : mauvaise syntaxe.")
########################################################################################################################
def upilab5_9_5 () :
    """5.9.5. Exercice UpyLaB 5.25 - Parcours bleu rouge
Écrire une fonction trace(M) qui reçoit en paramètre une matrice M de taille {n}\times{n} contenant des valeurs
numériques (de type int ou float), et qui renvoie sa trace, c’est-à-dire la somme de tous les éléments de la première
diagonale.
Exemple 1 : L’appel suivant de la fonction : trace([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) doit retourner : 15
En effet, 1 + 5 + 9 est égal à 15.
Exemple 2 : L’appel suivant de la fonction : trace([]) doit retourner  : 0
"""
    def trace ( M ) :
        """ calcule la trace de la matrice = somme des valeurs diagonales """
        if M == [] : return 0

        liste = [ val for li, ligne in enumerate(M) for co, val in enumerate(ligne) if li == co ]
        somme = 0
        for elt in liste :
            somme += elt
        return somme

    test = [
        [],
        [[1]],
        [[1,0,0],[0,1,0],[0,0,1]]
            ]
    for t in test :
        print("La trace de : ")
        printMatrice(t)
        print(" vaut : ", trace(t))

########################################################################################################################
def upilab5_9_6() :
    """5.9.6. Exercice UpyLaB 5.26 - Parcours bleu rouge
Une matrice M = \{m_{ij}\} de taille {n}\times{n} est dite antisymétrique lorsque, pour toute paire d’indices i, j, on
a m_{ij} = - m_{ji}.
Écrire une fonction booléenne antisymetrique(M) qui teste si la matrice M reçue est antisymétrique.
Exemple 1 : L’appel suivant de la fonction : antisymetrique([[0, 1, 1], [-1, 0, 1], [-1, -1, 0]]) doit retourner : True
Exemple 2 : L’appel suivant de la fonction : antisymetrique([[0, 1], [1, 0]])                     doit retourner : False
Exemple 3 : L’appel suivant de la fonction : antisymetrique([[1, -2], [2, 1]])                    doit retourner : False
Exemple 4 :  L’appel suivant de la fonction : antisymetrique([])                                  doit retourner : True
"""

    def antisymetrique(M):
        """ teste si la matrice M est antisymétrique """
        rep = True
        if M == []:
            pass
        else:
            for li, ligne in enumerate(M):
                for co, val in enumerate(ligne):
                    if val != -M[co][li]: rep = False
        return rep

    test = [([[0, 1, 1], [-1, 0, 1], [-1, -1, 0]], True),
            ([[0, 1], [1, 0]], False),
            ([[1, -2], [2, 1]], False),
            ([], True),
            ([[0, -1, -9, -1, -3], [1, 0, -9, -1, -4], [9, 9, 0, -5, -7], [1, 1, 5, 0, -9], [3, 4, 7, 9, 0]], True)
            ]

    rep = [ "non ", ""]
    for M,r in test :
        print("La matrice : ")
        printMatrice(M)
        print(" devrait être : " + rep[int(r)] + " antisymétrique et la fonction la trouve" +
              + rep[int(antisymetrique(M))] + "antisymétrique")
########################################################################################################################
def upilab5_9_7 () :
    """5.9.7. Exercice UpyLaB 5.27 - Parcours rouge
Écrire une fonction symetrie_horizontale(A) qui reçoit une matrice carrée A (de taille {n}\times{n}) et qui renvoie
l’image de A par symétrie horizontale par rapport à la ligne du milieu : la première ligne devenant la dernière, la
seconde, l’avant-dernière, etc.
Exemple 1 : L’appel suivant de la fonction : symetrie_horizontale([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
doit retourner : [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
Exemple 2 : L’appel suivant de la fonction : symetrie_horizontale([['a', 'b'], ['c', 'd']]) doit retourner :
[['c', 'd'], ['a', 'b']]
Exemple 3 : L’appel suivant de la fonction : symetrie_horizontale([]) doit retourner : []
"""
    def symetrie_horizontale(M) :
        """ retourne la matrice symétrique par rapport à l'horizontale """
        nLi = len(M)
        nCo = 0 if nLi == 0 else len(M[0])
        for li in range( (nLi+1) // 2) :
            for co in range(nCo) :
                #print("pour val = ", M[li][co], " dans li = ", li, " col = ", co, " permutation avec ligne n° ",
                #     nLi - li - 1)
                M[li][co], M[nLi-li-1][co] = M[nLi-li-1][co], M[li][co]
        return M

    test = [
        [],
        [[1]],
        [[1,2],[3,4]],
        [[1,0,0],[0,1,0],[0,0,1]],
        [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]],
        [[9, 3, 5, 1, 10], [3, 5, 4, 4, 6], [10, 7, 10, 10, 8], [2, 6, 2, 5, 9], [2, 7, 5, 9, 6]]
            ]
    for t in test :
        print("La matrice : ")
        printMatrice(t)
        print(" à pour symétrique horizontale : ")
        printMatrice( symetrie_horizontale(t))

########################################################################################################################
def analyseTexte () :
    """ fonctions d'analyse de texte """
########################################################################################################################
def upilbab6_1_4() :
    """6.1.4. Mise en pratique des ensembles et dictionnaires avec UpyLaB
UpyLaB 6.1 - Parcours vert bleu rouge   EXERCICES UPYLAB 6.1 À 6.7
Réalisez de façon autonome les exercices 6.1 à 6.7 d’UpyLaB. Ces exercices vont vous permettre de manipuler les
ensembles et les dictionnaires.
ÉNONCÉ DE L’EXERCICE UPYLAB 6.1
Après avoir longuement réfléchi et un peu visité notre monde, le Petit Prince décide de ne pas rentrer sur sa planète
mais de s’installer dans les Cévennes pour profiter de la belle nature qu’on y trouve.
Il y trouve une petite demeure pour y habiter, et plusieurs de ses amis veulent l’aider en lui proposant des meubles,
des denrées, des livres ou d’autres choses qui pourraient l’intéresser pour aménager son nouveau domicile.
Nous vous proposons de l'aider.
Écrire une fonction inventaire(offres, objets) où :
    offres est un dictionnaire contenant, comme clés, les objets proposés par les amis du Petit Prince, et comme valeurs
    associées, le nom de l'ami proposant cet objet,
    objets est une liste contenant tous les objets dont a besoin le Petit Prince.
La fonction retourne l'ensemble des amis chez qui il lui faut se rendre pour sa récolte.
Exemple : L’appel suivant de la fonction :
inventaire({"lit" : "Antoine", "bibliothèque" : "Sébastien", "chaise" : "Isabelle",
            "livre 'Le vieil homme et la mer'" : "Ernest", "sac de bonbons" : "Thierry",
            "smartphone" : "Ted", "table" : "Sophie"},
           ["sac de bonbons", "table", "chaise", "lit", "livre 'Le vieil homme et la mer'"])
doit retourner (à l'ordre près) : {"Thierry", "Sophie", "Isabelle", "Antoine", "Ernest"}
"""
    def inventaire(offre : dict, objets : list ) -> list :
        listeAmis = set()    # set = ensemble = liste non redondante
        for ob in offre:
            if ob in objets:
                listeAmis.add(offre[ob])
        return listeAmis

    offre = [{'sac de bonbons': 'Thierry', 'bibliothèque': 'Sébastien', 'livre "le vieil homme et la mer"': 'Ernest',
              'smartphone': 'Ted', 'table': 'Sophie', 'lit': 'Antoine', 'chaise': 'Isabelle'}]
    objets = [['sac de bonbons', 'table', 'chaise', 'lit', 'livre "le vieil homme et la mer"']]
    reponse = [{'Sophie', 'Ernest', 'Thierry', 'Antoine', 'Isabelle'}]

    n = 0
    print("Le petit prince a besoin de ", objets[n], "\n l'offre est \n", offre[n])
    print("La réponse ", reponse[n], " est-elle bonne ? :", inventaire(offre[n],objets[n]) == reponse[n])
########################################################################################################################
def upilab6_1_5 () :
    """
6.1.5. Exercice UpyLaB 6.2 - Parcours vert bleu rouge
(D’après une idée de Jacky Trinh le 19/02/2018)
Monsieur Germain est une personne très âgée. Il aimerait préparer une liste de courses à faire à l’avance. Ayant un
budget assez serré, il voudrait que sa liste de courses soit dans ses capacités. Son seul petit souci est qu’il a une
très mauvaise vue et n’arrive donc pas à voir le prix associé à chaque produit contenu dans le catalogue de courses.
Écrire une fonction calcul_prix(produits, catalogue) où :
    produits est un dictionnaire contenant, comme clés, les produits souhaités par Monsieur Germain et comme valeurs
    associées, la quantité désirée de chacun d’entre eux,
    catalogue est un dictionnaire contenant tous les produits du magasin avec leur prix associé.
La fonction retourne le montant total des achats de Monsieur Germain.
Exemple : L’appel suivant de la fonction :
calcul_prix({"brocoli":2, "mouchoirs":5, "bouteilles d'eau":6},
            {"brocoli":1.50, "bouteilles d'eau":1, "bière":2,
             "savon":2.50, "mouchoirs":0.80})
doit retourner : 13.0
"""
    pass # cf fichier upilab_6.py
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################




if __name__ == '__main__' :
    """
    ne fonctionne que si ce module est exécuté directement
    """
    listeExo = ["upilab5_8_6","upilab5_8_7","upilab5_8_8","cours5_9_2Matrices",
                "upilab5_9_3", "upilab5_9_4", "upilab5_9_5", "upilab5_9_6", "upilab5_9_7",
                "analyseTexte", "upilbab6_1_4"]

    resume = ["","","","","",
              " imprime à l'écran une matrice.",
              " calcule la trace d'une matrice.",
              " test si une matrice est antisymétrique",
              " retourne la matrice symétrique par rapport à l'horizontale",
              " utilise des fonctions d'analyse de texte",
              " renvoie la liste des amis pouvant fournir des objets ..."]

    sortir = False
    while not sortir :
        print("\nAjouter au numéro du choix h pour obtenir des explications :")
        for i, exo in enumerate(listeExo) :
            print(i, " ) " + exo + " qui : " + resume[i] )
        choix = input("Taper le numéro de votre choix et valider :")
        if 'h' in choix.lower() :
            n = int((choix.lower()).replace('h', ''))
            help(eval(listeExo[n]))
        else :
            N = len(listeExo)
            try :
                n = int(choix)
            except :
                print("Attention vous devez taper un nombre !")
                n = 666666666666666
            if n < N :
                print("Votre choix est ", str(n), "  " + listeExo[n] + " qui " + resume[n])
                eval(listeExo[n]+'()')
            else : sortir = True
    """
    help(upilab13_11et12)
    upilab13_11et12()
    sortie = False
    while not sortie:
        #choix = int(input())
        choix = 1
        sortie = True
        if choix < 6 :
            pass"""