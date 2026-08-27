# STATUT 27 août 2026 (mis à jour)

| Brique | Statut |
|---|---|
| Mail `contact@upl-gabon.com` | **ACTIF** — PrivateEmail (Namecheap) |
| Domaine / DNS | **Namecheap** (ne pas casser les MX mail) |
| Site | Code v1 prêt — **à déployer sur Netlify** puis brancher www |
| Suite | Voir `01_DEPLOIEMENT_NETLIFY_NAMECHEAP.md` |

---

# Décision n°1 — Domaine, site, e-mail (AVANT tout le reste)

**Règle UPL :** on ne publie pas de formations « projet », on ne met pas d’adresses mail
inexistantes, on ne contacte pas Science Po / Polytechnique / HEC tant que
**le site minimal + au moins une boîte mail contrôlée par l’UPL** ne sont pas en place.

Date : 26 août 2026  
Responsable suivi : Calvin Blanchard MINANG  
Validation : Serge Patrick MINANG

---

## 0. Ce qui est vrai aujourd’hui

| Sujet | Réalité |
|---|---|
| Activité ouverte présentée au public | **Executive MBA uniquement** |
| Autres formations | **Projets éventuels** — peuvent aboutir ou non — **pas sur le site** |
| Partenariats grandes écoles FR | **Exploration future** — pas d’annonce |
| Mails @upl-gabon.com | **N’existent pas encore** (ou non contrôlés par vous) |
| Ancien site / réseaux | Codes bloqués par un tiers — **on recrée**, on ne rachète pas les accès |

---

## 1. Les 3 briques à trancher (dans cet ordre)

```
① DOMAINE  →  ② E-MAIL  →  ③ SITE EN LIGNE
```

Sans ①, pas de mail pro stable.  
Sans ②, pas de contact crédible pour un partenaire.  
Sans ③, pas de lien à mettre dans une signature.

---

## 2. Domaine

### Question A — Qui possède `upl-gabon.com` aujourd’hui ?

| Option | Action |
|---|---|
| **A1.** Le Président / UPL a le login registrar | Garder ce domaine. Noter registrar (OVH, Namecheap, Gandi, Amen…). |
| **A2.** Le prestataire a le domaine | Exiger transfert de propriété **écrit** OU abandonner et prendre un **nouveau** domaine UPL. |
| **A3.** Inconnu | WHOIS + essayer récupération ; sinon **nouveau domaine**. |

### Question B — Si nouveau domaine, lequel ?

Propositions (à checker disponibilité) :

1. `upl-gabon.com` (idéal si récupérable)
2. `upl.ga` (si extension .ga fiable pour vous)
3. `universite-upl.ga` / `upl-libreville.com` (secours)

**Décision à cocher :**

- [ ] On garde / récupère : `____________________`
- [ ] On crée un nouveau : `____________________`
- [ ] Registrar choisi : `____________________`
- [ ] Compte registrar au nom de : ☐ UPL / ☐ Président / ☐ Calvin (temporaire, à retransférer)

**Règle ownership :** 2 personnes UPL ont les identifiants (Président + Calvin). Jamais un prestataire seul.

---

## 3. E-mail professionnel

Dès que le DNS du domaine est à vous :

### Stack recommandée (simple, crédible)

| Choix | Pour qui | Coût ordre de grandeur |
|---|---|---|
| **Google Workspace** | Institution (Gmail pro + Drive) | ~ /utilisateur/mois |
| **Microsoft 365** | Si Teams déjà central | ~ /utilisateur/mois |
| **Zoho Mail** | Budget serré | faible |
| **Infomaniak** | Alternative EU | moyen |

### Boîtes minimales au démarrage (2 suffisent)

| Adresse | Usage |
|---|---|
| `contact@[domaine]` | Public, site, signature |
| `mba@[domaine]` ou `admissions@[domaine]` | Candidats MBA |

Plus tard seulement : `president@`, `partenariats@`, etc.

### Tant que ce n’est pas prêt

- Contact public = **téléphones UPL** (+ WhatsApp)
- Suivi Calvin = `calvin.minang@skema.edu` (personnel / études — **pas** comme mail institutionnel UPL sur le site)

**Décision à cocher :**

- [ ] Provider mail : ☐ Google Workspace ☐ Microsoft 365 ☐ Zoho ☐ Autre : ______
- [ ] Première boîte : `contact@________`
- [ ] Deuxième boîte : `________________@________`
- [ ] SPF + DKIM + DMARC activés : ☐

---

## 4. Hébergement du site

Le site actuel dans ce dépôt est **statique, léger** (4 pages) : parfait pour démarrer.

| Option | Avantage | Inconvénient |
|---|---|---|
| **Netlify** (recommandé v1) | Gratuit, HTTPS, custom domain, 10 min | Compte à créer au nom UPL |
| **Cloudflare Pages** | Rapide, DNS lié | Courbe légère |
| **GitHub Pages** | Lié au repo | Moins « marque » |
| **OVH / hébergeur classique** | Si déjà compte | Plus lourd pour du statique |

**Décision à cocher :**

- [ ] Hébergeur : ☐ Netlify ☐ Cloudflare Pages ☐ GitHub Pages ☐ Autre
- [ ] Compte créé avec e-mail : `________________` (idéalement la future `contact@`)
- [ ] URL provisoire : `https://________.netlify.app`
- [ ] Domaine branché (après DNS) : `https://www.________`

### Déploiement Netlify en 10 minutes

1. Créer compte Netlify (e-mail contrôlé par UPL/Calvin)
2. « Add new site » → **Deploy manually** → glisser le dossier `upl-web`
3. Noter l’URL `xxx.netlify.app`
4. Quand le domaine + DNS sont prêts : Domain settings → Add custom domain
5. Plus tard : lier GitHub pour mises à jour

---

## 5. GitHub (reprise / ne pas perdre le site)

- [ ] Compte GitHub : `________________` (UPL ou Calvin, 2e admin = Président)
- [ ] Repo **privé** : `upl-site` ou `site-institutionnel`
- [ ] Push de ce dossier `upl-web`
- [ ] 2 owners minimum

```bash
cd upl-web
git remote add origin git@github.com:VOTRE_ORG/upl-site.git
git branch -M main
git push -u origin main
```

---

## 6. Contenu du site v1 (figé volontairement)

| Page | Contenu autorisé |
|---|---|
| Accueil | Institution + MBA + médias |
| Executive MBA | Fiche programme ouvert |
| À propos | Qui, où, ce qu’on ne promet pas |
| Contact | Tél. + message (mail dès qu’il existe) |

**Interdit sur le site v1 :**

- Licences / masters / CPGE / DBA comme offres ouvertes
- « Partenaire HEC / Polytechnique / Sciences Po »
- Adresses `@upl-gabon.com` tant qu’elles ne reçoivent pas
- Grilles tarifaires multi-filières
- Master Plan 3,5 Md en vitrine grand public (sauf page privée plus tard)

Quand un partenaire réel exigera un bachelor / un autre format : **on modifiera le site à ce moment-là**.

---

## 7. Ordre d’exécution (ne pas sauter)

| Étape | Action | Fait ? |
|---|---|---|
| 1 | Trancher domaine (A1/A2/A3) | ☐ |
| 2 | Créer / récupérer compte registrar | ☐ |
| 3 | Choisir provider mail + payer 1er mois | ☐ |
| 4 | Créer `contact@` (+ 1 boîte MBA) | ☐ |
| 5 | Compte Netlify UPL + déployer `upl-web` | ☐ |
| 6 | Mettre `contact@` dans `contact.html` (`data-mailto`) | ☐ |
| 7 | Brancher le domaine sur Netlify | ☐ |
| 8 | Repo GitHub privé | ☐ |
| 9 | Signature mail + test d’envoi/réception | ☐ |
| 10 | **Ensuite seulement** : réseaux, com, appels partenaires | ☐ |

---

## 8. Décisions à me renvoyer (réponses courtes)

Répondez sur ces lignes pour qu’on configure la suite sans ambiguïté :

1. Domaine retenu : `_______________________________`
2. On a déjà le DNS ? ☐ oui ☐ non ☐ je ne sais pas
3. Provider mail : ☐ Google ☐ Microsoft ☐ Zoho ☐ autre ______
4. Hébergeur site : ☐ Netlify ☐ autre ______
5. E-mail qui doit apparaître sur le site : `________________`
6. Téléphone WhatsApp officiel unique (si un seul) : `________________`

---

## 9. Hors scope jusqu’à la fin de l’étape 9

- Sciences Po, Polytechnique, CentraleSupélec, HEC, etc.
- Nouvelles filières sur le site
- Campagne TikTok / Meta ads
- Refonte lourde multi-langues
- Ancien prestataire (sauf transfert domaine documenté)

---

*Document prioritaire du dépôt `upl-web`. Tout le reste attend cette décision.*
