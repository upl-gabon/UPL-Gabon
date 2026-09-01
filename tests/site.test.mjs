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
  assert.ok(js.includes("contact: {"), "config.js doit toujours porter le bloc contact public");
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


/* ---------- Réseaux : bios, compteurs, liste noire ---------- */
const SOCIAL_LIMITS = {
  "facebook.bio": 101, "facebook.about": 255,
  "instagram.bio": 150, "tiktok.bio": 80,
  "linkedin.headline": 220, "linkedin.tagline": 200, "linkedin.about": 2000, "linkedin.aboutEn": 2000,
  "whatsapp.bio": 139, "whatsapp.about": 256,
  "youtube.bio": 150, "youtube.about": 1000,
  "google.about": 750, "x.bio": 160,
};

function loadUplConfig(rel) {
  const win = {};
  new Function("window", read(rel))(win);
  if (!win.UPL || !win.UPL.config) throw new Error("window.UPL.config introuvable");
  return win.UPL.config;
}

function socialTexts(cfg) {
  const out = [];
  for (const [net, entry] of Object.entries(cfg.social || {})) {
    for (const field of ["bio", "about", "aboutEn", "headline", "tagline", "name", "category"]) {
      if (typeof entry[field] === "string") out.push([`${net}.${field}`, entry[field]]);
    }
  }
  return out;
}

test("bios des réseaux : dans les limites de chaque plateforme", () => {
  const cfg = loadUplConfig("assets/js/config.js");
  for (const [key, text] of socialTexts(cfg)) {
    if (!/\.(bio|about|aboutEn|headline|tagline)$/.test(key)) continue;
    const limit = SOCIAL_LIMITS[key];
    assert.ok(limit, `limite non documentée pour ${key}`);
    assert.ok(text.length <= limit, `${key} : ${text.length} caractères > ${limit} (éditer le texte dans config.js, jamais dans le doc)`);
    if (/\.(bio|about|aboutEn|headline|tagline)$/.test(key)) {
      const entry = cfg.social[key.split(".")[0]];
      const declared = entry[(key.split(".")[1]) + "Max"] ?? entry.bioMax;
      assert.equal(declared, limit, `${key}: la limite déclarée dans config.js doit coller au compteur de la plateforme`);
    }
  }
});

test("bios : la charte éditoriale est respectée (liste noire)", () => {
  const cfg = loadUplConfig("assets/js/config.js");
  const banned = [
    "admissions@", "partenariats@", "president@upl", "upl.com", "Maroc", "Ecobank",
    "garanti", "diplômé à coup sûr", "500 étudiants", "Calvin", "gmail.com", "Sciences Po",
    "Polytechnique", "HEC", "Journalisme", "Rejoignez l'Élite", "SyUXYUPj6hc", "remboursement",
    "bourse", "campus",
  ];
  for (const [key, text] of socialTexts(cfg)) {
    for (const b of banned) {
      assert.ok(!text.toLowerCase().includes(b.toLowerCase()), `${b} présent dans ${key}`);
    }
  }
});

test("bios : palier 1 = pré-inscriptions (et MBA ouvert depuis 2022)", () => {
  const cfg = loadUplConfig("assets/js/config.js");
  const open = ["facebook.bio", "instagram.bio", "tiktok.bio", "whatsapp.bio", "linkedin.tagline"];
  const joined = socialTexts(cfg).map(([k, v]) => v).join("\n");
  for (const key of open) {
    const [net, field] = key.split(".");
    assert.ok(cfg.social[net][field].includes("2026-2027"), `${key} doit porter la campagne 2026-2027`);
  }
  assert.ok(!/inscriptions ouvertes/i.test(joined) || /Executive MBA : inscriptions ouvertes/i.test(joined),
    "« inscriptions ouvertes » n'est admis que pour l'Executive MBA");
  assert.ok(joined.includes("2022"), "l'antériorité du MBA (2022) doit apparaître");
});

test("aucun handle générique @UPL sur les pages publiques (tiers, pas l'UPL)", () => {
  for (const p of walkHtml()) {
    const html = readFileSync(p, "utf8");
    assert.ok(!/youtube\.com\/@UPL\b/.test(html), `lien @UPL (générique) dans ${p}`);
    assert.ok(!/twitter\.com\/@UPL\b|x\.com\/@UPL\b/.test(html), `lien X @UPL dans ${p}`);
    assert.ok(!/upl\.com(?![-.a-z])/i.test(html.replace(/upl-gabon\.com/g, "")), `référence à upl.com dans ${p}`);
  }
});

test("bloc réseaux du site : rien d'affiché tant qu'un compte n'est pas live", () => {
  const cfg = loadUplConfig("assets/js/config.js");
  for (const [net, entry] of Object.entries(cfg.social)) {
    assert.ok(["live", "pending", "off"].includes(entry.status), `statut inconnu pour ${net} : ${entry.status}`);
    if (entry.status === "live") {
      assert.ok(/^https:\/\/(www\.)?(facebook|instagram|tiktok|linkedin|youtube|x)\./.test(entry.url),
        `${net} est à "live" sans URL officielle du bon domaine : ${entry.url}`);
      assert.ok(typeof entry.bio === "string" && entry.bio.length > 10, `${net} est à "live" sans bio`);
    }
  }
  const include = read("assets/js/include.js");
  assert.ok(include.includes('net.status !== "live"'), "include.js doit filtrer sur status 'live'");
  assert.ok(include.includes("showSocialLinks"), "include.js doit respecter le commutateur features.showSocialLinks");
  for (const f of ["contact.html", "en/contact.html"]) {
    assert.ok(read(f).includes("data-social"), `monteur [data-social] manquant dans ${f}`);
  }
  const css = read("assets/css/main.css");
  assert.ok(css.includes(".social-row") && css.includes(".social-panel"), "styles du bloc réseaux manquants");
});

test("BIOS_RESEAUX_2026.md reste calé sur config.js (générateur)", () => {
  const doc = read("docs/com/BIOS_RESEAUX_2026.md");
  assert.ok(!doc.includes("{{bio:"), "marqueurs non générés — lancer npm run bios:sync");
  const cfg = loadUplConfig("assets/js/config.js");
  for (const [net, entry] of Object.entries(cfg.social)) {
    for (const field of ["bio", "about", "headline", "tagline", "aboutEn"]) {
      if (typeof entry[field] !== "string") continue;
      for (const line of entry[field].split("\n").filter((l) => l.trim())) {
        assert.ok(doc.includes(line), `${net}.${field} introuvable dans le doc — npm run bios:sync`);
      }
    }
  }
});

test("flyers : le contenu généré vient bien de config.js (zéro chiffre recopié)", () => {
  const data = JSON.parse(read("docs/com/flyers/data/flyers.json"));
  const cfg = loadUplConfig("assets/js/config.js");
  assert.equal(data.tarifs.length, cfg.programmes.length, "un programme du site manque dans les flyers");
  cfg.programmes.forEach((p, i) => {
    assert.equal(data.tarifs[i].price, p.tuition, `tarif ${p.id} différent de config.js`);
    assert.equal(data.tarifs[i].label, p.title, `libellé ${p.id} différent de config.js`);
  });
  assert.equal(data.contact.email, cfg.contact.email);
  assert.deepEqual(data.contact.phones, cfg.contact.phonesUpl.map((p) => p.display));
  const index = read("index.html");
  for (const pole of data.poles) {
    assert.ok(index.includes(pole), `pôle absent du site : ${pole}`);
  }
  const flat = JSON.stringify(data.flyers) + JSON.stringify(data.copy);
  for (const b of ["admissions@", "upl.com", "Maroc", "inscriptions ouvertes pour la Licence"]) {
    assert.ok(!flat.includes(b), `${b} dans les flyers`);
  }
});

test("pack réseaux : visuels générés, aucun tarif codé à la main dans le script", () => {
  const script = read("docs/com/pack-reseaux/_build_pack.py");
  assert.ok(!/\d \d{3} \d{3} FCFA/.test(script), "un tarif figé dans _build_pack.py — passer par flyers.json");
  assert.ok(!script.includes("upl.com"), "upl.com dans le script du pack");
  for (const must of ["P11", "P12", "visage IA", "ZONES SÛRES", "256"]) {
    assert.ok(read("docs/com/pack-reseaux/2026-09/MODE-EMPLOI.txt").includes(must), `MODE-EMPLOI.txt sans ${must}`);
  }
  const files = readdirSync(join(ROOT, "docs/com/pack-reseaux/2026-09"));
  assert.ok(files.filter((f) => f.endsWith(".png")).length >= 20, "pack incomplet : " + files.length + " fichiers");
});

/* ---------- Sécurité : le dépôt ne publie pas les affaires internes ---------- */
test("GitHub Pages n'expose ni docs/, ni HANDOVER.md, ni README.md", () => {
  const cfg = read("_config.yml");
  for (const must of ["docs", "HANDOVER.md", "README.md", "tests"]) {
    assert.ok(cfg.includes("- " + must), `_config.yml doit exclure ${must}`);
  }
  assert.ok(!cfg.includes("- CNAME"), "CNAME doit rester publié (domaine upl-gabon.com)");
  assert.ok(!existsSync(join(ROOT, ".nojekyll")), ".nojekyll réactiverait la publication brute des docs");
});

test("Netlify (secours) renvoie le matériel interne en 404", () => {
  const t = read("netlify.toml");
  for (const path of ["/docs/*", "/HANDOVER.md", "/README.md"]) {
    assert.ok(t.includes(`from = "${path}"`), `règle 404 manquante pour ${path}`);
  }
});

test("les fichiers publiés par le site sont propres (ni lien Drive, ni contact personnel)", () => {
  const published = walkHtml().concat(
    walkHtml(join(ROOT, "assets")).map((f) => f.slice(ROOT.length + 1)),
    ["robots.txt", "sitemap.xml", "CNAME", "_config.yml"]
  );
  for (const abs of new Set(published)) {
    const rel = abs.startsWith(ROOT) ? abs.slice(ROOT.length + 1) : abs;
    const txt = read(rel);
    assert.ok(!/drive\.google\.com\/drive\/folders\/[A-Za-z0-9_-]+/.test(txt), `lien Drive dans ${rel}`);
    assert.ok(!/blanchardminang00|\+33 7 52 97/.test(txt), `contact personnel dans ${rel}`);
  }
});

test("aucun lien de dossier Drive nulle part dans le dépôt (docs internes inclus)", () => {
  const skip = new Set([".git", "node_modules"]);
  const re = /drive\.google\.com\/drive\/folders\/[A-Za-z0-9_-]{10,}/;
  (function walk(dir) {
    for (const e of readdirSync(dir, { withFileTypes: true })) {
      if (skip.has(e.name)) continue;
      const abs = join(dir, e.name);
      if (e.isDirectory()) walk(abs);
      else if (/\.(md|html|js|toml|yml|xml|txt)$/.test(e.name)) {
        const txt = readFileSync(abs, "utf8");
        assert.ok(!re.test(txt), `lien Drive dans ${abs.slice(ROOT.length + 1)} — le lien d'un dossier partagé n'a rien à faire dans un dépôt`);
      }
    }
  })(ROOT);
});

test("config.js ne porte plus les coordonnées privées (calvinEmergency retiré)", () => {
  const cfg = read("assets/js/config.js");
  assert.ok(!cfg.includes("calvinEmergency"), "coordonnées privées encore dans le fichier chargé par le navigateur");
  assert.ok(existsSync(join(ROOT, "docs/CONTACTS_HORS_SITE.md")), "les contacts internes doivent vivre dans docs/");
});

test("le kit de prompts vidéo verrouille le rendu et les interdits", () => {
  const f = read("docs/com/PROMPT_VIDEO_IA.md");
  for (const must of ["NE GÉNÈRE AUCUNE VIDÉO", "INTERDITS ABSOLUS", "[À COMPLÉTER PAR L'ÉCOLE]",
                      "FAITS VÉRIFIÉS", "Un seul rendu"]) {
    assert.ok(f.includes(must), `garde-fou manquant dans le kit de prompts : ${must}`);
  }
  assert.ok(!/upl\.com(?!-gabon)/.test(f.replace(/jamais upl\.com/g, "")), "upl.com nu (sans -gabon)");
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
    "quand elles seront réelles",
    "ce qu'il annonce",
    "ne s'affiche pas",
    "critère : la réalité",
    "when they are real",
    "is not displayed",
    "yardstick",
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
  assert.ok(
    main.includes("youtube-nocookie.com/embed") || index.includes("youtube.com/embed"),
    "lecteur vidéo intégré manquant"
  );
});

test("accueil : six cartes de formations et statuts 2026-2027", () => {
  for (const page of ["index.html", "en/index.html"]) {
    const html = read(page);
    assert.equal((html.match(/class="programme-card(?: programme-card-open)?"/g) || []).length, 6, `six cartes attendues dans ${page}`);
    assert.equal((html.match(/programme-card-open/g) || []).length, 1, `seul le MBA doit être ouvert dans ${page}`);
  }
});

test("header : heure de Libreville avec fuseau explicite", () => {
  const include = read("assets/js/include.js");
  assert.ok(include.includes('timeZone: "Africa/Libreville"'), "fuseau Africa/Libreville manquant");
  assert.ok(include.includes("data-libreville-time"), "horloge du header manquante");
});

test("a-propos : direction + liens Douala et ESSEC Douala", () => {
  const html = read("a-propos.html");
  assert.ok(html.includes("Serge Patrick MINANG"), "bloc président manquant");
  assert.ok(html.includes("univ-douala.com"), "lien Université de Douala manquant");
  assert.ok(html.includes("essec-dla.com/concours"), "lien ESSEC Douala manquant");
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
  assert.ok(index.includes("Rejoindre la liste de pré-inscription"), "CTA pré-inscription manquant");
  assert.ok(index.includes("Pré-inscriptions 2026-2027"), "kicker pré-inscriptions manquant");
  assert.ok(index.includes("sans engagement"), "mention sans engagement manquante");
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
  assert.ok(effects.includes('page-hero'), "effects.js doit couvrir toutes les pages (page-hero)");
  let withEffects = 0;
  for (const p of walkHtml()) {
    const html = readFileSync(p, "utf8");
    if (html.includes("effects.js")) withEffects++;
  }
  assert.ok(withEffects >= 10, "pluie dorée absente de certaines pages : " + withEffects);
  const main = read("assets/js/main.js");
  assert.ok(main.includes("IntersectionObserver") && main.includes("tl-visible"), "révélation timeline manquante");
  const css = read("assets/css/main.css");
  assert.ok(css.includes("@media (prefers-reduced-motion: reduce)"), "fallback CSS reduced-motion manquant");
  assert.ok(css.includes("gold-canvas"), "styles poussière d'or manquants");
});
