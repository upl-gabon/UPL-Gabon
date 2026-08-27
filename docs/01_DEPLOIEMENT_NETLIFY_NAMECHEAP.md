# Déploiement site UPL — Netlify + Namecheap

**Décidé :**
- Mail public : `contact@upl-gabon.com` (PrivateEmail / Namecheap) — **actif**
- DNS domaine : Namecheap (lié PrivateEmail)
- Site : vitrine minimale (MBA only)

---

## A. Mettre le site en ligne (15 min) — Netlify

1. Aller sur https://app.netlify.com — créer un compte avec un mail **que vous contrôlez**  
   (idéal : `contact@upl-gabon.com` ou mail Calvin en attendant)
2. **Add new site** → **Deploy manually**
3. Glisser-déposer le dossier `upl-web` (celui qui contient `index.html`)
4. Noter l’URL : `https://xxxxx.netlify.app`
5. Tester : Accueil, MBA, Contact, clic mail → doit ouvrir `contact@upl-gabon.com`

### Option Git (mieux pour la suite)
1. Créer repo GitHub privé `upl-site`
2. Pousser `upl-web`
3. Netlify → Import from Git → build vide, publish directory = `/`

---

## B. Brancher `www.upl-gabon.com` (Namecheap)

Dans **Namecheap** → Domain List → `upl-gabon.com` → **Advanced DNS**

### Ne pas casser le mail
PrivateEmail utilise déjà des enregistrements **MX** (et souvent TXT SPF).  
**Ne supprimez pas** les MX / SPF / DKIM existants.

### Ajouter pour Netlify (site)

Netlify vous donnera, dans Domain settings, soit :
- un **CNAME** pour `www`, soit des instructions A/ALIAS.

**Cas standard Netlify :**

| Type | Host | Value | TTL |
|---|---|---|---|
| CNAME | `www` | `xxxxx.netlify.app` (votre sous-domaine Netlify) | Automatic |
| URL Redirect (Namecheap) ou ALIAS/ANAME | `@` | vers `https://www.upl-gabon.com` | — |

Ou selon Netlify (certains comptes) :
| Type | Host | Value |
|---|---|---|
| A | `@` | `75.2.60.5` (IP Netlify load balancer — **vérifier dans le panel Netlify** au moment du branchement) |

**Procédure sûre :**
1. Netlify → Site → Domain management → Add custom domain → `www.upl-gabon.com`
2. Suivre **exactement** les records affichés par Netlify
3. Attendre HTTPS (Let’s Encrypt) — souvent 1–30 min
4. Forcer HTTPS dans Netlify

### Vérifications mail après DNS
```
# depuis un terminal
nslookup -type=MX upl-gabon.com
nslookup -type=TXT upl-gabon.com
```
Les MX PrivateEmail doivent toujours être là.  
Tester : envoyer un mail Gmail → `contact@upl-gabon.com` et répondre.

---

## C. Checklist post-mise en ligne

- [ ] `https://www.upl-gabon.com` ouvre l’accueil UPL
- [ ] Candide HTTPS sans alerte
- [ ] `contact@upl-gabon.com` reçoit toujours les mails
- [ ] Formulaire contact → mailto vers la bonne adresse
- [ ] Mobile OK
- [ ] 2 admins Netlify (Calvin + Président ou backup)
- [ ] Repo GitHub privé avec le code

---

## D. Contenu public figé (rappel)

Sur le site **uniquement** :
- Institution
- Executive MBA
- Contact (tél + contact@upl-gabon.com)

Pas de licences / masters / grandes écoles tant que non décidés.
