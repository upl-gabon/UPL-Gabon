# UPL — Site institutionnel

**Université Privée de Libreville** — Sablière, Libreville (Gabon)
Domaine officiel : `upl-gabon.com` · Mail : `contact@upl-gabon.com` (actif — ne pas casser les MX)

**Lire d'abord :** [`HANDOVER.md`](./HANDOVER.md) — passation complète (contexte, règles éditoriales, déploiement, contacts).

## En 30 secondes

- Site **statique** HTML/CSS/JS — zéro framework, zéro dépendance, reprise facile
- Offre publique : **Executive MBA uniquement** (partenaire : Université de Douala)
- Charte : bleu `#0B2A5B` · or `#C9A227` · blanc — rendu « grande école »
- **Config centrale** : `assets/js/config.js` — contacts, feature flags, programmes (architecture multi-université prête)
- Hébergement : **GitHub Pages** (branche de travail) — Netlify existant conservé en secours, non supprimé

## Démarrage

```bash
npm test          # 23 tests de stabilité — OBLIGATOIRE avant toute livraison
npm run serve     # serveur local → http://127.0.0.1:5173
```

Aucun `npm install` nécessaire (aucune dépendance).

## Structure

```
├── index.html            Accueil (type grande école)
├── mba.html              Fiche Executive MBA
├── a-propos.html         Institution + vision + direction
├── president.html        Mot du Président (Serge Patrick MINANG)
├── contact.html          Téléphones + contact@ + formulaire (mailto)
├── assets/
│   ├── css/main.css      Charte bleu/or + layout
│   ├── img/              logo-upl.png, illustration campus
│   └── js/
│       ├── config.js     ★ SOURCE DE VÉRITÉ (contacts, flags, programmes)
│       ├── include.js    Header / footer injectés
│       └── main.js       Nav, formulaire
├── tests/site.test.mjs   23 tests de stabilité (Node ≥ 18)
├── docs/                 Décisions & guides (domaine, DNS, GitHub, com)
├── HANDOVER.md           ★ Passation — à lire en premier
└── netlify.toml          Config Netlify conservée (publish = ".")
```

## Publication

| Cible | État |
|---|---|
| Prévisualisation / dépôt | GitHub Pages — voir `docs/04_PUBLICATION_GITHUB_PAGES_NAMECHEAP.md` |
| Domaine officiel `upl-gabon.com` | Branchement DNS Namecheap à faire côté UPL — guide : `docs/04` (⚠️ ne pas toucher aux MX mail) |
| Netlify (secours) | Déploiement existant conservé tant que le définitif n'est pas validé |

## Workflow de contribution (passation)

1. Créer une branche depuis `main`, travailler, **`npm test` vert**
2. Ouvrir une **Pull Request** vers `main` — jamais de push direct sur `main`
3. Revue + merge
4. CI (recommandé) : activer `docs/templates/ci-tests.yml.template` (voir le fichier, 1 minute) pour relancer les tests automatiquement à chaque PR
5. Toute action publique (mise en ligne, annonce partenaire, nouvelle filière) reste soumise à **validation du Président**

## Règles non négociables

- **MBA = seul programme ouvert** affiché — pas de filière « projet » publiée
- Pas de logo/partenariat non contractuel (HEC, Polytechnique, etc.)
- Pas de mail inventé (`admissions@`, `partenariats@`…)
- Calvin = appui digital été 2026 **urgence only** — jamais en contact public permanent
- Dossier bancaire Ecobank ≠ site public (ne jamais fusionner, ne jamais parler du Maroc)

© Université Privée de Libreville — SAS, Libreville (Gabon)
