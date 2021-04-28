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
"""


with open('BDD.csv', 'r') as fichier : # le bloc with ferme le fichier dès que le bloc est terminé
    
    BDD = []    #la table de base de données sera une liste de dictionnaires
    n = 0

    for ligne in fichier:
        if n == 0 : #lecture de la première ligne qui contient les clefs des dictionnaires
            clefs = ligne.split(',')
            nChamps = len(clefs)    #nombre de valeurs (et de clefs) dans chaque dictionnaire
            l = len(clefs[nChamps-1]) # longueur de la dernière clef
            clefs[nChamps-1] = clefs[nChamps-1][0:l-1]  #enlève les deux derniers caractères \n de retour à la ligne en fin de ligne
        else : 
            dictionnaire = {}   # le dictionnaire est initialisé
            # https://www.w3schools.com/python/python_strings.asp
            # pour voir les méthodes associées aux objets de type string
            enregistrement = ligne.split(',')
            m = 0
            #création d'une clef primaire
            dictionnaire ["clefPrim" ] = n 
            for valeur in enregistrement :
                if m == nChamps - 1 :
                    l = len(valeur) # longueur de la dernière valeur
                    valeur = valeur[0:l-1]  
                    #enlève les deux derniers caractères \n de retour à la ligne en fin de ligne

                dictionnaire [clefs [m] ] = valeur 
                m += 1
            BDD.append(dictionnaire)
            print("Enregistrement n° " , n+1, " : ", dictionnaire)
        n += 1 # compte les lignes lues
    
print ("____________________________________________________________________")
print ("BDD = ", BDD)

texte = "Requète : recherche des gens qui habitent dans un département dont le code postal est inférieur à 29990"
print ("\n\n\n",texte)
reponse = []

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
print ("BDD = ", BDD)
texte = "Requète : trier la BDD par ordre croissant de code postal"
print ("\n\n\n",texte)
reponse = []

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
