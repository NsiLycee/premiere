"""
        Programme NSI : lecture de données en Table, lecture de CSV
                        programmation orientée objet, TAD, Bases de données

        Auteur : Joël Dendaletche
        
        Projet : écriture de classe (objets) permettant de manipuler des
        données en tables (précurseur des bases de données)
        
        Surcharges :
        __lt__ lether than  	<
        __le__ lether equal 	<=
        __eq__ equal        	==
        __ge__ greater equal	>=
        __gt__ greater than		>
        __ne__ not equal		!=
"""
########################################################################
#  fonction qui crée un objet table par lecture d'un fichier csv
########################################################################
def csv2table(nomFichier, clefPrim = False) :
    """
    fonction qui ouvre en lecture un fichier au format csv situé dans 
    le chemin (path) indiqué, et renvoie un objet Table qui est une
    liste de dictionnaires.
    """
    # vérifications de la conformité du fichier
    longueurFichier = len(nomFichier) 
    # l'expression : assert (test logique) , "message si c'est faux"    
    # permet de traquer les erreurs (bugs)
    assert type(nomFichier) == str , "Erreur : le format du fichier doit être du texte"
    assert nomFichier[longueurFichier-4:longueurFichier] == '.csv' or nomFichier[longueurFichier-4:longueurFichier] == '.CSV' , "Erreur : le format du fichier doit finir par .csv ou .CSV"
    
    with open(nomFichier, "rt") as fichier : # le bloc with ferme le fichier dès que le bloc est terminé
        BDD = []    #la table de base de données sera une liste de dictionnaires
        n = 0		#compteur de lignes

        for ligne in fichier:
            if n == 0 : #lecture de la première ligne qui contient les clefs des dictionnaires
                clefs = ligne.split(',')
                nChamps = len(clefs)    #nombre de valeurs (et de clefs) dans chaque dictionnaire
                l = len(clefs[nChamps-1]) # longueur de la dernière clef
                clefs[nChamps-1] = clefs[nChamps-1][0:l-1]  #enlève le dernier caractère '\n' de retour à la ligne en fin de ligne
            else : 
                dictionnaire = {}   # le dictionnaire est initialisé
            # https://www.w3schools.com/python/python_strings.asp
            # pour voir les méthodes associées aux objets de type string
                enregistrement = ligne.split(',')
                m = 0
            #création d'une clef primaire
                if clefPrim : dictionnaire ["clefPrim" ] = n 
                for valeur in enregistrement :
                    if m == nChamps - 1 :
                        l = len(valeur) # longueur de la dernière valeur
                        valeur = valeur[0:l-1] #enlève le dernier caractère '\n' de retour à la ligne en fin de ligne

                    dictionnaire [clefs [m] ] = valeur # ajoute au dictionnaire le couple : clefs [m] : valeur
                    m += 1
                BDD.append(dictionnaire)
            n += 1 # compte les lignes lues
            
    return Table(BDD) # renvoie un objet Table

################################################################################
# objet liste de lignes d'un fichier CSV
class tableCSV :
    def __init__(self) :
        pass
################################################################################
# Objet Table  : liste de Dictionnaires de même dimension et clefs             # 
class Table :																   #
################################################################################
    def _assertListeDeDictionnairesConforme (self) :
        if self._liste == [] : assert True
        else :
            assert type(self._liste[0]) == dict, "La table doit être une liste de dictionnaires"
            listeClefs = list(self._liste[0].keys())
            for enregistrement in self._liste[1:] : #le premier dictionnaire est déjà testé
                assert listeClefs == list(enregistrement.keys())

    def __init__(self, listeDeDictionnaires = []) :
        assert type(listeDeDictionnaires) == list , "ATTENTION ! : une table est une liste de listes"
        self._liste = listeDeDictionnaires
        self._assertListeDeDictionnairesConforme ()
        if listeDeDictionnaires != [] :
            self._nEnregistrements = len(self._liste)
        else :
            self._nEnregistrements = 0
            
    def __len__(self) :
        return self._nEnregistrements
        
    def ajoutEnregistrement(self, dictionnaire ) :
        assert type(dictionnaire) == dict, "L'enregistrement doit être un dictionnaire"
        assert len(dictionnaire) == len(self._liste[0]), "le nombre de valeurs du nouvel enregistrement doit être le même que celui des autres enregistrements de la table"
        self._liste.append(dictionnaire)
        self._nEnregistrements += 1

    def convertirEnFichierCSV (self, nomFichier = "table.csv") :
        with open(nomFichier, "wt") as fichier :
            texte = ""
            for fiche in self._liste :
                pass 
                
    def _formaterColonnes (self) :
        """ Fonction qui renvoie un tuple :
    1) liste des clefs de la table ;
    2) taille du plus long élément de chaque 
    colonne sous forme d'une liste.
    Exemple pour : 
    table = [{"Nom" : "Doe"  , "Prenom" : "John"},
             {"Nom" : "Po"  ,  "Prenom" : "Edgard"},
             {"Nom" : "Ricki", "Prenom" : "Pictydirai"}]  
    La fonction renvoie : ["Nom", "Prenom"], [5, 10]
        """
        listeFormatsColonnes = []
        nC = len(self._liste[0]) # nombre de colonnnes

        listeClefs = self.Clefs() # liste des clefs de chaque dictionnaire de la table
        nF = len(self)    # nombre de fiches
        for col in range(nC) :
            taille = 0
            for numF in range(nF) :
                t = len(self._liste[numF][listeClefs[col]])
                if t > taille : taille = t
            tailleClef = len(listeClefs[col])
            if taille < tailleClef : taille = tailleClef
            listeFormatsColonnes.append(taille)
        return listeClefs, listeFormatsColonnes            
                
    def __str__(self) :            
        """ Fonction d'affichage ligne par ligne de la table 
        avec un format de type tableau en colonnes régulières """
        listeClefs, listeFormatsColonnes = self._formaterColonnes()
        nC, nF = len(listeClefs), len(self._liste)
        premiereLigne = "║"
        for elt in range(nC) :
        # écriture des bordures haute inter et basse
            if elt == 0 : 
                bordureHaut  = "╔" + (listeFormatsColonnes[elt] + 2)*"═" +"╦"
                bordureInter = "╠" + (listeFormatsColonnes[elt] + 2)*"═" +"╬"
                bordureBasse = "╚" + (listeFormatsColonnes[elt] + 2)*"═" +"╩"
            elif elt < nC - 1 : 
                bordureHaut  += (listeFormatsColonnes[elt] + 2)*"═" +"╦"
                bordureInter += (listeFormatsColonnes[elt] + 2)*"═" +"╬"
                bordureBasse += (listeFormatsColonnes[elt] + 2)*"═" +"╩"
            else : 
                bordureHaut  += (listeFormatsColonnes[elt] + 2)*"═" + "╗"
                bordureInter += (listeFormatsColonnes[elt] + 2)*"═" + "╣"
                bordureBasse += (listeFormatsColonnes[elt] + 2)*"═" + "╝"
        
            nEspaces = " " * (listeFormatsColonnes[elt]-len(listeClefs[elt]))
            premiereLigne += " " + listeClefs[elt] + nEspaces + " ║"
        texte = bordureHaut + "\n" + premiereLigne + "\n" + bordureInter + "\n"
        n = 0
        for fiche in self._liste :
            ligne = "║"
            for elt in range(nC) :
                valeur = fiche[listeClefs[elt]]
                nEspaces = " " * (listeFormatsColonnes[elt]-len(valeur))
                ligne += " " + str(valeur) + nEspaces + " ║"
            if n < nF - 1 :
                texte += ligne + "\n" + bordureInter + "\n"
            else :
                texte += ligne + "\n" + bordureBasse + "\n"
            n += 1  
        return texte
        
        
    def __repr__(self) :
        return __str__(self)
                
    def Clefs(self) :
        if self._liste != [] :
            return list(self._liste[0].keys())
        return []
           
    def chercher(self, clef, valeur) :
        for fiche in self._liste :
            if fiche [clef] == valeur : return fiche
        return None #si la valeur n'est trouvée dans aucune fiche ou enregistrement ou dictionnaire
        
    def trier (self, clef, boolCroissant = True) :
        pass
        
    def __eq__(self, table) : # le test == existe pour les listes
        return self._liste == table
    
    def sort(self, clef, croissant = True) :
        """ Fonction qui renvoie une table triée en fonction de la clef 
    spécifiée dans l'ordre croissant ou décroissant
        """
        # on vérifie si la clef existe dans table
        assert clef in self.Clefs(), "La clef "+clef+" de recherche n'existe pas dans la liste des clefs : "+self.Clefs()
        
        tab = self._liste.copy() #la copie permettra de ne pas toucher à l'original
        listeValeurs = []  # initialisation de la liste des valeurs à trier
        for fiche in tab :  
            listeValeurs.append(fiche[clef])
        # tri de liste
        listeValeurs.sort()    
        #print("Liste des valeurs triées pour la clef : ",clef, " : ", listeValeurs)
    
        if not croissant : listeValeurs = listeValeurs[::-1] #inversion
    
        tabTriee = []
        
        nF = len(tab)
        for i in range(nF) :
            for fiche in tab :
                if fiche[clef] == listeValeurs [i] :   
                   tabTriee.append(fiche)
                   tab.remove(fiche)
               #print("tabTriee  = ", tabTriee," tab = ",tab)
        
        # conversion en objet table        
        tableTriee = Table(tabTriee)
        return tableTriee

"""    # test logique plus petit que ; acronyme de "lether than"
    def __lt__(self, other):
        try:
            return self._liste < other._value
        except AttributeError:
        # I don't know how to compare to other
            return NotImplemented            
"""

""" TDD test driven developpement

        1) dresser la liste Pre des pré-conditions  ;
        2) dresser la listes Post des post-conditions ;
        3) écrire le code qui vérifie Pre et Post
        sources :

        https://openclassrooms.com/fr/courses/4425126-testez-votre-projet-avec-python/4435374-decouvrez-le-test-driven-development
"""

################################################################################
#                             Tests et applications                            #
################################################################################
def main() : # fonction principale = chef d'orchestre
    # production d'un exemple remplissant les préconditions
    clefs   =  ["prenom","nom"]
    donnees = [["Paul","Meurice"],["Jean","Bon"],["Pierre","Naud"],["Henri","Card"],
               ["Marie","Bisard"],["Lewis","Khy"],["Barnabee","Year"]]
    nClefs = len(clefs)
    nDonnees = len(donnees)

    tableCSV = []
    table = []
    for i in range(nDonnees) :
        dic = {}
        ligne = ""
        for j in range(nClefs) :
            dic[clefs[j]] = donnees[i][j]
            ligne += str(donnees[i][j]) + ','
        ligne = ligne[:len(ligne)-1] # enlève la dernière virgule
        ligne += '\n' # retour à la ligne en fin de ligne
        table.append(dic)
        tableCSV.append(ligne)

    print("tableCSV = ", tableCSV)
    print("Attention : l'ordre des clefs est arbitrairement choisi par python :")
    print("table = ")
    print(table)

    #table = csv2table("BDD.csv", True)
    table = Table(table)
    print(table)
    clef = input("Proposer une clef pour le tri parmi " + str(table.Clefs())+ " : ")
    while clef not in table.Clefs() : 
        print("Pour faire la recherche il faut que la clef existe !")
        clef = input("Proposer une clef pour le tri parmi " + str(table.Clefs())+ " : ")

    print("Table triée dans l'ordre croissant :")
    print(table.sort(clef, True))
    print("Table triée dans l'ordre décroissant :")
    print(table.sort(clef, False))
    
    print("Ajoutons vos informations dans la table.")
    fiche = {}
    fiche["prenom"] = input("Donnez SVP votre prénom : ")
    fiche["nom"] = input("Donnez SVP votre nom : ")
    print(fiche)
     
    table.ajoutEnregistrement(fiche)
    print(table)

########################################################################
if __name__ == "__main__":
    """ execute only if run as a script
    source : https://docs.python.org/fr/3/library/__main__.html
    """
    main()
    
        
        
        
        
    
    
    
    
    
    
    
    
