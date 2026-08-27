/**
 * Tests de stabilité site UPL
 * Exécution : npm test
 */
import { readFileSync, existsSync, readdirSync } from "fs";
import { join, dirname } from "path";
import { fileURLToPath } from "url";
import assert from "assert";

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = join(__dirname, "..");

function read(rel) {
  return readFileSync(join(ROOT, rel), "utf8");
}

function walkHtml(dir = ROOT, acc = []) {
  for (const name of readdirSync(dir, { withFileTypes: true })) {
    if (name.name === "node_modules" || name.name === ".git" || name.name === "docs") continue;
    const p = join(dir, name.name);
    if (name.isDirectory()) walkHtml(p, acc);
    else if (name.name.endsWith(".html")) acc.push(p);
  }
  return acc;
}

let failed = 0;
function test(title, fn) {
  try {
    fn();
    console.log("  ✓", title);
  } catch (e) {
    failed++;
    console.error("  ✗", title);
    console.error("   ", e.message);
  }
}

console.log("\nUPL site stability tests\n");

test("pages requises existent", () => {
  for (const f of ["index.html", "mba.html", "a-propos.html", "president.html", "contact.html"]) {
    assert.ok(existsSync(join(ROOT, f)), `manque ${f}`);
  }
});

test("assets critiques existent", () => {
  for (const f of [
    "assets/css/main.css",
    "assets/js/config.js",
    "assets/js/include.js",
    "assets/js/main.js",
    "assets/img/logo-upl.png",
    "HANDOVER.md",
    "netlify.toml",
    "package.json",
  ]) {
    assert.ok(existsSync(join(ROOT, f)), `manque ${f}`);
  }
});

test("charte bleu et or dans le CSS", () => {
  const css = read("assets/css/main.css");
  assert.ok(css.includes("#0B2A5B"), "bleu UPL manquant");
  assert.ok(css.includes("#C9A227"), "or UPL manquant");
});

test("config.js expose email et programmes", () => {
  const js = read("assets/js/config.js");
  assert.ok(js.includes("contact@upl-gabon.com"));
  assert.ok(js.includes("exec-mba"));
  assert.ok(js.includes('status: "open"'));
  assert.ok(js.includes("public: false"), "calvin doit rester public:false");
});

test("contact@upl-gabon.com sur les pages HTML", () => {
  for (const f of ["index.html", "mba.html", "contact.html"]) {
    const html = read(f);
    assert.ok(html.includes("contact@upl-gabon.com"), `${f} sans email`);
  }
});

test("téléphones UPL et présidence sur contact.html", () => {
  const html = read("contact.html");
  assert.ok(html.includes("+241 02 62 19 78") || html.includes("02 62 19 78"), "tél UPL 1");
  assert.ok(html.includes("+241 07 35 95 72") || html.includes("07 35 95 72"), "tél UPL 2");
  assert.ok(html.includes("+241 05 01 56 20") || html.includes("05 01 56 20"), "présidence");
});

test("Calvin urgence NOT in public HTML pages", () => {
  for (const p of walkHtml()) {
    const html = readFileSync(p, "utf8");
    assert.ok(!html.includes("7 52 97 58 09"), `num Calvin dans ${p}`);
    assert.ok(!html.includes("blanchardminang00"), `gmail Calvin dans ${p}`);
    assert.ok(!html.includes("+33 7 52"), `+33 Calvin dans ${p}`);
  }
});

test("pas de fausses offres multi-filières dans le HTML public", () => {
  const banned = [
    "Sciences Po",
    "Polytechnique",
    "partenariats@upl",
    "admissions@upl-gabon.com",
    "6 filières",
  ];
  for (const p of walkHtml()) {
    const html = readFileSync(p, "utf8");
    for (const b of banned) {
      const re = new RegExp(b.replace(/[.*+?^${}()|[\]\\]/g, "\\$&") + "(?![A-Za-zÀ-ÿ])");
      assert.ok(!re.test(html), `"${b}" trouvé dans ${p}`);
    }
  }
});

test("CPGE : offre officielle sur l'accueil, hors page MBA", () => {
  const index = read("index.html");
  assert.ok(index.includes("CPGE"), "CPGE manquant dans l'offre officielle");
  assert.ok(index.includes("2 200 000 FCFA"), "tarif CPGE manquant");
  const mba = read("mba.html");
  assert.ok(!/CPGE/.test(mba), "la page MBA doit rester centrée MBA");
});

test("pages chargent config.js puis include.js puis main.js", () => {
  for (const f of ["index.html", "mba.html", "a-propos.html", "president.html", "contact.html"]) {
    const html = read(f);
    const iConfig = html.indexOf("assets/js/config.js");
    const iInclude = html.indexOf("assets/js/include.js");
    const iMain = html.indexOf("assets/js/main.js");
    assert.ok(iConfig > -1 && iInclude > -1 && iMain > -1, `${f} scripts manquants`);
    assert.ok(iConfig < iInclude && iInclude < iMain, `${f} ordre scripts incorrect`);
  }
});

test("netlify.toml publish racine", () => {
  const t = read("netlify.toml");
  assert.ok(/publish\s*=\s*["']\.["']/.test(t), "publish doit être .");
});

test("HANDOVER mentionne autorisation Président et tests", () => {
  const h = read("HANDOVER.md");
  assert.ok(h.includes("Président") || h.includes("MINANG"));
  assert.ok(h.includes("npm test"));
  assert.ok(h.includes("contact@upl-gabon.com"));
});

test("formulaire contact pointe vers contact@", () => {
  const html = read("contact.html");
  assert.ok(html.includes('data-mailto="contact@upl-gabon.com"'));
});

console.log("");
if (failed) {
  console.error(`FAILED: ${failed} test(s)\n`);
  process.exit(1);
}
console.log("All tests passed.\n");

test("ton factuel : pas de langage interne ni d'éléments fictifs dans le HTML public", () => {
  const banned = [
    "grande école",
    "pas une coquille",
    "UPL_Campus_illustration",
    "multi-université",
    "Architecture prête",
    "Preuve d'activité",
    "le moment venu",
    "PrivateEmail",
    "Namecheap",
    "bientôt sur le site",
  ];
  for (const p of walkHtml()) {
    const html = readFileSync(p, "utf8");
    for (const b of banned) {
      assert.ok(!html.toLowerCase().includes(b.toLowerCase()), `"${b}" trouvé dans ${p}`);
    }
  }
});

test("vidéos : présentation TV en autoplay (accueil), interview sur le MBA, rentrée 2024 supprimée", () => {
  const index = read("index.html");
  assert.ok(index.includes("jh_iCTJuLKA"), "présentation TV manquante sur l'accueil");
  assert.ok(/embed\/[A-Za-z0-9_-]+\?autoplay=1&mute=1/.test(index), "autoplay muet manquant (accueil)");
  assert.ok(index.includes("Son coupé par défaut"), "note son manquante");
  assert.ok(!index.includes("SyUXYUPj6hc"), "Rentrée 2024 encore présente sur l'accueil");
  const mba = read("mba.html");
  assert.ok(mba.includes("FAKHfv8nN7I"), "interview manquante sur la page MBA");
  assert.ok(mba.includes("en-savoir-plus"), "ancre « En savoir plus » manquante");
  for (const p of walkHtml()) {
    const html = readFileSync(p, "utf8");
    assert.ok(!html.includes("SyUXYUPj6hc"), "Rentrée 2024 encore présente dans " + p);
  }
});

test("infos dynamiques : config expose citations et communiqués", () => {
  const js = read("assets/js/config.js");
  assert.ok(js.includes("quotes:"), "tableau quotes manquant");
  assert.ok(js.includes("news:"), "tableau news manquant");
  assert.ok(js.includes("Peter Drucker"), "citation manquante");
  assert.ok(js.includes("Inscriptions ouvertes"), "communiqué manquant");
});

test("accueil : ticker, citation rotative et grille de communiqués branchés", () => {
  const index = read("index.html");
  for (const marker of ["data-ticker", "data-quote-box", "data-news-grid", "quote-text", "quote-author"]) {
    assert.ok(index.includes(marker), `marqueur manquant : ${marker}`);
  }
  const main = read("assets/js/main.js");
  assert.ok(main.includes("youtube-nocookie.com/embed"), "lecteur vidéo intégré manquant");
});

test("a-propos : direction + liens Douala et ESSEC Douala", () => {
  const html = read("a-propos.html");
  assert.ok(html.includes("Serge Patrick MINANG"), "bloc président manquant");
  assert.ok(html.includes("univ-douala.com"), "lien Université de Douala manquant");
  assert.ok(html.includes("essec-douala.cm"), "lien ESSEC Douala manquant");
});

test("mot du Président : page, nav et liens footer", () => {
  assert.ok(existsSync(join(ROOT, "president.html")), "manque president.html");
  const pres = read("president.html");
  assert.ok(pres.includes("Serge Patrick MINANG"), "président non cité");
  assert.ok(pres.includes("contact@upl-gabon.com"), "email manquant");
  const include = read("assets/js/include.js");
  assert.ok(include.includes("president.html"), "lien nav/footer manquant");
});

test("compte à rebours rentrée : branché et masqué sans date", () => {
  const cfg = read("assets/js/config.js");
  assert.ok(cfg.includes("rentree:"), "config rentree manquante");
  const m = cfg.match(/rentree:\s*\{\s*date:\s*"([^"]*)"/);
  assert.ok(m, "date de rentrée illisible");
  const index = read("index.html");
  assert.ok(index.includes("data-countdown"), "marqueur countdown manquant");
  const main = read("assets/js/main.js");
  assert.ok(main.includes("data-countdown") && main.includes("J-"), "logique countdown manquante");
});

test("SEO : JSON-LD, robots.txt et sitemap.xml", () => {
  const index = read("index.html");
  assert.ok(index.includes("application/ld+json"), "JSON-LD manquant");
  assert.ok(index.includes("CollegeOrUniversity"), "type schema manquant");
  for (const f of ["robots.txt", "sitemap.xml"]) {
    assert.ok(existsSync(join(ROOT, f)), `manque ${f}`);
  }
  assert.ok(read("robots.txt").includes("sitemap.xml"));
});

test("paiement : Airtel Money, justificatif et confirmation UPL — parité retirée", () => {
  const cfg = read("assets/js/config.js");
  assert.ok(cfg.includes("Airtel Money"), "Airtel Money manquant dans config");
  assert.ok(cfg.includes("paymentNotices"), "situations paiement manquantes");
  assert.ok(cfg.includes("confirmation de l'UPL"), "règle confirmation UPL manquante");
  const mba = read("mba.html");
  assert.ok(mba.includes("Airtel Money") && mba.includes("confirmation de l'UPL"), "info paiement MBA manquante");
  const index = read("index.html");
  assert.ok(!index.includes("655,957"), "parité EUR/FCFA encore présente");
});

test("offre officielle 2026-2027 : tarifs verrouillés sur les supports officiels UPL", () => {
  const index = read("index.html");
  assert.ok(index.includes("Les formations de la rentrée"), "section formations manquante");
  for (const fee of ["1 000 000 FCFA", "1 200 000 FCFA", "1 500 000 FCFA", "2 000 000 FCFA", "2 200 000 FCFA", "4 000 000 FCFA"]) {
    assert.ok(index.includes(fee), `tarif officiel manquant ou modifié : ${fee}`);
  }
  assert.ok(index.includes("50 premières inscriptions"), "mention 50 premières inscriptions manquante");
  assert.ok(index.includes("6 tranches"), "modalité 6 tranches manquante");
  assert.ok(/places\s+limitées/i.test(index), "places limitées manquant");
  assert.ok(index.includes("Déposer mon dossier"), "CTA dossier manquant");
  assert.ok(index.includes("Faculté de Gouvernance, Leadership et Management"), "pôles manquants");
  assert.ok(index.includes("200 000 FCFA") && index.includes("300 000 FCFA"), "frais d'inscription L1 manquants");
  const enIndex = read("en/index.html");
  for (const fee of ["1,000,000 FCFA", "1,200,000 FCFA", "1,500,000 FCFA", "2,000,000 FCFA", "2,200,000 FCFA", "4,000,000 FCFA"]) {
    assert.ok(enIndex.includes(fee), `tarif EN manquant : ${fee}`);
  }
  const apropos = read("a-propos.html");
  assert.ok(/2026-2027/.test(apropos), "mention rentrée 2026-2027 manquante (à propos)");
});

test("site bilingue : 5 pages EN câblées (lang, base, scripts, bandeau d'action)", () => {
  for (const f of ["index.html", "mba.html", "a-propos.html", "president.html", "contact.html"]) {
    const html = read("en/" + f);
    assert.ok(html.includes('lang="en"'), `en/${f} : lang manquant`);
    assert.ok(html.includes('data-base="../"'), `en/${f} : data-base manquant`);
    assert.ok(html.includes('UPL.lang = "en"'), `en/${f} : UPL.lang manquant`);
    assert.ok(html.includes("../assets/css/main.css"), `en/${f} : css manquant`);
    assert.ok(html.includes("data-action-band"), `en/${f} : bandeau d'action manquant`);
    assert.ok(html.includes("data-include-footer"), `en/${f} : footer manquant`);
  }
  const include = read("assets/js/include.js");
  assert.ok(include.includes("lang-switch"), "bascule de langue manquante");
  assert.ok(include.includes("data-action-band"), "injection bandeau manquante");
  assert.ok(include.includes("bandApply") && include.includes("bandMeeting") && include.includes("bandPartner"), "CTAs du bandeau manquants");
});

test("config bilingue : citations, communiqués, notices et ticker traduits", () => {
  const cfg = read("assets/js/config.js");
  assert.ok((cfg.match(/textEn:/g) || []).length >= 6 + 3 + 4, "traductions textEn incomplètes");
  assert.ok((cfg.match(/titleEn:/g) || []).length >= 4, "traductions titleEn incomplètes");
  assert.ok((cfg.match(/sourceEn:/g) || []).length >= 3, "traductions sourceEn incomplètes");
  assert.ok((cfg.match(/tagEn:/g) || []).length >= 4, "traductions tagEn incomplètes");
  assert.ok(cfg.includes("labelEn"), "labelEn rentree manquant");
  assert.ok(cfg.includes('{ fr: "Cours du soir'), "tickerExtra non bilingue");
});

test("bandeau d'action présent sur toutes les pages (FR et EN)", () => {
  let count = 0;
  for (const p of walkHtml()) {
    const html = readFileSync(p, "utf8");
    assert.ok(html.includes("data-action-band"), `bandeau d'action manquant dans ${p}`);
    count++;
  }
  assert.ok(count >= 10, "pages inspectées insuffisantes : " + count);
});

test("sitemap bilingue", () => {
  const sm = read("sitemap.xml");
  for (const u of ["https://upl-gabon.com/en/", "https://upl-gabon.com/en/mba.html"]) {
    assert.ok(sm.includes(u), "URL EN manquante : " + u);
  }
});

test("animations sobres : trajectoire animée + poussière d'or avec garde-fous d'accessibilité", () => {
  const index = read("index.html");
  assert.ok(index.includes("data-timeline"), "timeline manquante (accueil)");
  assert.ok(index.includes("tl-cap"), "svg chapeau manquant");
  assert.ok(index.includes("effects.js"), "effects.js non chargé (accueil)");
  assert.ok(/La\s+trajectoire(\s|<br\s*\/>)+de l'UPL/.test(index), "titre trajectoire manquant");
  assert.ok(index.includes("chrono-year") && index.includes("chrono-vow"), "structure éditoriale manquante");
  const enIndex = read("en/index.html");
  assert.ok(enIndex.includes("data-timeline") && enIndex.includes("The UPL trajectory"), "timeline EN manquante");
  const effects = read("assets/js/effects.js");
  assert.ok(effects.includes("(prefers-reduced-motion: reduce)"), "effects.js sans garde reduced-motion");
  assert.ok(effects.includes("visibilitychange"), "effects.js sans pause onglet masqué");
  const main = read("assets/js/main.js");
  assert.ok(main.includes("IntersectionObserver") && main.includes("tl-visible"), "révélation timeline manquante");
  const css = read("assets/css/main.css");
  assert.ok(css.includes("@media (prefers-reduced-motion: reduce)"), "fallback CSS reduced-motion manquant");
  assert.ok(css.includes("gold-canvas"), "styles poussière d'or manquants");
});
