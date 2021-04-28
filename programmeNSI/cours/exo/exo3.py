"""
    Auteur : Joël Dendaletche

    Ouverture et lecture d'un fichier au format CSV
    Comma Separated values
    https://fr.wikipedia.org/wiki/Comma-separated_values

    utilisé pour échanger des données entre logiciels :
        carnet d'adresses sur gmail
        excel, libre office calc
"""
def lireCSV(pathFichier , clefPrim = False) :
    """
    Fonction qui lit un fichier csv et construit une liste de dictionnaires
    clefPrim est un booleen qui par défaut vaut False
    si clefPrim = True, une clef primaire numérique unique est ajoutée à chaque
    dictionnaire
    """
    # vérifications de la conformité de pathFichier
    longueurFichier = len(pathFichier)
    # l'expression : assert (test logique) , "message si c'est faux"
    # permet de traquer les erreurs (bugs)
    assert type(pathFichier) == str , "Erreur : le format du fichier doit être du texte"
    assert pathFichier[longueurFichier-4:longueurFichier] == '.csv' or pathFichier[longueurFichier-4:longueurFichier] == '.CSV' , "Erreur : le format du fichier doit finir par .csv ou .CSV"

    try : # essaye d'ouvrir le fichier et si cela ne fonctionne pas 
        # renvoie un message d'erreur explicatif -> cf. except IOError = erreur d'entrée sortie (IO = In/Out)
        with open(pathFichier, 'r') as fichier : # le bloc with ferme le fichier dès que le bloc est terminé
            BDD = []    #la table de base de données sera une liste de dictionnaires
            n = 0        #compteur de lignes

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
                    # print("Enregistrement n° " , n, " : ", dictionnaire)
                n += 1 # compte les lignes lues
        return BDD #renvoi la liste de dictionnaires = BDD
    
    except IOError:
        print('An error occured trying to read the file : \nune erreur est survenue en essayant de lire le fichier (absent ou ayant un autre nom).')
    
    except ValueError:
        print('Non-numeric data found in the file.')

    except ImportError:
        print ("NO module found")
        
    except EOFError:
        print('Why did you do an EOF on me?')

    except KeyboardInterrupt:
        print('You cancelled the operation.')

    except:
        print('An error occured.')
        
########################################################################
#  les codes suivants sont des codes de test :
########################################################################
########################################################################
# fonction d'affichage de la table
def printTable (table) :
    """ Fonction d'affichage dictionnaire par dictionnaires de la table """
    n = 0
    for  fiche in table :
        print("Fiche n° ", n, " de la table :", fiche)
        n +=1
########################################################################  
def main() :
    """
    Fonction de test de lireCSV
    """
    BDD = lireCSV("BDD.csv")
    printTable(BDD)
    print("\nLa table contient ", len(BDD), "lignes ou fiches ou enregistrements.")
	# permet de vérifier que la liste de dictionnaire est 
	# bien créée à partir de la lecture du fichier, sinon cela renvoie un 
	# message d'erreur et affiche None (le retour de la fonction)

if __name__ == "__main__":
    """
    Ne fonctionne que si c'est ce fichier qui est activé directement
    La variable __name__ prend la valeur du fichier activé en premier.
    """
    main()
