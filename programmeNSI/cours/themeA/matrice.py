"""
        Auteur : Joël Dendaletche
        Date de création : 2020 / 10 / 28
        But : implémenter l'objet (class) Matrice
"""

class Matrice :
    """ implémentation de l'objet Matice : tableau li x co = m x n """
    def __init__(self, matrice : list = [[]] ) :
        """ initialisation de l'objet """
        self._nLi = len(matrice)
        self._nCo = len(matrice[0])
        self._matrice = matrice
        self.__det = None
        self._trace = self.trace()

    def _init_mat(self):
        """ initialise la matrice li x co avec des zéro
        :param li:
        :param co:
        :return:  matrices de 0
        """
        return [[0 for i in range(self._nCo)] for j in range(self._nLi)]

    def lirePrompt (self) :
        self._nLi = int(input("Donner le nombre de lignes :"))
        assert self._nLi > 0, "Une matrice doit posséder un nombre entier strictement positif de lignes."
        self._nCo = int(input("Donner le nombre de colonnes :"))
        assert self._nLi > 0, "Une matrice doit posséder un nombre entier strictement positif de colonnes."
        #self._matrice = self._init_mat()
        self._matrice = [[int(input("valeur dans la "+str(li+1)+" ième ligne et la "+str(co+1)+" ième\
colonne")) for co in range(self._nCo)] for li in range(self._nLi) ]

    def lireDansFichierText ( nomFichier : str) -> None :
        """ lit les valeurs de la matrice dans un fichier texte (format *.txt) """
        try :
            with open(nomFichier, "r", encoding='utf-8') as fichier :
                mat = [[val for val in ligne.split()] for ligne in fichier]
                """
                mat = []
                for li, ligne in enumerate(fichier) :
                    listeLigne = []
                    for valeur in ligne.split() :
                        listeLigne.append(val)
                    mat.append(listeLigne)
                """
            self._matrice = mat
        except :
            print("Problème lors de la lecture du fichier : " + nomFichier)

    def trace (self) :
        """calcule la trace de la matrice ; c'est à dire la somme des valeurs dans sa première diagonale """
        if self._matrice == []: return 0
        M = self._matrice

        # liste des éléments de la diagonale où li == co (indices identiques)
        liste = [val for li, ligne in enumerate(M) for co, val in enumerate(ligne) if li == co]
        somme = 0
        for elt in liste:
            somme += elt
        return somme

    def stat (self, verbose : bool = False) -> tuple:
        """ méthode renvoyant un tuple des caractéristiques de la matrice """
        dete, self._trace = self.det(), self.trace()
        if verbose : #"My name is {fname}, I'am {age}".format(fname = "John", age = 36)
            print("La matrice a {li} lignes et {co} colonnes ; son déterminant vaut {det} et sa trace vaut {tr}".format(li = self._nLi , co = self._nCo, det = dete, tr = self._trace))
        return ( self._nLi, self._nCo, dete, self._trace )

    def det(self) -> float:
        """ retourne le déterminant de la matrice """
        if self._nLi == self._nCo :
            mat = self._matrice
            determinant = self._det(mat)   # à faire
        else :
            determinant = None
        return determinant

    def _det(self, mat : list) -> float :
        """ fonction récursive interne qui calcule le déterminant """
        nLi = len(mat)            # nombre de lignes
        if nLi < 2 :
            determinant = 0
        elif len(mat) == 2 :
            determinant = mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0]
        else :
            nCo = len(mat[0])     # nombre de colonnes
            for co in range(nCo) :
                mat[0][co] /= mat[0][0]     # l'élément 0,0 prend comme valeur 1
            # pourrait s'écrire   :   mat[0] = [val / mat[0][0] for val in M[0]]

            # C1 <- C1−mat[0][1]xC0, C2 <- C2−mat[0][1]xC0, ..., Cn <- Cn−mat[0][n]xCn
            # la première ligne devient alors    1  0   0  0  ... 0
            matReduite = []
            for li in range(1,nLi) :
                ligne = []
                for co in range(1,nCo) :
                    mat[li][co] - mat[0][co]*mat[li][0]
                    ligne.append(mat[li][co] - mat[0][co]*mat[li][0])
                matReduite.append(ligne)
            determinant = self._det(matReduite)
        return determinant

    def __neg__(self):
        """ retourne l'opposé de la matrice """
        return [[- val for val in ligne] for ligne in self._matrice ]

    def symetrique(self, direction = "Horizontale"):
        """ retourne la matrice symétrique par rapport à l'horizontale (par défaut) ou la verticale """
        pass

    def __mul__(self, autreM ) :
        """ renvoie le résultat de la multiplication de deux matrices """
        assert self._nCo == autreM._nLi, "pour multiplier A par B, il faut que les dimensions\
de A et B correspondent respectivement à n x x et y x n "
        # initialisation de la matrice résultats
        res = [[ 0 for co in range(autreM._nCo)] for li in range(self._nLi)]
        for li in range(self._nLi) :
            for co in range(autreM._nCo) :
                sommeProd = 0
                for n in range(self._nCo) :
                    sommeProd += self._matrice[li][n]*autreM._matrice[n][co]
                res[li][co] = sommeProd
        return Matrice(res)

    def __str__(self, marge = 2, bordure = True):
        """ écriture de la matrice par la fonction print """
        if self._nLi < 1 :
            texte = "Matrice vide"
        else :
            texte = ""
            for li in range(self._nLi) :
                if bordure : texte += "|" + marge*' '
                for co in range(self._nCo) :
                    texte += str(self._matrice[li][co])+ marge*' '
                texte += "|\n" if bordure else "\n"
        return texte

########################################################################################################################
def main() :
    """  fonction de test en utilisation locale à ce module """
    A = Matrice([[1],[2],[3]])
    print("A = ", A)
    print(A.stat(True))
    B = Matrice([[8,9,10]])
    print("B = ", B, B.stat(True))
    C = Matrice()
    print("C = ", C, C.stat(True))
    C.lirePrompt()
    print(C.stat(True))
    D = A*B
    print("D = AxB = ", D, "\n", D.stat(True))
    A= Matrice([[1,1],[1,1]])
    B = Matrice([[3,4],[5,6]])
    print(A, B, A*B)


# exécuté uniquement en local dans ce module
if __name__ == '__main__' : main()



