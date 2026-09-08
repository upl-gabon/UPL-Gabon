/**
 * Tests de la piste THÈSE (zone indépendante these/)
 * Exécution ciblée : npm run test:these
 * Exécution complète : npm test (piste UPL + piste thèse)
 */
import { readFileSync, existsSync } from "fs";
import { join, dirname } from "path";
import { fileURLToPath } from "url";
import assert from "assert";

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = join(__dirname, "..");
const THESE = join(ROOT, "these");

function read(rel) {
  return readFileSync(join(ROOT, rel), "utf8");
}

const PAGES = ["index.html", "plan.html", "supports.html", "documents.html"].map(
  (f) => "these/" + f
);

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

console.log("\nTHÈSE — tests de la zone indépendante\n");

test("these: pages, styles, script et guide existent", () => {
  for (const f of [...PAGES, "these/style.css", "these/app.js", "these/README.md"]) {
    assert.ok(existsSync(join(ROOT, f)), `manque ${f}`);
  }
});

test("these: noindex sur toutes les pages (zone discrète)", () => {
  for (const f of PAGES) {
    assert.ok(read(f).includes("noindex"), `${f} sans noindex`);
  }
});

test("these: indépendance — aucun asset ni script UPL chargé", () => {
  const banned = [
    "assets/",
    "config.js",
    "include.js",
    "main.js",
    "effects.js",
    "data-include-header",
    "data-include-footer",
    "logo-upl",
    "window.UPL",
    "UPL.config",
    "UPL.lang",
  ];
  for (const f of [...PAGES, "these/app.js", "these/style.css"]) {
    const content = read(f);
    for (const b of banned) {
      assert.ok(!content.includes(b), `"${b}" trouvé dans ${f}`);
    }
  }
});

test("these: charte propre — ni bleu ni or UPL", () => {
  for (const f of [...PAGES, "these/style.css"]) {
    const content = read(f).toLowerCase();
    assert.ok(!content.includes("#0b2a5b"), `bleu UPL trouvé dans ${f}`);
    assert.ok(!content.includes("#c9a227"), `or UPL trouvé dans ${f}`);
  }
});

test("these: ponts autorisés uniquement (pas de mail inventé, pas de lien sauvage)", () => {
  for (const f of PAGES) {
    const html = read(f);
    for (const m of html.matchAll(/mailto:([^"?\s>]+)/g)) {
      assert.equal(m[1], "contact@upl-gabon.com", `mailto non autorisé dans ${f} : ${m[1]}`);
    }
    for (const m of html.matchAll(/href="(\.\.\/[^"]+)"/g)) {
      assert.ok(
        ["../index.html", "../contact.html"].includes(m[1]),
        `lien sortant non autorisé dans ${f} : ${m[1]}`
      );
    }
  }
});

test("these: confidentialité — codes EPES-A..E, jamais de noms pressentis ni Matrix", () => {
  const banned = [
    "Saint-Exupéry",
    "Saint-Exupery",
    "BGFI",
    "SUP de COM",
    "EM Gabon",
    "Techniques Avancées",
    "Matrix",
  ];
  for (const f of PAGES) {
    const html = read(f);
    for (const b of banned) {
      assert.ok(!html.includes(b), `"${b}" trouvé dans ${f} (régime de confidentialité)`);
    }
  }
  assert.ok(read("these/plan.html").includes("EPES-A"), "codes EPES-A..E manquants");
});

test("these: contenu — question centrale, QR, P, méthode, supports", () => {
  const index = read("these/index.html");
  assert.ok(index.includes("sous quelles conditions l'articulation"), "question centrale manquante");
  for (const q of ["QR1", "QR2", "QR3", "QR4"]) {
    assert.ok(index.includes(q), `${q} manquant`);
  }
  for (let i = 1; i <= 7; i++) {
    assert.ok(new RegExp(`\\bP${i}\\b`).test(index), `P${i} manquant`);
  }
  const plan = read("these/plan.html");
  for (const marker of ["NVivo", "45 participants", "EPES-A", "Annexes", "Chapitre 6"]) {
    assert.ok(plan.includes(marker), `marqueur manquant (plan) : ${marker}`);
  }
  const supports = read("these/supports.html");
  for (const marker of ["27 tableaux", "13 figures", "Figure 3.1", "Tableau 6.4", "Source : auteur"]) {
    assert.ok(supports.includes(marker), `marqueur manquant (supports) : ${marker}`);
  }
});

test("these: bandeau d'échanges indépendant (marqueur + rendu propre)", () => {
  for (const f of PAGES) {
    assert.ok(read(f).includes("data-action-band"), `bandeau manquant dans ${f}`);
  }
  const app = read("these/app.js");
  assert.ok(app.includes("data-action-band"), "app.js ne rend pas le bandeau");
  assert.ok(app.includes("Recherche doctorale"), "objet « Recherche doctorale » manquant");
});

test("discrétion croisée : le site UPL ne référence pas /these/", () => {
  const uplPages = [
    "index.html",
    "mba.html",
    "a-propos.html",
    "president.html",
    "contact.html",
    "en/index.html",
    "en/mba.html",
    "en/a-propos.html",
    "en/president.html",
    "en/contact.html",
  ];
  for (const f of uplPages) {
    assert.ok(!read(f).includes("these/"), `référence à /these/ trouvée dans ${f}`);
  }
  assert.ok(!read("sitemap.xml").includes("these"), "/these/ ne doit pas figurer au sitemap");
});

console.log("");
if (failed) {
  console.error(`FAILED: ${failed} test(s) piste thèse\n`);
  process.exit(1);
}
console.log("These track: all tests passed.\n");
