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
      var text =
        "Demande UPL\n" +
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
  var news = C2.news || [];
  var quotes = C2.quotes || [];

  /* Bandeau "À la une" — rotation des titres de communiqués */
  var tickerItem = document.querySelector("[data-ticker-item]");
  if (tickerItem && news.length) {
    var titles = news.map(function (n) { return n.title; });
    if (reduceMotion) {
      tickerItem.textContent = titles.join("  ·  ");
    } else {
      var ti = 0;
      tickerItem.textContent = titles[0];
      setInterval(function () {
        ti = (ti + 1) % titles.length;
        tickerItem.style.opacity = "0";
        setTimeout(function () {
          tickerItem.textContent = titles[ti];
          tickerItem.style.opacity = "1";
        }, 350);
      }, 5000);
    }
  }

  /* Communiqués — rendu depuis config.js */
  var newsGrid = document.querySelector("[data-news-grid]");
  if (newsGrid && news.length) {
    newsGrid.innerHTML = news.map(function (n) {
      var head = (n.tag ? '<span class="news-tag">' + n.tag + "</span>" : "") +
                 (n.date ? '<span class="news-date">' + n.date + "</span>" : "");
      return '<article class="card">' + head +
        "<h3>" + n.title + "</h3>" +
        '<p class="small">' + n.text + "</p></article>";
    }).join("");
  }

  /* Citation de management — tirage aléatoire, rotation douce */
  var qText = document.getElementById("quote-text");
  var qAuthor = document.getElementById("quote-author");
  if (qText && qAuthor && quotes.length) {
    var qi = Math.floor(Math.random() * quotes.length);
    function showQuote(i) {
      qText.textContent = "\u00AB " + quotes[i].text + " \u00BB";
      qAuthor.textContent = "\u2014 " + quotes[i].author;
    }
    showQuote(qi);
    if (!reduceMotion && quotes.length > 1) {
      setInterval(function () {
        qi = (qi + 1) % quotes.length;
        var box = qText.parentNode;
        box.style.opacity = "0";
        setTimeout(function () {
          showQuote(qi);
          box.style.opacity = "1";
        }, 400);
      }, 9000);
    }
  }

})();
