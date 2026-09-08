# REPRISE — reprise instantanée (LIRE EN PREMIER)

> **Toute IA ouvrant une conversation sur ce dépôt commence ici.**
> Hypothèse par défaut : **la conversation précédente s'est arrêtée net** —
> ce fichier dit exactement où, et comment continuer.

## 0. Protocole obligatoire (chaque message, sans exception)

1. **Lire dans l'ordre** : ce fichier → `HANDOVER.md` (+ `README.md` si besoin).
   Vérifier `git log --oneline -5` et `git status`.
2. **Ouvrir ta réponse en disant EXACTEMENT où on s'est arrêté** (section 1).
3. **Continuer directement** le chantier (ton factuel, sobre ; rien d'inventé).
4. **À LA FIN DE CHAQUE MESSAGE : mettre à jour ce fichier**
   (État § 1, Chantiers § 2, Décisions § 3 si besoin, Journal § 5).
   Puis commiter + pusher si des fichiers ont changé.
5. Règle d'or : **un fait n'existe que s'il est écrit ici ou dans `HANDOVER.md`**.
   En cas de conflit entre ta mémoire de conversation et ce fichier, **ce fichier gagne**.

## 1. ÉTAT — où on s'est arrêté (màj : 08/09/2026, fin de message)

- **Fait à l'instant** : **dépôt UPL nettoyé** — la thèse a été extraite vers un dépôt
  séparé `these` (zip `these-SPM.zip` livré : site autonome, jury, reprise, tests 9/9).
  Supprimé ici : `these/`, `tests/these.test.mjs`, `docs/05_*`, `docs/06_*`.
  `README.md` recentré UPL, `package.json` : `npm test` = 30 tests site.
- **Ce dépôt = site UPL uniquement.** Ne jamais y recréer de contenu thèse.
  Thèse → dépôt `these` séparé (privé) ; jury et reprise thèse vivent là-bas.
- **En attente** : confirmation que le repo `these` est créé côté utilisateur.
  Chantiers UPL courants : mise en ligne (Pages/DNS, voir `HANDOVER.md`), com rentrée.
- **Tests 30/30 verts**, commité + poussé sur `arena/01a08225-upl-gabon`. Dépôt propre.

## 2. Chantiers ouverts (UPL)

| # | Chantier | Statut | Prochaine action |
|---|---|---|---|
| U1 | Maintenance site (contenus, tarifs, communiqués) | 🟢 continu | `npm test` avant toute livraison |
| U2 | Mise en ligne : Pages + DNS `upl-gabon.com` | ⏳ côté Président | Guide `docs/04` (ne pas toucher aux MX) |
| U3 | Com rentrée 2026-2027 | ⏳ validation Président | `docs/com/` (ne pas merger sur `main` sans GO) |

## 3. Décisions verrouillées (ne pas rouvrir sans GO explicite)

- D1. Offre affichée = supports officiels 2026-2027 ; tarifs verrouillés par les tests.
- D2. Pas de logo/partenariat non contractuel ; pas de mail inventé ;
  Calvin = urgence only (jamais en contact public).
- D3. Dossier bancaire Ecobank ≠ site public (ne jamais fusionner).
- D4. Thèse DBA = dépôt `these` séparé — **aucun contenu thèse ici** (ni pages, ni docs).
- D5. Jamais de push direct sur `main` (branche → PR → merge). `npm test` vert avant merge.

## 4. Règles express (rappel sec)

- Parler français. Ton : factuel, sobre ; jamais défensif, jamais de promesse.
- Tests : `npm test` (30 tests site) — Node ≥ 18. Aperçu : `npm run serve` → `/`.
- Termes bannis dans le HTML : voir `tests/site.test.mjs`.
- Validation : toute action publique → Président.

## 5. Journal (bref — derniers en haut)

- **08/09/2026 (PM)** : nettoyage UPL — `these/`, `tests/these.test.mjs`, `docs/05`,
  `docs/06` supprimés ; `README.md`/`package.json`/`REPRISE.md` recentrés UPL. 30/30, poussé.
- **08/09/2026 (PM)** : zip `these-SPM.zip` livré (dépôt autonome : site racine, liens
  absolus, jury Rive/Valax/Loufrani, reprise, tests 9/9, guide de création).
- **08/09/2026 (PM)** : système de reprise + bascule priorité thèse (annulée par
  l'extraction : chaque dépôt a désormais sa reprise et sa priorité propres).
- **Antériorité** : zone `these/`, double piste, jury simulé — conçus ici le 08/09/2026
  puis **déménagés** dans le dépôt `these` (voir son `REPRISE.md`). Historique Git conservé.
