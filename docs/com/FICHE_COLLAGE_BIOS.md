# Fiche de collage — 4 comptes vides (01/09/2026)

Version imprimable / écran séparé de `BIOS_RESEAUX_2026.md`. **Un seul e-mail de compte :
`contact@upl-gabon.com`. Un seul lien : `https://upl-gabon.com`** (jamais `upl.com` — c'est un tiers).
Les textes sont verrouillés par `npm test` : 100/101, 252/255, 113/150, 60/80, 157/220, 114/200.

---

## 1 · FACEBOOK — la Page

| Champ | À remplir |
|---|---|
| Nom | Université Privée de Libreville |
| Catégorie | Université |
| Nom d'utilisateur | `uplgabon` |
| Site web | https://upl-gabon.com |
| E-mail | contact@upl-gabon.com |
| Téléphone | +241 02 62 19 78 |
| Adresse | Sablière, Libreville, Gabon |
| Avatar | logo UPL · Couverture : visuel 01 (après validation P1) |

**Bio (intro) — 100 caractères / limite 101**

```text
Université Privée de Libreville, Gabon. Pré-inscriptions 2026-2027 : Licence, Master, CPGE, MBA, DBA
```

**À propos — 252 caractères / limite 255** (3 lignes = 3 paragraphes, coller tel quel)

```text
Établissement privé d’enseignement supérieur, Sablière, Libreville.
Executive MBA depuis 2022, avec l’appui académique de l’Université de Douala — près de 80 cadres formés, cours du soir 17h–21h.
contact@upl-gabon.com · +241 02 62 19 78 · upl-gabon.com
```

> Le compte de gestion (celui qui a des **amis**) ne publie pas en son nom : il administre la Page,
> qui elle a des **abonnés**. Nom du profil = une personne réelle du secrétariat, pas l'école.

---

## 2 · INSTAGRAM

| Champ | À remplir |
|---|---|
| Nom d'affichage | Université Privée de Libreville |
| Utilisateur | `upl.gabon` |
| Catégorie | Établissement d'enseignement supérieur |
| Site web | https://upl-gabon.com |
| E-mail professionnel | contact@upl-gabon.com |

**Bio — 113 caractères / limite 150**

```text
Université Privée de Libreville (Gabon) · Sablière · Pré-inscriptions 2026-2027 : Licence, Master, CPGE, MBA, DBA
```

---

## 3 · TIKTOK

| Champ | À remplir |
|---|---|
| Nom | Université Privée de Libreville |
| Utilisateur | `upl.gabon` |
| Catégorie | Éducation |
| Site web (compte Pro) | https://upl-gabon.com |

**Bio — 60 caractères / limite 80**

```text
Université Privée de Libreville · Pré-inscriptions 2026-2027
```

---

## 4 · LINKEDIN

### a) Titre du profil de travail (celui du secrétariat) — 157 / 220

```text
Secrétariat — Université Privée de Libreville (UPL) · Executive MBA depuis 2022 · Pré-inscriptions 2026-2027 : Licence, Master, CPGE, DBA · Libreville, Gabon
```

Le titre actuel (« Programme universitaire chez Université Privée de Libreville (UPL) ») ne dit rien :
à remplacer. Profil = outil de travail, la vitrine reste la **Page entreprise**.

### b) Page entreprise — slogan / tagline — 114 / 200

```text
Établissement privé d’enseignement supérieur à Libreville. Executive MBA depuis 2022 · Pré-inscriptions 2026-2027.
```

### c) Page entreprise — « À propos » (FR) — 751 / 2000

```text
Université Privée de Libreville (UPL) — établissement privé d’enseignement supérieur, Sablière, Libreville (Gabon).

Executive MBA ouvert depuis 2022, avec l’appui académique de l’Université de Douala. Près de 80 cadres formés. Cours du soir 17h–21h, compatibles avec une activité professionnelle. Scolarité payable en tranches.

Pré-inscriptions 2026-2027 : Licence, Master, CPGE, Executive MBA, DBA — gratuites et sans engagement. Le secrétariat rappelle chaque candidat pour les pièces et les places disponibles.

Entreprises et institutions : coopérations étudiées au cas par cas (stages, modules professionnels, formation des équipes) après un premier échange avec le secrétariat.

contact@upl-gabon.com · +241 02 62 19 78 · https://upl-gabon.com
```

### d) Company Page — About (EN) — 517 caractères

```text
Université Privée de Libreville (UPL) — private higher-education institution, Sablière, Libreville (Gabon).

Executive MBA running since 2022, with the academic support of the University of Douala. Nearly 80 professionals trained. Evening classes, 5 to 9 pm, compatible with full-time work. Tuition payable in instalments.

Pre-registration for the 2026-2027 academic year: Bachelor's, Master's, CPGE, Executive MBA, DBA — free and without commitment.

contact@upl-gabon.com · +241 02 62 19 78 · https://upl-gabon.com
```

---

## 5 · Trois réflexes qui évitent les ennuis

1. **2ᵉ administrateur UPL** sur chaque compte + **2FA par application** (téléphone de l'école),
   codes de secours sous enveloppe au secrétariat — jamais dans un fichier, jamais dans un chat.
2. **Ne rien publier avant le VALIDÉ** du Président sur les bios (pièce **P11**) ; la publication
   épinglée ensuite = pièce **P1** (pré-inscriptions 2026-2027).
3. **Jamais** dans une bio : `admissions@`, partenaires français non signés, « inscriptions ouvertes »
   pour Licence / Master / CPGE / DBA, tarif DBA chiffré, date de rentrée, Calvin, « garanti »,
   MBA Journalisme / Sport / Santé, `upl.com`.

## 6 · Une fois collé

Prévenir la personne qui tient le site : `config.js → social.<réseau>.url` + `status: "live"`,
puis `features.showSocialLinks = true` → le bloc « Nous suivre » s'affiche en pied de page et sur la
page Contact. Un compte qui n'est pas fini reste invisible.
