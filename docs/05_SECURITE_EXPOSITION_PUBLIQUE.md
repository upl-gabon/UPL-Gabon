# Exposition publique du dépôt — incident et remédiation

Constaté le **01/09/2026**, en vérifiant ce que le site publie réellement. **Priorité : à traiter
aujourd'hui**, avant de merger quoi que ce soit d'autre.

---

## 1. Ce qui est en ligne (vérifié, pas supposé)

Le dépôt `upl-gabon/UPL-Gabon` est **public** (`private=false`) et **GitHub Pages est activé sur la
racine** avec le domaine `upl-gabon.com`. Comme `netlify.toml` publie aussi `publish = "."`, tout le
contenu du dépôt est servi, y compris la partie interne. URLs testées à l'instant :

| URL | Contenu réellement accessible |
|---|---|
| `upl-gabon.com/HANDOVER.md` | passation complète : numéros personnels, Gmail personnel de l'appui digital, arbitrage « ce qui n'est PAS vrai », dossier bancaire mentionné, historique des décisions |
| `upl-gabon.com/docs/com/00_COMPTES_NEUFS_CONTACT_UPL.html` | procédure des comptes réseaux, e-mail de reprise des Pages payées, litige agence, nom du compte WhatsApp personnel |
| `upl-gabon.com/docs/BRIEF_Partenariats_France_UPL.html` (et `docs/com/LANCEMENT_…`) | **contenaient le lien direct du dossier Drive de l'école** — dossier qui mélange visuels de com, dossier bancaire 80 M, annexes juridiques, facture du registrar |

Le lien Drive a été **retiré des fichiers de ce dépôt** (ce commit). Mais deux choses restent vraies :

1. **le dossier Drive est lisible sans authentification** — c'est le vrai problème, côté Google, pas côté GitHub ;
2. **le texte des fichiers déjà publiés est dans l'historique git** (et potentiellement dans le cache
   de Google/Archive.org). Retirer le fichier du dépôt ne le retire pas de l'histoire.

## 2. À faire maintenant, dans cet ordre

| # | Action | Où | Délai |
|---|---|---|---|
| 1 | Dossier Drive → **Partager → Restreint** (uniquement les adresses UPL) ; puis créer `UPL – Communication` (visuels seuls) et garder `UPL – Banque & juridique` **hors de tout lien** | Google Drive | 15 min |
| 2 | Vérifier que personne d'extérieur n'a demandé accès au dossier (Drive → *Détails du partage* → demandes en attente ; et l'onglet « Activité ») | Google Drive | 5 min |
| 3 | Publier ce dépôt en **excluant les docs** : le fichier `_config.yml` ajouté ici dit à Jekyll de ne pas générer `docs/`, `HANDOVER.md`, `README.md`, `tests/` ; `netlify.toml` renvoie les mêmes chemins en 404. **Merger puis contrôler** les trois URLs du § 1 : elles doivent rendre 404 | GitHub (merge) | 10 min |
| 4 | Décision structurelle (voir § 3) : dépôt privé + Netlify pour le site, **ou** deux dépôts (site public / interne privé) | Président + appui | cette semaine |
| 5 | Purger l'historique si le contenu sensible doit disparaître durablement : nouveau dépôt propre à partir de l'arborescence actuelle, sans l'ancien historique, et suppression du dépôt public (ou bascule en privé) | appui digital, **avec accord écrit du Président** | quand #4 est tranché |
| 6 | Considérer comme **publiques** les informations déjà exposées : numéro et Gmail de l'appui digital, arbitrages internes, existence du dossier bancaire, URL du Drive. En tirer les conséquences (ne plus mettre de donnée personnelle dans un dépôt, même privé) | — | continu |

## 3. Les deux architectures possibles (à trancher, pas les deux)

| Option | Ce qu'on fait | Conséquences |
|---|---|---|
| **A. Un seul dépôt privé** (recommandée) | `Settings → General → Danger zone → Change visibility → Private`. Le site est servi par **Netlify** (déjà configuré, `publish = "."`), le DNS `upl-gabon.com` pointe vers Netlify au lieu de GitHub Pages | Pages gratuit disparaît → Netlify gratuit prend le relais ; le site peut ne pas répondre pendant les modifications DNS ; **ne jamais** toucher aux MX ; les docs internes ne sont plus publiés. ⚠️ GitHub Pages sur un dépôt privé exige un plan payant : c'est pour ça que le site passe chez Netlify |
| **B. Deux dépôts** | `upl-gabon/site-web` (public, **sans** `docs/` ni `HANDOVER.md`, Pages activé) + `upl-gabon/com-interne` (privé, tout le kit com) | le site garde GitHub Pages ; mais la séparation est à maintenir à la main à chaque session, et le dépôt public garde l'historique actuel → à créer **neuf**, sans historique |

Dans les deux cas : 2 admins minimum, 2FA par application, et **aucun** mot de passe, jeton ou code de
secours dans un fichier du dépôt (règle déjà écrite dans le kit com).

## 4. Garde-fous automatiques ajoutés aux tests

`npm test` vérifie désormais :

- `_config.yml` exclut bien `docs`, `HANDOVER.md` et ne casse pas le domaine (`CNAME` conservé) ;
- `netlify.toml` renvoie `/docs/*`, `/HANDOVER.md`, `/README.md` en 404 ;
- **aucune URL `drive.google.com`** dans le dépôt ;
- aucun e-mail personnel (gmail) dans un fichier publié (`index.html`, `en/`, `assets/`).

Si un futur commit réintroduit un lien Drive ou un document personnel dans la racine, la CI casse.
