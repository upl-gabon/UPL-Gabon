# Dépôt à priorité THÈSE — UPL en base de données

**Principe (décision du 08/09/2026) :** connecté à GitHub, on travaille **en priorité sur la thèse**.
L'UPL reste en production (ne rien casser) et devient la **base de données** de référence :
contenus vérifiés du secteur EPES au service de la thèse. Les deux pistes sont étanches
(fichiers disjoints, tests séparés, règles écrites) — le simultané reste possible sans confusion.

> Reprise instantanée : lire [`REPRISE.md`](../REPRISE.md) en premier, à chaque conversation.

## Carte du dépôt — thèse prioritaire, UPL en base

| | Piste THÈSE (prioritaire) | Base UPL (ressource — ne rien casser) |
|---|---|---|
| Dossier | `these/` uniquement | racine : `index.html`, `mba.html`, `a-propos.html`, `president.html`, `contact.html`, `en/`, `assets/` |
| Doc d'entrée | `REPRISE.md` → `these/README.md` | `REPRISE.md` → `HANDOVER.md` + `README.md` |
| Garde-fous | `docs/06_JURY_SIMULE_THESE.md` (Chabanne-Rive · Valax · Loufrani) | règles éditoriales `HANDOVER.md` |
| Tests | `npm run test:these` (9 tests) | `npm run test:upl` (30 tests) |
| Charte | encre / bronze / papier (`these/style.css`) | bleu `#0B2A5B` / or `#C9A227` (`assets/css/main.css`) |
| Scripts | `these/app.js` seul | `assets/js/config.js` + `include.js` + `main.js` + `effects.js` |
| Visibilité | `noindex`, hors sitemap, lien direct `/these/` | public, sitemap, référencé |
| Validation | Auteur (tout contenu thèse) | Président (action publique UPL) |

**Fichiers partagés (rares, attention) :** `package.json` (scripts), `netlify.toml` (publish `.`
— couvre les deux pistes), `HANDOVER.md` (journal commun), `README.md` (aiguillage),
`REPRISE.md` (état courant — maintenu à chaque message).
Les modifier = penser aux deux pistes + `npm test` complet.

## Ce qui appartient à quoi (anti-confusion)

- **THÈSE (prioritaire)** : question centrale, plan, tableaux/figures, méthode, documents de
  travail, confidentialité terrain (codes EPES-A à EPES-E), échanges scientifiques, jury simulé.
- **BASE UPL (ressource)** : formations, tarifs, admissions, communiqués, partenariats
  institutionnels, bâtiment R+2 / Matrix Group (dossier UPL, PAS la thèse), com rentrée, SEO.
  La thèse **LIT** cette base (documentation, références secteur) ; elle ne la modifie **jamais**
  pour ses besoins propres. Toute modification UPL suit les règles `HANDOVER.md` + validation Président.
- **Ponts autorisés (les SEULS)** : `these/` → `../index.html`, `../contact.html`,
  `mailto:contact@upl-gabon.com?subject=Recherche doctorale`. Aucun lien UPL → `these/`.

## Travailler en simultané (règles)

1. **Fichiers disjoints = conflits impossibles** : la piste thèse ne touche jamais à la racine/`assets/`
   et la base UPL ne touche jamais à `these/`. Deux personnes (ou deux sessions IA) peuvent
   avancer en parallèle sans se marcher dessus.
2. **Une PR / un commit par piste** : ne jamais mélanger UPL + thèse dans le même commit.
   Message explicite : `these: …` ou `upl: …`.
3. **Tests ciblés pendant le travail** : `npm run test:these` (prioritaire) ou `npm run test:upl`.
4. **`npm test` complet avant tout merge** : il enchaîne les deux suites + les garde-fous
   transverses (discrétion croisée, ton factuel, absence de contenus sensibles).
5. **Fichiers partagés** (`package.json`, `netlify.toml`, `HANDOVER.md`, `README.md`, `REPRISE.md`) :
   une seule piste à la fois, annoncer la modification (journal HANDOVER § 10).
6. **Jamais de push direct sur `main`** : branche → PR → revue → merge (les deux pistes).
7. **Fin de chaque message IA : mettre à jour `REPRISE.md`** (état, chantiers, journal) —
   la conversation suivante s'arrête par défaut et reprend sans contexte.

## Garde-fous automatiques transverses

- `tests/site.test.mjs` : ton factuel, pas de fausses offres, Calvin hors pages publiques,
  bandeau sur toutes les pages (y compris `these/`), tarifs UPL verrouillés.
- `tests/these.test.mjs` : indépendance (aucun asset UPL), charte propre, `noindex`,
  ponts autorisés uniquement, confidentialité terrain, discrétion croisée (UPL ⇏ thèse).
- CI (à activer, 1 min) : `docs/templates/ci-tests.yml.template` → `npm test` à chaque push/PR.

## Aperçu local

```bash
npm run serve
# Thèse (prioritaire) → http://127.0.0.1:5173/these/
# Base UPL            → http://127.0.0.1:5173/
```

## En cas de doute

- « Où mettre X ? » → tableau ci-dessus + `these/README.md` (règle 5 : rien d'inventé).
- Conflit entre pistes → le Président/auteur arbitre ; par défaut, **la thèse ne contraint
  jamais la base UPL** (pas de lien, pas de dépendance, pas de mention),
  et la base UPL ne freine jamais la thèse (lecture libre, sans modification).
