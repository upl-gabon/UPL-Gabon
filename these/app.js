/* Zone thèse — script INDÉPENDANT de la piste UPL.
   Zéro dépendance : navigation mobile, année, bandeau d'échanges. */
(function () {
  "use strict";

  /* Menu mobile */
  var toggle = document.querySelector("[data-these-nav-toggle]");
  var nav = document.querySelector("[data-these-nav]");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  /* Année courante */
  var year = new Date().getFullYear();
  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = year;
  });

  /* Bandeau d'échanges scientifiques — rendu dans [data-action-band].
     Charte propre à la zone thèse (encre/bronze), sans reprise du bandeau UPL. */
  var band = document.querySelector("[data-action-band]");
  if (band) {
    band.outerHTML =
      '<section class="these-band" aria-label="Échanges scientifiques">' +
        '<div class="container">' +
          "<h2>Échanges scientifiques</h2>" +
          "<p>Une question sur cette recherche, une demande de documentation ou un terrain d'enquête&nbsp;? " +
          "Écrivez à l'auteur — objet «&nbsp;Recherche doctorale&nbsp;».</p>" +
          '<div class="btn-row">' +
            '<a class="btn btn-bronze" href="mailto:contact@upl-gabon.com?subject=Recherche%20doctorale">Contacter l\u2019auteur</a>' +
            '<a class="btn btn-outline" style="color:#F4EFE2;border-color:rgba(244,239,226,0.5)" href="documents.html">Documents &amp; accès</a>' +
          "</div>" +
          '<p class="small" style="margin:1rem 0 0">Manuscrit, corpus et données sensibles : accès réservé, sur demande motivée.</p>' +
        "</div>" +
      "</section>";
  }
})();
