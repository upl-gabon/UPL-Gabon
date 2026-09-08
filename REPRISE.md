# REPRISE — reprise instantanée (LIRE EN PREMIER)

> **Toute IA ouvrant une conversation sur ce dépôt commence ici.**
> Hypothèse par défaut : **la conversation précédente s'est arrêtée net** —
> ce fichier dit exactement où, et comment continuer.

## 0. Protocole obligatoire (chaque message, sans exception)

1. **Lire dans l'ordre** : ce fichier → `these/README.md` → `docs/06_JURY_SIMULE_THESE.md`
   → `HANDOVER.md` § 10 (journal). Vérifier `git log --oneline -5` et `git status`.
2. **Ouvrir ta réponse en disant EXACTEMENT où on s'est arrêté** (section 1 : état,
   dernier commit, tests, question en suspens).
3. **Continuer directement** le chantier, avec par défaut la lentille jury :
   critique, pistes d'amélioration, réflexion, rigueur, **exigence DBA**
   (savoir actionnable, preuves tracées, rien d'inventé).
4. **À LA FIN DE CHAQUE MESSAGE : mettre à jour ce fichier**
   (État § 1, Chantiers § 3, Décisions § 4 si besoin, Journal § 6).
   Puis commiter + pusher si des fichiers ont changé.
5. Règle d'or : **un fait n'existe que s'il est écrit ici ou dans `docs/06`**.
   En cas de conflit entre ta mémoire de conversation et ce fichier, **ce fichier gagne**.

## 1. ÉTAT — où on s'est arrêté (màj : 08/09/2026, fin de message)

- **Fait à l'instant** : système de reprise créé (`REPRISE.md`) + bascule de priorité actée
  (dépôt = **thèse d'abord**, UPL = **base de données**). `README.md` et `docs/05` réécrits
  dans ce sens. Tests **39/39 verts**, commité + poussé sur `arena/01a08225-upl-gabon`.
- **Composition verrouillée** : jury simulé = Chabanne-Rive (Lyon) · Valax (Nice) ·
  Loufrani (Nice) — `docs/06`, passage n° 0 journalisé (3 × ⚠️).
- **Question en suspens** : GO du Président pour lancer le **passage jury n° 1 —
  fiche concept « gouvernance augmentée » (§ 3.2–3.3)** : définition 1 §, 4–6 attributs
  observables, 3 exclusions, 2 cas-limites tranchés, glossaire discipliné.
- **Aucun fichier à moitié écrit, aucun test rouge, dépôt propre.**

## 2. Priorités (décision du 08/09/2026 — prime sur tout le reste)

1. **Ce dépôt sert PRIORITAIREMENT la thèse** (DBA Serge Patrick MINANG, `these/`).
2. **UPL = BASE DE DONNÉES** : le site institutionnel reste en production (ne rien casser),
   et devient la **ressource documentaire de référence** au service de la thèse
   (connaissance du secteur EPES, contenus vérifiés, tarifs, contacts).
   La thèse **LIT** la base UPL ; elle ne la modifie **jamais** pour ses besoins propres.
3. Ordre de travail par défaut : thèse d'abord. UPL : maintenance + alimentation de la base.

## 3. Chantiers ouverts (jury — ordre = bloquants d'abord)

| # | Chantier | Statut | Verdicts R/V/L | Prochaine action |
|---|---|---|---|---|
| T1 | Fiche concept GA (§ 3.2–3.3) | ⏳ en attente GO | — | Rédiger + passage jury n° 1 |
| T2 | Protocole de cas (annexes C–D) + règle de saturation | 🔴 non démarré | Loufrani ❌ potentiel | Cadrer après T1 |
| T3 | Typologie des usages IA (tab. 5.3) + grille d'observation | 🔴 non démarré | Exigence permanente n° 3 | Cadrer après T1 |
| T4 | 4e regard expert IA (chap. 5) | 📌 rappel | — | Le moment venu → identifier un nom |
| U1 | Maintenance site UPL / base de données | 🟢 continu | — | `npm run test:upl` avant toute livraison |

## 4. Décisions verrouillées (ne pas rouvrir sans GO explicite)

- D1. Zone `these/` : indépendance totale (aucun asset UPL, charte propre, `noindex`,
  hors sitemap/nav UPL, accès `/these/`). Ponts autorisés UNIQUEMENT : `../index.html`,
  `../contact.html`, `mailto:contact@upl-gabon.com?subject=Recherche doctorale`.
- D2. Confidentialité terrain : codes **EPES-A à EPES-E** en public ; noms pressentis,
  correspondances, consentements, enregistrements : **jamais sur le site ni dans Git**.
- D3. Jury simulé = Chabanne-Rive · Valax · Loufrani (simulation interne, non-implication
  explicite). 1 × ❌ = reprise exigée. 10 exigences conjointes (`docs/06`).
- D4. Rien d'inventé : pas d'université d'inscription, directeur, date de soutenance,
  mail, tarif ou partenaire supposés. Tout contenu thèse vient des documents de l'auteur.
- D5. Dossier Matrix Group R+2 = chantier UPL, **pas** la thèse (exclu de `these/`).
- D6. Fichiers partagés (`package.json`, `netlify.toml`, `HANDOVER.md`, `README.md`,
  `REPRISE.md`) : une piste à la fois, `npm test` complet avant merge. Jamais de push sur `main`.

## 5. Règles express (rappel sec)

- Parler français. Ton : factuel, sobre ; jamais défensif, jamais de promesse.
- Tests : `npm run test:these` (9) / `npm run test:upl` (30) / `npm test` (39) — Node ≥ 18.
- Aperçu local : `npm run serve` → `/` (UPL) et `/these/` (thèse).
- Serveur de démo éventuel : binder `0.0.0.0`, jamais `localhost` côté navigateur.
- Termes bannis dans le HTML (tests) : voir `tests/site.test.mjs` + `tests/these.test.mjs`.
- Validation : thèse → auteur ; action publique UPL → Président.

## 6. Journal des échanges (bref — derniers en haut)

- **08/09/2026 (PM)** : système de reprise (`REPRISE.md` + protocole § 0) + bascule
  priorité thèse / UPL = base de données (`README.md`, `docs/05` réécrits). 39/39, poussé.
- **08/09/2026 (PM)** : jury recomposé Rive/Valax/Loufrani + annexe « oxymore ou slogan /
  § 3.3 décisive » (`docs/06` réécrit). Proposition passage n° 1 (fiche concept GA).
- **08/09/2026 (PM)** : jury initial Pesqueux/Giordano/Dejoux + critique + explication/critique
  de la thèse en conversation.
- **08/09/2026 (PM)** : double piste outillée (`tests/these.test.mjs`, `these/README.md`,
  `docs/05`, scripts `test:upl`/`test:these`). 39/39.
- **08/09/2026 (PM)** : zone `these/` créée (4 pages FR + CSS/JS autonomes, `noindex`)
  depuis le Drive « Thèse president privé » (plan harmonisé + liste 27 tab./13 fig.).
  Dossier Matrix exclu (chantier bâtiment, pas thèse).
