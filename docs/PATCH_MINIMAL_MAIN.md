# Les 5 minutes qui coupent la fuite — à appliquer sur `main` depuis l'interface GitHub

Le correctif est déjà dans cette branche (`_config.yml`, `netlify.toml`, `assets/js/config.js`, liens
Drive retirés). **Mais GitHub Pages publie `main`, pas ma branche** : tant que ces modifications ne sont
pas sur `main`, les URLs du § 1 de `05_SECURITE_EXPOSITION_PUBLIQUE.md` restent lisibles.

Comme `docs/com/` ne doit jamais être mergé, **ne pas ouvrir de PR depuis cette branche**. Faire les
4 micro-modifications à la main sur `main` (bouton ✏️ / **Add file → Create new file**, puis *Commit
directly to main*). Chacune est indépendante et réversible.

## 1. Créer le fichier `_config.yml` à la racine (le plus important)

**Add file → Create new file** → nom : `_config.yml` → coller exactement :

```yaml
# GitHub Pages (Jekyll) — le dépôt contient du matériel interne qui ne doit PAS être publié.
# Pages publie la racine ; ces exclusions retirent les docs du site généré.
# ⚠️ Ne pas ajouter `.nojekyll` : sans Jekyll, tout est copié tel quel et les docs republient.
# CNAME est conservé (domaine upl-gabon.com).
exclude:
  - docs
  - tests
  - HANDOVER.md
  - README.md
  - package.json
  - netlify.toml
  - _config.yml
```

## 2. Coller ces lignes à la **fin** de `netlify.toml` (hébergement de secours)

```toml
# Matériel interne jamais publié (miroir de _config.yml côté GitHub Pages).
[[redirects]]
  from = "/docs/*"
  to = "/"
  status = 404
  force = true

[[redirects]]
  from = "/HANDOVER.md"
  to = "/"
  status = 404
  force = true

[[redirects]]
  from = "/README.md"
  to = "/"
  status = 404
  force = true
```

## 3. Effacer le lien Drive dans les deux fichiers qui le contiennent

`docs/BRIEF_Partenariats_France_UPL.md`, **ligne 157** :

```text
**Drive :** https://drive.google.com/drive/folders/1bGyjIui… (ID complet dans le fichier, non recopié ici)
```

→ remplacer par :

```text
**Drive :** lien du dossier donné par le secrétariat (ne jamais l'écrire dans un fichier du dépôt)
```

`docs/com/LANCEMENT_COM_RENTREE_2026.md`, **ligne 104** : même URL au début de la ligne
(`Drive interne : https://drive.google.com/…`), même remplacement. Le fichier ne doit plus contenir
l'ID du dossier : c'est précisément ce qui a fuité.

## 4. Retirer les coordonnées personnelles de `assets/js/config.js`

`assets/js/config.js`, **lignes 44 à 56** (du commentaire `/** Calvin Blanchard MINANG …` jusqu'au
`},` qui ferme `calvinEmergency`) → **supprimer ce bloc** et le remplacer par :

```js
    /* Les coordonnées personnelles (appui digital, portable privé, Gmail) ne sont PAS ici :
       config.js est chargé par le navigateur de n'importe quel visiteur. Elles vivent dans
       docs/CONTACTS_HORS_SITE.md — jamais dans un fichier publié. */
```

Aucune page du site n'utilise ce bloc (vérifié) : rien ne casse côté affichage. Les coordonnées sont
recopiées dans `docs/CONTACTS_HORS_SITE.md` sur cette branche, et la règle est rappelée au § 4 de
`README.md`.

## 5. Contrôler (30 secondes)

Ouvrir, en navigation privée :

- https://upl-gabon.com/HANDOVER.md → doit afficher **404 / Page not found**
- https://upl-gabon.com/docs/com/00_COMPTES_NEUFS_CONTACT_UPL.html → **404**
- https://upl-gabon.com/ et https://upl-gabon.com/contact.html → le site doit être **normal**

Si le site entier tombe en 404 : revenir en arrière sur `_config.yml` (le `CNAME` ne doit pas être
dans la liste `exclude`) et me le dire, je corrige ici.

## Et côté Google (à faire en premier, avant tout le reste)

Dossier Drive → **Partager → Restreint** (seulement les adresses `@upl-gabon.com`), puis séparer en deux
dossiers : `UPL – Communication` (visuels seuls) et `UPL – Banque & juridique` (jamais liené). Le texte
déjà publié reste dans l'historique du dépôt et possiblement dans le cache de Google : considérer le
numéro et le Gmail de l'appui digital, l'existence du dossier bancaire et l'URL du Drive comme **publics**
— d'où les points 3 et 4.
