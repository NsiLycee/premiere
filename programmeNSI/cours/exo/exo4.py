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
                
    Correction proposée pour l'exercices 4 : fonctions d'affichage
                                             d'une table en tableau
"""
from exo3 import lireCSV  # fonction de lecture et de construction 
# de la liste de dictionnaires

# La mauvaise solution c'est :
########################################################################
# fonction d'affichage de la table par dictionnaires
def printTable (table) :
    """ Fonction d'affichage dictionnaire par dictionnaires de 
    la table """
    n = 0
    try :
        for  fiche in table :
            print("Fiche n° ", n, " de la table :", fiche)
            n +=1
    except : print("La table estvide !")
########################################################################
def formaterColonnes (table) :
    """ Fonction qui renvoie un tuple :
    1) liste des clefs de la table ;
    2) taille du plus long élément de chaque 
    colonne sous forme d'une liste.
    Exemple pour : 
    table = [{"Nom" : "Doe"  , "Prenom" : "John"},
             {"Nom" : "Po"  ,  "Prenom" : "Edgard"},
             {"Nom" : "Ricki", "Prenom" : "Pictydirai"}]  
    La fonction renvoie : ["Nom", "Prenom"], [5, 10]"""
    if table == [] : return [], []
    listeFormatsColonnes = []
    nC = len(table[0]) # nombre de colonnnes
    #source : https://www.science-emergence.com/Articles/Obtenir-une-liste-des-cl%C3%A9s-dun-dictionnaire-sous-python/
    listeClefs = list(table[0].keys()) # liste des clefs de chaque dictionnaire de la table
    nF = len(table)    # nombre de fiches
    for col in range(nC) :
        #print("\nPour : ",listeClefs[col], "\n")
        taille = 0
        for numF in range(nF) :
            t = len(table[numF][listeClefs[col]])
            #print(table[numF][listeClefs[col]], " de taille ", t)
            if t > taille : taille = t
        tailleClef = len(listeClefs[col])
        if taille < tailleClef : taille = tailleClef
        listeFormatsColonnes.append(taille)
        #print("Taille max de ", listeClefs[col] ," = ", taille)
    return listeClefs, listeFormatsColonnes
########################################################################
# une des bonnes solutions (sans décorations) :
########################################################################
# fonction d'affichage simple de la table
def printTableformatee (table) :
    """ Fonction d'affichage ligne par ligne de la table 
    avec un format de type tableau en colonnes de largeur régulière  """
    
    if table == [] : 
        print("La table estvide !")
        return None
        
    listeClefs, listeformatsColonnes = formaterColonnes (table)
    
    nC, nF = len (listeClefs), len (table)
    #nC est le nombre de colonne
    #nF est le nombre de lignes (ou fiches de données)
    
    #affichage de l'entête du tableau avec les noms de colonnes :
    premiereLigne = "║"      # le caractère "║" c'est pour faire joli
    for  elt in range(nC) :
        nEspaces = " " * (listeformatsColonnes[elt]-len (listeClefs[elt]))
        premiereLigne += " " + listeClefs[elt] + nEspaces + " ║"
    premiereLigne += "\n"     # retour à la ligne !
    
    #affichage des lignes du tableau
    n = 0
    for  fiche in table :
        ligne = "║"
        for  elt in range(nC) :
            valeur = fiche[listeClefs[elt]]
            nEspaces = " " * (listeformatsColonnes[elt]-len (valeur))
            ligne += " " + str(valeur) + nEspaces + " ║"
        print(ligne + "\n"  )
        n += 1
########################################################################
# fonction d'affichage décoratif de la table
########################################################################
def printTableformateeDeco (table) :
    """ Fonction d'affichage ligne par ligne de la table 
    avec un format de type tableau en colonnes de largeur régulière  """
    
    if table == [] : 
        print("La table estvide !")
        return None

    listeClefs, listeformatsColonnes = formaterColonnes (table)
    
    nC, nF = len (listeClefs), len (table)
    #nC est le nombre de colonne
    #nF est le nombre de lignes (ou fiches de données)
    
    premiereLigne = "║"     # élément décoratif !
    for  elt in range(nC) :
         # écriture des bordures haute inter et basse
        if elt == 0 : 
            bordureHaut  = "╔" + (listeformatsColonnes[elt] + 2)* "═" + "╦"   # 2 espaces sont ajoutés, un avant et un après la plus grande largeur
            bordureInter = "╠" + (listeformatsColonnes[elt] + 2)* "═" + "╬"
            bordureBasse = "╚" + (listeformatsColonnes[elt] + 2)* "═" + "╩"
        elif elt < nC - 1 : 
            bordureHaut  += (listeformatsColonnes[elt] + 2)* "═" + "╦"
            bordureInter += (listeformatsColonnes[elt] + 2)* "═" + "╬"
            bordureBasse += (listeformatsColonnes[elt] + 2)* "═" + "╩"
        else :  
            bordureHaut  += (listeformatsColonnes[elt] + 2)* "═" + "╗"
            bordureInter += (listeformatsColonnes[elt] + 2)* "═" + "╣"
            bordureBasse += (listeformatsColonnes[elt] + 2)* "═" + "╝"
        
        nEspaces = " " * (listeformatsColonnes[elt]-len (listeClefs[elt]))
        premiereLigne += " " + listeClefs[elt] + nEspaces + " ║"
    print(bordureHaut + "\n" + premiereLigne + "\n" + bordureInter)
    n = 0
    for  fiche in table :
        ligne = "║"
        for  elt in range(nC) :
            valeur = fiche[listeClefs[elt]]
            nEspaces = " " * (listeformatsColonnes[elt]-len (valeur))
            ligne += " " + str(valeur) + nEspaces + " ║"
        if n < nF - 1 :
             print(ligne + "\n" + bordureInter )
        else : 
             print(ligne + "\n" + bordureBasse )
        n += 1
########################################################################
########################################################################
#  les codes suivants sont des codes de test :
######################################################################## 
def main() :
    """
    Fonction de test de lireCSV
    """
    print("Deux tables sont lues : BDD.csv et BDDdbl.csv")
    print("_____________________________________________")
    
    BDD1 = lireCSV("BDD.csv")
    BDD2 = lireCSV("BDDdbl.csv")
    
    # test de la première fonction d'affichage simple
    printTableformatee (BDD1)
    print("\nLa table contient ", len(BDD1), 
            "lignes ou fiches ou enregistrements.\n\n")
    
    # test de la deuxième fonction d'affichage décoratif
    printTableformateeDeco (BDD2)
    print("\nLa table contient ", len(BDD2), 
            "lignes ou fiches ou enregistrements.")

    # permet de vérifier que la liste de dictionnaire est 
    # bien créée à partir de la lecture du fichier, sinon cela renvoie un 
    # message d'erreur et affiche None (le retour de la fonction)

if __name__ == "__main__":
    """
    Ne fonctionne que si c'est ce fichier qui est activé directement
    La variable __name__ prend la valeur du fichier activé en premier.
    """
    main()
