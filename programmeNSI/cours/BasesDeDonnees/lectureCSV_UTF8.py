﻿"""
    Auteur : Joël Dendaletche

    Ouverture et lecture d'un fichier au format CSV
    Comma Separated values
    https://fr.wikipedia.org/wiki/Comma-separated_values

    utilisé pour échanger des données entre logiciels :
        carnet d'adresses sur gmail
        excel, libre office calc
        
https://docs.python.org/3/library/csv.html?highlight=cs#module-csv
"""
import io      # librairie de fonctions in/out = entrées/sorties

# exemple et source : https://www.w3schools.com/python/python_file_handling.asp

fichier = io.open("BDD.csv", mode="r", encoding="utf-8")    #ouverture en lecture r = read   et texte t par défaut
tab = []
compteur = 0

# lecture et affichage de chaque ligne
for ligne in fichier :
    tab.append(ligne)
    print ("ligne ",compteur+1," : ",ligne)
    compteur += 1

"""
	cela ne fonctionne que si tous les caractères sont codés en ASCII
	

fichier BDD.csv :  la première ligne contient les clefs de chaque dictionnaire contitué
par une ligne de tableau, soit un enregistrement de table de base de donnée

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
"""
