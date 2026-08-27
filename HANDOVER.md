# HANDOVER UPL — Site web & GitHub

**À lire en premier** si vous êtes une IA, un développeur, ou un collaborateur autorisé par le Président.

**Autorisation :** on suppose que le lecteur a l’accord de **Serge Patrick MINANG**, Président-Fondateur de l’UPL, pour intervenir sur le site / le dépôt.

**Date de ce handover :** 27 août 2026  
**Aide digital été 2026 (urgence only, non permanent) :** Calvin Blanchard MINANG — +33 7 52 97 58 09  

---

## 1. Qu’est-ce que l’UPL (fait)

| | |
|---|---|
| Nom | Université Privée de Libreville (UPL) |
| Activité ouverte sur le site | **Executive MBA uniquement** (depuis 2022) |
| Partenaire MBA | Université de Douala |
| ~80 cadres formés | Ordre de grandeur historique MBA |
| Scolarité MBA | 4 000 000 FCFA |
| Siège | Sablière, Libreville (face Résidence Amb. Arabie Saoudite) |
| Président | Serge Patrick MINANG |
| Domaine | `upl-gabon.com` (Namecheap) |
| Mail pro | `contact@upl-gabon.com` (PrivateEmail / Namecheap) — **actif** |
| Charte | Bleu `#0B2A5B` · Or `#C9A227` · Blanc · rendu institution / grande école |

### Contacts téléphoniques

| Usage | Numéro |
|---|---|
| UPL institution | **+241 02 62 19 78** · **+241 07 35 95 72** |
| Présidence / secrétariat (Président & épouse) | **+241 05 01 56 20** |
| Calvin (urgence digital été 2026 **only**) | +33 7 52 97 58 09 — **ne pas mettre en permanent sur le site public** |

### Ce qui n’est PAS vrai / PAS à publier

- Licences, masters, CPGE, DBA comme **offres ouvertes** (projets possibles seulement)
- Partenariats HEC / Polytechnique / Sciences Po / etc. **non signés**
- Mails inventés (`admissions@`, `partenariats@`) tant qu’ils n’existent pas
- Calvin comme contact public institutionnel permanent

---

## 2. Stack technique du site

```
upl-web/
├── index.html          Accueil type grande école
├── mba.html            Fiche Executive MBA
├── a-propos.html       Institution + limites éditoriales
├── contact.html        Tél + contact@ + formulaire mailto
├── assets/
│   ├── css/main.css    Charte + layout
│   ├── img/            logo-upl.png, illustration campus
│   └── js/
│       ├── config.js   ★ SOURCE DE VÉRITÉ contacts / flags / programmes
│       ├── include.js  Header / footer
│       └── main.js     Nav, formulaire
├── tests/
│   └── site.test.mjs   Tests de stabilité (Node)
├── docs/               Décisions domaine, Netlify, GitHub, vision
├── HANDOVER.md         Ce fichier
├── package.json
└── netlify.toml
```

- **Pas de framework** (HTML/CSS/JS) — reprise facile, Netlify Drop OK  
- Config centralisée : **`assets/js/config.js`**  
- Feature flags : `features.showMultiFilieres`, etc. — tout à `false` sauf MBA  

### Architecture multi-université (future)

Dans `config.js` : tableaux `schools[]` et `programmes[]` avec `schoolId` + `status` (`open` | `project` | `planned`).  
Quand une nouvelle école/filière est **réellement** ouverte : ajouter une entrée `status: "open"` et une page — **ne pas inventer**.

---

## 3. Créer GitHub très vite (compte UPL)

### Objectif
Repo **privé** propriété UPL, pour reprise humaine **ou** IA, sans dépendre du seul Gmail de Calvin.

### Étapes (compte `contact@upl-gabon.com`)

1. Ouvrir https://github.com/signup  
2. Email : **`contact@upl-gabon.com`** (valider via PrivateEmail)  
3. Username suggéré : `upl-gabon`  
4. Activer **2FA** (application TOTP — pas SMS si numéro Google bloqué)  
5. (Recommandé) Créer une **Organization** `upl-gabon`  
6. New repository **private** : `site-web`  
7. Inviter en **Admin** le compte GitHub de Calvin (Gmail `blanchardminang00@gmail.com`)  
8. En local :

```bash
cd upl-web
git remote add origin git@github.com:upl-gabon/site-web.git
# ou https://github.com/upl-gabon/site-web.git
git branch -M main
git push -u origin main
```

9. Netlify → Import from Git → publish directory = `/` (racine avec index.html)  
10. **Ne pas supprimer** l’ancien deploy Netlify tant que le définitif n’est pas validé  

### Plan B si signup refuse contact@
- Compte avec Gmail Calvin  
- Créer **Organization** `upl-gabon` (le code vit dans l’org)  
- Ajouter `contact@upl-gabon.com` comme email vérifié  
- Documenter : compte de service UPL, autorisé par le Président  

### Secrets / ownership
- 2 admins minimum (UPL mail + Calvin)  
- Jamais un prestataire seul owner  
- Tokens GitHub / Netlify dans un coffre (pas dans le repo)  

---

## 4. Tests de stabilité (obligatoires avant merge / deploy)

```bash
cd upl-web
npm test
```

Les tests vérifient notamment :
- Pages requises présentes  
- Charte couleurs dans le CSS  
- `contact@upl-gabon.com` présent  
- Téléphones UPL + présidence présents sur contact  
- **Absence** de fausses offres (Licence 1, CPGE comme programme, six filières…)  
- **Absence** de mails inventés  
- Calvin **pas** affiché en contact public permanent dans le HTML  
- Scripts config / include / main cohérents  
- `netlify.toml` publish = `.`  

Ajouter des tests si vous ajoutez une page.

---

## 5. Règles éditoriales (non négociables)

1. MBA = seul programme `open` jusqu’à décision contraire du Président  
2. Pas de logo partenaire non contractuel  
3. Ton : grande école sobre + usage africain (mobile, clarté) — pas template IA générique  
4. Paiements futurs : **Moov Money / Airtel Money d’abord**  
5. Dossier bancaire Ecobank ≠ pages marketing partenaires France (ne pas mélanger)  

---

## 6. Commandes utiles

```bash
# local
npm run serve
# → http://127.0.0.1:5173

# tests
npm test

# zip livraison
# (depuis le parent) zip -r UPL_Site_Web_v1.zip upl-web -x "upl-web/.git/*"
```

---

## 7. Docs liées

| Fichier | Sujet |
|---|---|
| `docs/00_DECISION_DOMAINE_MAIL_HEBERGEMENT.md` | Domaine / mail / host |
| `docs/01_DEPLOIEMENT_NETLIFY_NAMECHEAP.md` | Brancher www sans casser MX |
| `docs/02_GITHUB_ET_VISION_SITE.md` | GitHub + vision produit |
| `docs/03_CREATE_GITHUB_NOW.md` | Checklist création compte 10 min |

---

## 8. Message d’init pour une IA

```
Tu reprends le site UPL (Université Privée de Libreville).
Lis HANDOVER.md et assets/js/config.js en premier.
Autorisation Président supposée.
MBA seul programme ouvert. contact@upl-gabon.com actif.
Charte #0B2A5B / #C9A227. Ne supprime pas Netlify existant.
Lance npm test avant de livrer. Ne publie pas de filières projet.
Calvin = urgence été 2026 only, pas contact public permanent.
Téléphones : UPL +241 02 62 19 78 / +241 07 35 95 72 ;
présidence +241 05 01 56 20.
Tâche demandée : […]
```

---

## 9. Lien dossier bancaire (contexte séparé)

Package crédit Ecobank : `/home/user/UPL_Dossier_Ecobank_V12/`  
Handover bancaire : `0_HANDOVER_Reprise_Contexte_UPL_Ecobank.pdf`  
**Ne pas fusionner** le pitch crédit 80 M et le site grand public partenaires.

---

*Fin HANDOVER — UPL site-web*

---

## 10. Journal des mises à jour

**27/08/2026 — structuration du dépôt `upl-gabon/UPL-Gabon` (agent Arena)**
- Code du site extrait du zip **à la racine** du dépôt (fini le zip versionné) — `index.html` à la racine.
- Ajouts pro passation : `README.md` complet, `.editorconfig`, CI **GitHub Actions** (`.github/workflows/tests.yml` → `npm test` sur chaque push/PR).
- Publication **GitHub Pages** activée (préview) ; guide de branchement du domaine officiel **sans casser le mail** : `docs/04_PUBLICATION_GITHUB_PAGES_NAMECHEAP.md`.
- `netlify.toml` conservé ; déploiement Netlify existant **non touché**.
- `npm test` : 13/13 ✅.
- Dépôt recommandé **privé** (documents internes présents) — voir `docs/04` § Confidentialité.
