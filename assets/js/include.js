/**
 * Header / footer / bandeau d'action injectés — lit window.UPL.config
 * Charger config.js AVANT ce fichier.
 *
 * Multilingue : window.UPL.lang = "fr" (défaut) | "en" — défini dans les pages /en/.
 * Sous-dossier : <html data-base="../"> sur les pages /en/ pour retrouver les assets.
 * Push-to-action standardisé : [data-action-band] présent sur chaque page.
 */
(function () {
  var BASE = document.documentElement.getAttribute("data-base") || "";
  var LANG = (window.UPL && window.UPL.lang) || "fr";
  var C = (window.UPL && window.UPL.config) || {};
  var contact = C.contact || {};
  var email = contact.email || "contact@upl-gabon.com";

  var T = LANG === "en" ? {
    menu: "Menu",
    navLabel: "Main navigation",
    nav: { home: "Home", mba: "Executive MBA", about: "About", president: "President's message", contact: "Contact" },
    slogan: "Excellence · Innovation · Leadership",
    footerTagline: "Université Privée de Libreville — private higher-education institution, Libreville (Gabon).",
    footerAddress: "Sablière, opposite the Residence of the Embassy of Saudi Arabia",
    colPath: "Programmes",
    colContact: "Contact",
    colFollow: "Follow",
    socialLead: "Official channels, run by the UPL Secretariat.",
    form: "Form",
    tel: "Tel. ",
    footerBottom: "Blue & gold charter · Institutional website",
    bandTitle: "Take action",
    bandLead: "One e-mail or one call is enough — the Secretariat answers every request.",
    bandApply: "MBA application",
    bandMeeting: "Request a meeting",
    bandPartner: "Partnership",
    bandWhatsapp: "WhatsApp",
    bandCall: "or call ",
    subjApply: "MBA%20Application",
    subjMeeting: "Meeting%20request",
    subjPartner: "Partnership",
  } : {
    menu: "Menu",
    navLabel: "Navigation principale",
    nav: { home: "Accueil", mba: "Executive MBA", about: "À propos", president: "Mot du Président", contact: "Contact" },
    slogan: "Excellence · Innovation · Leadership",
    footerTagline: "Université Privée de Libreville — établissement d'enseignement supérieur privé, Libreville (Gabon).",
    footerAddress: "Sablière, en face de la Résidence de l'Ambassade d'Arabie Saoudite",
    colPath: "Parcours",
    colContact: "Contact",
    colFollow: "Nous suivre",
    socialLead: "Canaux officiels de l'UPL, animés par le secrétariat.",
    form: "Formulaire",
    tel: "Tél. ",
    footerBottom: "Charte bleu & or · Site institutionnel",
    bandTitle: "Passer à l'action",
    bandLead: "Un e-mail ou un appel suffit — le secrétariat répond à chaque demande.",
    bandApply: "Candidature MBA",
    bandMeeting: "Demander un rendez-vous",
    bandPartner: "Partenariat",
    bandWhatsapp: "WhatsApp",
    bandCall: "ou appelez ",
    subjApply: "Candidature%20MBA",
    subjMeeting: "Demande%20de%20rendez-vous",
    subjPartner: "Partenariat",
  };

  var PAGES = { home: "index.html", mba: "mba.html", about: "a-propos.html", president: "president.html", contact: "contact.html" };
  function href(key) { return BASE + PAGES[key]; }

  /**
   * Réseaux sociaux — seul ce qui est prêt sort à l'écran.
   * Un réseau est affiché si features.showSocialLinks = true ET config.social[k].status = "live"
   * ET qu'une URL officielle est renseignée. Tant qu'une bio n'est pas validée par le Président,
   * le réseau reste à "pending" : rien n'apparaît, aucun emplacement vide.
   */
  var SOCIAL_ORDER = ["facebook", "instagram", "tiktok", "linkedin", "youtube", "x"];
  function liveSocial() {
    var cfg = (C.features && C.features.showSocialLinks) ? (C.social || {}) : {};
    var out = [];
    SOCIAL_ORDER.forEach(function (key) {
      var net = cfg[key];
      if (!net || net.status !== "live" || !net.url) return;
      out.push({ key: key, label: net.label || key, url: net.url, handle: net.handle || "" });
    });
    return out;
  }

  function socialFooterHTML(items) {
    if (!items.length) return "";
    return (
      '<div><h4>' + T.colFollow + '</h4><ul class="social-row">' +
      items.map(function (it) {
        return '<li><a href="' + it.url + '" target="_blank" rel="noopener me">' + it.label + "</a></li>";
      }).join("") +
      "</ul></div>"
    );
  }

  function socialPanelHTML(items) {
    if (!items.length) return "";
    return (
      '<div class="social-panel">' +
      '<p class="small">' + T.socialLead + "</p>" +
      '<ul class="social-row social-row-pills">' +
      items.map(function (it) {
        return (
          '<li><a class="btn btn-outline" href="' + it.url + '" target="_blank" rel="noopener me">' +
          it.label + (it.handle ? ' <span class="social-handle">' + it.handle + "</span>" : "") +
          "</a></li>"
        );
      }).join("") +
      "</ul></div>"
    );
  }


  function langSwitchHTML() {
    var file = location.pathname.split("/").pop() || "index.html";
    if (!/\.html$/.test(file)) file = "index.html";
    var other = LANG === "en" ? BASE + file : "en/" + file;
    if (LANG === "en") {
      return '<span class="lang-switch">' +
        '<a href="' + other + '" lang="fr" hreflang="fr">FR</a>' +
        '<b aria-current="true">EN</b></span>';
    }
    return '<span class="lang-switch">' +
      '<b aria-current="true">FR</b>' +
      '<a href="' + other + '" lang="en" hreflang="en" rel="alternate">EN</a></span>';
  }

  function headerHTML() {
    return (
      '<header class="site-header">' +
      '<div class="container header-inner">' +
      '<a class="brand" href="' + href("home") + '">' +
      '<img src="' + BASE + 'assets/img/logo-upl.png" alt="Logo UPL" width="96" height="61" />' +
      '<span class="brand-text"><strong>Université Privée de Libreville</strong>' +
      "<span>" + T.slogan + "</span></span></a>" +
      '<span class="libreville-time"><span>' + (LANG === "en" ? "Libreville time" : "Heure de Libreville") + '</span><time data-libreville-time>--:--</time></span>' +
      '<button class="nav-toggle" type="button" data-nav-toggle aria-expanded="false" aria-controls="site-nav">' + T.menu + "</button>" +
      '<nav id="site-nav" class="nav" data-nav aria-label="' + T.navLabel + '">' +
      '<a href="' + href("home") + '">' + T.nav.home + "</a>" +
      '<a href="' + href("mba") + '">' + T.nav.mba + "</a>" +
      '<a href="' + href("about") + '">' + T.nav.about + "</a>" +
      '<a href="' + href("president") + '">' + T.nav.president + "</a>" +
      '<a class="nav-cta" href="' + href("contact") + '">' + T.nav.contact + "</a>" +
      langSwitchHTML() +
      "</nav></div></header>"
    );
  }

  function footerHTML() {
    var phones = (contact.phonesUpl || []).map(function (p) {
      return "<li>" + T.tel + p.display + "</li>";
    }).join("");
    var socialItems = liveSocial();
    var cols = socialItems.length ? "2fr 1fr 1fr 1fr" : "2fr 1fr 1fr";
    return (
      '<footer class="site-footer">' +
      '<div class="container footer-grid" style="grid-template-columns:' + cols + '">' +
      "<div><h4>UPL</h4>" +
      '<p class="small">' + T.footerTagline + "</p>" +
      '<p class="small">' + T.footerAddress + "</p></div>" +
      '<div><h4>' + T.colPath + '</h4><ul>' +
      '<li><a href="' + href("mba") + '">' + T.nav.mba + "</a></li>" +
      '<li><a href="' + href("president") + '">' + T.nav.president + "</a></li>" +
      '<li><a href="' + href("about") + '">' + T.nav.about + "</a></li>" +
      '<li><a href="' + href("contact") + '">' + T.nav.contact + "</a></li>" +
      "</ul></div>" +
      '<div><h4>' + T.colContact + '</h4><ul>' +
      phones +
      '<li><a href="' + ((contact.whatsapp && contact.whatsapp.href) || "https://wa.me/24102621978") + '" target="_blank" rel="noopener">WhatsApp ' + ((contact.whatsapp && contact.whatsapp.display) || "+241 02 62 19 78") + "</a></li>" +
      '<li><a href="mailto:' + email + '">' + email + "</a></li>" +
      '<li><a href="' + href("contact") + '">' + T.form + "</a></li>" +
      "</ul></div>" +
      socialFooterHTML(socialItems) +
      "</div>" +
      '<div class="container footer-bottom">' +
      "<span>© <span data-year></span> Université Privée de Libreville</span>" +
      "<span>" + T.footerBottom + "</span>" +
      "</div></footer>"
    );
  }

  /* Bandeau d'action standard — candidature / rendez-vous / partenariat */
  function bandHTML() {
    var phones = (contact.phonesUpl || []).map(function (p) { return p.display; }).join(" · ");
    return (
      '<section class="section section-bleu action-band" aria-label="' + T.bandTitle + '">' +
      '<div class="container" style="text-align:center">' +
      "<h2 style=\"margin:0 0 0.4rem\">" + T.bandTitle + "</h2>" +
      '<p class="small" style="margin:0 0 1rem">' + T.bandLead + "</p>" +
      '<div class="band-actions">' +
      '<a class="btn btn-primary" href="mailto:' + email + "?subject=" + T.subjApply + '">' + T.bandApply + "</a>" +
      '<a class="btn btn-secondary" href="mailto:' + email + "?subject=" + T.subjMeeting + '">' + T.bandMeeting + "</a>" +
      '<a class="btn btn-secondary" href="mailto:' + email + "?subject=" + T.subjPartner + '">' + T.bandPartner + "</a>" +
      '<a class="btn btn-whatsapp" href="' + ((contact.whatsapp && contact.whatsapp.href) || "https://wa.me/24102621978") + '" target="_blank" rel="noopener">' + T.bandWhatsapp + "</a>" +
      "</div>" +
      '<p class="small" style="margin:0.9rem 0 0">' + T.bandCall + phones + "</p>" +
      "</div></section>"
    );
  }

  var h = document.querySelector("[data-include-header]");
  if (h) h.outerHTML = headerHTML();

  var clock = document.querySelector("[data-libreville-time]");
  if (clock) {
    var clockFormat = new Intl.DateTimeFormat(LANG === "en" ? "en-GB" : "fr-FR", {
      timeZone: "Africa/Libreville", hour: "2-digit", minute: "2-digit", second: "2-digit"
    });
    var updateClock = function () { clock.textContent = clockFormat.format(new Date()); };
    updateClock();
    window.setInterval(updateClock, 1000);
  }
  var f = document.querySelector("[data-include-footer]");
  if (f) f.outerHTML = footerHTML();
  var band = document.querySelector("[data-action-band]");
  if (band) band.outerHTML = bandHTML();
  /* Panneau « Nous suivre » (page Contact) — disparaît si aucun réseau n'est live. */
  document.querySelectorAll("[data-social]").forEach(function (mount) {
    mount.outerHTML = socialPanelHTML(liveSocial());
  });
})();
