""""
    Auteur : Moi
Lecture écriture de fichier au format CSV

https://fr.wikipedia.org/wiki/Comma-separated_values

"""
# ouverture du fichir BDD.csv en lecture (read = r)
fichier = open("BDD2.csv","r")

# lit le contenu du fichier
print(fichier.read())

fichier.close()
print("ok c'est bien ouvert")

# ouverture du fichir BDD.csv en lecture (read = r)
fichier = open("BDD2.csv","r")

# lit le contenu du fichier ligne par ligne
compteur = 0
for ligne in fichier :
    compteur += 1
    print("Ligne n° ",compteur," : ",ligne)

fichier.close()
print("ok")
