/*

    Mise en place des menus

*/

// jeu de données
menu_data = {
  0 : {
    href : "../../../niveau_1.html",
    innerText : "retour à la page NSI",
    title : "revient à la page principale"
  },
  1 : {
    href : "../../../programmeNSI/cours/themeA/typesBase.html",
    innerText : "A : types et valeurs de base",
    title : "Représentation des données : types et valeurs de base"
  },
  2 : {
    href: "../../../programmeNSI/cours/themeB/typesConstruits.html",
		title:"Représentation des données : types construits",
		innerText :"B : types construits"
  },
  3 : {
    href:"../../../programmeNSI/cours/themeC/traitementDonneesEnTables.html",
		title:"Traitement de données en tables",
		innerText :"C : Traitement de données en tables"
  },
  4 : {
    href:"../../../programmeNSI/cours/themeD/web2.0.html",
		title:"Interactions entre l’homme et la machine sur le Web 2.0",
		innerText : "D : Web 2.0"
  },
  5 : {
    href:"../../../programmeNSI/cours/themeE/systemeLinux.html",
    title:"",
		innerText : "E : architecture système"
  },
  6 : {
    href : "../../../programmeNSI/cours/themeF/langagesProgrammation.html",
    title : "",
		innerText : "F : langages de programmation"
  },
  7 : {
    href:"../../../programmeNSI/cours/themeG/algorithmique.html",
    title : "",
		innerText : "G : algorithmique"
  },
  8 : { 
    href : "../../../programmeNSI/quiz/entrainementE3C.html",
    title : "quiz d'entraînement basés sur les annales de l'ancien programme de première",
		innerTex : "Quiz d'entraînement"
  },
  9 : {
    href:"../../../programmeNSI/ressources/ressource_0.html",
    title : "",
		innerText : "bonnes pratiques"
  },
  10 : {
    href:"../../../programmeNSI/ressources/ressource_0.html",
    title : "",
		innerText : "bonnes pratiques"
  }
}
// création des items du menu
function createMenu () {
	var menu = document.getElementsByTagName("NAV")[0];
	menu.innerHTML = "";  // efface le menu builtin
	
	let liste = document.createElement("ul");
	liste.classList.add("menu");
	for (let n_item in menu_data) {
		let li = document.createElement("li");
		let lien = document.createElement("a");
		lien.href = menu_data[n_item].href;
		lien.title = menu_data[n_item].title;
		lien.innerText = menu_data[n_item].innerText;
		li.appendChild(lien);
		liste.appendChild(li);
	}
	menu.appendChild(liste);
}

createMenu ();
