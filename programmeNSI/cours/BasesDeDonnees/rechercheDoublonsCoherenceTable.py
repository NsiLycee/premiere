"""
    Auteur : Joël Dendaletche

    Ouverture et lecture d'un fichier au format CSV
    Comma Separated values
    https://fr.wikipedia.org/wiki/Comma-separated_values

    utilisé pour échanger des données entre logiciels :
        carnet d'adresses sur gmail
        excel, libre office calc
        
https://docs.python.org/3/library/csv.html?highlight=cs#module-csv

Lecture d'un fichier csv d'une table de données (cf. BDD.csv ci-dessous)

Puis ensuite :
	-recherche de doublons, en partant du principe que deux doublons
	possèdent les même données, ce sont donc des dictionnaires identiques
	dans notre cas.
	d1 est le doublon de d2 si d1 == d2 est vrai
	la recherche des doublons va conduire à la contruction d'une liste de
	des listes de doublons, par exemple : 
			listeDoublons = [[d1,d15],[d3,d9,d65],[d7,d48,d57,d125]]
			
	- élimination des doublons : elle peut se faire au fur et à mesure 
	de leur découverte avec la méthode pop(), exemple :
			if d1 == d2 :
			    tableau.pop()
------------------------------------------------------------------------
La fonction lireCSV(pathFichier) lit les données d'une table sauvegardée 
en format CSV (dont le chemin et le nom sont pathFichier)
et renvoie une liste de dictionnaires dont les clefs sont les titres des
colonnes de la table et les données, celles de chaque ligne de données 
dans la table. Une clefPrimaire numérique est ajoutée au début
de  chaque dictionnaire (qui pourra être appelé par ailleurs fiche). 
Un argument clefPrim booléen ajoutera une clef primaire si 
clefPrim == True													 """

def lireCSV(pathFichier , clefPrim) :
    # vérifications de la conformité de pathFichier
    longueurFichier = len(pathFichier) 
    # l'expression : assert (test logique) , "message si c'est faux"    
    # permet de traquer les erreurs (bugs)
    assert type(pathFichier) == str , "Erreur : le format du fichier doit être du texte"
    assert pathFichier[longueurFichier-4:longueurFichier] == '.csv' or pathFichier[longueurFichier-4:longueurFichier] == '.CSV' , "Erreur : le format du fichier doit finir par .csv ou .CSV"

    with open(pathFichier, 'r') as fichier : # le bloc with ferme le fichier dès que le bloc est terminé
    
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
                print("Enregistrement n° " , n+1, " : ", dictionnaire)
            n += 1 # compte les lignes lues
    return BDD #renvoi la liste de dictionnaires = BDD
########################################################################
#																	   #
#						Utilisation de la table						   #
#																	   #
########################################################################
BDD = lireCSV("BDD.csv", True)
print ("____________________________________________________________________")
N = len(BDD) # nombre total d'enregistrements dans la table
print ("BDD de "+str(N)+ " enregistrements : ", BDD)
print ("____________________________________________________________________")
########################################################################

texte = "Requète : recherche des gens qui habitent dans un département dont le code postal est inférieur à 29990"
print ("\n\n\n",texte)

reponse = [] #initialisation de la liste des réponses attendues
for enregistrement in BDD :
    if int(enregistrement["code Postal"]) < 30000 :
        reponse.append(enregistrement)
        
nRep = len(reponse)       # nombre de réponses
if nRep == 0 :
    print("Il n'y a aucun enregistrement qui correspond à la requète")
else:
    print ("Il y a " + str(nRep) + " réponses : ")
    for fiche in reponse :
        print(fiche)
print ("____________________________________________________________________")
########################################################################

texte = "Requète : pourcentage d'enregistrements dont le numéro de dossier est plus grand que 2000 inclus"
print ("\n\n\n",texte)

reponse = [] #initialisation de la liste des réponses attendues

for enregistrement in BDD :
    if int(enregistrement["Dossier num"]) >= 2000 :
        reponse.append(enregistrement)
        
nRep = len(reponse)       # nombre de réponses
print("Il y a ",nRep/N*100,"% des enregistrements qui correspondent à la requète : ",
"\npourcentage d'enregistrements dont le numéro de dossier est plus grand que 2000 inclus")
print("liste des enregistrements dont le numéro de dossier est >= à 2000")
for fiche in reponse :
    print(fiche)
print ("____________________________________________________________________")
########################################################################
print ("\n\n\n") # saut de trois lignes
texte = "Requète : lister les doublons : créer une liste des listes de doublons"
print ("\n\n\n",texte, "\n un doublon d'un enregistrement contient rigoureusement les mêmes données")
print("La table suivante est redondante :")
BDD = lireCSV("BDDdbl.csv", False) # attention cette fois il y a des doublons !

N = len(BDD) # nombres d'enregistrements ou fiches de la table (ou BDD)
Nitems = len(BDD[0])-1 # nombre de colonnes ou de clefs dans la table

nDoublon = 0
for n in range(0,N-1) :
    for i in range(n+1,N) :
        if BDD[n] == BDD[i] : # and n != i est inutile car i aut au minimum n+1
            print("La fiche ",n, " est le doublon de la fiche ", i)
            nDoublon += 1
            
def pluriel(n) : # fonction pour écrire l'accord du pluriel sur un mot
    if n > 0 : return "s"
    else : return ""
print("\nIl y a ", nDoublon, " doublon"+ pluriel(nDoublon))

print("\n\nEssayons ne créer des listes de doublons différents !")

########################################################################
def inListeDeListes( a ,LL): 
    for i in range(len(LL)) :
        if a in LL[i] : return True
    return False

listesDbl = [] # initialisation de la liste des listes de doublons
for n in range(0,N-1) : # on va comparer les n-1 éléments de la table avec ...
    listeD = [BDD[n]]
    for i in range(n+1,N) : # un nombre décroissant d'éléments pour ne pas refaire deux fois la même comparaison
        if BDD[i] in listeD and not inListeDeListes( BDD[i] ,listesDbl) : # and n != i est inutile car i aut au minimum n+1
            print("La fiche ",n, " est le doublon de la fiche ", i)
            listeD.append(BDD[i])
    if len(listeD) > 1 : 
        listesDbl.append(listeD)
                    
print("\nIl y a ", len(listesDbl), " doublon"+ pluriel(len(listesDbl))+" :")

n = 1
for liste in listesDbl :
    print("\nDoublon n° ", n, " : ", liste, "\nCette liste contient ", len(liste), " éléments redondants")
    n += 1
########################################################################
print ("____________________________________________________________________")
print ("\n\n\n") # saut de trois lignes
texte = "Requète : éliminer les doublons ; une fonction est créée pour cela"
print ("\n\n\n",texte)

liste = [1,2,2,5,2,6,5,9,5,12,1]
print("Prenons comme exemple la liste : ", liste)

"""   algorithme à debugguer
def eliminerDoublons (table) :
    N = len(table)
    print("Taille de la liste initiale : ", N)
    listeIndexDoublons = []
    for n in range(0,N-1) :
        nD = 0 # compte les doublons repérés
        for i in range(n+1,N) :
            print("n = ", n , " i = ", i)
            if table[n] == table[i] :
                listeIndexDoublons.append(i-nD)
                nD += 1 # compte les doublons repérés
                print("Doublon : ", i)
    tableEpuree = []
    for i in range(N) :
        if table[i] not in listeIndexDoublons :
            tableEpuree.append(table[i])
    print("Taille de la liste finale : ", len(tableEpuree))
    print("Liste des indices de doublons : ", listeIndexDoublons)
    return tableEpuree

tableEpuree = eliminerDoublons (liste)
print("Table épurée des doublons : \n", tableEpuree)"""
print("Remarque importante : la fonction set(liste) crée un set qui est ",
"justement un ensemble ; c'est à dire une liste d'objets sans ",
"redondance !", "\n par exemple set(",liste,") affiche ",set(liste),
"\nLe set peut être converti en liste en faisant list(set(liste)) ",
"et cela donne la liste : ",list(set(liste)))




"""
Pour aller plus loin :
https://python.developpez.com/cours/TutoSwinnen/?page=page_18  
utilisation de import Gadfly et MySQL

fichier BDD.csv :  la première ligne contient les clefs de chaque 
dictionnaire contitué par une ligne de tableau, soit un enregistrement 
de table de base de donnée

Prenom,		Nom,			Dossier num,	courriel,						adresse,				code Postal

Jean,		Bon,			9112,			Jean.Bon@ac-from.fr,			955 rue des Bon,		22120
Marie,		DeVeaux,		1917,			Marie.DeVeaux@ac-from.fr,		3434 rue des DeVeaux,	87990
Jean-Pierre,Quiroul,		7037,			Jean-Pierre.Quiroul@ac-from.fr,	1696 rue des Quiroul,	29920
Emile,		Borne,			3438,			Emile.Borne@ac-from.fr,			4313 rue des Borne,		56550
Joel ,		Etlui,			1777,			Joel .Etlui@ac-from.fr,			4084 rue des Etlui,		68270
Jarod,		Enhyessenne,	989,			Jarod.Enhyessenne@ac-from.fr,	494 rue des Enhyessenne,4610
Marcel,		Lule,			5954,			Marcel.Lule@ac-from.fr,			801 rue des Lule,		36270
Sophie,		Philo,			2203,			Sophie.Philo@ac-from.fr,		3473 rue des Philo,		6050
Etienne,	Bienlebou,		7987,			Etienne.Bienlebou@ac-from.fr,	283 rue des Bienlebou,	47110
Adele,		Blancsec,		3817,			Adele.Blancsec@ac-from.fr,		3599 rue des Blancsec,	37730
Paul,		Igarchie,		4891,			Paul.Igarchie@ac-from.fr,		2544 rue des Igarchie,	55970
Sandy,		Manche,			4359,			Sandy.Manche@ac-from.fr,		220 rue des Manche,		45420
Marie,		Pierre,			7522,			Marie.Pierre@ac-from.fr,		173 rue des Pierre,		36600
Eude,		Trois,			4308,			Eude.Trois@ac-from.fr,			459 rue des Trois,		59320
Laly ,		Lala,			7272,			Laly .Lala@ac-from.fr,			1446 rue des Lala,		24020

Remarque : tous les caractères accentués non ascii ont été remplacés
par des caractères sans accent pour éviter une erreur de lecture

Opération d'ouverture et de lecture d'un fichier texte :
--------------------------------------------------------
f = open('BDD.csv','r')    # fichier texte par défaut
print(f.read()) # affiche toutes les lignes du fichier texte

print(f.read()) #n'affiche plus rien car le fichier est lu comme un itérateur et une
fois qu'il est parcouru, on reste à la fin du fichier
f.close()    # une fois le fichier fermé, on ne peut plus le lire

"""
