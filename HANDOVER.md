# HANDOVER UPL — Site web & GitHub

**À lire en premier** si vous êtes une IA, un développeur, ou un collaborateur autorisé par le Président.

**Autorisation :** on suppose que le lecteur a l’accord de **Serge Patrick MINANG**, Président-Fondateur de l’UPL, pour intervenir sur le site / le dépôt.

**Date de ce handover :** 27 août 2026  
**Aide digital été 2026 (urgence only, non permanent) :** Calvin Blanchard MINANG — +33 7 52 97 58 09  


---

## ⭐ ÉTAT DE LIVRAISON — v2.6 (27/08/2026, fin de session)

**Livré et testé (28 tests verts)** : site bilingue FR/EN (10 pages) · offre officielle 2026-2027 en
palier 1 « pré-inscriptions » (tarifs verrouillés) · MBA ouvert (4 M, jusqu’à 8 échéances) · vidéos TV
(autoplay accueil + interview MBA) · ticker à la une + citations de management · trajectoire éditoriale
animée + pluie dorée discrète sur toutes les pages · mot du Président · bandeau d’action
(candidature / RDV / partenariat) · paiements Airtel Money + justificatif/confirmation UPL ·
SEO (JSON-LD, robots, sitemap) · CI en template (`docs/templates/`).

**Reste à faire (côté Président/Calvin)** :
1. Mettre le dépôt **privé** (Settings → General → Danger Zone) — documents internes présents.
2. Merger la PR #1 sur `main` puis activer **GitHub Pages** (Settings → Pages → main / root).
3. DNS Namecheap → `upl-gabon.com` (guide : `docs/04_…`) — sans toucher aux MX.
4. Fournir : photos réelles (upload GitHub web), échéancier exact des tranches, date de rentrée,
   photo du Président, validation du Mot du Président.

**Pour une nouvelle session Arena** : ouvrir ce dépôt, lire ce fichier + `config.js`,
coller le message d’init du § 8. Toute l’historique des décisions est dans le journal (§ 10).

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

1. Rentrée 2026-2027 — décision du Président (27/08) : offre ouverte Licence, Master, CPGE, Executive MBA, DBA (supports officiels : roll-up + fiche des frais) ; l'Executive MBA reste le programme historique depuis 2022
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

## 8. Message d’init pour une IA (à jour — 27/08/2026, v2.6)

```
Tu reprends le site UPL (Université Privée de Libreville).
Dépôt : github.com/upl-gabon/UPL-Gabon — lis HANDOVER.md + assets/js/config.js en premier.
Autorisation du Président Serge Patrick MINANG supposée. contact@upl-gabon.com actif.
Charte #0B2A5B / #C9A227. Site bilingue FR (racine) / EN (dossier en/).
Offre affichée (supports officiels 2026-2027) : Licence, Master, CPGE, Executive MBA (ouvert
depuis 2022), DBA — en PALIER 1 « pré-inscriptions » (pas d’encaissement promis en ligne).
Tarifs officiels VERROUILLÉS par les tests — ne jamais modifier un chiffre sans consigne Président.
Rentrée 2026-2027 réelle ouverte au public = bascule palier 2 « inscriptions ouvertes »
(voir journal v2.2/v2.3). Ne jamais réintroduire de tournures défensives (liste noire des tests).
Ton : factuel, pro, jamais défensif ; pas de campus fictif, pas de promesse, pas de « Maroc ».
Lance npm test (28 tests) avant toute livraison. Bascule de langue FR/EN dans le header.
Calvin = urgence digitale été 2026 only, pas contact public permanent.
Téléphones : UPL +241 02 62 19 78 / +241 07 35 95 72 ; présidence +241 05 01 56 20.
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

**27/08/2026 (16) — lancement com rentrée (site inchangé)**
- Site **non modifié**. Kit `docs/com/` : WhatsApp Président = hub ; pages Facebook/LinkedIn **déjà payées** à réclamer (pas à nier) ; campagne = post épinglé + événement 2026-2027 sur la page mère.
- **Ne pas merger `docs/com/` sur `main`**. Aucune publication sans VALIDÉ Président.

**27/08/2026 (15) — v2.5 « ton assumé, fini l'autodéfense » (retour Président)**
- Phrase signalée (« les ouvertures seront annoncées… quand elles seront réelles ») et toutes ses sœurs supprimées : la note du chapitre, le jalon +1, la chute de la trajectoire, le paragraphe vision d'À propos et le mot du Président (FR + EN).
- Remplaçants : tournures prospectives et factuelles — « la prochaine campagne d'inscription sera confirmée par communiqué officiel », « à chaque rentrée », valeurs Excellence/Innovation/Leadership en clôture du mot du Président.
- Ces formulations défensives sont désormais **interdites par les tests** (liste noire étendue).
- Tests 28/28.

**27/08/2026 (14) — v2.4 « hero élargi + cache-busting » (retour preview Président)**
- Bug signalé : titre du hero écrasé en colonne gauche — cause : `max-width: 14ch` conçu pour l'ancien titre long. Corrigé (pleine largeur + `text-wrap: balance`), lead élargi à 40 rem.
- Le « fond campus » aperçu dans la capture = **ancienne illustration supprimée restée dans le cache navigateur** (aucune trace dans le code, aucun commit externe). Remède : **cache-busting** `?v=20260827b` sur CSS/JS des 10 pages — les mises à jour se voient immédiatement après refresh simple.
- Tests 28/28.

**27/08/2026 (13) — v2.3 « palier 1 : pré-inscriptions » (arbitrage Calvin/Président)**
- Débat : com immédiate (Président) vs attendre les partenaires (Calvin — « rien de réel à cette heure »). Arbitrage retenu : **communiquer maintenant, promettre moins** — le site passe en **« pré-inscriptions 2026-2027 »** (collecte de contacts, gratuit, sans engagement, rappel par le service des admissions) au lieu d'« inscriptions ouvertes ».
- Tarifs officiels conservés à l'affichage (décidés, factuels) ; MBA inchangé (réellement ouvert depuis 2022).
- `config.js` : statut des nouveaux programmes = `preopen` (MBA reste `open`).
- **Bascule palier 2 (« inscriptions ouvertes »)** : 1 commit, dès que les 3 verrous sont levés — autorisation ministérielle des filières, partenariats/corps enseignant, capacité d'accueil. La v2.2 est l'état cible.
- Tests 28/28 (CTA et kicker pré-inscriptions verrouillés).

**27/08/2026 (12) — v2.2 « offre officielle 2026-2027 en ligne » (PIVOT validé par les supports du Président)**
- Les roll-up/fiches officiels UPL (« Inscriptions ouvertes 2026-2027 », fiche des frais) **supersèdent** la règle « MBA seul » : l'accueil affiche la **vraie offre chiffrée** — Licence 1 (1 000 000 / 50 premières · 1 200 000 / normales), Master 1 (1 500 000), Master 2 (2 000 000), CPGE (2 200 000), Executive MBA (4 000 000), DBA (sur dossier).
- Frais d'inscription L1 : 200 000 / 300 000 exigibles au dépôt du dossier, solde en 6 tranches ; reçu pour tout paiement ; places limitées ; échéancier conditionne la validation administrative.
- Cinq pôles affichés + CPGE ; `config.js` (programmes[], schools[]) = source de vérité mise à jour.
- MBA : « jusqu'à huit échéances » (note officielle 04/07/2026).
- Bloc « Et demain » remplacé par l'offre réelle ; a-propos, ticker et communiqué alignés (FR/EN).
- Tests réécrits : **tarifs officiels verrouillés** (toute divergence de chiffre casse la CI). 28/28.
- Photos campus (9 WhatsApp) : toujours bloquées côté sandbox (pièces jointes non persistées ; Drive inaccessible en binaire). Chemin fiable : upload web GitHub puis `git pull`.

**27/08/2026 (11) — v2.1 « trajectoire : format éditorial » (retours Président : « fait trop IA »)**
- Ligne du temps à cartes symétriques **remplacée** par un **chapitre éditorial de rapport annuel** : fond bleu pleine page, colonne gauche sticky (chapeau au trait d'or qui se dessine, titre), chronologie en **grands chiffres serif dorés** (2022 · ≈ 80 · 17h · +1) séparés par des filets fins — plus aucune carte, plus aucun arrangement symétrique de template.
- Typographie éditoriale étendue : `Georgia/serif` sur le H1 du hero, la citation et les chiffres de la trajectoire (police système, zéro dépendance).
- La révélation au scroll et les garde-fous d'accessibilité sont conservés ; tests 28/28.

**27/08/2026 (10) — v2.0 « animation sobre : la trajectoire » (retours Président)**
- Arbitrage Président/agent : **panthère et pluie d'or écartées** (risque kitsch face aux universités prestigieuses) ; retenues deux animations uniques mais dignes :
  1. **Poussière d'or du hero** (`assets/js/effects.js`, canvas) : 26 particules dorées lentes, scintillement discret. Garde-fous : coupée si `prefers-reduced-motion`, en pause onglet masqué, canvas confiné au hero.
  2. **Ligne du temps « La trajectoire de l'UPL »** (accueil FR + EN) : chapeau de diplômé en trait doré qui se dessine (SVG stroke), ligne or qui se déploie, 5 jalons révélés au scroll (2022 → ≈80 cadres → aujourd'hui → en préparation → la vocation : référence du Gabon et d'Afrique centrale). IntersectionObserver + fallback sans JS visible + reduced-motion = statique.
- Le « lead académique » est exprimé par les faits de la timeline, jamais par un slogan.
- Tests portés à **28** (timeline FR/EN, garde-fous a11y).

**27/08/2026 (9) — v1.9 « push-to-action + bilingue FR/EN » (retours Président)**
- **Bandeau d'action standard** (`[data-action-band]`, injecté par include.js) sur les 10 pages : **Candidature MBA · Demander un rendez-vous · Partenariat** (mails pré-remplis) + lignes UPL. L'ancien CTA accueil remplacé.
- **Bilinguisme complet** : dossier `en/` = 5 pages miroir traduites (lang="en", data-base="../"), bascule **FR ⇄ EN** dans le header, `sitemap.xml` bilingue. Contenus dynamiques bilingues dans `config.js` (`titleEn/textEn/tagEn/dateEn`, `textEn/sourceEn`, citations = citations originales anglaises, `tickerExtra` objets {fr,en}) — en EN, un communiqué sans traduction est masqué (jamais de mélange de langues).
- **Demande de RDV** : mail pré-rempli objet « Demande de rendez-vous » / « Meeting request » (pas d'outil de planification encore).
- Rédaction à venir (attente fichiers réels, ne pas improviser) : **extrait de cours** (1 PDF choisi, accord des enseignants, pas de supports complets) — prévoir `assets/docs/`.
- Tests portés à **27** (pages EN câblées, config bilingue, bandeau sur toutes les pages, sitemap).

**27/08/2026 (8) — v1.8 « formations à venir — perche tendue, zéro maintenance » (retours Président)**
- Accueil : nouvelle section **« Et demain — D'autres formations en préparation »** : licences, masters et programmes spécialisés annoncés **sans date et sans promesse** (« chaque ouverture sera annoncée dès que les conditions pédagogiques et réglementaires seront réunies »). Deux CTA : étudiants/pros → abonnement lettre d'information ; entreprises/institutions → partenariat.
- a-propos : vision alignée (formations en préparation, annonce à l'ouverture effective).
- **Bloc volontairement evergreen** : aucune mise à jour quotidienne nécessaire. Le jour où une formation ouvre réellement : `config.js → programmes[] → status: "open"` + page dédiée + retirer du bloc « en préparation ».
- Tests portés à **23** (garde-fou : aucune date d'ouverture inventée).

**27/08/2026 (7) — v1.7 « vidéo TV en autoplay + interview sur le MBA » (retours Président)**
- **Vidéo « Rentrée 2024 » supprimée** du site et de `config.media` (sur demande du Président).
- Accueil : section **« Replay — L'UPL à la télévision »**, lecteur BFM-style : **démarrage automatique muet** (`autoplay=1&mute=1`, la seule méthode sans erreur d'autoplay des navigateurs), note « son coupé par défaut », panneau bleu/or avec arguments factuels + CTA vers l'interview.
- Page MBA : nouvelle section **« Le MBA en images »** (`#en-savoir-plus`) avec **l'interview télévisée** (lecture au clic) + « Pourquoi ce programme marche » (5 arguments factuels).
- Tests portés à 22 (nouveau test vidéos : autoplay accueil, interview MBA, absence Rentrée 2024 partout).

**27/08/2026 (6) — v1.6 « ticker continu + paiement » (retours Président)**
- Bandeau « À la une » : **défilement continu type chaîne d'infos** (marquee CSS, pause au survol, statique si prefers-reduced-motion) — contenus = communiqués + infos pratiques (`config.js → tickerExtra`).
- Bandeau citation : **alterne citations de management et situations pratiques** (`config.js → paymentNotices`) : tranches, Airtel Money, justificatif + confirmation UPL.
- Règle d'inscription mise en avant (source Président) : **justification de paiement + confirmation UPL indispensables** — affichée sur MBA, contact et communiqué dédié. Paiement Airtel Money = via le processus du secrétariat (pas de paiement en ligne sur le site).
- **Parité EUR/FCFA retirée** (inutile pour un public gabonais) — repères : OHADA, CEMAC, cours du soir.
- Tests portés à **22**.

**27/08/2026 (5) — v1.5 « personnalisation Président + préparation SEO »**
- Nouvelle page **`president.html` — Mot du Président** (brouillon sobre et factuel rédigé par l'agent : conviction, chiffres réels, « programme après programme, critère : la réalité ») — **à valider/ajuster par le Président** avant mise en ligne définitive. Ajoutée à la nav + footer.
- **Compte à rebours de rentrée** prêt : `config.js → rentree: { date: "AAAA-MM-JJ" }` — caché tant que la date n'est pas confirmée (aucune date inventée). S'affiche sur la carte MBA de l'accueil (J-XX).
- **SEO** : JSON-LD `CollegeOrUniversity` (fiches enrichies Google), `robots.txt`, `sitemap.xml` (URLs upl-gabon.com — actives après branchement DNS).
- Tests portés à **21**.

**27/08/2026 (4) — v1.4 « site vivant, à l'image du Président »**
- Accueil : bandeau **« À la une »** (ticker) qui fait tourner les titres des communiqués ; **bandeau citation de management** (rotation aléatoire — Drucker, Ford, Mandela, Maxwell) + repères factuels (parité 655,957 FCFA/EUR BEAC, OHADA, CEMAC) ; section **Communiqués** rendue depuis `config.js` (`news: []` — le plus récent en premier, dates au mois, faits réels uniquement).
- Rotation désactivée si `prefers-reduced-motion` (accessibilité).
- a-propos : bloc **Direction** (Serge Patrick MINANG — Président-Fondateur, ingénieur, MBA, doctorant DBA) + **Liens utiles** : Université de Douala (partenaire MBA, univ-douala.com), ESSEC Douala (essec-douala.cm, école de gestion de l'Université de Douala), chaîne YouTube UPL.
- Pour actualiser l'école : éditer `assets/js/config.js` (news, quotes) — c'est la source de vérité. Un vrai flux temps réel (RSS/API) pourra être branché plus tard côté V2.
- Tests portés à **17**.

**27/08/2026 (3) — v1.3 « contenu réel » (retours Président)**
- Vidéos YouTube : lecture **intégrée dans la page** au clic (youtube-nocookie, bouton lecture + miniature).
- MBA : modules réels des promotions précédentes (droit des affaires, comptabilité OHADA, management stratégique, qualité, marketing, étude de cas) + **exemple d'emploi du temps 2025–2026** (cours du soir 17h–21h, séances de 4 h, module ≈ 20 h, Sablière) — sans noms d'enseignants (privé).
- Scolarité affichée **payable en tranches** (« 4 000 000 FCFA l'année, payable en tranches ») — échéancier réel détaillé remis par le secrétariat ; ne pas inventer de montants de tranches tant que le Président ne les a pas fournis.
- Contact : espace dédié « Vous êtes… » — candidature (envoi dossier par mail objet « Candidature MBA » ou dépôt au secrétariat), **demandes de partenariat** (objet « Partenariat »), **abonnement aux actualités** (objet « Abonnement »). Options ajoutées au formulaire.

**27/08/2026 (2) — v1.2 « sobre & factuel » (retours Président)**
- Suppression de tous les « signes IA » : plus de « grande école », « pas une coquille », « Preuve d'activité », « Comment on grandit », chips de composantes, roadmap paiement publique, mention Namecheap/PrivateEmail côté public.
- **Illustration de campus fictive supprimée** (repo + hero CSS) : l'UPL est à la Sablière — le site ne montre aucun campus irréaliste. Hero = bleu profond uni.
- Section **Médias** sur l'accueil avec les 3 vidéos officielles (Rentrée 2024, interview TV, présentation institutionnelle).
- a-propos recentré : institution + vision. Tests portés à **15** (ton factuel + vidéos).

**27/08/2026 — structuration du dépôt `upl-gabon/UPL-Gabon` (agent Arena)**
- Code du site extrait du zip **à la racine** du dépôt (fini le zip versionné) — `index.html` à la racine.
- CI **GitHub Actions** prête à activer : `docs/templates/ci-tests.yml.template` (`npm test` à chaque push/PR — 1 min par un admin, l'agent ne pouvant pas créer de workflows).
- Publication **GitHub Pages** préparée (à activer par un admin : Settings → Pages) ; guide de branchement du domaine officiel **sans casser le mail** : `docs/04_PUBLICATION_GITHUB_PAGES_NAMECHEAP.md`.
- `netlify.toml` conservé ; déploiement Netlify existant **non touché**.
- `npm test` : 13/13 ✅.
- Dépôt recommandé **privé** (documents internes présents) — voir `docs/04` § Confidentialité.
