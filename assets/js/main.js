(function () {
  var C = (window.UPL && window.UPL.config) || {};
  var email = (C.contact && C.contact.email) || "contact@upl-gabon.com";

  var toggle = document.querySelector("[data-nav-toggle]");
  var nav = document.querySelector("[data-nav]");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  var path = (location.pathname.split("/").pop() || "index.html").toLowerCase();
  document.querySelectorAll("[data-nav] a").forEach(function (a) {
    var href = (a.getAttribute("href") || "").split("/").pop().toLowerCase();
    if (href === path || (path === "" && href === "index.html")) {
      a.setAttribute("aria-current", "page");
    }
  });

  var form = document.querySelector("[data-contact-form]");
  if (form) {
    var target = form.getAttribute("data-mailto") || email;
    form.setAttribute("data-mailto", target);
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var fd = new FormData(form);
      var name = (fd.get("name") || "").toString().trim();
      var from = (fd.get("email") || "").toString().trim();
      var phone = (fd.get("phone") || "").toString().trim();
      var message = (fd.get("message") || "").toString().trim();
      var interest = (fd.get("interest") || "Executive MBA").toString().trim();
      var text = LANG === "en"
        ? "UPL enquiry\n" +
          "Interest: " + interest + "\n" +
          "Name: " + name + "\n" +
          "Email: " + from + "\n" +
          "Phone: " + phone + "\n\n" +
          message
        : "Demande UPL\n" +
          "Intérêt : " + interest + "\n" +
          "Nom : " + name + "\n" +
          "Email : " + from + "\n" +
          "Téléphone : " + phone + "\n\n" +
          message;
      var subject = encodeURIComponent("UPL — " + interest + " — " + name);
      window.location.href =
        "mailto:" + target + "?subject=" + subject + "&body=" + encodeURIComponent(text);
    });
  }

  var year = document.querySelector("[data-year]");
  if (year) year.textContent = String(new Date().getFullYear());

  /* Skip link focus */
  document.documentElement.classList.add("js");

  /* Vidéos : lecture intégrée au clic (YouTube sans cookies) */
  document.querySelectorAll("[data-yt]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var id = btn.getAttribute("data-yt");
      var frame = document.createElement("iframe");
      frame.className = "video-frame";
      frame.setAttribute("src", "https://www.youtube-nocookie.com/embed/" + id + "?autoplay=1&rel=0");
      frame.setAttribute("title", "Vidéo UPL");
      frame.setAttribute("allow", "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share");
      frame.setAttribute("allowfullscreen", "");
      btn.replaceWith(frame);
    });
  });


  /* ===== Infos dynamiques (type fil d'actualité) ===== */
  var reduceMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var C2 = (window.UPL && window.UPL.config) || {};
  var LANG = (window.UPL && window.UPL.lang) || "fr";
  function pick(obj, frKey, enKey) {
    if (LANG === "en" && obj && obj[enKey || (frKey + "En")]) return obj[enKey || (frKey + "En")];
    return obj ? obj[frKey] : "";
  }
  var news = C2.news || [];
  var quotes = C2.quotes || [];

  /* Bandeau "À la une" — défilement continu (type infos en continue d'une chaîne) */
  var tickerItem = document.querySelector("[data-ticker-item]");
  if (tickerItem) {
    var titles = news.map(function (n) { return pick(n, "title"); });
    var extras = (C2.tickerExtra || []).map(function (t) {
      return (typeof t === "string") ? t : (pick(t, "fr", "en") || t.fr || "");
    });
    var items = titles.concat(extras);
    if (items.length) {
      if (reduceMotion) {
        tickerItem.textContent = items.join("  ·  ");
      } else {
        tickerItem.remove();
        var sep = '<span class="ticker-sep" aria-hidden="true">\u2022</span>';
        var groupHtml = items.map(function (t) {
          return '<span class="ticker-item">' + t + "</span>" + sep;
        }).join("");
        var track = document.createElement("div");
        track.className = "ticker-track";
        track.style.setProperty("--ticker-duration", (items.length * 6) + "s");
        track.innerHTML = '<div class="ticker-group">' + groupHtml + "</div>" +
          '<div class="ticker-group" aria-hidden="true">' + groupHtml + "</div>";
        tickerItem.parentNode.appendChild(track);
      }
    }
  }

  /* Communiqués — rendu depuis config.js */
  var newsGrid = document.querySelector("[data-news-grid]");
  if (newsGrid && news.length) {
    var visible = news.filter(function (n) { return LANG !== "en" || n.titleEn; });
    newsGrid.innerHTML = visible.map(function (n) {
      var tag = pick(n, "tag");
      var date = n.date;
      var head = (tag ? '<span class="news-tag">' + tag + "</span>" : "") +
                 (date ? '<span class="news-date">' + date + "</span>" : "");
      return '<article class="card">' + head +
        "<h3>" + pick(n, "title") + "</h3>" +
        '<p class="small">' + pick(n, "text") + "</p></article>";
    }).join("");
  }

  /* Citation de management — tirage aléatoire, rotation douce */
  var qText = document.getElementById("quote-text");
  var qAuthor = document.getElementById("quote-author");
  var notices = C2.paymentNotices || [];
  var flow = [];
  var maxLen = Math.max(quotes.length, notices.length);
  for (var k = 0; k < maxLen; k++) {
    if (quotes[k]) flow.push({ text: pick(quotes[k], "text"), author: quotes[k].author, isQuote: true });
    if (notices[k]) flow.push({ text: pick(notices[k], "text"), author: pick(notices[k], "source"), isQuote: false });
  }
  if (qText && qAuthor && flow.length) {
    var qi = Math.floor(Math.random() * flow.length);
    function showQuote(i) {
      var it = flow[i];
      qText.textContent = it.isQuote ? "\u00AB " + it.text + " \u00BB" : it.text;
      qAuthor.textContent = "\u2014 " + it.author;
    }
    showQuote(qi);
    if (!reduceMotion && flow.length > 1) {
      setInterval(function () {
        qi = (qi + 1) % flow.length;
        var box = qText.parentNode;
        box.style.opacity = "0";
        setTimeout(function () {
          showQuote(qi);
          box.style.opacity = "1";
        }, 400);
      }, 9000);
    }
  }


  /* Trajectoire : révélation au défilement (fallback sans JS = visible) */
  var timeline = document.querySelector("[data-timeline]");
  if (timeline) {
    timeline.classList.add("tl-anim");
    if (reduceMotion || !("IntersectionObserver" in window)) {
      timeline.classList.add("tl-visible");
    } else {
      var tObs = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (e.isIntersecting) { timeline.classList.add("tl-visible"); tObs.disconnect(); }
        });
      }, { threshold: 0.15 });
      tObs.observe(timeline);
    }
  }

  /* Compte à rebours de rentrée — affiché uniquement si la date est confirmée dans config.js */
  var countdownEl = document.querySelector("[data-countdown]");
  if (countdownEl && C2.rentree && C2.rentree.date) {
    var target = new Date(C2.rentree.date + "T00:00:00");
    var now = new Date();
    if (!isNaN(target.getTime()) && target.getTime() > now.getTime()) {
      var days = Math.ceil((target.getTime() - now.getTime()) / 86400000);
      var label = (LANG === "en" ? (C2.rentree.labelEn || "Academic year opening") : (C2.rentree.label || "Rentrée"));
      var dateStr = target.toLocaleDateString(LANG === "en" ? "en-GB" : "fr-FR", { day: "numeric", month: "long", year: "numeric" });
      countdownEl.innerHTML = "<strong>" + label + " : " + (LANG === "en" ? "D-" : "J-") + days +
        "</strong> \u2014 " + dateStr + (LANG === "en"
          ? ". Send your application now."
          : ". Dossier \u00E0 d\u00E9poser d\u00E8s maintenant.");
      countdownEl.hidden = false;
    }
  }

})();
