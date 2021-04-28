"""
    Auteur : Joël Dendaletche

    Mise en forme de l'affichage d'une table de données en format
    CSV :
    Comma Separated values
    https://fr.wikipedia.org/wiki/Comma-separated_values

    utilisé pour échanger des données entre logiciels :
        carnet d'adresses sur gmail
        excel, libre office calc
        
    Exercices : http://jodenda.free.fr/programmeNSI/cours/
                traitementDonneesEnTables.html
                
    Correction proposée pour l'exercices 6 : recherche et épuration
    des doublons
"""
from exo3 import lireCSV  # fonction de lecture et de construction 
# de la liste de dictionnaires

# fonctions d'affichage
from exo4 import printTableformateeDeco 

# fonction d'affichage complémentaire
from exo5 import printTitre 

########################################################################
 # fonction pour écrire l'accord du pluriel sur un mot
def pluriel(n, oux = False) : 
    if not oux :
        if n > 0 : return "s"
        else :  return ""
    else :
        if n > 0 : return "x"
        else :  return ""
########################################################################
#  exo6 : créer une liste des listes de doublons
########################################################################
def exo6 (BDD) :
    texte = "Requète : lister les doublons : créer une liste des listes de doublons"
    print ("\n\n\n",texte, "\n un doublon d'un enregistrement contient",
            " rigoureusement les mêmes données")
    N = len (BDD)  # nombres d'enregistrements ou fiches de la table (ou BDD)
    Nitems = len (BDD[0])-1  # nombre de colonnes ou de clefs dans la table

    nDoublon = 0
    for  n in range(0,N-1) :
        for  i in range(n+1,N) :
            # and n != i est inutile car i vaut au minimum n+1
            if BDD[n] == BDD[i] :
                print("La fiche ",n, " est le doublon de la fiche ", i)
                nDoublon += 1
                
    print("\nIl y a ", nDoublon, " doublon"+ pluriel(nDoublon))

    print("\nAvec l'exercice suivant (n°7),\nessayons de ne créer que",
                " des listes de doublons différents !")
 
########################################################################
#  exo7 : éviter de recompter deux fois les mêmes doublons
######################################################################## 
def inListeDeListes( a ,LL): 
    for  i in range(len (LL)) :
        if a in LL[i] : return True
    return False
######################################################################## 
def chercherListesDoublons(BDD) :
    N = len(BDD)
    listesDbl = []  # initialisation de la liste des listes de doublons
    for  n in range(0,N-1) :  # on va comparer les n-1 éléments de la table avec ...
        listeD = [BDD[n]]
        for  i in range(n+1,N) :  # un nombre décroissant d'éléments pour ne pas refaire deux fois la même comparaison
            if BDD[i] in listeD and not inListeDeListes( BDD[i] ,listesDbl) :  # and n != i est inutile car i vaut au minimum n+1
                print("La fiche ",n, " est le doublon de la fiche ", i)
                listeD.append(BDD[i])
        if len (listeD) > 1 : 
            listesDbl.append(listeD)
    return listesDbl 
######################################################################## 
def exo7 (BDD) :
    listePhrases = ["Pour continuer, il va falloir éviter de recompter deux fois les mêmes doublons ;",
    " pour cela, une liste de liste de doublons sera créée au fur et à mesure ",
    "que des doublons seront trouvés ;", " la liste de liste permettra de ne pas enregistrer comme doublon un enregistrement qui est déjà dans une des listes.",
    "Commencer par créer une fonction booléenne (qui fait un test vrai/faux),"," qui en entrée reçoit deux arguments : ",
    "le premier qui est la fiche ou dictionnaire dont on cherche si c'est un doublon ; ","le second qui est la liste de listes de doublons. ",
    "Pour s'en sortir, travailler sur papier avec une table très simple comprenant quelques doublons …"]
    for phrase in listePhrases :
        print(phrase)
    listesDbl = chercherListesDoublons(BDD)      

    nDbl = len (listesDbl)
    print("\nIl y a ", nDbl, " doublon" +     pluriel(nDbl)+" :")
########################################################################

    n = 1
    for  liste in listesDbl :
        print("\nDoublon n° ", n, " : ", liste, "\nCette liste contient ", 
                len (liste), " éléments redondants.")
        n += 1        
    
########################################################################
#  exo8 : écrire une fonction qui épure (enlève) les doublons.
######################################################################## 
def eliminerDoublons (table) :
    """ eliminerDoublons (table) permet de retourner une table épurée de
    ses doublons    """ 
    listesDbl = chercherListesDoublons(table)
    tableEpuree = []
    for  fiche in table :
        # traduire le test logique qui suit en français vulgarisé
        if not inListeDeListes(fiche ,listesDbl) or (not fiche in tableEpuree and inListeDeListes(fiche ,listesDbl)):
            tableEpuree.append(fiche)
    
    return tableEpuree
######################################################################## 
def exo8 (BDD) :
    paragraphe = ["la table non redondnate est reconstruite élément par élément",
    " en vérifiant qu'ils ne sont pas dans la liste des listes de doublons renvoyée par la fonction chercherListesDoublons(BDD).",
    "La fonction logique inListeDeListes( a ,LL) est utilisée pour tester si un enregistrement se retrouve au delà de une fois dans cette liste de listes\n"]
    for phrase in paragraphe :
        print(phrase)

    tableEpuree = eliminerDoublons (BDD)

    P = len (BDD)
    Q = len (tableEpuree)
    print("\nTable épurée des doublons : \n")
    printTableformateeDeco (tableEpuree)
    print( "\nCette table contient ", Q, " éléments, soit ", P - Q, " éléments de moins que la table redondante" )   

########################################################################
#  les codes suivants sont des codes de test :
######################################################################## 
def main() :
    """
    Fonction de test de lireCSV
    """
    print("Efface l'écran : "+ 57 * "\n")
              
    print("La table suivante est redondante : ")
    table = lireCSV("BDDdbl.csv", False)  # attention cette fois il y a des doublons !
    printTableformateeDeco (table)
    
    print("\nLa table contient ", len(table), 
            "lignes ou fiches ou enregistrements.")

    printTitre("Choix de l'exercice à tester")
    listeTitres = ["créer une liste des listes de doublons",
    "éviter de recompter deux fois les mêmes doublons",
    "écrire une fonction qui épure (enlève) les doublons."]
    for i in range(6,9) :
        print("- exercice n° ", i, "   ", listeTitres [i-6])
    n = int(input("numéro :"))
    
    if   n == 6 : exo6 (table)
    elif n == 7 : exo7 (table)
    elif n == 8 : exo8 (table)
    else        : print("Dommage, vous ne savez pas lire !")

if __name__ == "__main__":
    """
    Ne fonctionne que si c'est ce fichier qui est activé directement
    La variable __name__ prend la valeur du fichier activé en premier.
    """
    main()
