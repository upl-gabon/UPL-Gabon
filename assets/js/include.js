/**
 * Header / footer injectés — lit window.UPL.config
 * Charger config.js AVANT ce fichier.
 */
(function () {
  var C = (window.UPL && window.UPL.config) || {};
  var contact = C.contact || {};
  var email = contact.email || "contact@upl-gabon.com";
  var phones = (contact.phonesUpl || []).map(function (p) {
    return "<li>Tél. " + p.display + "</li>";
  }).join("");

  function headerHTML() {
    return (
      '<header class="site-header">' +
      '<div class="container header-inner">' +
      '<a class="brand" href="index.html">' +
      '<img src="assets/img/logo-upl.png" alt="Logo UPL" width="96" height="61" />' +
      '<span class="brand-text"><strong>Université Privée de Libreville</strong>' +
      "<span>Excellence · Innovation · Leadership</span></span></a>" +
      '<button class="nav-toggle" type="button" data-nav-toggle aria-expanded="false" aria-controls="site-nav">Menu</button>' +
      '<nav id="site-nav" class="nav" data-nav aria-label="Navigation principale">' +
      '<a href="index.html">Accueil</a>' +
      '<a href="mba.html">Executive MBA</a>' +
      '<a href="a-propos.html">À propos</a>' +
      '<a class="nav-cta" href="contact.html">Contact</a>' +
      "</nav></div></header>"
    );
  }

  function footerHTML() {
    return (
      '<footer class="site-footer">' +
      '<div class="container footer-grid" style="grid-template-columns:2fr 1fr 1fr">' +
      "<div><h4>UPL</h4>" +
      "<p class=\"small\">Université Privée de Libreville — établissement d'enseignement supérieur privé, Libreville (Gabon).</p>" +
      "<p class=\"small\">Sablière, en face de la Résidence de l'Ambassade d'Arabie Saoudite</p>" +
      "<p class=\"small muted-on-dark\">Activité ouverte présentée : Executive MBA. Architecture prête pour d'autres composantes le moment venu.</p></div>" +
      "<div><h4>Parcours</h4><ul>" +
      '<li><a href="mba.html">Executive MBA</a></li>' +
      '<li><a href="a-propos.html">À propos</a></li>' +
      '<li><a href="contact.html">Contact / inscription</a></li>' +
      "</ul></div>" +
      "<div><h4>Contact</h4><ul>" +
      phones +
      '<li><a href="mailto:' + email + '">' + email + "</a></li>" +
      '<li><a href="contact.html">Formulaire</a></li>' +
      "</ul></div></div>" +
      '<div class="container footer-bottom">' +
      "<span>© <span data-year></span> Université Privée de Libreville</span>" +
      "<span>Charte bleu &amp; or · Site institutionnel</span>" +
      "</div></footer>"
    );
  }

  var h = document.querySelector("[data-include-header]");
  var f = document.querySelector("[data-include-footer]");
  if (h) h.outerHTML = headerHTML();
  if (f) f.outerHTML = footerHTML();
})();
