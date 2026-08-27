/**
 * UPL — effets d'animation sobres (accueil)
 * 1) Poussière d'or du hero : particules rares, lentes, dorées — élégance, pas spectacle.
 * 2) (La trajectoire est animée via main.js + CSS, cf. [data-timeline].)
 *
 * Garde-fous :
 * - désactivé si prefers-reduced-motion (accessibilité)
 * - en pause quand l'onglet est masqué (batterie/perf)
 * - canvas confiné au hero, pointer-events none
 */
(function () {
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var hero = document.querySelector(".hero-ge");
  if (!hero || reduce) return;

  var canvas = document.createElement("canvas");
  canvas.className = "gold-canvas";
  canvas.setAttribute("aria-hidden", "true");
  hero.appendChild(canvas);
  var ctx = canvas.getContext("2d");
  if (!ctx) return;

  var dpr = Math.min(window.devicePixelRatio || 1, 2);
  var W = 0, H = 0, parts = [];
  var COUNT = 26; /* rare : sobriété */

  function spawn(fromBottom) {
    return {
      x: Math.random() * W,
      y: fromBottom ? H + 8 : Math.random() * H,
      r: 0.6 + Math.random() * 1.6,
      vy: 0.08 + Math.random() * 0.25,
      vx: (Math.random() - 0.5) * 0.12,
      a: 0.15 + Math.random() * 0.45,
      tw: Math.random() * Math.PI * 2,
      tws: 0.008 + Math.random() * 0.02,
    };
  }

  function resize() {
    W = hero.clientWidth;
    H = hero.clientHeight;
    canvas.width = W * dpr;
    canvas.height = H * dpr;
    canvas.style.width = W + "px";
    canvas.style.height = H + "px";
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  }

  resize();
  for (var i = 0; i < COUNT; i++) parts.push(spawn(false));

  var running = true;
  document.addEventListener("visibilitychange", function () {
    var was = running;
    running = !document.hidden;
    if (running && !was) requestAnimationFrame(loop);
  });

  function loop() {
    if (!running) return;
    ctx.clearRect(0, 0, W, H);
    for (var i = 0; i < parts.length; i++) {
      var p = parts[i];
      p.y -= p.vy;
      p.x += p.vx;
      p.tw += p.tws;
      if (p.y < -6 || p.x < -6 || p.x > W + 6) parts[i] = spawn(true);
      var alpha = p.a * (0.6 + 0.4 * Math.sin(p.tw));
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      ctx.fillStyle = "rgba(201,162,39," + alpha.toFixed(3) + ")";
      ctx.fill();
    }
    requestAnimationFrame(loop);
  }

  window.addEventListener("resize", resize);
  requestAnimationFrame(loop);
})();
