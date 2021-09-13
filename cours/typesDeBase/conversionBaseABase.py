'''
  projet de mini-site Web selon une architecture 
  Modèle-Vue-Contrôleur MVC
  https://fr.wikipedia.org/wiki/Mod%C3%A8le-vue-contr%C3%B4leur#En_Python

  Auteur : Joël Dendaletche


from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'
'''

# création de deux dictionnaires de traduction nombre vs symbole
dic10Base, dicBase10 = {}, {}
for i in range(36) :
  dic10Base[i] = str(i) if i < 10 else chr(87+i)
  if i < 10 :
    dicBase10[chr(48+i)] = i
  else :
    dicBase10[chr(97+i-10)] = i

def convert(nombre, baseInit = 10, baseFinale = 10) :
  '''
  converti un nombre (entier ou chaîne de caractère) d'une base 
  :baseInit: par défaut = 10
  vers une autre
  :baseFinale: par défaut = 10
  '''
  nombre = str(nombre)    # devient ou reste un string
  lInit = len(nombre)

  dec = 0
  debug = False

  for i in range(lInit) :
    symbole = nombre[i].lower()     # chiffre de rang converti (éventuellement) en minuscule
    try : 
      # calcul en base décimale de la valeur de chaque symbole
      dec += dicBase10[symbole]*baseInit**(lInit-i-1)
      if debug or nombre == "coucou" : print("dec = {} à l'étape {}, symbole = {} ; {} x {}^{} = {}".format(dec,i, symbole, dicBase10[symbole], baseInit,lInit-i-1,dicBase10[symbole]*baseInit**(lInit-i-1)))
    except :
      print("Le symbole {} n'est pas compatible avec un nombre écrit en base {}".format(symbole,baseInit))
      return False
  
  if debug : print(nombre, " en base {} est ".format(baseInit), dec, " en base 10")
  quotient, reste, nombre = dec, dec % baseFinale, ""

  debug = False

  while quotient != 0 :
    symbole = dic10Base[reste]
    if debug : print ("quotient = {}, nombre = {}, reste = {}, symbole = {}".format(quotient, nombre, symbole, reste))
    quotient = quotient // baseFinale
    nombre = str(symbole)+nombre
    if debug : print("Nombre = {}, quotient = {}, reste = {}".format(nombre, quotient, reste))
    reste = quotient % baseFinale

  return nombre
     
print(dic10Base, "\n\n", dicBase10)

essais = [("00101011", 2, 16),("00101011", 2, 10), ("coucou", 36, 10), ("coucou", 36, 2), (767321022, 10, 36),("Mot2Pass",36,2),("101101101111000110001110111110",2,36)]

for nombre, baseI, baseF in essais :
  print("\n{} en base {} s'écrit {} en base {}\n".format(nombre, baseI, convert(nombre,baseI,baseF),baseF))

nombre = "00101011"
for n in range(3,36) :
  print("\n{} en base {} s'écrit {} en base {}\n".format("00101011", 2, convert(nombre,2,n),n))

symbolesClavier = '²¤~#{[|`\^@]}¨£^$ù*%µ,;:!?.2/§<>+-*/€&é"\'(-è_çà)='
print("symboles du clavier : {} au nombre de {}".format(symbolesClavier, len(symbolesClavier)))