"""

        Corrigés d'Upilab fin du 5 et 6 en entier

"""
motClefsPython = ["False", "None", "True", "and", "as", "assert", "async", "await", "break", "class",
                  "continue", "def", "del", "elif", "else", "except", "finally", "for", "from", "global",
                  "if", "import", "in", "is", "lambda", "nonlocal", "not", "or", "pass", "raise", "return",
                  "try", "while", "with", "yield"]
def VF( booleen : bool) -> bool :
    "traduction en mots de la valeur d'un booléen."
    return "vrai" if booleen else "faux"

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
    def calcul_prix(produits, catalogue):
        somme = 0
        for p in produits:
            somme += catalogue[p] * produits[p]
        return somme

    test = [({'pack de fruits': 1, 'poisson': 2, 'jambon': 1, 'citron': 1, 'tomate': 1, 'pâtes': 1, 'sucre': 1,
              'pack de légumes': 1, 'café': 1, 'brocoli': 1, 'déodorant': 1, 'bière': 1},
             {'confiture': 3.15, 'vin': 6.3, 'poisson': 6.45, 'jambon': 2.1, 'pain': 1.25, 'shampooing': 2.5,
              "bouteilles d'eau": 1, 'tomate': 0.75, 'yaourts': 2.85, 'sucre': 0.65, 'pack de légumes': 4.2,
              'café': 4.75, 'brocoli': 1.5, 'riz': 3.1, 'jus de fruits': 2.25, 'déodorant': 2.2, 'dentifrice': 1.95,
              'fromage': 2.65, 'chocolats': 3.2, 'pack de fruits': 3.3, 'viande': 5.2, 'petits gâteaux': 4.35,
              'citron': 0.9, 'mouchoirs': 0.8, 'frites': 3.55, 'farine': 0.95, 'pâtes': 1.1, 'savon': 1.9,
              'bière': 2, 'huile': 1.65}),
            ({'chocolats': 1, 'jambon': 1, 'citron': 1, 'fromage': 2, 'yaourts': 1, 'pâtes': 2, 'savon': 1,
              'pack de légumes': 1, 'café': 2, 'brocoli': 1, 'riz': 2, 'mouchoirs': 1},
             {'confiture': 3.15, 'vin': 6.3, 'poisson': 6.45, 'jambon': 2.1, 'pain': 1.25, 'shampooing': 2.5,
              "bouteilles d'eau": 1, 'tomate': 0.75, 'yaourts': 2.85, 'sucre': 0.65, 'pack de légumes': 4.2,
              'café': 4.75, 'brocoli': 1.5, 'riz': 3.1, 'jus de fruits': 2.25, 'déodorant': 2.2, 'dentifrice': 1.95,
              'fromage': 2.65, 'chocolats': 3.2, 'pack de fruits': 3.3, 'viande': 5.2, 'petits gâteaux': 4.35,
              'citron': 0.9, 'mouchoirs': 0.8, 'frites': 3.55, 'farine': 0.95, 'pâtes': 1.1, 'savon': 1.9, 'bière': 2,
              'huile': 1.65})]
    reponse =[36.35, 40.650000000000006]
    for produits, catalogue in test :
        print("Le pépé a besoin de : ")
        for article in produits :
            print(produits[article], " x l'article : ", article)
        cout = calcul_prix(produits, catalogue)
        print( "cela coûtera", cout)
        printt("tes réussi ? : ", cout == reponse[test.index((produit,catalogue))])

########################################################################################################################
def upilab6_1_6 () :
    """6.1.6. Exercice UpyLaB 6.3 - Parcours bleu rouge
(D’après une idée de Jacky Trinh le 24/02/2018)
Un jury doit attribuer le prix du « Codeur de l’année ».
Afin de récompenser les trois candidats ayant obtenu la meilleure moyenne, nous vous demandons d’écrire une fonction
top_3_candidats(moyennes) qui reçoit un dictionnaire contenant comme clés les noms des candidats et comme valeurs la
moyenne que chacun a obtenue.
Cette fonction doit retourner un tuple contenant les noms des trois meilleurs candidats, par ordre décroissant de leurs
moyennes.
Exemple : L’appel suivant de la fonction :
top_3_candidats({'Candidat 7': 2, 'Candidat 2': 38, 'Candidat 6': 85,
                 'Candidat 1': 8, 'Candidat 3': 17, 'Candidat 5': 83,
                 'Candidat 4': 33})
doit retourner : ('Candidat 6', 'Candidat 5', 'Candidat 2')
"""
    def top_3_candidats(tableScores) :
        scores = []
        for candidat in tableScores :
            scores.append(tableScores[candidat])
        scores.sort(reverse=True)
        podium = []
        for i in range(3) :
            for candidat in tableScores :
                if scores[i] == tableScores[candidat] :
                    podium.append(candidat)
        return tuple(podium)

    test = {'Candidat 7': 2, 'Candidat 2': 38, 'Candidat 6': 85,
                 'Candidat 1': 8, 'Candidat 3': 17, 'Candidat 5': 83,
                 'Candidat 4': 33}
    reponse = ('Candidat 6', 'Candidat 5', 'Candidat 2')
    print("Pour la table des scores suivants :")
    print ("Nom du candidat     score")
    for candidat in test :
        print(candidat, "        ", test[candidat])
    podium = top_3_candidats(test)
    print("Podium :", podium)
    print("test réussi ? :", podium == reponse)

########################################################################################################################
def upilab6_1_7 () :
    """6.1.7. Exercice UpyLaB 6.4 - Parcours bleu rouge
Lors de prises de notes, il nous arrive souvent de remplacer des mots par des abréviations (bonjour est remplacé par bjr
par exemple).
Nous allons utiliser un dictionnaire qui associe à chacune de ces abréviations sa signification.
Écrire une fonction substitue(message, abreviation) qui renvoie une copie de la chaîne de caractères message dans
laquelle les mots qui figurent parmi les clés du dictionnaire abreviation sont remplacés par leur signification (valeur).
Exemple : L’appel suivant de la fonction :
substitue('C. N. cpt 2 to inf', {'C.' : 'Chuck','N.' : 'Norris','cpt' : 'counted','2' : 'two times','inf' : 'infinity'})
doit retourner : 'Chuck Norris counted two times to infinity'
"""
    def trouveDifference (texte1, texte2) :
        listeDiff = []
        for n, car in enumerate(texte1) :
            if texte1[n] != texte2[n] :
                listeDiff.append(n)
        return listeDiff

    def substitue(texte, dico) :
        """ subsitue des abréviations par les mots correspondant dans un dictionnaire."""
        mots = texte.split() # décompose le texte en liste de mots
        N = len(mots)
        t = ""  # texte à retourner
        for n, mot in enumerate(mots) : # pour chaque mot de la liste mots
            espace = ' ' if n < N-1 else ''
            if mot in dico :   # si le mot est une abréviation présente dans dico
                t += dico[mot] + espace   # le mot entier remplace l'abréviation
            else :
                t += mot + espace
        return t

    test = [('C. N. cpt 2 to inf',{'C.' : 'Chuck','N.' : 'Norris','cpt' : 'counted','2' : '2 times','inf' : 'infinity'}),
         ('viva C. N. : C. N. cpt 2 to inf and even further', {'2': '2 times', 'cpt': 'counted', 'N.': 'Norris',
                                                               'C.': 'Chuck', 'inf': 'infinity'}),
            ('A A A A is it good', {'2': '2 times', 'inf': 'infinity', 'A': 'Ha', 'N.': 'Norris', 'cpt': 'counted'}),
            ('mm les c', {'mm': 'messieurs', 'c': 'commissaires'})
         ]
    reponse = ['Chuck Norris counted 2 times to infinity',
               'viva Chuck Norris : Chuck Norris counted 2 times to infinity and even further',
               'Ha Ha Ha Ha is it good',
               'messieurs les commissaires']

    for p, d in test :
        r = substitue(p,d)
        rep = reponse[test.index((p,d))]
        print(p + " devient \n" + r )
        print("Test passé ? : \n|", r, "|\n|", rep,'|', rep == r,
              trouveDifference(rep, r))

########################################################################################################################
def upilab6_1_8 () :
    """6.1.8. Exercice UpyLaB 6.5 - Parcours vert bleu rouge
L'exercice suivant correspond à un problème dont la solution a déjà été donnée.
Mais pourrez-vous le refaire sans allez voir la solution donnée ?
Notez que la résolution de cet exercice vous donne quand même droit à un point  !
ÉNONCÉ DE L’EXERCICE UPYLAB 6.5
Écrire une fonction construction_dict_amis qui reçoit une liste de couples (prenom1, prenom2) signifiant que prenom1
déclare prenom2 comme étant son ami.
La fonction construit et renvoie un dictionnaire dont les clés sont les prénoms des personnes nommées, et la valeur de
chaque entrée est l’ensemble des amis de la personne.
Exemple : L’appel suivant de la fonction :
construction_dict_amis([('Quidam', 'Pierre'),
                        ('Thierry', 'Michelle'),
                        ('Thierry', 'Pierre')])
doit retourner : {'Quidam' : {'Pierre'}, 'Pierre' : set(), 'Thierry' : {'Michelle', 'Pierre'}, 'Michelle' : set()}
"""
    def construction_dict_amis(listeTupleCouples) :
        """ reconstitue l'ensemble des amis de chaque personne """
        dicReseau = {}
        for p1, p2 in listeTupleCouples :
            if p1 not in dicReseau : dicReseau[p1] = set()
            if p2 not in dicReseau : dicReseau[p2] = set()
            dicReseau[p1].add(p2)
        return dicReseau

    test = [[('Quidam', 'Pierre'),('Thierry', 'Michelle'),('Thierry', 'Pierre')],
            [('Pierre', 'Pierre'), ('Thierry', 'Pierre'), ('Pierre', 'Quidam'), ('Bernadette', 'Bernadette')],
            [('Bernadette', 'Bernadette'), ('Bernadette', 'Bernadette'), ('Thierry', 'Pierre'), ('Thierry', 'Michelle'),
             ('Bernadette', 'Michelle'), ('Pierre', 'Thierry'), ('Bernadette', 'Michelle'), ('Thierry', 'Bernadette'),
             ('Pierre', 'Michelle'), ('Ariane', 'Quidam'), ('Michelle', 'Michelle'), ('Michelle', 'Bernadette')],
            [('Thierry', 'Michelle'), ('Pierre', 'Bernadette'), ('Michelle', 'Pierre'), ('Bernadette', 'Bernadette'),
             ('Thierry', 'Michelle'), ('Michelle', 'Michelle'), ('Quidam', 'Michelle'), ('Thierry', 'Michelle'),
             ('Ariane', 'Bernadette'), ('Thierry', 'Thierry'), ('Michelle', 'Quidam'), ('Ariane', 'Ariane'),
             ('Thierry', 'Ariane'), ('Thierry', 'Michelle'), ('Ariane', 'Ariane')]
        ]
    reponse = [{'Quidam' : {'Pierre'}, 'Pierre' : set(),
                                                        'Thierry' : {'Michelle', 'Pierre'}, 'Michelle' : set()},
        {'Thierry': {'Pierre'}, 'Bernadette': {'Bernadette'}, 'Pierre': {'Pierre', 'Quidam'}, 'Quidam': set()},
               {'Ariane': {'Quidam'}, 'Thierry': {'Bernadette', 'Michelle', 'Pierre'}, 'Quidam': set(),
                'Bernadette': {'Bernadette', 'Michelle'}, 'Michelle': {'Bernadette', 'Michelle'},
                'Pierre': {'Michelle', 'Thierry'}},
               {'Ariane': {'Ariane', 'Bernadette'}, 'Thierry': {'Ariane', 'Michelle', 'Thierry'},
                'Quidam': {'Michelle'}, 'Bernadette': {'Bernadette'}, 'Michelle': {'Michelle', 'Pierre', 'Quidam'},
                'Pierre': {'Bernadette'}}
    ]

    for n, t in enumerate(test) :
        print("test réussi ? : ", construction_dict_amis(test[n]) == reponse[n] )
########################################################################################################################
def upilab6_1_9 () :
    """6.1.9. Exercice UpyLaB 6.6 - Parcours rouge
Écrire une fonction symetrise_amis qui reçoit un dictionnaire d d’amis où les clés sont des prénoms et les valeurs, des
ensembles de prénoms représentant les amis de chacun.
Cette fonction modifie le dictionnaire d de sorte que si une clé prenom1 contient prenom2 dans l’ensemble de ses amis,
l’inverse soit vrai aussi.
La fonction accepte un second paramètre englobe.
Si englobe est vrai, la fonction ajoutera les éléments nécessaires pour symétriser le dictionnaire d.
Sinon, la fonction enlèvera les éléments nécessaires pour symétriser d.
Exemple 1 : L’exécution du code suivant :
d = {'Thierry': {'Michelle', 'Bernadette'},
     'Michelle': {'Thierry'},
     'Bernadette': set()}
symetrise_amis(d, True)
print(d) doit afficher, à l’ordre près :
{'Thierry': {'Michelle', 'Bernadette'},
 'Michelle' : {'Thierry'},
 'Bernadette' : {'Thierry'}}

Exemple 2 :L’exécution du code suivant :
d = {'Thierry': {'Michelle', 'Bernadette'},
     'Michelle': {'Thierry'},
     'Bernadette': set()}
symetrise_amis(d, False)
print(d)
doit afficher, à l’ordre près :
{'Thierry': {'Michelle'},
 'Michelle' : {'Thierry'},
 'Bernadette' : set()}
 Montre l'importance de faire une copie profonde si on souhaite modifier le type construit dans la fonction
"""
    def symetrise_amis(dico, englobe) :
        """ modifie le dictionnaire des amis pour le symétriser :
        * soit en l'étandant        : englobe = True ;
        * soit en le contractant    : englobe = False ;"""
        dicCopy = {}  # copie profonde
        for p1 in dico :
            dicCopy[p1] = set() # copie profonde, la valeur est nouvelle
            # from copy import deepcopy      dicCopy = deepcopy ( dico )
            for p2 in dico[p1] :
                dicCopy[p1].add(p2)  # reconstitution d'un nouveau set
                mm
        for p1 in dicCopy :
            #set   + add   - discard
            for p2 in dicCopy[p1] :
                if englobe :    # add     = ajoute un élément
                    if p1 not in dicCopy[p2] :
                        dico[p2].add(p1)
                else :          # discard = enlève un élément
                    if p1 not in dicCopy[p2]:
                        dico[p1].discard(p2)
        """dico = {} marche pas dans ce sens ??? à partir de là dico n'est pas modifié en externe
        for p1 in dicCopy :
            dico[p1] = set() # copie profonde, la valeur est nouvelle
            for p2 in dicCopy[p1] :
                dico[p1].add(p2)  # reconstitution d'un nouveau set
        return dicCopy"""

    test =  [
        ({'Thierry': {'Michelle', 'Bernadette'}, 'Michelle': {'Thierry'}, 'Bernadette': set()}, True  ),
        ({'Thierry': {'Michelle', 'Bernadette'}, 'Michelle': {'Thierry'}, 'Bernadette': set()}, False )
            ]

    extension = [ " la contraction ", " l'extension "]

    reponse = [{'Thierry': {'Michelle', 'Bernadette'}, 'Michelle' : {'Thierry'}, 'Bernadette' : {'Thierry'} },
               {'Thierry': {'Michelle'}              , 'Michelle' : {'Thierry'}, 'Bernadette' : set()        }
               ]

    for t, b in test :
        print("Pour dico initial = \n", t, extension[int(b)], " donne ")
        dicCopy = symetrise_amis(t, b)
        print(t, " devrait être\n", reponse[test.index((t,b))])
        print(dicCopy)
        print("Test réussi ? :", t == reponse[test.index((t,b))])

########################################################################################################################
def upilab6_1_10 () :
    """6.1.10. Exercice UpyLaB 6.7 - Parcours vert bleu rouge
Écrire une fonction prime_odd_numbers(numbers) qui reçoit une liste de nombres et qui renvoie un couple d’ensembles
contenant respectivement les nombres premiers présents dans la liste et les nombres impairs.
Pour cela, nous vous demandons d’écrire au préalable deux fonctions annexes qui seront appelées dans le corps de la
fonction prime_odd_numbers :
    la fonction even qui accepte un nombre entier en paramètre et renvoie l’ensemble des nombres naturels pairs qui lui
    sont inférieurs ou égaux
    la fonction prime_numbers qui accepte un nombre entier en paramètre et renvoie l’ensemble des nombres premiers qui
    lui sont inférieurs ou égaux.
Exemple 1 : L’appel de la fonction suivant : prime_odd_numbers([1, 2, 6, 5, 11, 9, 13, 14, 12, 15, 17, 18])
retourne, à l’ordre près, :({2, 5, 11, 13, 17}, {1, 5, 11, 9, 13, 15, 17})
Exemple 2 : L’appel de la fonction suivant : prime_odd_numbers([1, 4, 6, 12, 9, 15, 16, 21, 18])
retourne, à l’ordre près, : (set(), {1, 9, 15, 21})
"""
    def even( nombre ) :
        """ renvoie l'ensemble des nombres pairs qui sont inférieurs ou égaux à nombre """
        ensemblePair = set()
        for n in range(0, nombre + 1, 2) :
            ensemblePair.add(n)
        return ensemblePair

    def maxL (liste) :
        """ retourne la valeur max d'une liste """
        max = -9e20
        for n in liste :
            if n > max : max = n
        return max

    def estPremier( n ) :
        """ teste si n est premier """
        premier = True if n % 2 != 0 else False
        for div in range(3,n,2) :
            if n % div == 0 : premier = False
        return premier

    def prime_numbers(nombre) :
        """ renvoie l'ensemble des nombres premiers inférieurs ou égaux à nombre """
        ensemblePremier = set()
        if nombre >= 2 :
            ensemblePremier.add(2)
            for n in range(3, nombre + 1, 2):
                if estPremier(n) : ensemblePremier.add(n)
        return ensemblePremier

    def prime_odd_numbers(numbers) :
        """ renvoie un tuple formé de l'ensemble des nombres pairs et l'ensemble des nombres premiers de la liste
            numbers """
        max = maxL(numbers)                     # nombre max de la liste
        print("max = ", max)
        premiers = prime_numbers(max)           # ensemble des premiers <= max
        pairs = even(max)                       # ensemble des nb pairs <= max
        print("ensemble des premiers : ", premiers, " ensemble des pairs : ", pairs)
        prem, impair = set(), set()
        for n in numbers :
            if n not in pairs :
                impair.add(n)
            if n in premiers :
                prem.add(n)
        return prem, impair

    test = [[1, 2, 6, 5, 11, 9, 13, 14, 12, 15, 17, 18], [1, 4, 6, 12, 9, 15, 16, 21, 18],
            [401, 562, 723, 884, 1045, 1206, 1367]]
    reponse = [({2, 5, 11, 13, 17}, {1, 5, 11, 9, 13, 15, 17}),
               (set(), {1, 9, 15, 21}), ({401, 1367}, {401, 723, 1045, 1367})]

    for n, t in enumerate(test) :
        tup = prime_odd_numbers(t)
        print("Dans la liste", t, " le retour donne ", tup)
        print("Test réussi ? :", tup == reponse[n])
########################################################################################################################
def upilab6_3_3 () :
    """6.3.3. Exercice UpyLaB 6.8 - Parcours vert bleu rouge
Écrire une fonction store_email(liste_mails) qui reçoit en paramètre une liste d’adresses e-mail et qui renvoie un
dictionnaire avec comme clés les domaines des adresses e-mail et comme valeurs les listes d’utilisateurs correspondantes, triées par ordre croissant (UTF-8).
Exemple :
L’appel de la fonction suivant :
store_email(["ludo@prof.ur", "andre.colon@stud.ulb",
             "thierry@profs.ulb", "sébastien@prof.ur",
             "eric.ramzi@stud.ur", "bernard@profs.ulb",
             "jean@profs.ulb" ])
retourne le dictionnaire :
{ 'prof.ur' : ['ludo', 'sébastien'],
  'stud.ulb' : ['andre.colon'],
  'profs.ulb' : ['bernard', 'jean', 'thierry'],
  'stud.ur' : ['eric.ramzi'] }"""
    def store_email(liste_mails) :
        listeDom = []
        dictDomNom = {}
        for email in liste_mails :
            [nom, domaine] = email.split('@')
            if domaine in listeDom :
                dictDomNom[domaine].append(nom)
                dictDomNom[domaine].sort()
            else :
                dictDomNom[domaine] = [nom]
                listeDom.append(domaine)
        return dictDomNom

    test = [["ludo@prof.ur", "andre.colon@stud.ulb","thierry@profs.ulb", "sébastien@prof.ur","eric.ramzi@stud.ur",
             "bernard@profs.ulb", "jean@profs.ulb" ],
            ['ludo@prof.ur', 'andre.colon@stud.ulb', 'thierry@profs.ulb', 'sébastien@prof.ur', 'eric.ramzi@stud.ur',
             'bernard@profs.ulb', 'jean@profs.ulb'],
            ['ludo@prof.ur', 'ludo@stud.ulb', 'ludo@profs.ulb', 'sébastien@prof.ur', 'sébastien@stud.ur',
             'sébastien@profs.ulb']
           ]
    reponse = [{ 'prof.ur' : ['ludo', 'sébastien'],  'stud.ulb' : ['andre.colon'],
                 'profs.ulb' : ['bernard', 'jean', 'thierry'],  'stud.ur' : ['eric.ramzi'] },
               {'profs.ulb': ['bernard', 'jean', 'thierry'], 'stud.ulb': ['andre.colon'],
                'prof.ur': ['ludo', 'sébastien'], 'stud.ur': ['eric.ramzi']},
               {'profs.ulb': ['ludo', 'sébastien'], 'stud.ulb': ['ludo'], 'prof.ur': ['ludo', 'sébastien'],
                'stud.ur': ['sébastien']}
               ]
    for n, t in enumerate(test) :
        dic = store_email(t)
        print("\n\n"+120*'_'+"à partir de ", t, "\n la fonction renvoie : \n", dic, "\n et il est attendu :\n", reponse[n] )
        print("Test réussi ? :", dic == reponse[n])
########################################################################################################################
def upilab6_3_4 () :
    """ 6.3.4. Exercice UpyLaB 6.9 - Parcours bleu rouge
Écrire une fonction compteur_lettres(texte) qui renvoie un dictionnaire contenant toutes les lettres de l’alphabet associées à leur nombre d’apparition dans texte.
Exemple : L’appel de la fonction suivant :
compteur_lettres("Dessine-moi un mouton !")
retourne :
{'a': 0, 'b': 0, 'c': 0, 'd': 1, 'e': 2,
 'f': 0, 'g': 0, 'h': 0, 'i': 2, 'j': 0,
 'k': 0, 'l': 0, 'm': 2, 'n': 3, 'o': 3,
 'p': 0, 'q': 0, 'r': 0, 's': 2, 't': 1,
 'u': 2, 'v': 0, 'w': 0, 'x': 0, 'y': 0,
 'z': 0}
Consignes
    Dans cet exercice, il vous est demandé d’écrire seulement la fonction compteur_lettres. Le code que vous soumettez
    à UpyLaB doit donc comporter uniquement la définition de cette fonction, et ne fait en particulier aucun appel à
    input ou à print.
    Les clés du dictionnaire seront les lettres de l’alphabet en minuscule. Si le texte contient des majuscules,
    celles-ci seront comptabilisées comme la lettre minuscule correspondante.
    Le texte passé en paramètre ne comportera aucun caractère accentué.
    Les espaces et autres caractères de ponctuation doivent être ignorés.

"""
    alphabet = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0,
                'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0,
                'y': 0, 'z': 0}
    accent = {'ñ' : 'n', 'à' : 'a', 'â' : 'a', 'ù' : 'u', 'é' : 'e', 'è' : 'e', 'ë' : 'e', 'ê' : 'e', 'ï' : 'i' }
    def compteur_lettres(texte) :
        """ renvoie un dictionnaire de la fréquence de chaque lettre de l'alphabet (non accentué et en minuscule) """
        dico = alphabet.copy()
        # Création du dictionnaire des lettre de l'alphabet, les fréquence (valeurs) sont nulles
        for car in texte :
            if car.isalpha() and car.isascii() :
                dico[car.lower()] += 1
            elif car.lower() in accent :  # remplace les caractères accentués par des non accentués
                dico[accent[car.lower()]] += 1
        return dico

    test = ["Dessine-moi un mouton !",
            'Je viens d’arriver a l’Universite Libre de Bruxelles et pour l’instant je m’y plais tres bien.',
            'Python est un langage de programmation objet, multi-paradigme et multiplateformes. Il favorise la \
programmation imperative structuree, fonctionnelle et orientee objet. Il est dote d’un typage dynamique fort, d’une \
gestion automatique de la memoire par ramasse-miettes et d’un systeme de gestion d’exceptions. Il est egalement \
apprecie par certains pedagogues qui y trouvent un langage ou la syntaxe, clairement separee des mecanismes de bas \
niveau, permet une initiation aisee aux concepts de base de la programmation.'
            ]
    reponse = [{'a': 0, 'b': 0, 'c': 0, 'd': 1, 'e': 2, 'f': 0, 'g': 0, 'h': 0, 'i': 2, 'j': 0, 'k': 0, 'l': 0,
                'm': 2, 'n': 3, 'o': 3, 'p': 0, 'q': 0, 'r': 0, 's': 2, 't': 1, 'u': 2, 'v': 0, 'w': 0, 'x': 0,
                'y': 0, 'z': 0},
               {'w': 0, 'i': 8, 'v': 3, 'n': 5, 'r': 8, 's': 6, 'b': 3, 'o': 1, 'g': 0, 'u': 3, 'p': 2, 'q': 0, 'f': 0,
            'l': 6, 'y': 1, 'z': 0, 'a': 4, 'k': 0, 'x': 1, 'e': 13, 'j': 2, 'c': 0, 't': 5, 'd': 2, 'm': 1, 'h': 0},
               {'w': 0, 'i': 32, 'v': 4, 'n': 30, 'r': 24, 's': 25, 'b': 4, 'o': 26, 'g': 14, 'u': 19, 'p': 17, 'q': 3,
                'f': 4, 'l': 16, 'y': 6, 'z': 0, 'a': 41, 'k': 0, 'x': 3, 'e': 71, 'j': 2, 'c': 9, 't': 41, 'd': 15,
                'm': 23, 'h': 1}
               ]
    for n, t in enumerate(test) :
        dic = compteur_lettres(t)
        print("\n\n"+120*'_'+"à partir de ", t, "\n la fonction renvoie : \n", dic, "\n et il est attendu :\n",
              reponse[n] )
        print("Test réussi ? :", dic == reponse[n])
########################################################################################################################
def upilab6_3_5 () :
    """6.3.5. Exercice UpyLaB 6.10 - Parcours rouge
Écrire une fonction valeurs(dico) qui doit fournir, à partir du dictionnaire donné en paramètre, une liste des valeurs
du dictionnaire triées selon leur clé.
Exemple : L’appel de la fonction suivant :
valeurs({'three': 'trois', 'two': 'deux', 'one': 'un'})
retourne : ['un', 'trois', 'deux']
En effet, les clés correspondantes sont “one” < “three” < “two” (ordre UTF-8).
Consignes
    Dans cet exercice, il vous est demandé d’écrire seulement la fonction valeurs. Le code que vous soumettez à UpyLaB
    doit donc comporter uniquement la définition de cette fonction, et ne fait en particulier aucun appel à input ou à
    print.
    Vous pourrez supposer que les clés du dictionnaire sont des chaînes de caractères.
"""
    def valeurs(dico) :
        """ retourne à partir du dictionnaire donné en paramètre, une liste des valeurs
du dictionnaire triées selon leur clé"""
        liste = []
        listeClefs = list(dico.keys())
        listeClefs.sort()
        for key in listeClefs :
            liste.append(dico[key])
        return liste

    test = [{'three': 'trois', 'two': 'deux', 'one': 'un'},
            {'Bernadette': ['Luc', 'Michel', 'Jules'], 'Jules': ['Bernadette'], 'Germaine': ['Catherine'],
             'Jean': ['Germaine'], 'Catherine': ['Jean'], 'Michel': ['Luc'], 'Luc': []},
            {'2': 'deux', '3': 'trois', '4': 'quatre', '6': 'six', '1': 'un', '5': 'cinq'}
            ]
    reponse = [['un', 'trois', 'deux'],
               [['Luc', 'Michel', 'Jules'], ['Jean'], ['Catherine'], ['Germaine'], ['Bernadette'], [], ['Luc']],
               ['un', 'deux', 'trois', 'quatre', 'cinq', 'six']
               ]

    for n, t in enumerate(test) :
        liste = valeurs(t)
        print("\n\n"+120*'_'+"à partir de \n", t, "\n la fonction renvoie : \n", liste, "\n et il est attendu :\n",
              reponse[n] )
        print("Test réussi ? :", liste == reponse[n])
########################################################################################################################
def differentsAnagrammes () :
    """Compare différents algorithmes de comparaison d'anagrammes :
6.4.1. Quiz de synthèse sur les structures de données
QUIZ DE SYNTHESE :
D’après le Larousse : une anagramme (le mot est féminin) est un mot formé en changeant de place les lettres d’un autre
mot. Par exemple, une anagramme de gare est rage.
Pour simplifier les exercices qui suivent :
    un "mot" correspond à une chaîne de caractères qui ne sera pas forcément un mot de la langue française ;
    nous incluons dans l’ensemble des anagrammes d’un mot le mot lui même : par exemple gare est une anagramme de gare ;
    un code correct est sensible à la casse ('S' n’est pas anagramme de 's') et aux accents ('é' n’est pas anagramme de
    'e') ;
    un cas limite est bien sûr la chaîne de caractère vide "" qui est anagramme d’elle-même ; vous pouvez supposer ici
    que ni a ni b ne sont des chaînes vides (chacune a au moins un caractère).
(Attention : un seul essai possible pour chaque question)
Pour chacune des fonctions suivantes, et en étant assuré que a et b sont bien des chaînes de caractères non vides,
déterminez pour la fonction si :
    le code est correct : son exécution teste bien pour n’importe quelles valeurs des chaînes de caractères a et b si
    oui ou non a et b sont des anagrammes ;
    le code peut se planter : c’est-à-dire, lors de l’exécution de la fonction avec certaines chaînes a et b,
    l’interpréteur peut provoquer une erreur ;
    le résultat peut être faux : pour certaines chaînes de caractères a et b données en paramètre, l’exécution de la
    fonction peut renvoyer
        True alors que les mots ne sont pas des anagrammes entre eux ou
        False alors que les mots sont des anagrammes.
Indication : Rappelez-vous que pour qu’une fonction soit correcte, elle doit donner le bon résultat pour tous les
paramètres permis. Avant de répondre à chaque question, nous vous conseillons vivement de tester les codes sur plusieurs
exemples bien choisis. Ne vous contentez pas de les tester sur des exemples simples comme pour les mots gare et rage
mais imaginez des cas plus compliqués.

Ainsi, pour cet exemple, les raisons principales pour qu’une fonction ne fasse pas toujours correctement son travail,
est que pour certains exemples, elle renvoie un résultat True alors que les mots ne sont pas des anagrammes entre eux.
La démarche de tester un code est d’aller à la chasse aux exemples où le code dysfonctionne pour une raison ou une
autre ; dans la jargon informatique on appelle cela : aller à la chasse aux bogues (bugs).
"""
    def anagramme_str1(a, b): #bad code
        res = False
        for i in a:
            res = (i in b)
        return res

    def anagramme_str2(a, b): #bad code
        res = True
        for i in a:
            if i not in b:
                res = False
        return res

    def anagramme_0(a, b):
        return sorted(a) == sorted(b)

    def anagramme_1(a, b):# plantage
        a.sort()
        b.sort()
        return a == b

    def anagramme_2(a, b): # bad toujours vrai car None  == None
        liste_a = list(a)
        liste_a = liste_a.sort()
        liste_b = list(b)
        liste_b = liste_b.sort()
        return liste_a == liste_b

    def anagramme_3(a, b):
        liste_a = list(a)
        liste_a.sort()
        liste_b = list(b)
        liste_b.sort()
        return liste_a == liste_b

    def anagramme_dico(a, b):
        res = False
        if len(a) == len(b):
            dic_a = {}
            dic_b = {}
            for i in a:
                dic_a[i] = dic_a.get(i, 0) + 1
            for i in b:
                dic_b[i] = dic_b.get(i, 0) + 1
            res = dic_a == dic_b
        return res

    def anagramme_dico2(a, b):
        res = False
        if len(a) == len(b):
            dic_a = {}
            dic_b = {}
            for i in a:
                dic_a[i] = dic_a.setdefault(i, 0) + 1
            for i in b:
                dic_b[i] = dic_b.setdefault(i, 0) + 1
            res = dic_a == dic_b
        return res

    def anagramme_list(a, b):
        res = False
        if len(a) == len(b):
            liste_b = list(b)
            res = True
            for i in a:
                if i in liste_b:
                    liste_b.remove(i)
                else:
                    res = False
        return res
    """NOTE SUR L’ITÉRATION SUR LES FONCTIONS
Supposons comme dans le dernier quiz que l’on désire tester différentes fonctions avec les mêmes arguments en nombre et 
valeurs, Python permet d’itérer sur une séquence de fonctions comme montré dans l’exemple qui suit :"""
    for f in (anagramme_str1, anagramme_str2, anagramme_0, anagramme_2,
              anagramme_3, anagramme_dico, anagramme_dico2,
              anagramme_list):
        print("avec la fonction", f.__name__)
        print(f('bonjour', 'jourbon'))
        print(f('bonjour', 'jouxron'))
        print(f('bonjour', 'bonjur'))
        print(f('bonjour', 'jjourbon'))
        """où les différentes fonctions anagramme_xxx ont toutes été définies avant. À chaque itération f référence une 
        des fonctions de la séquence. Notez l’utilisation de l’attribut __name__ pour imprimer le nom de la fonction 
        utilisée à chaque itération."""

########################################################################################################################

if __name__ == '__main__' :
    """
    ne fonctionne que si ce module est exécuté directement
    """
    listeExo = ["upilab5_9_4", "upilab5_9_5", "upilab5_9_6", "upilab5_9_7",
                "analyseTexte", "upilbab6_1_4", "upilab6_1_5","upilab6_1_6",
                "upilab6_1_7", "upilab6_1_8", "upilab6_1_9","upilab6_1_10",
                "upilab6_3_3", "upilab6_3_4", "upilab6_3_5", "differentsAnagrammes"
                ]

    resume = [
              " imprime à l'écran une matrice.",
              " calcule la trace d'une matrice.",
              " test si une matrice est antisymétrique",
              " retourne la matrice symétrique par rapport à l'horizontale",
              " utilise des fonctions d'analyse de texte",
              " renvoie la liste des amis pouvant fournir des objets ...",
              " calcul du cout d'une liste d'articles à acheter ...",
              " affichage du podium d'un concours",
              " subsitue des abréviations par les mots correspondant dans un dictionnaire.",
              " construction d'un dictionnaire d'ensembles d'amis. ",
              " symétrise le réseau d'amis en l'étendant ou le contractant.",
              " renvoie l'ensemble des nombres premiers et impairs de la liste en entrée.",
              " renvoie un dictionnaire d'utilisateurs de domaines à partir de la liste d'adresses mail",
              " renvoie un dictionnaire donnant la fréquence d'apparition de chaque lettre de l'alphabet dans le texte",
              "retourne à partir du dictionnaire donné en paramètre, une liste des valeurs du dictionnaire triées \
selon leur clé",
              "Compare différents algorithmes de comparaison d'anagrammes "
            ]

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
                n = 666666
            if n < N :
                print("Votre choix est ", str(n), "  " + listeExo[n] + " qui " + resume[n])
                eval(listeExo[n]+'()')
            else : sortir = True
