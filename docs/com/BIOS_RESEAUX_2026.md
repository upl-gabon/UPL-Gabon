# Bios officielles — réseaux UPL (campagne 2026-2027)

**Statut : procédure interne — ne pas merger sur `main`** (GitHub Pages publie la racine).

**Source de vérité des textes : `assets/js/config.js` → `social`.** Ce fichier est **généré** :
ne jamais retoucher un texte de bio ici. On corrige `config.js`, puis :

```bash
npm run bios:sync      # recale ce document sur config.js
npm test               # vérifie les compteurs et la liste noire
```

**Ordre de marche (décision du 01/09/2026) :**

```
① bio validée par écrit (pièce P11 de TEXTES_A_VALIDER.md)
   → ② bio collée sur le réseau + 2 admins UPL + e-mail contact@
      → ③ status "live" dans config.js  →  le réseau apparaît sur le site
```

Aucun réseau n'est ajouté au site avant l'étape ③. C'est ce qui évite la vitrine
à moitié remplie : le site affiche les comptes **finis**, pas les comptes en cours.

---

## 1. Identité commune — la même sur les 6 réseaux

| Champ | Valeur à utiliser |
|---|---|
| Nom d'établissement | **Université Privée de Libreville** |
| Forme courte admise | **Université Privée de Libreville (UPL)** — « UPL » seul = jamais |
| Identifiants visés | `@uplgabon` (Facebook, X) · `@upl.gabon` (Instagram, TikTok) · `/company/upl-gabon` (LinkedIn) · `@UPLGabon` (YouTube) |
| **Domaine** | **`upl-gabon.com`** — ⚠️ **jamais `upl.com`** (voir § 2) |
| E-mail de contact + e-mail du compte | `contact@upl-gabon.com` |
| Téléphones | `+241 02 62 19 78` · `+241 07 35 95 72` |
| Présidence / secrétariat | `+241 05 01 56 20` (à donner en messagerie privée, pas en bio) |
| Adresse | Sablière, Libreville — en face de la Résidence de l'Ambassade d'Arabie Saoudite |
| Catégorie / secteur | Université · Établissement d'enseignement supérieur · Formation |
| Année à citer | **2022** (Executive MBA ouvert depuis 2022) — pas 2026 « depuis » |
| Logo | `assets/img/logo-upl.png` (avatar carré, fond blanc ou bleu) |
| Couverture | `docs/com/visuels/01-preinscriptions-carre.png` une fois P1 validé |
| Langues | FR d'abord ; l'EN n'est fourni que pour LinkedIn et YouTube (cadres, partenaires) |

**Règle de consistance :** un visiteur qui tape « UPL Gabon » doit trouver le même nom, le même
logo, la même phrase et le même lien sur Facebook, Instagram, TikTok, LinkedIn, YouTube et WhatsApp.

---

## 2. Le domaine : `upl-gabon.com`, pas `upl.com`

Le domaine de l'UPL est **`upl-gabon.com`** (Namecheap, boîte `contact@` active). Écrire
`upl.com` dans une bio serait **envoyer les candidats chez un tiers** :

- `upl.com` / `upl-ltd.com` = **UPL Limited**, groupe indien de pesticides/agriculture (Mumbai) —
  c'est lui qui occupe le mot « UPL » sur les moteurs et les réseaux ;
- **Université Protestante de Lubumbashi** (RDC) signe déjà « UPL » sur Facebook / Instagram ;
- le handle générique `@UPL` (YouTube, X…) n'est pas à l'UPL : le site ne doit jamais le relayer.

Conséquences pratiques :

- [ ] bios, liens de profil, signatures : `upl-gabon.com` partout ;
- [ ] tous les @identifiants portent **gabon** ou **libreville** ;
- [ ] si `upl.com` appartient bien à l'UPL (à vérifier au registrar), on en parle au Président
      **avant** de l'écrire où que ce soit — tant que ce n'est pas écrit noir sur blanc, il est tiers.

---

## 3. Signature réutilisable (fin de post, message d'accueil, champ long)

```text
Université Privée de Libreville — UPL
Sablière, Libreville · Gabon
contact@upl-gabon.com · +241 02 62 19 78
https://upl-gabon.com
```

C'est le seul bloc de contact autorisé en public. Pas d'`admissions@`, pas de `partenariats@`,
pas de numéro personnel — ils n'existent pas ou ne sont pas institutionnels.

---

## 4. Une fiche par réseau

### 4.1 Facebook — la Page (pas le profil)

| Champ | Valeur |
|---|---|
| Nom de la Page | Université Privée de Libreville |
| Catégorie | Université |
| Nom d'utilisateur | `uplgabon` → `facebook.com/uplgabon` |
| Site web | https://upl-gabon.com |
| E-mail / téléphone / adresse | § 1 |
| Bio (intro) | ≤ 101 caractères |
| À propos / description | ≤ 255 caractères |

**Bio (champ court, affiché sous le nom) :**

```text
Université Privée de Libreville, Gabon. Pré-inscriptions 2026-2027 : Licence, Master, CPGE, MBA, DBA
```
_100 caractères — limite plateforme 101, vérifié par npm test_

**À propos :**

```text
Établissement privé d’enseignement supérieur, Sablière, Libreville.
Executive MBA depuis 2022, avec l’appui académique de l’Université de Douala — près de 80 cadres formés, cours du soir 17h–21h.
contact@upl-gabon.com · +241 02 62 19 78 · upl-gabon.com
```
_252 caractères — limite plateforme 255, vérifié par npm test_

Sur Facebook, deux objets distincts :

- la **Page** = la vitrine de l'institution → **abonnés (followers)**, commentaires publics,
  statistiques, publicité, WhatsApp rattaché. C'est elle qui porte la bio ci-dessus.
- le **profil** qui administre = le compte de travail (créé avec `contact@upl-gabon.com`) →
  **amis**, pas d'audience institutionnelle. Il ne publie pas en son nom.

La Page de 2022 (≈ 500 abonnés) et la reprise de l'ancien travail : **`FACEBOOK_PAGE_500.md`**.
Le nom à donner au profil d'administration et les précautions de compte : § 1 et § 5 de ce même fichier.

---

### 4.2 Instagram

| Champ | Valeur |
|---|---|
| Nom d'affichage | Université Privée de Libreville |
| Utilisateur | `upl.gabon` |
| Catégorie | Établissement d'enseignement supérieur |
| Site web | https://upl-gabon.com |
| E-mail commercial | contact@upl-gabon.com |
| Bio | ≤ 150 caractères |

```text
Université Privée de Libreville (Gabon) · Sablière · Pré-inscriptions 2026-2027 : Licence, Master, CPGE, MBA, DBA
```
_113 caractères — limite plateforme 150, vérifié par npm test_

L'Instagram se crée **depuis le même Business Manager** que Facebook, avec la Page rattachée :
les deux partagent bio, visuels et boîte de réception.

---

### 4.3 TikTok

| Champ | Valeur |
|---|---|
| Utilisateur | `upl.gabon` |
| Nom | Université Privée de Libreville |
| Catégorie | Éducation / Formation |
| Site web (dès que le compte Pro l'autorise) | https://upl-gabon.com |
| Bio | ≤ 80 caractères |

```text
Université Privée de Libreville · Pré-inscriptions 2026-2027
```
_60 caractères — limite plateforme 80, vérifié par npm test_

Sur TikTok : vrais visuels (campus, cours du soir, secrétariat) ou habillages graphiques validés —
**aucun visage généré**, aucune vidéo « Rentrée 2024 » (`SyUXYUPj6hc`), aucun montage emprunté.

---

### 4.4 LinkedIn — deux comptes, un seul porte-voix

| Objet | Rôle | Ce qu'on y écrit |
|---|---|---|
| **Page entreprise** — Université Privée de Libreville (UPL) | la vitrine institutionnelle | tagline + « À propos », site, secteur |
| **Profil personnel d'administration** (ex. `in/upl-contact-…`) | outil de travail du secrétariat | titre § ci-dessous, pas de promo en nom propre |

Le profil personnel **n'est pas** la vitrine de l'école : il sert à administrer la Page et à
répondre en message privé. Le titre reste sobre et factuel :

**Titre du profil (≤ 220) :**

```text
Secrétariat — Université Privée de Libreville (UPL) · Executive MBA depuis 2022 · Pré-inscriptions 2026-2027 : Licence, Master, CPGE, DBA · Libreville, Gabon
```
_157 caractères — limite plateforme 220, vérifié par npm test_

**Page entreprise — tagline (≤ 200) :**

```text
Établissement privé d’enseignement supérieur à Libreville. Executive MBA depuis 2022 · Pré-inscriptions 2026-2027.
```
_114 caractères — limite plateforme 200, vérifié par npm test_

**Page entreprise — À propos (FR) :**

```text
Université Privée de Libreville (UPL) — établissement privé d’enseignement supérieur, Sablière, Libreville (Gabon).

Executive MBA ouvert depuis 2022, avec l’appui académique de l’Université de Douala. Près de 80 cadres formés. Cours du soir 17h–21h, compatibles avec une activité professionnelle. Scolarité payable en tranches.

Pré-inscriptions 2026-2027 : Licence, Master, CPGE, Executive MBA, DBA — gratuites et sans engagement. Le secrétariat rappelle chaque candidat pour les pièces et les places disponibles.

Entreprises et institutions : coopérations étudiées au cas par cas (stages, modules professionnels, formation des équipes) après un premier échange avec le secrétariat.

contact@upl-gabon.com · +241 02 62 19 78 · https://upl-gabon.com
```
_751 caractères — limite plateforme 2000, vérifié par npm test_

**Company Page — About (EN) :**

```text
Université Privée de Libreville (UPL) — private higher-education institution, Sablière, Libreville (Gabon).

Executive MBA running since 2022, with the academic support of the University of Douala. Nearly 80 professionals trained. Evening classes, 5 to 9 pm, compatible with full-time work. Tuition payable in instalments.

Pre-registration for the 2026-2027 academic year: Bachelor's, Master's, CPGE, Executive MBA, DBA — free and without commitment.

contact@upl-gabon.com · +241 02 62 19 78 · https://upl-gabon.com
```
_517 caractères_

URL personnalisée de la Page : `linkedin.com/company/upl-gabon`. Une Page entreprise et un profil
ne sont **pas** un doublon : LinkedIn les traite comme deux objets différents, avec des audiences
différentes (abonnés de la Page vs réseau du profil).

---

### 4.5 WhatsApp Business (numéro du Président — déjà en service)

On n'ouvre **pas** de second compte. On aligne la fiche existante sur le site.

| Champ | Limite |
|---|---|
| « À propos » | ≤ 139 caractères |
| Description de l'entreprise | ≤ 256 caractères |
| Site web | https://upl-gabon.com |
| Catégorie | Formation / Éducation |
| Horaires | ceux réellement pratiqués par le secrétariat (17h–21h = horaires **des cours**) |

**À propos :**

```text
Université Privée de Libreville — Sablière. Pré-inscriptions 2026-2027. Executive MBA depuis 2022.
```
_98 caractères — limite plateforme 139, vérifié par npm test_

**Description :**

```text
Établissement privé d’enseignement supérieur, Sablière, Libreville. Executive MBA depuis 2022 (appui Université de Douala). Pré-inscriptions 2026-2027 : Licence, Master, CPGE, DBA.
```
_180 caractères — limite plateforme 256, vérifié par npm test_

À retirer de la fiche actuelle : MBA Journalisme / MBA Sport / MBA Santé (hors site), l'accroche
« Rejoignez l'Élite », le lien Rentrée 2024 (`youtu.be/SyUXYUPj6hc`), le nom affiché « Papa ».
Films TV autorisés : `jh_iCTJuLKA` (présentation) et `FAKHfv8nN7I` (interview MBA).

---

### 4.6 YouTube — `@UPLGabon` (à ouvrir, pas encore à l'UPL)

| Champ | Valeur |
|---|---|
| Nom de la chaîne | Université Privée de Libreville — UPL |
| Handle | `@UPLGabon` — **jamais `@UPL`** (handle générique déjà pris, § 2) |
| Pays | Gabon |
| Description | ≤ 1000 caractères |
| E-mail de la chaîne | contact@upl-gabon.com |

**Description courte :**

```text
Université Privée de Libreville (Gabon) — Executive MBA depuis 2022, pré-inscriptions 2026-2027.
```
_96 caractères — limite plateforme 150, vérifié par npm test_

**Description de la chaîne :**

```text
Chaîne de l'Université Privée de Libreville (UPL), Sablière, Libreville (Gabon).

Executive MBA depuis 2022, avec l'appui académique de l'Université de Douala. Pré-inscriptions 2026-2027 : Licence, Master, CPGE, DBA.

Films de télévision déjà publiés : présentation institutionnelle et interview Executive MBA.
https://upl-gabon.com · contact@upl-gabon.com · +241 02 62 19 78
```
_375 caractères — limite plateforme 1000, vérifié par npm test_

Statut : `off` dans `config.js` tant que la chaîne n'est pas créée et que les deux films n'y sont
pas rattachés. Le site renvoie déjà vers les **deux films** (page À propos + page MBA) — c'est
suffisant, et c'est exact.

---

### 4.7 Google — compte UPL + fiche d'établissement

Le compte Google ouvert avec l'adresse UPL est un **compte ordinaire** (pas Workspace) : c'est lui
qui porte la **fiche d'établissement Google** (le panneau à droite des recherches), YouTube et le
Drive de l'école. Il n'est **pas** en doublon avec les réseaux sociaux — ce n'est pas un réseau
social, c'est l'annuaire. Le texte à y coller :

```text
Université Privée de Libreville (UPL) — établissement privé d’enseignement supérieur, Sablière, Libreville (Gabon).

Executive MBA ouvert depuis 2022, avec l’appui académique de l’Université de Douala : près de 80 cadres formés, cours du soir 17h–21h, scolarité payable en tranches.

Rentrée 2026-2027 : pré-inscriptions gratuites et sans engagement en Licence, Master, CPGE et DBA.

contact@upl-gabon.com · +241 02 62 19 78 · https://upl-gabon.com
```
_448 caractères — limite plateforme 750, vérifié par npm test_

| Champ de la fiche | Valeur |
|---|---|
| Nom | Université Privée de Libreville |
| Catégorie | Université |
| Adresse | Sablière, Libreville, Gabon |
| Téléphone | +241 02 62 19 78 |
| Site | https://upl-gabon.com |
| Horaires | ceux du secrétariat |
| Description | le bloc ci-dessus |

Comptes Google : ce qu'ils protègent et ce qui les menace (récupération, 2 admins, 2FA) →
`EMAIL_ROUTAGE.md` § 3.

---

### 4.8 X (Twitter) — handle réservé, pas d'animation

Décision : on **réserve** `@uplgabon`, on n'anime pas (audience bacheliers/parents faible au Gabon).
La bio de réserve existe pour que le handle ne soit pas pris par un tiers :

```text
Université Privée de Libreville (Gabon) · Executive MBA depuis 2022 · upl-gabon.com
```
_83 caractères — limite plateforme 160, vérifié par npm test_

Statut `off` dans `config.js` : rien de ce compte n'apparaît sur le site.

---

## 5. Liste noire (aucune dérogation, même « une fois »)

Ne doit apparaître dans **aucune** bio, aucun post, aucune réponse :

| Interdit | Pourquoi |
|---|---|
| `upl.com`, `@UPL`, « UPL » seul | tiers (UPL Ltd / Lubumbashi) — § 2 |
| « inscriptions ouvertes » pour Licence / Master / CPGE / DBA | palier 1 = **pré-inscriptions** |
| tarifs autres que ceux du site, tarif DBA chiffré | chiffres verrouillés par les tests |
| `admissions@`, `partenariats@`, tout mail non créé | n'existe pas |
| HEC, Polytechnique, Sciences Po, « partenariat France » signé | non contractuel |
| « Maroc », dossier Ecobank, 3,5 Md | hors périmètre public |
| Calvin, un Gmail perso, un numéro personnel | appui ponctuel, pas contact public |
| « garanti », « sécurisé », « diplômé à coup sûr », bourse promise | promesse non tenue |
| « 500 étudiants », « campus », photos de stock, visages IA | non vérifié / non autorisé |
| Rentrée 2024 (`SyUXYUPj6hc`), MBA Journalisme / Sport / Santé | retirés sur demande du Président |
| date de rentrée | pas de date avant communiqué |

---

## 6. Coller une bio puis basculer le site — checklist

Pour **chaque** réseau, dans cet ordre :

- [ ] le compte est créé avec **`contact@upl-gabon.com`** (jamais un Gmail personnel)
- [ ] **2 administrateurs UPL** minimum (Président/secrétariat + un second de l'institution)
- [ ] 2FA par application d'authentification sur un **téléphone UPL** ; codes de secours au secrétariat
- [ ] pièce **P11** validée par écrit par le Président (`TEXTES_A_VALIDER.md`)
- [ ] nom, @identifiant, catégorie, logo, couverture, site, e-mail, téléphone : § 1
- [ ] bio collée **telle quelle** (le compteur est vérifié par `npm test`)
- [ ] URL officielle notée dans `RESEAUX_ETAT.md`
- [ ] publication épinglée = P1 (pré-inscriptions 2026-2027)

Puis, **une fois** les réseaux voulus à l'état « fini » :

- [ ] `config.js → social.<reseau>.url` = l'URL officielle ; `status: "live"`
- [ ] `config.js → features.showSocialLinks = true`
- [ ] `npm test` vert → le bloc « Nous suivre » apparaît en pied de page et sur la page Contact
- [ ] un réseau qui repasse à `pending` disparaît du site sans autre modification

À livrer au Président pour signature : les bios ci-dessus, en une page imprimable —
c'est la pièce **P11** du kit de validation.

---

## 7. Compteurs : ce qui est vérifié automatiquement

| Réseau | Champ | Limite plateforme | Texte UPL |
|---|---|---|---|
| Facebook | Bio / intro | 101 | ✅ test `npm test` |
| Facebook | À propos | 255 | ✅ |
| Instagram | Bio | 150 | ✅ |
| TikTok | Bio | 80 | ✅ |
| LinkedIn | Titre du profil | 220 | ✅ |
| LinkedIn | Tagline de la Page | 200 | ✅ |
| LinkedIn | À propos (FR / EN) | 2000 | ✅ |
| WhatsApp | À propos | 139 | ✅ |
| WhatsApp | Description | 256 | ✅ |
| YouTube | Description courte / chaîne | 150 / 1000 | ✅ |
| Google | Description de la fiche | 750 | ✅ |
| X | Bio | 160 | ✅ |

Les maxima sont écrits dans `config.js` (`bioMax`, `aboutMax`, `headlineMax`, `taglineMax`) : un texte
trop long **casse `npm test`**. Au moment de coller, c'est le compteur affiché par la plateforme qui
fait foi — si elle a bougé, on raccourcit le texte dans `config.js` (et on met à jour la limite),
jamais l'inverse.
