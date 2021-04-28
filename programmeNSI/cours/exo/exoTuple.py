"""
    Auteur : Joël Dendaletche

    Exercices sur les tuples
"""

"""
Exo 1 : écrire une fonction qui cherche simultanément l'élément de 
valeur minimale et l'élément de valeur maximale dans la liste des 
éléments d'un tuple 
et
renvoie un tuple (min, max)

Afficher le résultat pour les éléments du jeuDeTetsts suivant :
"""

jeuDeTests=[(5,-4,8,-3,1,0), (); (0,1,2,3,4) ; 
# une solution avec gestion d'erreur
def min_max ( t ):
    try :
        mini=t[0]
        maxi=t[0]
        for e in t : # pour chaque élément e de t faire :
            if mini > e : # si mini > e alors
                mini = e  # mini devient e
            elif maxi < e :
                maxi = e
        return(mini,maxi)
    except : # l'argument n'est pas un tuple valide
        return None

for t in jeuDeTests :
    print("Pour le tuple t = ",t," min_max(t) = ",min_max(t) )

"""
Ecrire une fonction qui prend en entrée un tuple (ici Mytuple)

"""
MyTuple=(0,1,​1​,​0,1,​1​,0,0,1,0,1)

​def​ Comptage(MyTuple):
    nb_0, nb_1 = 0, 0   # initialisation des compteurs
    for​ element in Mytuple :
        if​ element ==​ 0 ​:
            nb_0 += 1   # incrémentation du compteur
        ​else​ :
            nb_1 += 1
    return​(nb_0,nb_1)   # incrémentation du compteur

​print​(Comptage(MyTuple))

"""
"""
myTuple=(​4​,​8​,​−5​,​8​,​−2​,​1​)
​def​ SommeTuple(myTuple):
    somme =​​ 0
    n = ​len​(myTuple)
    i=​​ 0
  ​  while​ ( i < n ) :
        somme = somme + myTuple[i]
        i += 1
  ​return​(somme)
  
​​print​​(SommeTuple(myTuple))

"""

"""
