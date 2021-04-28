"""
    Code Caesar : code de cryptographie inventé par l'empereur César
    Principe : chaque lettre de l'alphabet est remplacée par une autre décalée dans le même alphabet d'une valeur
    convenue et toujours la même, par exemple : ici chaque lettre est remplacée par une autre 13 caratères plus loin
    dans l'alphabet (modulo 26).

    Remarque : le décodage se fait en faisant un décalage négatif (ici ce sera de -13).

    Implémentation par : Joël Dendaletche
    Outils python : utilisation de dictionnaire (type dict) et de chaîne de caractères (type str)

"""
# importation de module
import this     # module créé par Tim Peters : https://en.wikipedia.org/wiki/Tim_Peters_(software_engineer)

# help(this) donne les deux informations suivantes :

code13 = {'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R', 'F': 'S', 'G':'T','H': 'U' ,
        'I' : 'V', 'J': 'W', 'K' :'X', 'L' : 'Y', 'M' : 'Z', 'N' : 'A', 'O':'B' ,
        'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G' , 'U':'H', 'V':'I', 'W':'J',
        'X':'K' , 'Y':'L', 'Z' :'M' }

# texte à décoder
s = "Gur Mra bs Clguba, ol Gvz Crgref\n\nOrnhgvshy vf o...bar ubaxvat ..."

# traduction en français du texte intégral du module this

integralFr = "\n\
---------------------------------------------------------------------------------------------------------------------\n\
Beau est mieux que laid.\n\
L'explicite vaut mieux que l'implicite.\n\
Le simple vaut mieux que le complexe.\n\
Complexe vaut mieux que compliqué.\n\
Evident est mieux que caché.\n\
Clairsemé vaut mieux que dense.\n\
La lisibilité compte.Les cas spéciaux ne sont pas assez spéciaux pour enfreindre les règles.\n\
Bien que l'aspect pratique l'emporte sur la pureté.\n\
Les erreurs ne doivent jamais passer en silence.\n\
À moins d'être explicitement réduit au silence.\n\
Face à l'ambiguïté, refusez la tentation de deviner.\n\
Il devrait y avoir une - et de préférence une seule - façon évidente de le faire.\n\
Bien que cette manière ne soit pas évidente au début, sauf si vous êtes allemand.\n\
Maintenant est mieux que jamais.\n\
Bien que jamais ne soit souvent mieux que * maintenant *.\n\
Si l'implémentation est difficile à expliquer, c'est une mauvaise idée.\n\
Si la mise en œuvre est facile à expliquer, cela peut être une bonne idée.\n\
Les espaces de noms sont une excellente idée - faisons-en plus!\n\
---------------------------------------------------------------------------------------------------------------------\n"
print(integralFr)

# construction de l'alphabet (pour s'échauffer)
alphabet = []
for elt in code13 :
    alphabet.append(elt)

alphabet.sort()   # tri croissant    A -> Z
print(alphabet)   #['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  # 'U', 'V', 'W', 'X', 'Y', 'Z']

#algorithme de transcription
phraseEnClair =""
for car in s :
    if car.upper() in code13 : # lettre de l'alphabet qui peut être remplacée par une du dictionnaire code13
        if car == car.upper() :
            phraseEnClair += code13[car]      # une majuscule donne une majuscule
        else :
            phraseEnClair += code13[car.upper()].lower()    # minuscule
    else :
        phraseEnClair+= car     # autre symbole non alphabétique (ou signé)

print(phraseEnClair)

def construireCodeCesar(decalage : int) -> dict :
    """
    Construit un dictionnaire utilisable pour le codage à la façon de César
    :param decalage: entier entre 0 et 26 (ou plus modulo 26 ; négatif pour inverser ...)
    :return texte chiffré :
    """
    code = {}
    for car in range(26) :
        code[alphabet[car]] = alphabet[(car + decalage) % 26]
    return code

# tous les codes césar
#for i in range(26) :
#   print(construireCodeCesar(i))

def transcrireEnCodeCesar(texte : str, decalage : int = 13) -> str :
    """
    :param texte: texte à chiffrer
    :param decalage: par défaut 13, mais peut être n'importe quel entier modulo 26
    :return: texte déchiffré
    """
    code = construireCodeCesar( decalage % 26 )
    texteChiffre = ""
    for car in texte :
        if car.upper() in code :
            if car == car.upper() :
                texteChiffre += code[car]
            else :
                texteChiffre += code[car.upper()].lower()
        else :
            texteChiffre += car
    return texteChiffre

texteChiffre = transcrireEnCodeCesar(phraseEnClair)
print("\n-----------------------------------------------------------------------------------------------------------\n",
      phraseEnClair,
      "\n-----------------------------------------------------------------------------------------------------------\n"+
      "\n donne :\n"+
      "-------------------------------------------------------------------------------------------------------------\n",
      texteChiffre,
      "\n-----------------------------------------------------------------------------------------------------------\n",
      s ,
      "\n-----------------------------------------------------------------------------------------------------------\n",
      " <- vs -> ",
      "\n-----------------------------------------------------------------------------------------------------------\n",
      texteChiffre, "\ntextes identiques ?  : ", s == texteChiffre,
      "\n-----------------------------------------------------------------------------------------------------------\n",
      transcrireEnCodeCesar(s,-13))