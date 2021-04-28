/*
        Auteur  : Joël Dendaletche
        But     : Gérer les animations et conversions diverses
                  pour illustrer le cours sur les types de base

*/
// définition et initialisation des variables globales
var titrePage = "NSI en première : thème A";
var aurevoir = "NSI en première : thème A ; À bientôt, revenez vite !";
var arret = false;
var nbr = 0,
    id; // identifiant pour la fonction setInterval

function init () {
    /**/
    test();
  //construireListeSommaire ();
	construireListeSymboles ("Dec");
}

function test () {
    /**/
    document.getElementById("demoDec").innerHTML += "test OK";
    enumeration('Dec');
    document.getElementById('demoDec').style.display = 'block';
}
//var id = setInterval(ma_fontion, 1000);
function titre(texte)
{
	document.title = texte;
}
function construireListeSymboles (base)
{
    contenu = "<select>";
    let i;

    for (i = 0 ; i < 36 ; i++) {
        contenu += "<option>"+ i +"</option>";
        }
    contenu += "</select>";
    document.getElementById("demo"+base).innerHTML = contenu;
}

function enumeration(base)
{   /* construit un formulaire sous forme de tableau pour lancer une animation : */
       commentaires = "visualise l'énumération de n premiers entiers écrits soit dans le sens "+
"normalisé (arabe) soit 'à l'envers' ou dans le sens de l'écriture occidentale ; cela démontre "+
"que l'usage de la notation arabe n'est pas cohérente avec l'écriture occidentale ...";

    document.getElementById("demo"+base).title = commentaires;

            let contenu = "<table style='border : solid black 2px;"+
    "border-collapse:collapse;width:30%;'>"+
    "<caption>&Eacute;numération de nombres écrit"+
    " normalement ou à l'envers !</caption><tr><th>&Agrave; l'envers</th>"+
    "<th>&Agrave; l'endroit</th></tr><tr><td id='nombre"+base+"'><input type='text' disabled placeholder='012345'/></td>"+
    "<td id='nombreEnvers"+base+"'><input type='text' placeholder='543210'  disabled/></td></tr>" +
    "<tr><td class='15percent'><input type='button' value='lancer' id='stop"+
     base+"' onclick='lancerEnum(&quot;"+base+"&quot;);'/></td>"+
    "<td class='15percent'>"+
    "<input type='button' value='cacher' "+
    "onclick='document.getElementById(&quot;demo"+base+
    "&quot;).style.display = &quot;None&quot;'/>"+        //arret = true;
    "</td></tr></table>";

	document.getElementById("demo"+base).innerHTML = contenu;
}

function lancerEnum(base)
{
    if (arret == false ) {
	id = setInterval(compter, 20); // 5 chiffres par seconde
	document.getElementById('stop'+base).value = 'arrêter';
	arret = true;
	}
	else {
    arret = false;
    document.getElementById("stop"+base).value = "compter";
    clearInterval(id);
    nbr = 1;
	}
}
base = 'Dec';
function compter()
{
		nbr += 1; // incrémentation toutes les 200 ms
		// affichage du décompte
			document.getElementById("nombre"+base).innerHTML =
		"<bdo dir='rtl' title='écriture du nombre dans le sens : right-to-left = rtl.' class='test'>"+nbr+
				"</bdo>";
			document.getElementById("nombreEnvers"+base).innerHTML =
		"<bdo dir='ltr' title='écriture du nombre dans le sens : left-to-right = ltr.' class='test'>"+nbr+
				"</bdo>";
}
	// remet tout à zéro dans le décompte

// fonctions permettant la conversion des nombres