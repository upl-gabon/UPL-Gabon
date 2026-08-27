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
})();
