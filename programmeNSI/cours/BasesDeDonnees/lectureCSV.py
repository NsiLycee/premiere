"""
    Auteur : Joël Dendaletche

    Ouverture et lecture d'un fichier au format CSV
    Comma Separated values
    https://fr.wikipedia.org/wiki/Comma-separated_values

    utilisé pour échanger des données entre logiciels :
        carnet d'adresses sur gmail
        excel, libre office calc

"""

# exemple et source : https://www.w3schools.com/python/python_file_handling.asp
fichier = open("BDD.csv")    #ouverture en lecture r = read   et texte t par défaut
tab = []
compteur = 0

# lecture et affichage de chaque ligne
for ligne in fichier :
    tab.append(ligne)
    print ("ligne ",compteur+1," : ",ligne)
    compteur += 1

"""
	cela ne fonctionne que si tous les caractères sont codés en ASCII
	
"""
