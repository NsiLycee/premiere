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
                
    Correction proposée pour l'exercices 5 : requètes et leurs 
    solutionnement utilisant les tables
"""
from exo3 import lireCSV  # fonction de lecture et de construction 
# de la liste de dictionnaires

# fonctions d'affichage
from exo4 import printTableformatee, printTableformateeDeco 

########################################################################
def printTitre( texte ) :
    l = len(texte)
    print(" " * 10 + "╔"+ "═" * (l+4) + "╗")
    print(" " * 10 + "║  ",texte,"║")
    print(" " * 10 + "╚"+ "═" * (l+4) + "╝")    
                 
########################################################################
#  exo5 1 : compter les enregistrements dont le code postal est 
#           inférieur à codePostal
######################################################################## 
def exo5_1 (table) :
    printTitre("Exercice 5.1 : statistiques sur le code postal")
    
    codePostal = ""
    while codePostal == "" :
        try : # essaye ce qui suit
            codePostal = int(input("Donner un nombre à 5 chiffres de code postal :"))

            print ("\n\n\nRequète : recherche des gens qui habitent ",
                   "dans un département dont le code postal est ",
                   "inférieur à ",         str(codePostal) )

        except : # est exécuté si l'essai a conduit à un retour d'erreur
            print("SVP rentrer un nombre valide de code Postal")
        reponse = [] #initialisation de la liste des réponses attendues
    ####################################################################        
    for  enregistrement in table :
        if int(enregistrement["code Postal"]) < 30000 :
            reponse.append(enregistrement)
    ####################################################################           
    nRep = len (reponse)        # nombre de réponses
    if nRep == 0 :
         print("Il n'y a aucun enregistrement qui correspond à la ",
                "requète")
    else :
        print ("Il y a " + str(nRep) + " réponses : ")
        
    printTableformateeDeco (reponse)
########################################################################
#  exo5 2 : compter les fiches ou enregistrements dont le numéro de 
#            dossier est inférieur à numDossier
######################################################################## 
def exo5_2 (table) :
    printTitre("Exercice 5.2 : statistiques sur le numéro de dossier")
    
    numDossier = 0
    while numDossier <= 0 or numDossier > 9999 :
        try : # essaye ce qui suit
            numDossier = int(input("Donner un numéro de dossier à 4 chiffres :"))

        except : # est exécuté si l'essai a conduit à un retour d'erreur
            print("SVP rentrer un nombre à 4 chiffres !")
        
    
    print("Requète : pourcentage d'enregistrements dont le numéro de ",
        "dossier est plus grand que ", numDossier ," inclus")
    reponse = [] #initialisation de la liste des réponses attendues
    ####################################################################        
    for  enregistrement in table :
        if int(enregistrement["Dossier num"]) >=  numDossier :
            reponse.append(enregistrement)
    ####################################################################           
    nRep = len (reponse)        # nombre de réponses
    if nRep == 0 :
        print("Il n'y a aucun enregistrement qui correspond à la ",
                "requète")
    else :
        print("Il y a ",nRep / len(table) * 100, "% des enregistrements",
        " qui correspondent à la requète.")
    printTitre("Table des fiches dont le numéro de dossier est plus "+
				"grand que "+str( numDossier)+ " inclus")
    printTableformateeDeco (reponse)
########################################################################
#  exo5 3 : pourcentage d'enregistrements dont le nom commence par lettre
######################################################################## 
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m', 'n',
			'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def exo5_3 (table) :
    texte =" Exercice 5.3 : pourcentage d'enregistrements dont le nom commence par une lettre à choisir :"
    printTitre(texte)
    
    lettre = ""
    while lettre.lower() not in alphabet :
        try : # essaye ce qui suit
            lettre = input("Donner une lettre de l'alphabet :")

        except : # est exécuté si l'essai a conduit à un retour d'erreur
            print("Donner une seule lettre de l'alphabet !")
        
    
    print("Requète : pourcentage d'enregistrements dont le nom ",
        "commence par ", lettre)
    reponse = [] #initialisation de la liste des réponses attendues
    ####################################################################        
    for  enregistrement in table :
        if enregistrement["Nom"][0].lower() ==  lettre :
            reponse.append(enregistrement)
    ####################################################################           
    nRep = len (reponse)        # nombre de réponses
    if nRep == 0 :
        print("Il n'y a aucun enregistrement qui correspond à la ",
                "requète")
    else :
        print("Il y a ",nRep / len(table) * 100, "% des enregistrements",
        " qui correspondent à la requète.")
    printTitre("Table des fiches dont le nom commence par "+ lettre)
    
    printTableformateeDeco (reponse)
######################################################################## 
def viderEcran () :
    import os
    #os.system('cls')  # efface l'écran de la console cmd.exe sur windows
    os.system('clear')  # on linux / os x
    
    print("Le fichier BDD.csv est lu et converti en liste de ",
          "dictionnaires")

########################################################################
#  les codes suivants sont des codes de test :
######################################################################## 
def main() : 
    """
    Fonction de test de lireCSV
    """
    print("Efface l'écran : "+ 57 * "\n")
    print("___________________________________________________________",
          "____")
              
    table = lireCSV("BDD.csv")
    # test de la deuxième fonction d'affichage décoratif
    printTableformateeDeco (table)
    print("\nLa table contient ", len(table), 
            "lignes ou fiches ou enregistrements.")

    printTitre("Choix de l'exercice à tester")
    for i in range(1,4) :
        print("- exercice n° 5.", i)
    n = int(input("numéro :"))
    
    if   n == 1 : exo5_1 (table)
    elif n == 2 : exo5_2 (table)
    elif n == 3 : exo5_3 (table)
    else        : print("Dommage, vous ne savez pas lire !")

if __name__ == "__main__":
    """
    Ne fonctionne que si c'est ce fichier qui est activé directement
    La variable __name__ prend la valeur du fichier activé en premier.
    """
    main()



