def estPremier(n):
    """ teste si n est premier """
    premier = True if n % 2 != 0 or n == 2 else False
    for div in range(3, int((n+1)**.5), 2):
        if n % div == 0: premier = False
    return premier

def nombreNPremiers (n) :
    """ nombre des nombres premiers de 2 jusqu'à n inclus """
    li = []
    for i in range(2,n+1) :
        if estPremier(i) :
            print(i)
            li.append(i)
    return li, len(li)

nb = [10,100,1000]

def exoNPremiersNombresPremiers () -> None :
    """ imprime les n nombres premiers
    :return: None
    """
    nb = [10, 100, 1000]
    for i in nb :
        l, n = nombreNPremiers (i)
        print("Il y a ", n, " nombres premiers de 0 à ", i , "\nListe = ",l,"\n"+120*'_')

    print(l)

########################################################################################################################

def strSommeDiv (listeDiv : list) -> str :
    """ pour [1, 2, 3] renvoie "1 + 2 + 3"
    :param listeDiv: liste des diviseurs propres d'un nombre
    :return: phrase formée de la somme des éléments de la liste
    """
    somme =""
    N = len(listeDiv)
    for i, n in enumerate(listeDiv) :
        somme += str(n) + " + " if i != N-1 else str(n)
    return somme

def divPropre (nombre : int) -> list :
    """ exemple renvoie [1, 2, 3] pour n = 6
    :param n: nombre dont on cherche les diviseurs propres
    :return: liste des diviseurs propre de n
    """
    listeDivPropre = [1]
    for i in range(2, nombre):
        if nombre % i == 0:
            if i not in listeDivPropre:
                listeDivPropre.append(i)
    return listeDivPropre

def estParfait (nombre) :
    """Combien y a-t-il de nombres parfaits entre 1 et 1000 ?
(Un nombre parfait est égal à la somme de ses diviseurs propres (donc sans le compter lui-même comme diviseur !).
Par exemple, 6 = 1 + 2 + 3 est parfait."""
    rep = False
    somme = 0
    if estPremier(nombre) :
        rep = False
    else :
        listeDivPropre = divPropre(nombre)
        for i in listeDivPropre :
            somme += i

    if somme == nombre :
        rep = True
        print(nombre, " est un nombre parfait car ", nombre, " = " + strSommeDiv (listeDivPropre))
    return rep

########################################################################################################################
def nombresParfaits (n) :
    """ renvoie la liste et le nombre de nombres parfaits de 0 à n inclus
    Il y a  4  nombres parfaits de 2 à  10000  inclus, la liste en est :  [6, 28, 496, 8128]

     Un nombre parfait est égal à la somme de ses diviseurs propres (donc sans le compter lui-même comme diviseur ;
     Par exemple, 6 = 1 + 2 + 3 est parfait
     Dans le IXème livre des Eléments, Euclide d’Alexandrie (-320? ; -260?) expose une façon de générer des nombres
     parfaits :
"Lorsque la somme d’une suite de nombres doubles les uns des autres est un nombre premier, il suffit de multiplier ce
nombre par le dernier terme de cette somme pour obtenir un nombre parfait."
1+2=3 qui est premier donc 2x3=6 est parfait.
1+2+4=7 qui est premier donc 4x7=28 est parfait.
1+2+4+8=15 n’est pas premier.
1+2+4+8+16=31 est premier donc 16x31=496 est parfait.
En découle une formule qui porte aujourd’hui le nom de Formule d’Euclide :
2^(p-1)(2^p - 1) est parfait si p et (2^p - 1) sont premiers.
Source : https://www.maths-et-tiques.fr/index.php/histoire-des-maths/nombres/les-nombres-parfaits"""
    li = []
    for i in range(4,n+1) :
        if estParfait(i) :
            #print(i)
            li.append(i)
    return li, len(li)


def exoNombresParfaits () :
    """ renvoie la liste des nombres parfaits et compte leur  jusqu'à n """
    n = [10, 100,1000, 10000, 100000]

    for i in n :
        listeParfait, nbP = nombresParfaits (i)
        print("Il y a ", nbP, " nombres parfaits de 2 à ", i, " inclus, la liste en est : ", listeParfait)
########################################################################################################################
def chercheIndexDeDans(n, liste -> lst ) -> int :
    """
    :param n:
    :param liste:
    :return:
    """
    N = len(iste)


def rechercheNombresParfaitsSelonEuclide () -> list :
    """formule qui porte aujourd’hui le nom de Formule d’Euclide :
2^(p-1)(2^p - 1) est parfait si p et (2^p - 1) sont premiers.
Source : https://www.maths-et-tiques.fr/index.php/histoire-des-maths/nombres/les-nombres-parfaits
    :return: liste des nombres parfaits <= à n
    """
    def rechercheNP( n ) :
        with open("nombresParfaits.dat", "r", encoding="utf-8") as fichNP :
            listeNP = []
            for n in listeNP : listeNP.append(n)
        N = len(listeNP)
        if n in listeNP or n < listeNP [N-1] :
            i = chercheIndexDeDans(n, listeNP)
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
    listeExo = ["exoNPremiersNombresPremiers",
                "exoNombresParfaits",
                "rechercheNombresParfaitsSelonEuclide"
                ]
    resume = [
                " recherche de nombres premiers",
                " algorithme (très long) de recherche des nombres parfaits ",
                " algorithme de recherche des nombres parfaits selon la méthode d'Euclide"
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
                print("Votre choix est ", str(n-1), "  " + listeExo[n-1] + " qui " + resume[n-1])
                eval(listeExo[n-1]+'()')
            else : sortir = True