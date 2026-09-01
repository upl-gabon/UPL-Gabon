# État des comptes UPL — 1er septembre 2026

**Statut : procédure interne — ne pas merger sur `main`.** Registre des comptes : c'est **ici**
qu'on note l'URL officielle, les admins et le statut de chaque compte. **Jamais de mot de passe,
jamais de code de secours dans ce fichier** (coffre + enveloppe au secrétariat).

Constat établi depuis l'écran du secrétariat (onglets ouverts le 01/09/2026) : un compte Google
« ordinaire » au nom de l'école, un profil LinkedIn d'administration, un compte Facebook de gestion,
des comptes TikTok / Instagram en cours, la Page Facebook de 2022 (~500 abonnés), GitHub, Netlify.

---

## 1. Registre

| Plateforme | Objet constaté | Rôle | E-mail du compte | Admins | Bios | Statut |
|---|---|---|---|---|---|---|
| **Google** | compte UPL (Gmail + Drive « UPL – Administration » + fiche d'établissement à claimer) | outil de travail, annuaire, YouTube, Drive | adresse de l'école | **1 seul — à corriger** | § 4.7 | **à sécuriser** |
| **Facebook — Page** | « Université Privée de Libreville », ≈ 500 abonnés, créée 2022 | **la vitrine officielle** | à vérifier (A/B/C de `FACEBOOK_PAGE_500.md`) | agence ? inconnu | § 4.1 | **à reprendre** |
| **Facebook — compte de gestion** | `profile.php?id=61593884705328`, affiché « Universiteprivee Libreville » | administrer la Page, ne pas publier en son nom | adresse de l'école | 1 | — | **à aligner** (nom = personne réelle du secrétariat) |
| **Instagram** | compte ouvert, non animé | vitrine jeunes + visuels | adresse de l'école | 1 | § 4.2 | **à remplir** |
| **TikTok** | handle affiché « Upl-gabon (@upl… » — handle exact à confirmer | bacheliers | adresse de l'école | 1 | § 4.3 | **à confirmer + à remplir** |
| **LinkedIn — profil** | `linkedin.com/in/upl-contact-9ab981432`, titre « Programme universitaire chez Université Privée de Libreville (UPL) » | outil de travail, réponse aux cadres | adresse de l'école | 1 | § 4.4 (titre) | **titre + URL à corriger** |
| **LinkedIn — Page entreprise** | « Université Privée de Libreville (UPL) » existe (page payée 2022 ?) | vitrine cadres / entreprises | à confirmer | inconnu | § 4.4 | **à réclamer** |
| **YouTube** | handle `@UPL` **appartient à un tiers** ; les deux films TV sont en ligne sur une chaîne à identifier | bibliothèque des films | — | — | § 4.6 | **off** (rien à publier tant que `@UPLGabon` n'est pas créé) |
| **WhatsApp Business** | numéro du Président, en service | hub des leads | — | Président | § 4.5 | **fiche à aligner** |
| **X (Twitter)** | handle `@uplgabon` à réserver seulement | — | — | — | § 4.8 | **off** |
| **GitHub** | org `upl-gabon`, repo `UPL-Gabon` (site + docs) | code du site | à basculer sur l'adresse de l'école | à vérifier | — | **repo à passer privé** |
| **Netlify / Namecheap** | déploiement de secours + domaine + boîte `contact@` | technique, **MX à ne pas toucher** | adresse de l'école | 1-2 | — | **2ᵉ admin à ajouter** |

---

## 2. Trois corrections à faire tout de suite (hors contenu)

1. **Un second administrateur UPL partout** (Google, Meta, TikTok, LinkedIn, GitHub, Netlify, Namecheap).
   Aujourd'hui, chaque compte ne tient qu'à une seule personne : c'est exactement ce qui a produit
   les pages bloquées de 2022-2024.
2. **2FA par application d'authentification**, installée sur un **téléphone de l'école** (pas le numéro
   personnel d'un appui), codes de secours imprimés et sous enveloppe au secrétariat.
3. **Le compte de gestion Facebook change d'identité** : le nom d'un profil doit être une personne
   réelle. Le profil s'appelle (par exemple) « Secrétariat UPL » côté affichage famille, **la Page**
   porte le nom de l'institution. Le compte Google suit la même logique : nom de l'institution,
   pas une personne inventée.

## 3. Ordre de marche (une semaine, sans publier quoi que ce soit avant la fin)

| Jour | Gestes |
|---|---|
| **J1** | registre complété (URL exactes, e-mails, admins) ; second admin sur Google + Meta ; 2FA |
| **J2** | réclamation de la Page Facebook de 2022 et de la Page LinkedIn (pièces : facture agence, pièce du Président, document d'existence, captures) |
| **J3** | bios collées sur les comptes **déjà** sous contrôle (Instagram, TikTok, WhatsApp, LinkedIn — § 4 de `BIOS_RESEAUX_2026.md`), logo en avatar, lien `upl-gabon.com` |
| **J4** | pièce P11 (bios) + P12 (pont Facebook) validées par écrit par le Président |
| **J5** | `config.js` : URL + `status: "live"` des réseaux finis, `showSocialLinks = true`, `npm test`, mise en ligne |
| **J6-J7** | publication épinglée P1 sur chaque réseau prêt, puis premier post du kit ; réponses aux commentaires |

**Règle :** le site ne montre que ce qui est fini. Un réseau en cours de reprise reste `pending` :
il n'apparaît ni dans le pied de page ni dans la page Contact, et il n'y a pas d'encart vide.

## 4. Ce qui bloque encore (et qui n'empêche pas les bios)

- date de rentrée réelle (aucune communication d'une date inventée) ;
- photos réelles du campus et du Président (upload web GitHub, puis `git pull`) ;
- échéancier exact des tranches hors MBA ;
- facture / nom de l'agence qui a créé les pages de 2022 (nécessaire pour la réclamation) ;
- décision « passation » du repo : le rendre **privé** (documents internes présents).

## 5. À ne pas confondre (rappel)

| « UPL » désigne aussi | Comment on se distingue |
|---|---|
| Université Protestante de **Lubumbashi** (RDC) — « Officiel UPL » sur Facebook / Instagram | tous nos identifiants portent **Gabon / Libreville / upl-gabon.com** |
| **UPL Limited** (groupe indien, agrochimie) — `upl.com` / `upl-ltd.com`, ≈ 770 000 abonnés Facebook | on n'utilise **jamais** `upl.com` dans une bio, un lien ou un mail |
| tout compte au handle `@UPL` seul (YouTube, X) | nos handles : `uplgabon`, `upl.gabon`, `UPLGabon` |
