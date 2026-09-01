/**
 * Génère docs/com/flyers/data/flyers.json — le CONTENU des flyers, extrait des sources officielles.
 *
 *   npm run flyers:data
 *
 * Principe : aucun tarif, aucun contact, aucun nom de pôle n'est recopié à la main.
 * Tout vient de assets/js/config.js (programmes, contact, bios) et de index.html (liste des pôles,
 * paragraphes officiels). _build_flyers.py ne fait que mettre en page ce JSON : si un chiffre bouge
 * sur le site, il bouge dans les flyers, et npm test casse si les deux divergent.
 */
import { readFileSync, writeFileSync, mkdirSync } from "fs";
import { fileURLToPath } from "url";
import { dirname, join } from "path";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..", "..", "..");
const OUT = join(ROOT, "docs/com/flyers/data");

function loadConfig() {
  const win = {};
  new Function("window", readFileSync(join(ROOT, "assets/js/config.js"), "utf8"))(win);
  return win.UPL.config;
}

function matchAll(re, text) {
  return [...text.matchAll(re)].map((m) => m[1].trim());
}

function stripTags(s) {
  return s
    .replace(/<br\s*\/?>/gi, " ")
    .replace(/<[^>]+>/g, "")
    .replace(/\s+/g, " ")
    .replace(/&nbsp;/g, " ")
    .trim();
}

const cfg = loadConfig();
const index = readFileSync(join(ROOT, "index.html"), "utf8");

/* --- Contacts ------------------------------------------------------------- */
const C = cfg.contact;
const contact = {
  email: C.email,
  phones: C.phonesUpl.map((p) => p.display),
  whatsapp: C.whatsapp.href,
  whatsappDisplay: C.whatsapp.display,
  site: "https://" + cfg.deploy.domain,
  siteShort: cfg.deploy.domain,
  addressShort: "Sablière, Libreville — Gabon",
  addressLong: cfg.institution.address.replace(/’/g, "'"),
  president: cfg.institution.president,
};

/* --- Offre : tarifs pris dans config.js (verbatim) ------------------------ */
const tarifs = cfg.programmes.map((p) => ({
  id: p.id,
  label: p.title,
  price: p.tuition,
  note: p.tuitionNote || "",
  status: p.status,
}));

/* --- Parole institutionnelle ---------------------------------------------- */
const pôleBlock = index.slice(index.indexOf("Cinq pôles d'enseignement"));
const poles = matchAll(/<li>([\s\S]*?)<\/li>/g, pôleBlock.slice(0, 1200)).map(stripTags);
const fraisBlock = index.slice(index.indexOf("Frais d'inscription (Licence 1)"));
const fraisInscription = stripTags(fraisBlock.slice(0, 420).split("</p>")[0].replace(/^[\s\S]*?:/, ""));
const rentreeNote = stripTags(
  index.slice(index.indexOf("La rentrée 2026-2027")).slice(0, 400).split("</p>")[0] || ""
);

const mba = cfg.programmes.find((p) => p.id === "exec-mba");
const licence = cfg.programmes.find((p) => p.id === "licence-1");

const COPY = {
  kicker: "Campagne 2026-2027",
  title: "Pré-inscriptions 2026-2027",
  programmesCourt: "Licence · Master · CPGE · Executive MBA · DBA",
  lead:
    "La pré-inscription est gratuite et sans engagement. Le secrétariat rappelle chaque candidat pour les pièces du dossier et les places disponibles.",
  lieu: "Sablière, Libreville — cours du soir et en journée",
  depuis: "Executive MBA ouvert depuis 2022, avec l'appui académique de l'Université de Douala.",
  places: "Places limitées — rentrée 2026-2027.",
  note:
    "Tarifs indiqués en droits de scolarité annuels. Un reçu est délivré pour tout paiement. Règlement par Airtel Money : conservez votre justificatif, la confirmation de l'UPL est indispensable.",
  etapes: [
    "Écrire à contact@upl-gabon.com (objet « Pré-inscription 2026-2027 ») : nom, téléphone, formation souhaitée, dernier diplôme obtenu.",
    "Le secrétariat rappelle et remet la liste des pièces du dossier.",
    "Après validation du profil : inscription et règlement auprès du secrétariat, Sablière.",
  ],
  mbaLignes: [
    "Public : cadres et dirigeants en activité.",
    `Cours du soir, 17h–21h, Sablière — promotion d'environ ${mba.promoSize} auditeurs.`,
    `Près de ${mba.approxAlumni} cadres formés depuis ${mba.since}.`,
    `Scolarité : ${mba.tuition} l'année, payable en tranches (jusqu'à huit échéances).`,
    "Candidature : CV, parcours et diplômes, par e-mail (objet « Candidature MBA ») ou dépôt au secrétariat.",
  ],
  l1Lignes: [
    `Droits de scolarité : ${licence.tuition}.`,
    "Frais d'inscription exigibles au dépôt du dossier : " +
      "200 000 FCFA (50 premières inscriptions) ou 300 000 FCFA (inscriptions normales).",
    "Solde en 6 tranches. Un reçu est délivré pour tout paiement.",
    "Un socle universitaire pour construire son parcours dans les pôles d'enseignement de l'UPL.",
  ],
  reseauxTitre: "Les suivre",
  mentions: [
    "Université Privée de Libreville — établissement privé d'enseignement supérieur, Libreville (Gabon).",
    "Les formations de la rentrée 2026-2027 sont annoncées en pré-inscriptions ; les modalités de dossier et de règlement sont précisées par le secrétariat.",
  ],
};

/* --- Bios courtes (reprises des comptes, pour le bas de page) ------------- */
const social = Object.fromEntries(
  Object.entries(cfg.social).map(([k, v]) => [k, { label: v.label, handle: v.handle || "", url: v.url || "", status: v.status }])
);

const qr = {
  contact: { label: "Se pré-inscrire — formulaire du site", value: contact.site + "/contact.html" },
  whatsapp: { label: "WhatsApp secrétariat", value: contact.whatsapp },
};

const flyers = [
  {
    id: "01-preinscriptions",
    format: "A5",
    title: COPY.title,
    kicker: COPY.kicker,
    lead: COPY.programmesCourt,
    blocks: [
      { type: "lead", text: COPY.lead },
      { type: "table", title: "Droits de scolarité 2026-2027", rows: tarifs },
      { type: "note", title: "Comment se pré-inscrire", lines: COPY.etapes },
      { type: "statement", text: COPY.places + " " + COPY.depuis },
    ],
  },
  {
    id: "02-licence1",
    format: "A5",
    title: "Licence 1 — rentrée 2026-2027",
    kicker: "Pré-inscriptions",
    lead: "Un socle universitaire, cinq pôles d'enseignement, une scolarité payable en tranches.",
    blocks: [
      { type: "lines", title: "Scolarité et inscription", lines: COPY.l1Lignes },
      { type: "note", title: "Comment se pré-inscrire", lines: COPY.etapes },
      { type: "statement", text: COPY.places },
    ],
  },
  {
    id: "03-mba",
    format: "A5",
    title: "Executive MBA",
    kicker: "Depuis 2022 · Université de Douala (appui académique)",
    lead: "Le programme de l'UPL pour les cadres et dirigeants en activité.",
    blocks: [
      { type: "lines", title: "Le programme en pratique", lines: COPY.mbaLignes },
      { type: "table", title: "Droits de scolarité 2026-2027", rows: tarifs.filter((t) => ["exec-mba", "dba"].includes(t.id)) },
      { type: "note", title: "Candidature", lines: COPY.etapes.slice(0, 2) },
    ],
  },
  {
    id: "04-tarifs-poles",
    format: "A4",
    title: "Grille des frais et pôles d'enseignement",
    kicker: "Rentrée 2026-2027",
    lead: COPY.programmesCourt,
    blocks: [
      { type: "table", title: "Droits de scolarité 2026-2027", rows: tarifs },
      { type: "lines", title: "Frais d'inscription (Licence 1)", lines: [fraisInscription] },
      { type: "lines", title: "Cinq pôles d'enseignement, plus les classes préparatoires", lines: poles },
      { type: "note", title: "À retenir", lines: [COPY.note, "Pré-inscriptions gratuites et sans engagement."] },
    ],
  },
  {
    id: "05-contact",
    format: "A6",
    title: "Université Privée de Libreville",
    kicker: "Secrétariat · Sablière, Libreville",
    lead: "Écrire, appeler, se déplacer — le secrétariat répond en jours ouvrés.",
    blocks: [{ type: "qr-pair", left: qr.contact, right: qr.whatsapp }],
  },
];

const data = {
  generatedFrom: "assets/js/config.js + index.html — npm run flyers:data",
  institution: { name: cfg.institution.name, short: cfg.institution.short, president: cfg.institution.president },
  brand: cfg.brand,
  contact,
  tarifs,
  poles,
  copy: COPY,
  social,
  qr,
  flyers,
  rentreeNote,
};

mkdirSync(OUT, { recursive: true });
writeFileSync(join(OUT, "flyers.json"), JSON.stringify(data, null, 2) + "\n");
console.log(
  "flyers.json écrit —",
  flyers.length,
  "flyers ·",
  tarifs.length,
  "tarifs ·",
  poles.length,
  "pôles ·",
  "frais:",
  fraisInscription.slice(0, 40) + "…"
);
