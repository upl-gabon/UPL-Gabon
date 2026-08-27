# Publication du site — GitHub Pages + domaine officiel upl-gabon.com

> Objectif : publier le site **directement depuis GitHub** (sans dépendre de Netlify)
> sur `upl-gabon.com`, **sans jamais casser le mail** `contact@upl-gabon.com`.

## État (27/08/2026)

| Élément | État |
|---|---|
| Code + guide de publication | ✅ prêts (ce dépôt, PR à merger) |
| GitHub Pages | ⏳ à activer par un admin (Settings → Pages — 2 clics, cf. étape A) |
| Domaine officiel branché | ⏳ à faire côté Namecheap (étapes B et C ci-dessous) |
| Netlify existant | conservé en secours — **ne rien supprimer** |

## Étape A — GitHub Pages (à activer par un admin du compte upl-gabon)

1. (Si pas déjà fait) merger la Pull Request de passation sur `main`.
2. Dépôt → **Settings → Pages** → Source : *Deploy from a branch* → branche `main` → dossier `/ (root)` → Save.
3. L'URL `https://upl-gabon.github.io/UPL-Gabon/` sert alors le site.

> Note : l'agent Arena ne peut pas activer Pages ni changer la visibilité du dépôt
> (réservé aux admins). Si le dépôt est **privé** et que l'offre GitHub du compte
> `upl-gabon` est l'offre gratuite, Pages exige alors une offre payante (GitHub Pro)
> **ou** un dépôt public. Voir § « Confidentialité ».

## Étape B — DNS chez Namecheap (10 minutes)

⚠️ **RÈGLE ABSOLUE : ne pas modifier les enregistrements MX / SPF / DKIM** (mail PrivateEmail).

Dans **Namecheap → Domain List → upl-gabon.com → Advanced DNS** :

1. **Sous-domaine www** : `CNAME` · Host `www` · Value `upl-gabon.github.io` · TTL Auto
   (supprimer l'éventuel ancien CNAME www pointant vers Netlify **uniquement après validation finale**)
2. **Domaine racine (apex)** : 4 enregistrements `A` · Host `@` · TTL Auto :
   - `185.199.108.153`
   - `185.199.109.153`
   - `185.199.110.153`
   - `185.199.111.153`
3. Laisser **tous les enregistrements mail (MX, SPF/TXT, DKIM/CNAME mail)** strictement inchangés.

## Étape C — Brancher le domaine dans GitHub

1. Dépôt → **Settings → Pages → Custom domain** : saisir `upl-gabon.com` → Save.
2. Attendre le check DNS (quelques minutes à 24 h).
3. Cocher **Enforce HTTPS** (certificat automatique).
4. Vérifier : `https://upl-gabon.com`, `https://www.upl-gabon.com` → même site.

## Vérifications post-basculement

- [ ] Mail `contact@upl-gabon.com` : **envoi + réception** OK (le mail passe par Namecheap, pas par le site)
- [ ] Site accessible en `https://` sur apex et www
- [ ] `npm test` vert sur `main`
- [ ] Ancien déploiement Netlify laissé intact (optionnel : le débrancher du DNS seulement après quelques jours de recul)

## Rollback

Le DNS fait foi : repointer `@`/`www` vers Netlify dans Namecheap = retour arrière immédiat, sans perte.

## Confidentialité

- Le dépôt contient des documents internes (`HANDOVER.md`, `docs/`, PDF de reprise) : le dépôt
  **doit rester privé** (recommandation du PDF global § 2.1).
- Si Pages est utilisé depuis un dépôt privé, l'offre GitHub du compte doit le permettre ;
  sinon alternatives : (a) offre GitHub Pro, (b) dépôt public **nettoyé** de tout document interne
  (garder uniquement le code du site), (c) conserver Netlify.
- Ne jamais stocker de mots de passe GitHub / PrivateEmail / Namecheap dans le dépôt.
