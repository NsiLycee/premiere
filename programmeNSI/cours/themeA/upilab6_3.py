"""
            Dernière partie du mooc Apprendre à coder avec Python
            Solutions proposées par Joël Dendaletche

"""
def upilab6_5_2 () :
    """
6.5.2. Exercice UpyLaB 6.11 - Parcours vert bleu rouge
Le Petit Prince a peur des baobabs qui, en poussant, pourraient abîmer sa minuscule planète. Par contre, il adore les
arbres à fleurs que Monsieur Jardinier lui montre.
Touché par son enthousiasme, Monsieur Jardinier lui offre 1 000 graines de ces arbres à fleurs, mais maintenant, le
Petit Prince doit trouver une planète suffisamment grande pour les accueillir, sachant que chacun de ces arbres
nécessite une surface de 50 m2 pour se développer sereinement.
Écrire une fonction booléenne bonne_planete(diametre) qui reçoit en paramètre un nombre représentant le diamètre, en
mètres, d'une planète candidate. La fonction retourne la valeur True ou False selon que la planète convient ou non.
Écrire ensuite un programme qui lit un diamètre depuis l'entrée et affiche
    la chaîne de caractères "Bonne planète" si le résultat de l'appel à la fonction bonne_planete est True
    la chaîne de caractères "Trop petite" sinon
Exemple 1 : L’exécution du programme avec le nombre suivant en entrée  : 500 affiche : "Bonne planète"
Exemple 2 : L’exécution du programme avec le nombre suivant en entrée  : 10 affiche : "Trop petite"
Consignes :
    Dans cet exercice, il vous est demandé d’écrire une fonction, puis un programme appelant cette fonction. Notez
    qu’UpyLaB testera ces deux points, en exécutant le programme entier mais aussi en appelant directement la fonction
    avec les arguments de son choix.
    Nous rappelons que l'aire d'une sphère, solide auquel est assimilée une planète pour les besoins de l'exercice,
     s'obtient par le calcul π * d2 où d désigne le diamètre de la sphère.
"""
    import math

    def bonne_planete(diametre) :
        return True if math.pi * diametre**2 >= 50000 else False

    diam = int(input())
    print( "Bonne planète" if bonne_planete(diam) else "Trop petite")

########################################################################################################################
def upilab6_5_3 () :
    """6.5.3. Exercice UpyLaB 6.12 - Parcours vert bleu rouge
Écrire une fonction belongs_to_file(word, filename) qui reçoit deux chaînes de caractères en paramètre. La première
correspond à un mot, et la deuxième au nom d’un fichier contenant une liste de mots, chacun sur sa propre ligne. La
fonction vérifie si le mot figure dans cette liste, et retourne True si c’est bien le cas, False sinon.
Exemple
L’appel de la fonction suivant, où words.txt est le fichier indiqué dans les consignes ci-dessous et en supposant qu'il
se trouve dans le même répertoire que le programme :
belongs_to_file("renard", "words.txt")
retourne : False
Consignes
    Dans cet exercice, il vous est demandé d’écrire seulement la fonction belongs_to_file. Le code que vous soumettez à
    UpyLaB doit donc comporter uniquement la définition de cette fonction, et ne fait en particulier aucun appel à input
    ou à print.
    Vous pourrez supposer que le fichier passé en paramètre contient bien une liste de mots, chacun sur sa propre ligne.
    N’oubliez pas d’ouvrir le fichier dans le code de la fonction.
    Le fichier utilisé par UpyLaB pour effectuer les tests est disponible à l’adresse :
    https://upylab.ulb.ac.be/pub/data/words.txt
"""
    def belongs_to_file(word, filename) :
        """ teste si word est dans le fichier filename """
        with open(filename, 'r', encoding="utf-8") as fichier :
            rep = False
            for mot in fichier :
                if word == mot[:len(mot)-1] :
                    print("\n",mot, "\n", word)
                    rep = True
        return rep

    test = [("renard", "words.txt"), ("abandonments", "words.txt")]
    reponse = [False, True]

    for n, (w,f) in enumerate(test) :
        rep = belongs_to_file(w,f)
        print("\n\n"+120*'_'+"\nà partir du mot :", w, " dans le fichier ", f, "\n la fonction renvoie : \n", rep,
              "\n et il est attendu :\n",
              reponse[n] )
        print("Test réussi ? :", rep == reponse[n])
########################################################################################################################
def upilab6_5_4() :
    """6.5.4. Exercice UpyLaB 6.13 - Parcours vert bleu rouge
Voici le début d’une suite logique inventée par John Horton Conway (et connue donc sous le nom de suite de Conway).
1
1 1
2 1
1 2 1 1
1 1 1 2 2 1
3 1 2 2 1 1
...
Chaque ligne, à partir de la deuxième, décrit la précédente :
    la première ligne, 1, est formée de un “1”, d’où la deuxième ligne : 1 1 ;
    la troisième ligne décrit la deuxième ligne, où l’on voit deux “1”, d’où 2 1 ;
    la quatrième ligne décrit la troisième ligne, où l’on voit un “2” et un “1”, d’où 1 2 1 1 ;
    et ainsi de suite.
Écrire une fonction next_line(line) qui reçoit une liste d’entiers décrivant une ligne de cette suite, et qui retourne
la liste correspondant à la ligne suivante.
Exemple 1 : L’appel suivant de la fonction : next_line([1, 2, 1, 1]) doit retourner : [1, 1, 1, 2, 2, 1]
Exemple 2 : L’appel suivant de la fonction : next_line([1]) doit retourner : [1, 1]
Exemple 3 : L’appel suivant de la fonction : next_line([])
doit retourner : [1]
Consignes :
    Dans cet exercice, il vous est demandé d’écrire seulement la fonction next_line. Le code que vous soumettez à
    UpyLaB doit donc comporter uniquement la définition de cette fonction, et ne fait en particulier aucun appel à
    input ou à print.
    Notez que l’appel next_line([]) sur la liste vide retourne par convention la liste [1].
"""
    def next_line( liste ) :
        listeConway = []
        if liste == [] : listeConway = [1]
        else :
            #print("LCi = ", liste)
            N = len(liste)
            compte, n = 0, 0
            while n < N :
                val = liste[n]
                #print("val = ", val, " n = ", n)
                compte += 1
                while n + compte < N and val == liste[n+compte] :
                    compte += 1
                listeConway.extend([compte, val])
                #print("LC = ", listeConway, "compte = ", compte)
                compte, n = 0, n + compte

        return listeConway

    test = [[1,1,2,3,1,5], [1,1,1,1,1,2]]
    reponse = [[2,1,1,2,1,3,1,1,1,5], [5,1,1,2]]

    for n, l in enumerate(test) :
        rep = next_line(l)
        print("\n\n"+120*'_'+"\nà partir de la liste  :", l , "\n la fonction renvoie : \n", rep,
              "\n et il est attendu :\n",
              reponse[n] )
        print("Test réussi ? :", rep == reponse[n])


    n, N, liste = 0, int(input("Combien d'éléments à la suite de Conway : ? (suggestion < 10)")), [1]
    print("\n" + "_" * 120 + "\n" + 20 * ' ' + "Les ",n," premiers éléments de la suite de Conway :")
    while n < N :
        print(liste)
        liste = next_line(liste)
        n+=1
########################################################################################################################
def upilab6_5_5 () :
    """
    6.5.5. Exercice UpyLaB 6.14 - Parcours vert bleu rouge
(D’après une idée de Jacky Trinh le 15/02/2018)
Puissance 4 est un jeu de stratégie combinatoire abstrait dont le but est d’aligner une suite de quatre pions de même
couleur sur une grille comptant six rangées et sept colonnes.
Chaque joueur possède vingt-et-un pions d’une couleur (jaune ou rouge). À chaque tour, le joueur suivant doit placer un
pion dans la colonne de son choix. Le pion tombe dans la position la plus basse possible.
Le vainqueur est le premier qui a réussi à aligner horizontalement, verticalement ou diagonalement, de manière
consécutive, quatre de ses pions.
Écrire une fonction placer_pion(couleur, colonne, grille) où :
    couleur est la couleur du pion, qui peut être soit 'R' (rouge), soit 'J' (jaune),
    colonne est l’indice de la colonne où le joueur souhaite placer le pion (allant de 0 à 6),
    grille est la grille de jeu sous forme de matrice.
Cette matrice contient donc six listes de lignes contenant chacune sept éléments.
La ligne à l’indice 0 représente le bas du jeu.
Les éléments de cette matrice seront soit 'R', soit 'J' ou soit 'V' pour un emplacement encore vide.
Cette fonction placera un pion dans la grille du jeu et renverra un couple de valeurs :
    si le placement est possible, la valeur booléenne True et la grille modifiée,
    sinon, la valeur booléenne False et la grille non modifiée.
Exemple 1 :
L’appel suivant de la fonction :
placer_pion("R", 3, [['V', 'V', 'V', 'J', 'V', 'V', 'V'],
                     ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                     ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                     ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                     ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                     ['V', 'V', 'V', 'V', 'V', 'V', 'V']])
doit retourner :
(True, [['V', 'V', 'V', 'J', 'V', 'V', 'V'],
        ['V', 'V', 'V', 'R', 'V', 'V', 'V'],
        ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
        ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
        ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
        ['V', 'V', 'V', 'V', 'V', 'V', 'V']])
Exemple 2 :
L’appel suivant de la fonction :
placer_pion("J", 4, [['J', 'J', 'J', 'J', 'R', 'R', 'R'],
                     ['R', 'R', 'R', 'R', 'R', 'V', 'V'],
                     ['J', 'J', 'J', 'J', 'J', 'V', 'V'],
                     ['V', 'R', 'J', 'R', 'J', 'V', 'V'],
                     ['V', 'V', 'V', 'V', 'J', 'V', 'V'],
                     ['V', 'V', 'V', 'V', 'R', 'V', 'V']])
doit retourner :
(False, [['J', 'J', 'J', 'J', 'R', 'R', 'R'],
         ['R', 'R', 'R', 'R', 'R', 'V', 'V'],
         ['J', 'J', 'J', 'J', 'J', 'V', 'V'],
         ['V', 'R', 'J', 'R', 'J', 'V', 'V'],
         ['V', 'V', 'V', 'V', 'J', 'V', 'V'],
         ['V', 'V', 'V', 'V', 'R', 'V', 'V']])
Consignes :
    Dans cet exercice, il vous est demandé d’écrire seulement la fonction placer_pion. Le code que vous soumettez à
    UpyLaB doit donc comporter uniquement la définition de cette fonction, et ne fait en particulier aucun appel à
    input ou à print.
    Vous pourrez supposer que les arguments passés à la fonction seront valides.
    Il n’est pas demandé de vérifier si la grille contient un alignement gagnant.
    :return:
    """
    def placer_pion(couleur, colonne, matrice) :
        """ place le pion de couleur dans la colonne spécifiée ou renvoie false et la même matrice """
        ret = False
        mat = [[coul for coul in ligne] for ligne in matrice]
        for li in range(6) :
            if not ret and matrice[li][colonne] == 'V' :
                mat[li][colonne] = couleur
                ret = True
        return ret, mat

    test = [("R", 3, [['V', 'V', 'V', 'J', 'V', 'V', 'V'],
                     ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                     ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                     ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                     ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                     ['V', 'V', 'V', 'V', 'V', 'V', 'V']]),
            ("J", 4, [['J', 'J', 'J', 'J', 'R', 'R', 'R'],
                     ['R', 'R', 'R', 'R', 'R', 'V', 'V'],
                     ['J', 'J', 'J', 'J', 'J', 'V', 'V'],
                     ['V', 'R', 'J', 'R', 'J', 'V', 'V'],
                     ['V', 'V', 'V', 'V', 'J', 'V', 'V'],
                     ['V', 'V', 'V', 'V', 'R', 'V', 'V']])
            ]
    reponse = [
        (True, [['V', 'V', 'V', 'J', 'V', 'V', 'V'],
                ['V', 'V', 'V', 'R', 'V', 'V', 'V'],
                ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                ['V', 'V', 'V', 'V', 'V', 'V', 'V']]),
        (False, [['J', 'J', 'J', 'J', 'R', 'R', 'R'],
                 ['R', 'R', 'R', 'R', 'R', 'V', 'V'],
                 ['J', 'J', 'J', 'J', 'J', 'V', 'V'],
                 ['V', 'R', 'J', 'R', 'J', 'V', 'V'],
                 ['V', 'V', 'V', 'V', 'J', 'V', 'V'],
                 ['V', 'V', 'V', 'V', 'R', 'V', 'V']])
                ]

    for n, (coul, col, mat) in enumerate(test) :
        rep = placer_pion(coul, col, mat)
        print("\n\n"+120*'_'+"\nà partir de la matrice  :\n", mat , "\nla couleur",coul, " dans la colonne ", col,
              "\n la fonction renvoie : ",rep,
              "\n et il est attendu :\n",
              reponse[n] )
        print("Test réussi ? :", rep == reponse[n])

########################################################################################################################
def upilab6_5_6 () :
    """
    6.5.6. Exercice UpyLaB 6.15 - Parcours rouge
(D’après une idée de Jacky Trinh le 15/02/2018)
Puissance 4 est un jeu de stratégie combinatoire abstrait dont le but est d’aligner une suite de quatre pions de même
couleur sur une grille comptant six rangées et sept colonnes.
Chaque joueur possède vingt-et-un pions d’une couleur (jaune ou rouge). À chaque tour, le joueur suivant doit placer un
pion dans la colonne de son choix. Le pion tombe dans la position la plus basse possible.
Le vainqueur est le premier qui a réussi à aligner horizontalement, verticalement ou diagonalement, de manière
consécutive, quatre de ses pions.
Écrire une fonction gagnant(grille) où grille est la grille de jeu sous forme de matrice.
Cette matrice contient donc six listes de lignes contenant chacune sept éléments.
La ligne à l’indice 0 représente le bas du jeu.
Les éléments de cette matrice seront soit 'R', soit 'J' ou soit 'V' pour un emplacement encore vide.
Cette fonction renverra 'R' si le joueur à la couleur rouge a gagné, 'J' si le joueur à la couleur jaune a gagné ou
bien None si aucun joueur n’a gagné.
Exemple 1 : L’appel suivant de la fonction :
gagnant([['V', 'V', 'V', 'J', 'R', 'R', 'J'],
         ['V', 'V', 'V', 'R', 'J', 'R', 'R'],
         ['V', 'V', 'V', 'V', 'R', 'J', 'J'],
         ['V', 'V', 'V', 'V', 'V', 'V', 'J'],
         ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
         ['V', 'V', 'V', 'V', 'V', 'V', 'V']])
doit retourner : 'J'
Exemple 2 : L’appel suivant de la fonction :
gagnant([['V', 'R', 'J', 'J', 'J', 'R', 'V'],
         ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
         ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
         ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
         ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
         ['V', 'V', 'V', 'V', 'V', 'V', 'V']])
doit retourner : None
Consignes :
    Dans cet exercice, il vous est demandé d’écrire seulement la fonction gagnant. Le code que vous soumettez à UpyLaB
doit donc comporter uniquement la définition de cette fonction, et ne fait en particulier aucun appel à input ou à
print. Vous pourrez supposer que la matrice passée à la fonction est valide, et qu’il n’y a pas à la fois une
configuration gagnante pour chacune des couleurs.
    :return:
    """
    def chercheH ( coul, li, co, mat ) :
        """teste si un alignement horizontal de 4 pions existe
        """
        res = False
        if co < 4 and mat[li][co+1] == coul and mat[li][co+2] == coul and mat[li][co+3] == coul :
            res = True
        return res

    def chercheV ( coul, li, co, mat ) :
        """teste si un alignement vertical de 4 pions existe
        """
        res = False
        if li < 3 and mat[li+1][co] == coul and mat[li+2][co] == coul and mat[li+3][co] == coul :
            res = True
        return res

    def chercheD ( coul, li, co, mat ) :
        """teste si un alignement diagonal de 4 pions existe
        """
        def diagGauche ( coul, li, co, mat ) :
            return coul == mat[li+1][co-1] == mat[li+2][co-2] == mat[li+3][co-3]

        def diagDroit ( coul, li, co, mat ) :
            return coul == mat[li+1][co+1] == mat[li+2][co+2] == mat[li+3][co+3]

        res = False
        if li < 3 : # il n'y a que 6 lignes ! Les diagonales se forment de la ligne 0 à la 2 seulement
            if co < 3 and diagDroit (coul, li, co, mat ) : # diagonale droite
                res = True
            elif co > 3 and diagGauche(coul, li, co, mat ) : # co > 3 diagonale gauche
                res = True
            elif co == 3 and (diagDroit (coul, li, co, mat ) or diagGauche(coul, li, co, mat )) :
                res = True
        return res

    def gagnant( mat ) :
        """ retourne la couleur gagnante au puissance 4 ou None s'il n'y a pas d'alignement de 4 pions """
        res = None
        for li, ligne in enumerate(mat) :
            for co, coul in enumerate(ligne) :
                if coul != 'V' :
                    if  chercheH( coul, li, co, mat ) or \
                        chercheV( coul, li, co, mat ) or \
                        chercheD( coul, li, co, mat ) : res = coul
        return res

    test = [[['V', 'V', 'V', 'J', 'R', 'R', 'J'],
         ['V', 'V', 'V', 'R', 'J', 'R', 'R'],
         ['V', 'V', 'V', 'V', 'R', 'J', 'J'],
         ['V', 'V', 'V', 'V', 'V', 'V', 'J'],
         ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
         ['V', 'V', 'V', 'V', 'V', 'V', 'V']],
            [['V', 'R', 'J', 'J', 'J', 'R', 'V'],
             ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
             ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
             ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
             ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
             ['V', 'V', 'V', 'V', 'V', 'V', 'V']],
            [['J', 'R', 'J', 'J', 'J', 'R', 'R'], ['V', 'R', 'R', 'J', 'R', 'J', 'J'],
             ['V', 'J', 'R', 'V', 'J', 'V', 'R'], ['V', 'V', 'R', 'V', 'J', 'V', 'V'],
             ['V', 'V', 'V', 'V', 'V', 'V', 'V'], ['V', 'V', 'V', 'V', 'V', 'V', 'V']],
            [['J', 'R', 'J', 'J', 'J', 'R', 'R'], ['R', 'R', 'R', 'J', 'R', 'J', 'J'],
             ['J', 'J', 'R', 'R', 'J', 'V', 'R'], ['V', 'V', 'R', 'V', 'J', 'V', 'V'],
             ['V', 'V', 'V', 'V', 'V', 'V', 'V'], ['V', 'V', 'V', 'V', 'V', 'V', 'V']],

            [['J', 'R', 'J', 'J', 'J', 'R', 'R'],
             ['R', 'R', 'R', 'J', 'R', 'J', 'J'],
             ['J', 'J', 'J', 'R', 'J', 'R', 'R'],
             ['R', 'R', 'J', 'R', 'J', 'R', 'J'],
             ['J', 'J', 'R', 'J', 'V', 'R', 'J'],
             ['R', 'J', 'J', 'R', 'R', 'R', 'J']]
    ]
    reponse = ['J', None, None, 'R', 'R'
    ]
    for n, mat in enumerate(test) :
        rep = gagnant( mat)
        print("\n\n"+120*'_'+"\nà partir de la matrice  :\n", mat ,
              "\n la fonction renvoie : ",rep,
              "\n et il est attendu :\n",
              reponse[n] )
        print("Test réussi ? :", rep == reponse[n])
########################################################################################################################
def upilab6_5_7():
    """6.5.7. Exercice UpyLaB 6.16 - Parcours rouge
    Écrire une fonction file_histogram(fileName) qui prend en paramètre le nom, sous forme d’une chaîne de caractères,
    d’un fichier texte, et qui renvoie un dictionnaire associant à chaque caractère du texte contenu dans ce fichier son
    nombre d’occurrenc

    Écrire une fonction words_by_length(fileName) qui prend en paramètre le nom, sous forme d’une chaîne de caractères,
    d’un fichier texte, et qui renvoie un dictionnaire associant à une longueur l la liste triée (dans l’ordre utf-8
    croissant) des mots de longueur l présents dans le texte contenu dans le fichier. Ces mots seront écrits en
    minuscules.
Exemple 1 : L’appel de la fonction suivant : file_histogram('/pub/data/Zola.txt') retourne :
{'f': 14, 'î': 1, "'": 10, 'v': 15, 'm': 24,
 'N': 1, 'o': 49, 'a': 95, 'h': 13, 'd': 37,
 'é': 21, 'b': 12, 'E': 2, '\n': 1, 'x': 2,
 'y': 3, 'U': 1, 'M': 2, 'u': 50, 'à': 3,
 'e': 168, 'i': 73, ' ': 209, 'r': 64, 'p': 24,
 'D': 3, 's': 105, ',': 35, 't': 82, '-': 1,
 'è': 4, 'g': 16, 'c': 39, '.': 10, '?': 1,
 'L': 1, 'n': 81, 'ç': 1, 'j': 4, 'A': 2,
 'l': 71, 'ô': 1, 'q': 5}
Exemple 2 : L’appel de la fonction suivant : words_by_length('/pub/data/Zola.txt') retourne :
{1: ['a', 'c', 'd', 'l', 'n', 's', 'à'],
 2: ['ce', 'de', 'du', 'en', 'et', 'il',
     'la', 'le', 'là', 'sa', 'se', 'si', 'un'],
 3: ['aux', 'des', 'ils', 'les', 'par', 'pas',
     'que', 'qui', 'ses', 'sol', 'une', 'vie'],
 4: ['avec', 'blés', 'ciel', 'dans', 'dont',
     'loin', 'plus', 'pour', 'sous', 'sève',
     'tous', 'voix'],
 5: ['armée', 'astre', 'avril', 'bruit', 'cette',
     'comme', 'coups', 'faire', 'flanc', 'futur',
     'grand', 'haies', 'noire', 'parts', 'pieds',
     'pièce', 'plein', 'terre', 'vives', 'était'],
 6: ['allait', 'arbres', 'autres', 'baiser', 'besoin',
     'cassée', 'champs', 'chaque', 'droite', 'encore',
     'gauche', 'germes', 'gloire', 'grosse', 'herbes',
     'hommes', 'jeunes', 'plaine', 'rauque', 'rayons',
     'rumeur', 'siècle', 'soleil', 'suivre', 'toutes',
     'vertes', 'échine'],
 7: ['bientôt', 'chaleur', 'coulait', 'croyait',
     'fussent', 'germait', 'graines', 'lumière',
     'maheude', 'matinée', 'montait', 'poussée',
     'sillons', 'souffle', 'éclater', 'étaient'],
 8: ['campagne', 'enjambée', 'feuilles', 'jeunesse',
     'obstinés', 'profonds', 'récoltes', 'tapaient', 'épandait'],
 9: ['bourgeons', 'camarades', 'crevaient', 'enfantait', 'enflammés',
     'entendait', 'gerçaient', 'lentement', 'rayonnait'],
 10: ['accompagné', 'betteraves', 'gonflaient', 'maintenant',
      'nourricier', 'poussaient', 'rapprochés', 'rivelaines',
      'ronflement', 'vengeresse', 'échauffant'],
 11: ['débordement', 'germination', 'grandissant', 'jaillissait',
      'reconnaître', 'travaillées', 'ventilateur'],
 12: ['allongeaient', 'chuchotantes', 'continuaient'],
 13: ['distinctement'], 14: ['tressaillaient']}
Consignes
    Dans cet exercice, il vous est demandé d’écrire seulement des fonctions. Le code que vous soumettez à UpyLaB doit
    donc comporter uniquement la définition de ces fonctions, et ne fait en particulier aucun appel à input ou à print.
    Les fichiers utilisés par UpyLaB pour tester votre code sont :
            https://upylab.ulb.ac.be/pub/data/words.txt
            https://upylab.ulb.ac.be/pub/data/le-petit-prince.txt
            https://upylab.ulb.ac.be/pub/data/Zola.txt
    Pour la fonction words_by_length, on supposera qu’un mot est une séquence de caractères alphabétiques. La méthode
    isalpha() pourra être utile.
Par exemple, la chaîne de caractères 'cat4dog' sera considérée comme formant deux mots : 'cat' et 'dog'.
Veillez aussi à ce qu’un même mot n’apparaisse pas plusieurs fois dans la même liste.
    :return:
    """
    def file_histogram( nomFich ) :
        """ renvoie le dictionnaire des fréquences pour chaque caractère du texte """
        dic = {}
        with open( nomFich, 'r', encoding='utf-8') as F :
            texte = F.read()
            for car in texte :
                #car = car.lower()
                dic[car] = dic.get(car,0) + 1
        return dic

    test = ['Zola.txt', 'words.txt', 'le-petit-prince.txt']
    reponse = [{'M': 2, 'à': 3, 'i': 73, 'N': 1, 'o': 49, 'm': 24, 'c': 39, 'E': 2, 'n': 81, 'r': 64, 's': 105,
                'b': 12, 'v': 15, 'î': 1, 'g': 16, 'x': 2, 'ç': 1, 'd': 37, 'p': 24, ' ': 209, 'q': 5, 'A': 2,
                'ô': 1, 'L': 1, '?': 1, 'l': 71, '-': 1, '\n': 1, 'y': 3, 'U': 1, 'a': 95, 'f': 14, 'D': 3, 'è': 4,
                'e': 168, 'j': 4, 'é': 21, 't': 82, "'": 10, 'u': 50, '.': 10, 'h': 13, ',': 35},
               {'z': 3750, 'h': 20200, 's': 86547, 'n': 60513, 'p': 25789, 'v': 9186, 'b': 17798, 't': 57059,
                'u': 31161, 'j': 1780, 'c': 34287, 'f': 12714, '\n': 113809, 'k': 9370, 'e': 106758, 'a': 68582,
                'o': 54542, 'd': 34552, 'g': 27848, 'r': 64965, 'y': 13473, 'x': 2700, 'l': 47011, 'i': 77412,
                'm': 24741, 'w': 8535, 'q': 1632},
               {'8': 3, ':': 112, 'p': 1994, 'P': 65, '5': 5, 'a': 4355, ')': 6, 'i': 4941, 'N': 25, 'v': 845, 'û': 39,
                '1': 26, 'J': 220, 'n': 4290, 'S': 51, ',': 942, 'O': 50, 'u': 3876, 'ç': 97, '0': 5, '?': 142,
                's': 5033, 'C': 202, 'F': 9, 'à': 248, 'D': 27, '"': 126, 'ù': 29, '!': 135, 'c': 1563, '.': 1693,
                'V': 29, 'e': 9060, '(': 6, 'Z': 1, '-': 681, "'": 1074, 'E': 176, 'é': 1004, 'ê': 112, '6': 8, '*': 56,
                'j': 491, '3': 11, 'l': 3296, 'g': 514, 'x': 235, '4': 3, '\n': 1550, ';': 1, 'À': 6, 'É': 2, 't': 4563,
                'I': 155, 'f': 541, 'ï': 12, 'L': 157, 'Q': 58, 'm': 1755, '2': 24, '7': 4, 'M': 154, 'B': 42, '\t': 3,
                'T': 95, 'H': 10, 'A': 83, 'è': 236, ' ': 13992, 'o': 3260, 'î': 34, 'ë': 2, 'h': 507, 'y': 118, '9': 6,
                'b': 594, 'ô': 26, 'â': 32, 'q': 625, 'U': 14, 'd': 1979, 'r': 4005, 'Ç': 23, 'z': 62, 'R': 9}
               ]

    for n, fN in enumerate(test) :
        dic = file_histogram(fN)
        if dic == reponse[n]:
            print("test réussi pour file_histogram(", fN, ")")
            print(dic)
            print(reponse[n])
        else:
            print("test raté pour file_histogram(", fN, ")", "dic = \n", dic, '\n', reponse[n])

    print(file_histogram('le-petit-prince.txt'))

    def words_by_length( nomFichier ) :
        """ renvoie un dictonnaire de liste de mots rangés par liste de taille croissante """
        dic = {}
        with open( nomFichier, 'r', encoding='utf-8') as F :
            mot, dansMot = "", False
            texte = F.read()
            for car in texte:
                if car.isalpha():
                    mot += car
                    dansMot = True
                else:
                    if dansMot:
                        taille = len(mot)
                        if taille in dic:
                            if mot.lower() not in dic[taille] :
                                dic[taille].append(mot.lower())
                        else:
                            dic[taille] = [mot.lower()]
                        mot = ""
                    dansMot = False
        for clef in dic :
            dic[clef].sort()
        return dic

    test = ['Zola.txt']
    reponse = [{1: ['a', 'c', 'd', 'l', 'n', 's', 'à'],  2: ['ce', 'de', 'du', 'en', 'et', 'il', 'la', 'le', 'là', 'sa', 'se', 'si', 'un'],
 3: ['aux', 'des', 'ils', 'les', 'par', 'pas', 'que', 'qui', 'ses', 'sol', 'une', 'vie'],
 4: ['avec', 'blés', 'ciel', 'dans', 'dont', 'loin', 'plus', 'pour', 'sous', 'sève', 'tous', 'voix'],
 5: ['armée', 'astre', 'avril', 'bruit', 'cette','comme', 'coups', 'faire', 'flanc', 'futur', 'grand', 'haies', 'noire',
     'parts', 'pieds', 'pièce', 'plein', 'terre', 'vives', 'était'],
 6: ['allait', 'arbres', 'autres', 'baiser', 'besoin', 'cassée', 'champs', 'chaque', 'droite', 'encore', 'gauche',
     'germes', 'gloire', 'grosse', 'herbes', 'hommes', 'jeunes', 'plaine', 'rauque', 'rayons', 'rumeur', 'siècle',
     'soleil', 'suivre', 'toutes', 'vertes', 'échine'],  7: ['bientôt', 'chaleur', 'coulait', 'croyait','fussent',
'germait', 'graines', 'lumière', 'maheude', 'matinée', 'montait', 'poussée', 'sillons', 'souffle', 'éclater', 'étaient'],
 8: ['campagne', 'enjambée', 'feuilles', 'jeunesse', 'obstinés', 'profonds', 'récoltes', 'tapaient', 'épandait'],
9: ['bourgeons', 'camarades', 'crevaient', 'enfantait', 'enflammés','entendait', 'gerçaient', 'lentement', 'rayonnait'],
 10: ['accompagné', 'betteraves', 'gonflaient', 'maintenant', 'nourricier', 'poussaient', 'rapprochés', 'rivelaines',
      'ronflement', 'vengeresse', 'échauffant'],
 11: ['débordement', 'germination', 'grandissant', 'jaillissait', 'reconnaître', 'travaillées', 'ventilateur'],
 12: ['allongeaient', 'chuchotantes', 'continuaient'], 13: ['distinctement'], 14: ['tressaillaient']}
               ]

    for n, fN in enumerate(test) :
        dic = words_by_length(fN)
        if dic == reponse[n] :
            print("test réussi pour words_by_length(", fN, ")")
            print(dic)
            print(reponse[n])
        else : print("test raté pour words_by_length(", fN, ")", "dic = \n", dic, '\n', reponse[n])
########################################################################################################################
def upilab6_5_8():
    """
6.5.8. Exercice UpyLaB 6.17 - Parcours bleu rouge
Le sudoku est un jeu de logique dans lequel le joueur reçoit une grille de 9 x 9 cases, chacune pouvant contenir un
chiffre de 1 à 9 ou bien être vide. La grille est divisée en 9 lignes, 9 colonnes ainsi qu’en 9 « sous-grilles »,
appelées régions, formées de 3 x 3 boîtes contiguës. Le but du jeu est de remplir les cases vides avec des chiffres de 1
à 9, de telle sorte que, dans chaque ligne, chaque colonne et chaque région, soient présents tous les chiffres de 1 à 9,
sans doublons.
Le but de cet exercice est d'écrire une fonction qui indiquera si la grille passée en argument est une grille de sudoku
correctement remplie.
Pour cela, vous allez écrire trois fonctions annexes, que vous pourrez tester et valider dans des exercices
intermédiaires.
Notez que chacun des 4 exercices est évalué, et comptabilisé pour 1 point (soit 4 points au total).
ÉNONCÉ DE L’EXERCICE UPYLAB 6.17a
Écrire une fonction check_rows(grid) qui prend en paramètre une grille sous forme de matrice à deux dimensions et
vérifie si toutes les lignes sont valides (c’est-à-dire que sur chaque ligne, chaque chiffre apparaît une et une seule
fois).
Exemple 1 : L’appel de la fonction suivant :
check_rows([[9, 6, 3, 1, 7, 4, 2, 5, 8],
            [1, 7, 8, 3, 2, 5, 6, 4, 9],
            [2, 5, 4, 6, 8, 9, 7, 3, 1],
            [8, 2, 1, 4, 3, 7, 5, 9, 6],
            [4, 9, 6, 8, 5, 2, 3, 1, 7],
            [7, 3, 5, 9, 6, 1, 8, 2, 4],
            [5, 8, 9, 7, 1, 3, 4, 6, 2],
            [3, 1, 7, 2, 4, 6, 9, 8, 5],
            [6, 4, 2, 5, 9, 8, 1, 7, 3]])
retourne : True
Exemple 2 : L’appel de la fonction suivant :
check_rows([[9, 6, 3, 1, 7, 4, 2, 5, 8],
            [1, 7, 8, 3, 2, 5, 6, 4, 9],
            [2, 5, 4, 6, 8, 9, 7, 3, 1],
            [8, 2, 1, 4, 3, 7, 5, 9, 6],
            [4, 9, 6, 8, 4, 2, 3, 1, 7],
            [7, 3, 5, 9, 6, 1, 8, 2, 4],
            [5, 8, 9, 7, 1, 3, 4, 6, 2],
            [3, 1, 7, 2, 4, 6, 9, 8, 5],
            [6, 4, 2, 5, 9, 8, 1, 7, 3]])
retourne :False
Consignes :    Dans cet exercice, le code que vous soumettez à UpyLaB doit comporter uniquement la définition de la
fonction check_rows, et ne fait en particulier aucun appel à input ou à print.
    Vous pourrez supposer que la grille passée en paramètre est valide.
    La fonction ne doit pas modifier la grille passée en paramètre.
    :return:    """
    def check_rows(grid) :
        """ teste si chaque ligne de la grille de sudoku est valide (tous les chiffres de 1 à 9 une seule fois ) """
        ret = True
        verif = {9: 1, 6: 1, 3: 1, 1: 1, 7: 1, 4: 1, 2: 1, 5: 1, 8: 1}
        for ligne in grid :
            dic = {}
            for car in ligne :
                dic[car] = dic.get(car,0) + 1
            if dic != verif : ret = False
        return ret

    test = [[[9, 6, 3, 1, 7, 4, 2, 5, 8],
            [1, 7, 8, 3, 2, 5, 6, 4, 9],
            [2, 5, 4, 6, 8, 9, 7, 3, 1],
            [8, 2, 1, 4, 3, 7, 5, 9, 6],
            [4, 9, 6, 8, 5, 2, 3, 1, 7],
            [7, 3, 5, 9, 6, 1, 8, 2, 4],
            [5, 8, 9, 7, 1, 3, 4, 6, 2],
            [3, 1, 7, 2, 4, 6, 9, 8, 5],
            [6, 4, 2, 5, 9, 8, 1, 7, 3]],

            [[9, 6, 3, 1, 7, 4, 2, 5, 8],
             [1, 7, 8, 3, 2, 5, 6, 4, 9],
             [2, 5, 4, 6, 8, 9, 7, 3, 1],
             [8, 2, 1, 4, 3, 7, 5, 9, 6],
             [4, 9, 6, 8, 4, 2, 3, 1, 7],
             [7, 3, 5, 9, 6, 1, 8, 2, 4],
             [5, 8, 9, 7, 1, 3, 4, 6, 2],
             [3, 1, 7, 2, 4, 6, 9, 8, 5],
             [6, 4, 2, 5, 9, 8, 1, 7, 3]]
            ]
    reponse = [True, False]

    for n, g in enumerate(test) :
        bool = check_rows(g)
        if bool == reponse[n] :
            print("test réussi pour check_rows(", g, ")")
            #print(g)
            print(reponse[n])
        else : print("test raté pour check_rows(", g, ")", " renvoie  = \n", bool, '\n Devrait être : ', reponse[n])
########################################################################################################################
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

def upilab6_5_9():
    """
6.5.9. Exercice UpyLaB 6.18 - Parcours rouge
Le sudoku est un jeu de logique dans lequel le joueur reçoit une grille de 9 x 9 cases, chacune pouvant contenir un
chiffre de 1 à 9 ou bien être vide. La grille est divisée en 9 lignes, 9 colonnes ainsi qu’en 9 « sous-grilles »,
appelées régions, formées de 3 x 3 boîtes contiguës. Le but du jeu est de remplir les cases vides avec des chiffres de 1
à 9, de telle sorte que, dans chaque ligne, chaque colonne et chaque région, soient présents tous les chiffres de 1 à 9,
sans doublons.
Une méthode de résolution passe par l’analyse des candidats uniques. Ce qu’on appelle candidat est un nombre permis pour
une case car on ne le retrouve pas ailleurs dans la ligne, la colonne et la région de cette case.
Si une grille est telle que chaque case vide se retrouve avec un candidat unique, alors la résolution du sudoku est
évidente.
Des deux grilles suivantes, seule la première peut être résolue de cette manière : par exemple, en indiçant le tableau à
partir de 0, (0,0) étant en haut à gauche, à la case d’indice (4,7), seule la valeur 3 est possible. On peut ensuite
faire de même jusqu’à la résolution complète du sudoku.
https://upylab.ulb.ac.be/pub/static/exemples_grilles.png
Écrire une fonction naked_single(grid) qui reçoit en paramètre une matrice 9 x 9 d’entiers représentant une grille de
sudoku, et qui renvoie un couple de valeurs :
    un booléen ok qui indique si la grille peut être résolue en utilisant cette seule méthode du candidat unique,
    la grille complétée si ok est égal à True, None sinon.
Exemple 1 : L’appel de la fonction suivant :
naked_single([[4, 0, 3, 0, 9, 6, 0, 1, 0],
              [0, 0, 2, 8, 0, 1, 0, 0, 3],
              [0, 1, 0, 0, 0, 0, 0, 0, 7],
              [0, 4, 0, 7, 0, 0, 0, 2, 6],
              [5, 0, 7, 0, 1, 0, 4, 0, 9],
              [1, 2, 0, 0, 0, 3, 0, 8, 0],
              [2, 0, 0, 0, 0, 0, 0, 7, 0],
              [7, 0, 0, 2, 0, 9, 8, 0, 0],
              [0, 6, 0, 1, 5, 0, 3, 0, 2]])
retourne : (True, [[4, 7, 3, 5, 9, 6, 2, 1, 8],
        [6, 5, 2, 8, 7, 1, 9, 4, 3],
        [9, 1, 8, 3, 2, 4, 5, 6, 7],
        [3, 4, 9, 7, 8, 5, 1, 2, 6],
        [5, 8, 7, 6, 1, 2, 4, 3, 9],
        [1, 2, 6, 9, 4, 3, 7, 8, 5],
        [2, 9, 5, 4, 3, 8, 6, 7, 1],
        [7, 3, 1, 2, 6, 9, 8, 5, 4],
        [8, 6, 4, 1, 5, 7, 3, 9, 2]])


Exemple 2 : L’appel de la fonction suivant :
naked_single([[0, 0, 6, 0, 4, 0, 1, 0, 0],
              [0, 5, 0, 0, 9, 0, 0, 6, 0],
              [8, 0, 0, 0, 0, 0, 0, 0, 5],
              [0, 0, 0, 3, 0, 4, 0, 0, 0],
              [3, 1, 0, 0, 0, 0, 0, 4, 8],
              [0, 0, 0, 8, 0, 7, 0, 0, 0],
              [6, 0, 0, 0, 0, 0, 0, 0, 9],
              [0, 2, 0, 0, 3, 0, 0, 5, 0],
              [0, 0, 1, 0, 5, 0, 7, 0, 0]])
retourne : (False, None)
Consignes :    Dans la grille passée en paramètre, les cases vides sont représentées par l’entier 0.
    :return:    """
    def naked_single( grille ) :
        """ renvoie True et la grille de sudoku complétée ou False et None """
        lignes = [{ val for val in ligne if val != 0 } for ligne in grille ]
        transpose = [[ligne[i] for ligne in grille] for i, ligne in enumerate(grille)]
        colonnes = [{ val for val in ligne if val != 0 } for ligne in transpose ]

        secteur = [[set() for co in range(3)] for li in range(3)]
        # nombre de valeurs non nulles
        N = 0
        for li, ligne in enumerate(grille) :
            for co, val in enumerate(ligne) :
                if val != 0 : secteur[li//3][co//3].add(val)
                else : N += 1
        print("Nombre de valeurs non nulles de la grille : ", N)
        s = { i for i in range(1,10)}
        # initialisation de la matrice du sudoku à compléter : copie profonde de grille
        mat = [[val for val in ligne] for ligne in grille]

        nbVal = 9*9 - N
        nbValFinales = nbVal
        for compteur in range(nbVal) :
            for li, ligne in enumerate(grille) :
                for co, val in enumerate(ligne) :
                    if val == 0 :
                        # liste des éléments résultats de la différence entre l'ensemble des valeurs possible au sudoku
                        l = list(s.difference(colonnes[co].union(lignes[li],secteur[li//3][co//3])))
                        if len(l) == 1 :
                            nouvelleVal = l[0]
                            #print("nouvelleVal = ",nouvelleVal, " pour li =", li, " co = ", co)
                            mat[li][co] = nouvelleVal
                            #printMatrice(mat)
                            #input("pause")
                            colonnes[co].add(nouvelleVal)
                            lignes[li].add(nouvelleVal)
                            secteur[li//3][co//3].add(nouvelleVal)
                            nbValFinales += 1

        print("Pour : \n")
        printMatrice(grille)
        print("lignes : ",lignes)
        print("colonnes : ",colonnes)
        print("secteur : ",secteur)
        print("Nb val init = ", nbVal, " nb val finale = ", nbValFinales)
        printMatrice(mat)

        return (True, mat) if nbValFinales == 81 else (False, None)

    test = [[[4, 0, 3, 0, 9, 6, 0, 1, 0],
              [0, 0, 2, 8, 0, 1, 0, 0, 3],
              [0, 1, 0, 0, 0, 0, 0, 0, 7],
              [0, 4, 0, 7, 0, 0, 0, 2, 6],
              [5, 0, 7, 0, 1, 0, 4, 0, 9],
              [1, 2, 0, 0, 0, 3, 0, 8, 0],
              [2, 0, 0, 0, 0, 0, 0, 7, 0],
              [7, 0, 0, 2, 0, 9, 8, 0, 0],
              [0, 6, 0, 1, 5, 0, 3, 0, 2]],

            [[0, 0, 6, 0, 4, 0, 1, 0, 0],
             [0, 5, 0, 0, 9, 0, 0, 6, 0],
             [8, 0, 0, 0, 0, 0, 0, 0, 5],
             [0, 0, 0, 3, 0, 4, 0, 0, 0],
             [3, 1, 0, 0, 0, 0, 0, 4, 8],
             [0, 0, 0, 8, 0, 7, 0, 0, 0],
             [6, 0, 0, 0, 0, 0, 0, 0, 9],
             [0, 2, 0, 0, 3, 0, 0, 5, 0],
             [0, 0, 1, 0, 5, 0, 7, 0, 0]],

            [[0, 0, 3, 0, 2, 0, 6, 0, 0],
             [9, 0, 0, 3, 0, 5, 0, 0, 1],
             [0, 0, 1, 8, 0, 6, 4, 0, 0],
             [0, 0, 8, 1, 0, 2, 9, 0, 0],
             [7, 0, 0, 0, 0, 0, 0, 0, 8],
             [0, 0, 6, 7, 0, 8, 2, 0, 0],
             [0, 0, 2, 6, 0, 9, 5, 0, 0],
             [8, 0, 0, 2, 0, 3, 0, 0, 9],
             [0, 0, 5, 0, 1, 0, 3, 0, 0]]
            ]
    reponse = [(True,
                [[4, 7, 3, 5, 9, 6, 2, 1, 8],
                [6, 5, 2, 8, 7, 1, 9, 4, 3],
                [9, 1, 8, 3, 2, 4, 5, 6, 7],
                [3, 4, 9, 7, 8, 5, 1, 2, 6],
                [5, 8, 7, 6, 1, 2, 4, 3, 9],
                [1, 2, 6, 9, 4, 3, 7, 8, 5],
                [2, 9, 5, 4, 3, 8, 6, 7, 1],
                [7, 3, 1, 2, 6, 9, 8, 5, 4],
                [8, 6, 4, 1, 5, 7, 3, 9, 2]]),
               (False, None),
               (True,
                [[4, 8, 3, 9, 2, 1, 6, 5, 7],
                 [9, 6, 7, 3, 4, 5, 8, 2, 1],
                 [2, 5, 1, 8, 7, 6, 4, 9, 3],
                 [5, 4, 8, 1, 3, 2, 9, 7, 6],
                 [7, 2, 9, 5, 6, 4, 1, 3, 8],
                 [1, 3, 6, 7, 9, 8, 2, 4, 5],
                 [3, 7, 2, 6, 8, 9, 5, 1, 4],
                 [8, 1, 4, 2, 5, 3, 7, 6, 9],
                 [6, 9, 5, 4, 1, 7, 3, 8, 2]])]

    for n, g in enumerate(test) :
        (booleen, mat) = naked_single(g)
        if booleen == reponse[n][0] :
            print("test réussi pour check_rows(", g, ")")
            #print(g)
            print(reponse[n])
        else : print("test raté pour check_rows(", g, ")", " renvoie  = \n", bool, '\n Devrait être : ', reponse[n])
########################################################################################################################
def upilab6_5_10():
    """
6.5.10. Exercice UpyLaB 6.19 - Parcours rouge
Un dictionnaire peut nous permettre de manipuler des tableaux partiellement remplis, en ne stockant que les cases non
vides et en leur associant leur valeur.
Par exemple, le tableau suivant
https://upylab.ulb.ac.be/pub/static/exemple_carte.png
peut être implémenté par :
MY_PRECIOUS = 1
TRAP = -1
my_map = {}
my_map[(2,2)] = MY_PRECIOUS
my_map[(3,4)] = TRAP
my_map[(5,6)] = TRAP
my_map[(2,4)] = TRAP
my_map[(4,3)] = TRAP
Notez que les cases vides n’apparaissent pas dans le dictionnaire.
    Écrire une fonction create_map(size, trapsNbr) qui reçoit deux entiers en paramètres, size, compris entre 2 et 100,
    et trapsNbr, de valeur strictement inférieure à size x size, et qui retourne un dictionnaire implémentant comme
    dans l’exemple précédent une carte de taille size et dans laquelle figurent trapsNbr cases contenant un piège
    (modélisé par la valeur -1) et une case contenant un trésor (modélisé par la valeur 1). L’emplacement de ces cases
    sera aléatoire.
    Écrire une fonction play_game(map_size, treasure_map) qui reçoit un entier et une carte de taille
    map_size x map_size, telle que celles obtenues grâce à la fonction create_map, et qui demande à l’utilisateur
    d’entrer les coordonnées d’une case, jusqu’à tomber sur une case occupée. Si l’utilisateur a trouvé le trésor, la
    fonction retourne la valeur True, sinon l’utilisateur est tombé sur un piège et la fonction retourne False.

Exemple 1 : L’appel de la fonction suivant :
create_map(4, 5)
pourrait retourner :
{(3, 1): 1, (4, 2): -1, (1, 1): -1,
 (1, 4): -1, (2, 2): -1, (4, 4): -1}
Exemple 2 : L’appel de la fonction suivant :
play_game(5, {(3, 4): -1, (4, 1): 1, (2, 3): -1, (1, 5): -1})
avec les valeurs suivantes saisies en entrée :
4 2
4 4
1 3
4 4
3 1
4 4
4 3
1 1
3 1
3 2
2 1
4 3
1 2
4 1
retourne : True
Exemple 3 :
L’appel de la fonction suivant :
play_game(5, {(3, 4): -1, (4, 1): 1, (2, 3): -1, (1, 5): -1})
avec les valeurs suivantes saisies en entrée :
4 7
4 3
2 5
2 3
retourne : False
Consignes :
    Dans cet exercice, il vous est demandé d’écrire seulement des fonctions. Le code que vous soumettez à UpyLaB doit
    donc comporter uniquement la définition de ces fonctions.
    Le code que vous soumettez à UpyLab ne doit rien afficher. Veillez en particulier à ne pas ajouter de paramètre lors
    de vos appels à input.
    Notez que la numérotation des cases de la carte commence à (1, 1).
    Pour la fonction create_map, pensez à utiliser le module random, et le dictionnaire retourné ne comportera que les
    cases occupées.
    Pour la fonction play_game, les coordonnées saisies par l'utilisateur seront données sous la forme d'une série de
    deux entiers séparés par une espace, une case par ligne.
    Pour la fonction play_game, si les valeurs saisies par le joueur ne sont pas du bon type (entières) , ni dans le
    bon intervalle (comprises entre 1 et map_size), ces saisies seront ignorées par le programme.
    Notez enfin que les deux fonctions sont séparées et indépendantes l’une de l’autre.
    :return:
    """
    # si on programme : import random, il faut ensuite utiliser random.randint(début, fin)
    from random import randint    # c'est mieux !

    def create_map(size, trapsNbr) :
        """ crée un carte du jeu size x size avec 2 < size < 100
            trapNbr < size**2 """
        MY_PRECIOUS = 1
        TRAP = -1
        my_map = {}
        x, y = randint(1, size),randint(1, size)
        my_map[(x, y)] = MY_PRECIOUS
        for n in range(trapsNbr) :
            bonTirage = False
            while not bonTirage :
                x, y = randint(1, size), randint(1, size)
                if (x, y) not in my_map :
                    bonTirage = True
                    my_map[(x,y)] = TRAP
        return my_map

    for s in range(3,5) :
        n = 3*s//2
        print("Pour size = ", s, " et n trap = ", n, " la carte est : ", create_map(s,n))

    def play_game(map_size, treasure_map) :
        """ permet de jouer au jeu en entrant la taille de la carte et la carte et en demandant au joueur des 
        coordonnées """
        MY_PRECIOUS = 1
        TRAP = -1
        gagne = False
        perd = False
        while not gagne and not perd :
            coord = input()
            x, y = coord.split()
            x, y = int(x), int(y)
            if (x, y) in treasure_map :
                if treasure_map[(x,y)] == MY_PRECIOUS :
                    gagne = True
                elif treasure_map[(x,y)] == TRAP :
                    perd = True
                
        return True if gagne else False   
        
########################################################################################################################
def upilab6_5_11():
    """6.5.11. Exercice UpyLaB 6.20 - Parcours rouge
Arthur nous a envoyé des statistiques produites par UpyLaB contenant des informations sur des exercices et sur des
apprenants. Nous souhaitons utiliser ces informations pour classer les exercices.
Chaque jeu de données est formé de deux fichiers de type csv (produit par un tableur du type Excel ou LibreOffice) :
    un fichier 'result-pass-fail.csv'
    un fichier 'result-count.csv'
La structure d’un fichier “result-pass-fail-i.csv”
est la suivante :
En première ligne, nous trouvons les intitulés des exercices, chacun séparé du suivant par un caractère point-virgule
“;”.
Chacune des lignes suivantes correspond aux résultats d’un apprenant : chaque ligne a le même nombre d’éléments que le
nombre d’intitulés, et chaque élément vaut soit le texte 'VRAI', soit le texte 'FAUX', soit est vide (respectivement
suivant que l’apprenant a validé tous les tests UpyLaB pour l’exercice correspondant, a demandé la validation par
UpyLaB, mais malheureusement ce dernier a répondu par la négative, ou n’a pas encore testé l’exercice dans UpyLaB). À
nouveau sur une même ligne, chaque valeur est séparée de la suivante par un caractère point-virgule “;”.
La structure du fichier “result-count-i.csv”
est similaire à celle du premier fichier, à la différence près que les textes “VRAI” ou “FAUX” sont remplacés par des
nombres naturels strictement positifs donnant le nombre de fois où l’apprenant a testé son code. À nouveau l’entrée est
vide si aucune validation n’a été demandée par l’apprenant.
De façon précise, la structure d’un fichier 'result-count-i.csv' est la suivante :
En première ligne, nous trouvons les intitulés des exercices, chacun séparé du suivant par un caractère point-virgule
“;”.
Chacune des lignes suivantes correspond aux résultats d’un apprenant : chaque ligne a le même nombre d’éléments que le
nombre d’intitulés, et chaque élément représente soit un nombre entier strictement positif, soit est vide
(respectivement suivant que l’apprenant a validé ou essayé de valider les tests UpyLaB pour l’exercice correspondant ou
 n’a pas encore testé l’exercice dans UpyLaB). À nouveau sur une même ligne, chaque valeur est séparée de la suivante
 par un caractère point-virgule “;”.
Écrire un programme qui lit depuis l’entrée deux chaînes de caractères, représentant les noms des deux fichiers décrits
ci-dessus (dans l’ordre, le fichier de type “result-pass-fail.csv” suivi du fichier du type “result-count.csv”), et qui
imprime la liste des intitulés, un par ligne, dans l’ordre décroissant des « valeurs » calculées comme suit.
La « valeur » d’un intitulé est le nombre des « apprenants fiables » ayant réussi l’exercice correspondant.
Un « apprenant fiable » est un apprenant qui n’a jamais testé plus de dix fois chacun des codes qu’il a essayé de
valider.
Par exemple, si un apprenant n’a testé que trois exercices en soumettant respectivement 1, 2 et 10 essais, il est réputé
« fiable ». Si un autre apprenant a testé tous les exercices, mais en soumettant 11 essais pour l’un d’entre eux, il
n’est pas considéré comme « fiable ».
Exemple
Avec le fichier result-pass-fail-0.csv contenant :
ex1;ex2;ex3
VRAI;VRAI;VRAI
VRAI;VRAI;VRAI
VRAI;FAUX;FAUX
VRAI;VRAI;VRAI
VRAI;VRAI;
FAUX;VRAI;VRAI
et le fichier result-count-0.csv contenant :
ex1;ex2;ex3
2;3;5
1;2;4
4;2;666
11;6;3
1;1;
7;7;7
le programme affiche :
ex2
ex3
ex1
En effet, les apprenants 3 et 4 ne sont pas fiables. Ainsi, la valeur de ex2 est égale à 4 ; ex1 et ex3 ont tous les
deux une valeur égale à 3 mais ex3 est supérieur à ex1 dans l’ordre utf-8.
Consignes
    Notez que dans cet exercice, il vous est demandé d’écrire un programme qui fera appel aux fonctions input et print.
    Nous rappelons que votre code sera évalué en fonction de ce qu’il affiche, donc veillez à n’imprimer que le résultat
    attendu. En particulier, il ne faut rien écrire à l’intérieur des appels à input( input() et non input("Entrer un
    nom de fichier : ") par exemple), ni ajouter du texte supplémentaire dans ce qui est imprimé (print(intitules) et
    non print("liste des intitulés :",intitules) par exemple).
    Les fichiers utilisés par UpyLaB pour tester votre code sont :
            https://upylab.ulb.ac.be/pub/data/result-pass-fail-0.csv
            https://upylab.ulb.ac.be/pub/data/result-count-0.csv
            https://upylab.ulb.ac.be/pub/data/result-pass-fail-1.csv
            https://upylab.ulb.ac.be/pub/data/result-count-1.csv
    En cas d’égalité, les exercices seront classés selon l’ordre décroissant UTF-8 de leurs intitulés.
    Nous vous conseillons de définir des fonctions annexes que votre programme appellera.
    Le nombre maximal d’essais pour être supposé « apprenant fiable », 10 ici, peut être vu comme une constante globale
    du programme.
Remarque
Cet exercice vous demande de lire des fichiers csv. Cela peut se faire bien entendu avec ce qui a été vu jusque là dans
ce cours, mais vous pouvez aussi consulter la section 6.6 qui présente les outils spécifiques à la manipulation de ces
fichiers csv.
    :return:
    """
    # Nombre d'exercices
    N_EXO = 3
    APPRENANT_FIABLE = 10

    def estFiable (dicPass, dicCount) :
        """si un apprenant n’a testé que trois exercices en soumettant respectivement 1, 2 et 10 essais, il est réputé
        « fiable ». Si un autre apprenant a testé tous les exercices, mais en soumettant 11 essais pour l’un d’entre
        eux, il n’est pas considéré comme « fiable »."""
        reussi = True
        nEssai = True
        for key in dicPass.keys :
            if not dicPass[key] == 'VRAI' : reussi = False
            if not dicCount[key] <= APPRENANT_FIABLE : nEssai = False
        return reussi and nEssai

    def lireLigneCSV (ligne) :
        #ligne = ligne[:len(ligne)-1] # enlève le caractère final \n
        listeElt = []
        mot, dansMot = '', False
        for car in ligne :
            if car == ';' or car == '\n' :
                dansMot = False
                listeElt.append(mot.strip())
            else :
                if not dansMot :
                    mot = car
                    dansMot = True
                else :
                    mot += car
        return listeElt
    #test de la fonction ci-dessus :
    print('1;1;\n donne :' , lireLigneCSV('1;1;\n'))


    def analyseResult( nomFichierResultPassFail, nomFichierResultCount) :
        """ ouvre et analyse les deux fichiers result-pass-fail-x.csv et result-pass-fail-x.csv
         :param nomFichierResultPassFail: ex1;ex2;ex3 \n VRAI;VRAI;VRAI \n VRAI;VRAI;FAUX \n VRAI;VRAI;VRAI
         :param nomFichierResultCount:    ex1;ex2;ex3 \n 2;3;5          \n 1;2;4          \n 21;4;1
         :return: liste ordonnée des exercices les mieux réussis (ici [ex2, ex1, ex3])
        """
        with open( nomFichierResultPassFail, "rt", encoding='utf-8') as nFRPF :
            dicPass= { 'ex1' : [], 'ex2' : [], 'ex3' : [] }
            for n, ligne in enumerate(nFRPF) :
                if n == 0 :
                    listeEntete = lireLigneCSV(ligne)
                else :
                    listePass = lireLigneCSV(ligne)
                    for exo, entete in enumerate(listeEntete) :
                        dicPass[entete].append(listePass[exo])

        print("dicPass = ", dicPass)
        nJoueurs = n

        with open( nomFichierResultCount, "rt", encoding='utf-8') as nFRPC :
            dicCount = { 'ex1' : [], 'ex2' : [], 'ex3' : [] }
            for n, ligne in enumerate(nFRPC) :
                if n == 0 :
                    listeEntete = lireLigneCSV(ligne)
                else :
                    listeCount = lireLigneCSV(ligne)
                    for exo, entete in enumerate(listeEntete) :
                        dicCount[entete].append(listeCount[exo])
                    print(dicCount)

        print("dicCount = ", dicCount)

        for n in range(nJoueurs) :
            if estFiable (dicPass, dicCount) :
                pass

        return ['ex1', 'ex2', 'ex3']


    #nomFichierResultPassFail = input()
    #nomFichierResultCount    = input()
    


    test = [
        ('result-pass-fail-0.csv','result-count-0.csv'),
        ('result-pass-fail-1.csv','result-count-0.csv')
    ]
    reponse = [
        ['ex2','ex3','ex1'],
        ['ex1', 'ex2', 'ex3']
    ]
    for n, (fP, fC) in enumerate(test) :
        liste = analyseResult(fP, fC)
        if liste == reponse[n] :
            print("test réussi pour analyseResult(", fP, ",", fC, ")")
            print(reponse[n])
        else : print("test raté pour analyseResult(", fP, ",", fC, ") qui renvoie  = \n", liste,
                     " au lieu de ", reponse[n])

########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################

if __name__ == '__main__' :
    """
    ne fonctionne que si ce module est exécuté directement
    """
    listeExo = ["upilab6_5_2", "upilab6_5_3","upilab6_5_4","upilab6_5_5","upilab6_5_6","upilab6_5_7","upilab6_5_8",
                "upilab6_5_9","upilab6_5_10","upilab6_5_11"
                ]
    resume = [
                    " retourne le résultat du test : est-ce que la planète est assez grande ...",
                    " le mot se trouve-t-il dans le fichier ?",
                    " retourne la liste de Conway qui doit succéder à la liste entrée",
                    " place le pion de couleur dans la colonne spécifiée ou renvoie false et la même matrice ...",
                    " retourne la couleur gagnante au puissance 4 ou None s'il n'y a pas d'alignement de 4 pions ",
                    " retourne un dictionnaire des fréquences de la chaque caractères d'une texte.",
                    " teste si chaque ligne de la grille de sudoku est valide (tous les chiffres de 1 à 9 une seule\
fois ) ",
                    " renvoie True et la grille de sudoku complétée ou False et None",
                    "crée un carte du jeu size x size avec 2 < size < 100   trapNbr < size**2",
                    "si un apprenant n’a testé que trois exercices en soumettant respectivement 1, 2 et 10 essais,\n il\
est réputé« fiable ». Si un autre apprenant a testé tous les exercices,\nmais en soumettant 11 essais pour l’un d’entre\
eux, il n’est pas considéré comme « fiable »."
             ]

    sortir = False
    while not sortir :
        print("\nAjouter au numéro du choix h pour obtenir des explications :")
        for i, exo in enumerate(listeExo) :
            print(i + 1, " ) " + exo + " qui : " + resume[i] )
        choix = input("Taper le numéro de votre choix et valider :")
        if 'h' in choix.lower() :
            n = int((choix.lower()).replace('h', ''))
            help(eval(listeExo[n-1]))
        else :
            N = len(listeExo)
            try :
                n = int(choix)
            except :
                print("Attention vous devez taper un nombre !")
                n = 666666
            if n <= N :
                print("Votre choix est ", str(n), "  " + listeExo[n-1] + " qui " + resume[n-1])
                eval(listeExo[n-1]+'()')
            else : sortir = True