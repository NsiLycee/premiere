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
                
    Correction proposée pour l'exercices 9 : 
    
tri de la table en fonction d'une clef donnée
"""
# importation des fonctions créées dans les exercices précédents
###################################################################
from exo3 import lireCSV  # fonction de lecture et de construction 
# de la liste de dictionnaires

# fonctions d'affichage
from exo4 import printTableformateeDeco 

# fonction d'affichage complémentaire
from exo5 import printTitre 

from exo6 import pluriel, inListeDeListes, eliminerDoublons

######################################################################## 
def triTable(table, clef, croissant = True) :
    """ Fonction qui renvoie une table triée en fonction de la clef 
    spécifiée dans l'ordre croissant ou décroissant
    on pourrait vérifier si la clef existe dans table"""
    tab = table.copy() #la copie permettra de ne pas toucher à l'original

    listeValeurs = []   # initialisation de la liste des valeurs à trier
    for  fiche in tab :  
        listeValeurs.append(fiche[clef])
    # pour debugguer : print(""Liste des valeurs pour la clef : "",clef, "" : "", listeValeurs)
 
     # tri de liste
    listeValeurs.sort()    
    # pour debugguer : # print(""Liste des valeurs triées pour la clef : "",clef, "" : "", listeValeurs)
    
    if not croissant : listeValeurs = listeValeurs[::-1] #inversion
    # pour debugguer : print(""Liste inversée des valeurs triées pour la clef : "",clef, "" : "", listeValeurs)
    
    tableTriee = []
    nF = len (tab)       # nombre de fiches de la table
    for  i in range(nF) :
        trouve = False
         # on cherche :
        
        for  fiche in tab :
            # print(""i = "",i,"" n = "", n, "" sur "", len (tab))
            if fiche[clef] == listeValeurs [i] :   
                # print(""fiche[""+clef+""] = "" , fiche[clef], ""listeValeurs [""+str(i)+""] = "", listeValeurs [i])
                # print(fiche)
                tableTriee.append(fiche)
                tab.remove(fiche)       # supprime la fiche déjà insérée
    return tableTriee
########################################################################
#  exo9 : tri de la table en fonction d'une clef donnée.
######################################################################## 
def exo9 () :
    print(60 * "\n")  # efface la page 
    printTitre ("exo9 : tri de la table en fonction d'une clef donnée")
    
    print ("\nLa table BDD est une liste de dictionnaires. Pour une ",
    "clef donnée , la liste des valeurs correspondantes (à cette clef)",
    " sera extraite à partir du parcours de chaque ligne de la table. ",
    "\nPuis la méthode sort() sera apliquée à cette liste. ",
    "\nCette liste sera ensuite parcourue pour reconstruire une table",
    " triée selon l'ordre croissant des valeurs associées à cette clef.",
    "\n Pour un ordre décroissant, la liste triée sera inversée par le ",
    "\nslice listeTriee[::-1] qui inverse en place la liste. \n\n")
 
 ########################################################################
#  les codes suivants sont des codes de test :
######################################################################## 
def main() :
    """
    Fonction de test de tris
    """
    exo9 ()   # présentation
              
    printTitre("Trier une table en fonction d'une clef choisie : ")
    
    table = lireCSV("BDD.csv", False)  
    print("\n")
    printTitre("Table non triée :")
    printTableformateeDeco (table)
    
    print("\nLa table contient ", len(table), 
            "lignes ou fiches ou enregistrements.")

    continuer = True
    while continuer :
        print("\n")
        printTitre("Choix du tri à tester")
        
        listeTitres = ["Tri croissant pour les éléments 'code Postal';",
        "Tri décroissant pour les éléments 'code Postal';",
        "Tri par nom croissant;",
        "Tri par 'Dossier num' décroissant."]
        
        N = len(listeTitres)
        for i in range(1,N+1) :
            print("- exemple n° ", i, "   ", listeTitres [i-1])
        n = int(input("\nVotre choix est le numéro : "))
        print(listeTitres[n-1])
        
        if   n == 1 : 
            printTableformateeDeco (triTable(table,"code Postal", True))
        elif n == 2 : 
            printTableformateeDeco (triTable(table,"code Postal", False))
        elif n == 3 : 
            printTableformateeDeco (triTable(table,"Nom", True))
        elif n == 4 : 
            printTableformateeDeco (triTable(table,"Dossier num", False))
        else        : print("Dommage, vous ne savez pas lire !")
        
        continuer = input("Voulez-vous continuer ? taper Y sinon autre chose :") == 'Y'

if __name__ == "__main__":
    """
    Ne fonctionne que si c'est ce fichier qui est activé directement
    La variable __name__ prend la valeur du fichier activé en premier.
    """
    main()


 
