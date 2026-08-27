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
    "Licence 1",
    "six filières",
    "6 filières",
    "Sciences Po",
    "Polytechnique",
    "partenariats@upl",
    "admissions@upl-gabon.com",
  ];
  for (const p of walkHtml()) {
    const html = readFileSync(p, "utf8");
    for (const b of banned) {
      assert.ok(!html.includes(b), `"${b}" trouvé dans ${p}`);
    }
  }
});

test("CPGE pas présenté comme offre ouverte (page dédiée / nav)", () => {
  const index = read("index.html");
  const mba = read("mba.html");
  assert.ok(!/CPGE/.test(index + mba), "CPGE ne doit pas apparaître offre");
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

test("les 3 vidéos officielles sont présentes sur l'accueil", () => {
  const index = read("index.html");
  for (const id of ["SyUXYUPj6hc", "FAKHfv8nN7I", "jh_iCTJuLKA"]) {
    assert.ok(index.includes(id), `vidéo manquante : ${id}`);
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
