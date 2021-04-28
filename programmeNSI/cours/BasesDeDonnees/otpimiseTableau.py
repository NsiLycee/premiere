"""
Calcul permettant d'optimiser l'affichage de valeurs dans un tableau
compact

Lorsque l'on souhaite ranger sous forme de tableau un ensemble ou liste
de données, il serait intéressant de le présenter sous une forme proche 
du carré. Par exempe 36 valeurs pourront se ranger dans un tableau de 6 
colonnes et 6 lignes, en revanche 37 valeurs se rangeront dans un 
tableau dont certaines cases (ou cellules) seront vides, par exempe :
6 colonnes et 7 lignes ou 7 colonnes et 6 lignes.

But chercher les nombres n et m diviseurs du nombre entier p qui
vérifient deux assertions :
	1) n x m = p
	2) abs(n-m) est minimal
	
	Exemple : pour p = 36
	on trouve :
		- 2 x 18 ;
		- 3 x 12 ;
		- 4 x 9 ;
		- 6 x 6 ; on s'arrête là, il ne peut pas y avoir mieux !
		Le tableau est il plein ?   Oui  ->  True
		
		le tuple (True, 6, 6) est la solution idéale
		
		37 renverra (False, 6, 7)
		Le tableau est il plein ?   Non  ->  False
		38 renverra (False, 6, 7) et (True, 2, 19)
		car 38 = 2 x 19; et c'est tout ! car 19 est un nombre premier

		48 renverra (True, 6, 8)
	si p % n == 0 alors m = p / n
	On pourra commencer par tester n = int (p**0.5) puis en décroissant 
	jusqu'à vérifier les conditions
"""
def trouverOptimum (N) :
    n = int(N**.5)
    div = N / n 
    if int(div)-div == 0 :
        return True, n, int(div)
    else :
        return False, n, int(div)+1
       
def reponse(t) :
    if t : return "plein"
    else : return "incomplet"

test = [ 25, 27, 30, 36, 42, 47, 48 ]
for i in range(len(test)) :
    t, n, m = trouverOptimum (test[i])
    print("pour le nombre "+str(test[i])+" le tableau aura "+str(n)+
		" colonnes et "+str(m)+ " lignes et sera "+reponse(t))

