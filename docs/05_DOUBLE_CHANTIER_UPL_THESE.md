# Double chantier : UPL + Thèse — organisation du dépôt

**Principe :** connecté à GitHub, on peut travailler **soit sur l'UPL, soit sur la thèse**,
éventuellement en simultané, **sans confusion** : les deux pistes sont étanches
(fichiers disjoints, tests séparés, règles écrites).

## Carte du dépôt — deux pistes étanches

| | Piste UPL (institutionnel) | Piste THÈSE (recherche personnelle) |
|---|---|---|
| Dossier | racine : `index.html`, `mba.html`, `a-propos.html`, `president.html`, `contact.html`, `en/`, `assets/` | `these/` uniquement |
| Doc d'entrée | `HANDOVER.md` + `README.md` | `these/README.md` |
| Tests | `npm run test:upl` (30 tests) | `npm run test:these` (9 tests) |
| Charte | bleu `#0B2A5B` / or `#C9A227` (`assets/css/main.css`) | encre / bronze / papier (`these/style.css`) |
| Scripts | `assets/js/config.js` + `include.js` + `main.js` + `effects.js` | `these/app.js` seul |
| Visibilité | public, sitemap, référencé | `noindex`, hors sitemap, lien direct `/these/` |
| Validation | Président (action publique UPL) | Auteur (tout contenu thèse) |

**Fichiers partagés (rares, attention) :** `package.json` (scripts), `netlify.toml` (-verbal publish `.`
— couvre les deux pistes), `HANDOVER.md` (journal commun), `README.md` (aiguillage).
Les modifier = penser aux deux pistes + `npm test` complet.

## Ce qui appartient à quoi (anti-confusion)

- **UPL** : formations, tarifs, admissions, communiqués, partenariats institutionnels,
  bâtiment R+2 / Matrix Group (dossier UPL, PAS la thèse), com rentrée, SEO.
- **THÈSE** : question centrale, plan, tableaux/figures, méthode, documents de travail,
  confidentialité terrain (codes EPES-A à EPES-E), échanges scientifiques.
- **Ponts autorisés (les SEULS)** : `these/` → `../index.html`, `../contact.html`,
  `mailto:contact@upl-gabon.com?subject=Recherche doctorale`. Aucun lien UPL → `these/`.

## Travailler en simultané (règles)

1. **Fichiers disjoints = conflits impossibles** : la piste thèse ne touche jamais à la racine/`assets/`
   et la piste UPL ne touche jamais à `these/`. Deux personnes (ou deux sessions IA) peuvent
   avancer en parallèle sans se marcher dessus.
2. **Une PR / un commit par piste** : ne jamais mélanger UPL + thèse dans le même commit.
   Message explicite : `these: …` ou `upl: …`.
3. **Tests ciblés pendant le travail** : `npm run test:upl` ou `npm run test:these` selon la piste.
4. **`npm test` complet avant tout merge** : il enchaîne les deux suites + les garde-fous
   transverses (discrétion croisée, ton factuel, absence de contenus sensibles).
5. **Fichiers partagés** (`package.json`, `netlify.toml`, `HANDOVER.md`) : une seule piste à la fois,
   annoncer la modification (journal HANDOVER § 10).
6. **Jamais de push direct sur `main`** : branche → PR → revue → merge (les deux pistes).

## Garde-fous automatiques transverses

- `tests/site.test.mjs` : ton factuel, pas de fausses offres, Calvin hors pages publiques,
  bandeau sur toutes les pages (y compris `these/`), tarifs UPL verrouillés.
- `tests/these.test.mjs` : indépendance (aucun asset UPL), charte propre, `noindex`,
  ponts autorisés uniquement, confidentialité terrain, discrétion croisée (UPL ⇏ thèse).
- CI (à activer, 1 min) : `docs/templates/ci-tests.yml.template` → `npm test` à chaque push/PR.

## Aperçu local

```bash
npm run serve
# UPL   → http://127.0.0.1:5173/
# Thèse → http://127.0.0.1:5173/these/
```

## En cas de doute

- « Où mettre X ? » → tableau ci-dessus + `these/README.md` (règle 5 : rien d'inventé).
- Conflit entre pistes → le Président/auteur arbitre ; par défaut, **la thèse ne contraint
  jamais le site UPL** (pas de lien, pas de dépendance, pas de mention).
