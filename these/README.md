# Piste THÈSE — zone indépendante `these/`

**Recherche doctorale (DBA) de Serge Patrick MINANG** : gouvernance augmentée des EPES gabonais,
articulation IA × intelligence émotionnelle. Travail en cours (septembre 2026).

Cette zone est un **site personnel de recherche**, distinct du site institutionnel de l'UPL.
Elle vit dans le même dépôt (même hébergement) mais **ne partage rien** : ni header, ni styles,
ni scripts, ni navigation.

## Règles non négociables

1. **Indépendance totale** — aucun `../assets/`, aucun `config.js` / `include.js` / `main.js` / `effects.js`
   UPL, aucun logo UPL, ni bleu `#0B2A5B` ni or `#C9A227`. Charte propre : encre + bronze + papier.
2. **Discrétion** — `noindex` sur chaque page, hors sitemap, hors menu UPL. Accès par lien direct `/these/`.
   Le site UPL ne doit jamais pointer vers `these/` (test de discrétion croisée).
3. **Ponts autorisés UNIQUEMENT** (verrouillés par les tests) :
   - liens `../index.html` et `../contact.html` (retour discret vers l'UPL) ;
   - `mailto:contact@upl-gabon.com` avec objet « Recherche doctorale » — **aucun mail inventé**.
4. **Confidentialité du terrain** — version publique sous codes **EPES-A à EPES-E** uniquement.
   Noms d'établissements pressentis, correspondances nominatives, consentements, enregistrements :
   **jamais sur le site** (ni dans `these/`, ni ailleurs). Testés automatiquement.
5. **Rien d'inventé** — tout contenu vient des documents de l'auteur (plan harmonisé, liste des supports).
   Pas d'université d'inscription, pas de directeur, pas de date de soutenance supposés.

## Structure

```
these/
├── index.html       Accueil : titre, question centrale, QR1–QR4, P1–P7, méthode, auteur
├── plan.html        Plan général harmonisé (3 parties, 6 chapitres, conclusion, annexes A–K)
├── supports.html    27 tableaux + 13 figures (intitulés provisoires, septembre 2026)
├── documents.html   Documents de travail, régime de confidentialité, demande d'accès
├── style.css        ★ Styles PROPRES (aucune dépendance vers assets/css/main.css)
├── app.js           ★ Script PROPRE : nav mobile, année, bandeau d'échanges indépendant
└── README.md        Ce fichier (règles de la piste thèse)
```

## Commandes

```bash
npm run test:these   # 9 tests de la piste thèse — OBLIGATOIRE avant toute livraison thèse
npm test             # les deux pistes (UPL + thèse) — OBLIGATOIRE avant merge
npm run serve        # aperçu local → http://127.0.0.1:5173/these/
```

## Ajouter une page thèse (checklist)

1. Copier le header/footer/nav d'une page existante (pas ceux de l'UPL).
2. `<meta name="robots" content="noindex, nofollow">` obligatoire.
3. `<div data-action-band></div>` avant `</main>` (rendu par `app.js`).
4. `<script src="app.js"></script>` + `<link rel="stylesheet" href="style.css">` uniquement.
5. Ajouter le lien dans la nav des 4 (+1) pages.
6. `npm run test:these` vert (puis `npm test` complet).

## Validation

Tout livrable thèse passe le **jury simulé** (`docs/06_JURY_SIMULE_THESE.md` — Chabanne-Rive ·
Valax · Loufrani) : un seul ❌ = reprise exigée. Puis validation finale de l'auteur
(Serge Patrick MINANG).
En cas de doute entre « UPL » et « thèse » : relire `docs/05_DOUBLE_CHANTIER_UPL_THESE.md`.
