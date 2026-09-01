/**
 * Génère les blocs de texte de docs/com/BIOS_RESEAUX_2026.md depuis assets/js/config.js.
 *
 *   npm run bios:sync        (ou : node docs/com/_sync_bios.mjs)
 *
 * Marqueurs dans le doc :  {{bio:reseau.champ}}
 *   ex. {{bio:facebook.bio}}  {{bio:linkedin.about}}  {{bio:whatsapp.about}}
 * Le marqueur est remplacé par un bloc de code prêt à copier-coller, suivi du compteur réel.
 * config.js reste la SEULE source de vérité — ne jamais retoucher un texte dans le doc.
 */
import { readFileSync, writeFileSync } from "fs";
import { fileURLToPath } from "url";
import { dirname, join, resolve } from "path";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..", "..");

export function loadSocial() {
  const src = readFileSync(join(ROOT, "assets/js/config.js"), "utf8");
  const win = {};
  new Function("window", src)(win);
  if (!win.UPL || !win.UPL.config || !win.UPL.config.social) {
    throw new Error("config.js : window.UPL.config.social introuvable");
  }
  return win.UPL.config.social;
}

export function render(doc, social) {
  return doc.replace(/\{\{bio:([a-z]+)\.([a-zA-Z]+)\}\}/g, (_m, net, field) => {
    const entry = social[net];
    if (!entry) throw new Error(`Réseau inconnu dans config.social : ${net}`);
    const text = entry[field];
    if (typeof text !== "string") throw new Error(`config.social.${net}.${field} absent`);
    const max = entry[field + "Max"] ?? entry.bioMax;
    const count = max
      ? `_${text.length} caractères — limite plateforme ${max}, vérifié par npm test_`
      : `_${text.length} caractères_`;
    return "```text\n" + text + "\n```\n" + count;
  });
}

if (process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  const file = join(ROOT, "docs/com/BIOS_RESEAUX_2026.md");
  const before = readFileSync(file, "utf8");
  const after = render(before, loadSocial());
  if (after.includes("{{bio:")) {
    throw new Error("Marqueur(s) non résolu(s) : " + after.match(/\{\{bio:[^}]+\}\}/g).join(", "));
  }
  writeFileSync(file, after);
  console.log("BIOS_RESEAUX_2026.md synchronisé avec config.js");
}
