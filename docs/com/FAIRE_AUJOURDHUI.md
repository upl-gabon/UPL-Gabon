# À faire — version simple

**Mise à jour : 1er septembre 2026.** Site **non modifié sur le fond** (bios et réseaux préparés en
`config.js`, rien d'affiché tant qu'un compte n'est pas validé). Rien n'est publié sans **VALIDÉ** du Président.

Ce fichier = la feuille d'action. Les textes : `BIOS_RESEAUX_2026.md` · l'état des comptes :
`RESEAUX_ETAT.md` · la Page de 2022 : `FACEBOOK_PAGE_500.md` · les mails : `EMAIL_ROUTAGE.md`.

---

## 1. Le principe retenu

```
bio validée  →  bio collée sur le réseau (+ 2 admins UPL)  →  status "live" dans config.js  →  le réseau apparaît sur le site
```

Un compte en cours n'apparaît **pas** sur le site. Aucun encart vide, aucun « à venir ».

## 2. Bios — une par réseau, déjà écrites

**Pour remplir les 4 comptes vides tout de suite : `FICHE_COLLAGE_BIOS.md`** (texte prêt à coller,
Facebook · Instagram · TikTok · LinkedIn, avec les compteurs). Le détail et les autres réseaux :
`BIOS_RESEAUX_2026.md`.

| Réseau | Champ | Où la coller |
|---|---|---|
| Facebook **Page** | bio (101) + À propos (255) | `BIOS_RESEAUX_2026.md` § 4.1 |
| Instagram | bio (150) | § 4.2 |
| TikTok | bio (80) | § 4.3 |
| LinkedIn | titre du profil (220) + tagline Page (200) + À propos FR/EN | § 4.4 |
| WhatsApp (Président) | À propos (139) + description (256) | § 4.5 |
| Google (fiche d'établissement) | description (750) | § 4.7 |
| YouTube `@UPLGabon`, X `@uplgabon` | réservés, **non publiés** | § 4.6 et § 4.8 |

**Partout** : e-mail du compte = `contact@upl-gabon.com`, lien = `https://upl-gabon.com`,
nom = **Université Privée de Libreville**, logo `assets/img/logo-upl.png`.
**Jamais** `upl.com` dans une bio (c'est un tiers — voir § 2 du fichier des bios).

## 3. Trois corrections de sécurité avant de publier quoi que ce soit

- [ ] **2ᵉ admin UPL** sur Google, Facebook/Meta, TikTok, LinkedIn, GitHub, Netlify, Namecheap
- [ ] **2FA par application** sur un téléphone de l'école + codes de secours sous enveloppe au secrétariat
- [ ] le **compte de gestion Facebook** prend un nom de personne réelle du secrétariat ; le nom de
      l'institution reste sur la **Page** (une Page a des abonnés, un profil a des amis)

## 4. La Page Facebook de 2022 (≈ 500 abonnés)

1. Tenter la reprise par `contact@upl-gabon.com` (réinitialisation), puis réclamation Meta avec la
   facture de l'agence + la pièce du Président + le document d'existence de l'UPL.
2. **Pas de Page jumelle** avant la réponse de Meta.
3. Si elle est perdue : une seule Page neuve, et le **pont** (textes T1-T4, 10 commentaires/jour,
   **aucun message privé en masse**). Pièce **P12** à faire valider.
4. Récupérer le travail d'il y a 4 ans : exporter l'ancien contenu, garder les 3 meilleures
   publications, les **rééditer** avec les infos 2026-2027, répondre aux commentaires historiques.

## 5. Mails

- [ ] alias `secretariat@` (puis `mba@`) créés dans Private Email, livrés dans `contact@` — **non publiés**
- [ ] lecture de `contact@` depuis le compte Google (IMAP ou transfert **avec copie conservée**) ; MX intouchés
- [ ] 7 étiquettes + filtres par objet (Pré-inscription · MBA · RDV · Partenariat · Abonnement · Scolarité · Presse)
- [ ] notifications des boîtes de réception réseaux → `contact@` ; tout contact reçu sur un réseau est
      **recopié par mail** sous 24 h (nom, téléphone, formation, réponse faite)
- [ ] compte Google : e-mail et téléphone de récupération = UPL, personne de confiance ajoutée

## 6. Sur le site, à la fin seulement

- [ ] `config.js → social.<reseau>.url` + `status: "live"` pour les comptes finis
- [ ] `features.showSocialLinks = true`
- [ ] `npm test` vert (les blocs « Nous suivre » du pied de page et de la page Contact ne s'affichent qu'alors)

## 6b. Vidéos (une fois les visuels en ligne)

`VIDEO_AI_PLAYBOOK.md` : l'IA monte **nos** rushes, elle n'invente rien. Trois prompts prêts à coller,
pièce **P14** à valider. ⚠️ Avant tout : passer les dossiers Drive en accès **restreint** (le dossier
de com contient aussi le dossier bancaire et les annexes juridiques).

## 7. Premier post (après VALIDÉ)

Texte **P1** de `TEXTES_A_VALIDER.md` + visuel `visuels/01-preinscriptions-carre.png`, épinglé sur
chaque réseau prêt. Toujours : **pré-inscriptions** (pas « inscriptions ouvertes »), sauf Executive MBA.
