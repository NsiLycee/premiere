# attention: python2
import random
import sys
random.seed(1234)
tab, t = [], []
somme, s2, s3 = 0, 0, 0

for i in range(10000):
  tab.append(random.randint(0,10000))
  s2 += tab[i]
  if tab[i] % 7 == 0 : s3 += 1
  if tab[i] == 9785 :
    somme += 1
    t.append((i,tab[i]))

print somme
print t
print s2, s3