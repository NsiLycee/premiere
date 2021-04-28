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

source : https://www.quennec.fr/comment/412#comment-412
"""

l = [['root', 'x', '0', '0', 'root', '/root', '/bin/bash'],
 ['daemon', 'x', '1', '1', 'daemon', '/usr/sbin', '/usr/sbin/nologin'],
 ['bin', 'x', '2', '2', 'bin', '/bin', '/usr/sbin/nologin'],
 ['sys', 'x', '3', '3', 'sys', '/dev', '/usr/sbin/nologin'],
 ['sync', 'x', '4', '65534', 'sync', '/bin', '/bin/sync'],
 ['games', 'x', '5', '60', 'games', '/usr/games', '/usr/sbin/nologin'],
 ['man', 'x', '6', '12', 'man', '/var/cache/man', '/usr/sbin/nologin'],
 ['lp', 'x', '7', '7', 'lp', '/var/spool/lpd', '/usr/sbin/nologin'],
 ['mail', 'x', '8', '8', 'mail', '/var/mail', '/usr/sbin/nologin'],
 ['news', 'x', '9', '9', 'news', '/var/spool/news', '/usr/sbin/nologin'],
 ['uucp', 'x', '10', '10', 'uucp', '/var/spool/uucp', '/usr/sbin/nologin'],
 ['proxy', 'x', '13', '13', 'proxy', '/bin', '/usr/sbin/nologin'],
 ['www-data', 'x', '33', '33', 'www-data', '/var/www', '/usr/sbin/nologin']]

import csv

# écriture
with open('passwd.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(l)
    
with open('passwd.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
"""
#lecture
with open('passwd.csv','r', newline='') as fichier
    print(fichier.read())
"""
