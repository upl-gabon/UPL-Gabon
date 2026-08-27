# GitHub + vision site UPL — décision (ne rien supprimer pour l’instant)

**Date :** 27 août 2026  
**Rappel :** le site Netlify provisoire pourra être retiré **une fois** le site définitif validé.  
**Pour l’instant : ne supprimer aucun déploiement, aucun repo, aucun DNS.**

---

## 1. GitHub — où créer le compte / le repo ?

### Contexte
- Gmail perso `blanchardminang00@gmail.com` : pratique, mais Google a déjà freiné le numéro (trop de comptes).
- Mail institutionnel : `contact@upl-gabon.com` (PrivateEmail / Namecheap) — **stable, sous votre contrôle**.
- Domaine réel UPL : **`upl-gabon.com`** (pas `upl.com`, qui est un autre propriétaire / hors sujet).

### Recommandation ferme

| Rôle | Compte | Pourquoi |
|---|---|---|
| **Propriétaire du repo (owner)** | Compte GitHub rattaché à **`contact@upl-gabon.com`** | Propriété UPL, survivra si Calvin change de Gmail, crédible pour un futur HEC / partenaire |
| **Admin n°2** | Compte GitHub rattaché à **`blanchardminang00@gmail.com`** | Travail quotidien Calvin, push, PR |
| **Admin n°3 (optionnel plus tard)** | Mail Président ou 2ᵉ boîte UPL | Continuité si Calvin indisponible |

**Ne pas :**
- mettre le repo **uniquement** sur le Gmail perso (risque de perte / blocage / départ) ;
- créer le repo sous un compte prestataire ;
- utiliser `upl.com` (ce n’est pas votre domaine).

### Création concrète (15 min)

1. Aller sur https://github.com/signup  
2. E-mail : **`contact@upl-gabon.com`** (PrivateEmail reçoit le mail de validation)  
3. Username proposé : `upl-gabon` ou `universite-privee-libreville`  
4. Activer **2FA** (app authenticator, pas SMS Google si le num est bloqué — TOTP marche)  
5. Créer org optionnelle plus tard : `upl-gabon`  
6. Repo **privé** : `site-web`  
7. Inviter `blanchardminang00` (compte GitHub lié au Gmail) en **Admin**  
8. Pousser le dossier `upl-web` actuel  

```text
Owner     = GitHub(contact@upl-gabon.com)
Collab    = GitHub(blanchardminang00@gmail.com)
Netlify   = lié au repo (deploy auto) — compte Netlify aussi sur contact@ si possible
```

### Si GitHub refuse le signup sur contact@
Plan B : créer le compte avec `blanchardminang00@gmail.com`, puis **immédiatement** :
- ajouter `contact@upl-gabon.com` comme e-mail vérifié du compte ;
- documenter que le compte est un **compte de service UPL** géré par Calvin ;
- créer une **Organization** `upl-gabon` et y mettre le repo (l’org = propriété institutionnelle).

L’organization GitHub est le vrai bon réflexe « comme HEC » : le code appartient à l’org, pas à une personne.

---

## 2. Vision produit du site (après la vitrine MBA actuelle)

La vitrine v1 (4 pages MBA) **reste**. Elle n’est pas jetée : elle devient la base, puis on enrichit **par couches**.

### Objectifs utilisateurs

| Public | Besoin | Priorité |
|---|---|---|
| Étudiant / auditeur gabonais | Comprendre, s’inscrire, payer simple | P0 |
| Président | Voir les dossiers, valider sans complexité | P0 |
| Candidat MBA | Info + contact + pièces | P0 |
| Futur partenaire type HEC | Image sérieuse, sobre, pas gadget | P1 |
| Grand public / parents | Confiance institutionnelle | P1 |

### Paiement — Afrique d’abord
- **Moov Money** et **Airtel Money** = moyens principaux (pas « carte bancaire d’abord »).
- Carte Visa/Mastercard = option secondaire si un jour un prestataire le permet.
- Parcours : choisir programme → dossier → **payer frais d’inscription via Mobile Money** → reçu → suivi.

*(Intégration technique Mobile Money = phase 2/3, après site + mail + GitHub. Souvent via API opérateur ou agrégateur type payin local.)*

### Modules cibles (ordre de construction)

| Phase | Module | Notes |
|---|---|---|
| **V1 (maintenant)** | Vitrine MBA + contact@ | **En cours** — Netlify OK, ne pas supprimer |
| **V1.1** | GitHub org + deploy auto Netlify | Dès compte GitHub UPL |
| **V2** | Espace **Inscription** (formulaire structuré, pièces, suivi statut) | Simple téléphone / WhatsApp en secours |
| **V2** | **Paiement** Moov / Airtel (frais inscription MBA d’abord) | 1 seul flux avant de complexifier |
| **V3** | **Bibliothèque** (ressources cours, PDF, liens — accès auditeurs) | Pas un Google Drive chaotique : catalogue simple |
| **V3** | Espace Président (liste candidatures, paiements, exports) | Écrans peu nombreux, gros boutons, clair |
| **Plus tard** | Nouvelles filières, partenaires, multi-écoles | **Seulement si décidé** (ex. hypothèse HEC Gabon) |

### Style — « pro HEC » sans site IA insipide

| Oui | Non |
|---|---|
| Photo réelle Libreville / promo MBA / Président | Banks d’images stock génériques « IA happy students » |
| Typo soignée, beaucoup d’air, or/bleu UPL | Gradients violets startup, glassmorphism excessif |
| Une accroche humaine gabonaise | Jargon « excellence synergique disruptive » |
| Illustrations locales / motifs discrets Afrique centrale | Copier-coller template HEC pixel-perfect sans âme |
| Français clair, phrases courtes | Pavés académiques illisibles sur mobile |
| Mobile-first (Moov/Airtel se paient sur téléphone) | Desktop-only |

**Référence d’ambition :** sérieux d’une grande école (HEC = sobriété, hiérarchie visuelle, confiance).  
**Réalité d’usage :** Afrique = mobile, Mobile Money, faible bande passante, WhatsApp.

Créativité = **direction artistique locale** (couleurs UPL, photos terrain, micro-interactions légères, icônes Mobile Money), pas plus de sections ni de texte IA.

---

## 3. Ce qu’on ne fait pas maintenant

- Supprimer le site Netlify  
- Annoncer HEC Gabon / Polytechnique / Sciences Po sur le site  
- Ouvrir licences/masters sur le site  
- Brancher 10 moyens de paiement  
- Refondre tout en React lourd sans besoin  

---

## 4. Décision à valider (cochez)

### GitHub
- [ ] **Option recommandée :** compte (ou org) GitHub avec `contact@upl-gabon.com` + admin Gmail Calvin  
- [ ] **Plan B :** compte Gmail Calvin + org `upl-gabon` + mail contact@ en secondary  

Username / org choisi : `________________________`

### Netlify
- [ ] On garde le deploy actuel jusqu’à validation du site définitif  
- [ ] Compte Netlify rattaché à : ☐ contact@ ☐ Gmail Calvin  

### Prochaine brique produit (après GitHub)
- [ ] Rester sur vitrine seule encore 1–2 semaines  
- [ ] Enchaîner maquette **Inscription + Moov/Airtel** (V2)  

---

## 5. Message court pour le Président

> On a un mail pro qui marche (contact@upl-gabon.com) et un site simple MBA.  
> On met le code sur GitHub au nom de l’UPL (pas seulement le Gmail de Calvin).  
> Netlify reste en test ; on ne supprime rien.  
> Ensuite seulement : inscription en ligne et paiement Moov / Airtel, adaptés aux étudiants gabonais.  
> L’objectif esthétique : aussi crédible qu’une grande école, aussi simple qu’un usage mobile africain.

---

*Document de cadrage — pas une spec technique complète V2.*
