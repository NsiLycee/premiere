/*
		Auteur : Joël Dendaletche
		Contenu : construction de la liste des items du sommaire
		Date de création : 23 / 09 /2019
  
 */
// ressources typographique à copier /coller : À Á Â Ä Æ Ç É È Ê Ë Î Ï  Ô Ö Ø  OE Ú Ù Û Ü 



// déclarations des variables
var tabItems = new Array();

var baseURL = "niveau";

var nItems = 4; // ne change pas
// initialisation des listes
tabItems = ["enseignement de SNT en seconde",          // 0
			"enseignement de NSI en première",
			"enseignement de NSI en terminale",
			"enseignement conception de documents et d'interfaces numériques (TD IUT Rodez) ",
			'divers exemples de pages dynamiques avec du javaScript', //4
			"différentes formes de stockage loacl ...",
			'projet collectif IUT info 1 : cahier des charges',
			"MIAGE"];												//7
//alert("debug1");

// fonction appelée par onload dans la balise body ou par init ()
function construireListeSommaire () {
	//alert("debug2");
	
	var listeSommaire = document.getElementById("listeSommaire");
	
	listeSommaire.innerHTML = "<h2>Sommaire :</h2><ul> <li><a href='index.html' style='font-size:200%;'>Accueil du site</a></li>";
	
	for (var i=0; i < nItems; i++) {
		listeSommaire.innerHTML += "<li><a href='"+baseURL+"_"+i+ ".html' target='_blank' >" +tabItems[i]+"</a></li>";
		}
		
	listeSommaire.innerHTML += "<li><a href='./exemples/unicode.html' target='_blank' >" +tabItems[4]+"</a></li>";
	listeSommaire.innerHTML += "<li><a href='./exemples/exempleStorage.html' target='_blank' >" +tabItems[5]+"</a></li>";
	listeSommaire.innerHTML += "<li><a href='./projets/cahierDesCharges/cahierCharges.html' target='_blank' >" +tabItems[6]+"</a></li>";
	listeSommaire.innerHTML += "<li><a href='./IUT/MIAGE/index.html' target='_blank' >" +tabItems[7]+"</a></li>";
	listeSommaire.innerHTML += "</ul>";
	}
