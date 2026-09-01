# E-mails — où ça arrive, qui répond, comment on redirige

**Statut : procédure interne — ne pas merger sur `main`.**
Mise à jour : 01/09/2026. Question traitée : *« rediriger les mails vers les comptes / les adresses »*,
dans les deux sens — ce qui **entre** dans la boîte de l'école, et l'adresse qui **identifie** l'école
sur chaque plateforme.

---

## 1. Le principe, en une ligne

**Une seule adresse publique : `contact@upl-gabon.com`.** Tout le reste (étiquettes, alias,
notifications des réseaux, WhatsApp) n'est que de la **distribution** autour de cette boîte.
Un candidat, un parent, un DRH ou un recteur doit pouvoir écrire à cette seule adresse et être
rappelé, quel que soit le canal par lequel il est entré.

Trois conséquences non négociables :

1. **la boîte de référence reste `contact@` sur Private Email (Namecheap)** : ne pas toucher aux
   **MX** du domaine — c'est ce qui ferait perdre la messagerie de l'école ;
2. **les réseaux s'ouvrent et se récupèrent avec cette adresse**, jamais avec un Gmail personnel :
   Facebook, Instagram, TikTok, LinkedIn, YouTube, Google, GitHub, Netlify, registrar ;
3. **aucune adresse inventée n'est publiée.** `admissions@`, `partenariats@`, `presse@` : on peut les
   créer comme *alias internes* (§ 4), elles n'apparaissent **pas** sur le site ni dans une bio avant
   le test d'envoi/réception et l'accord écrit du Président.

---

## 2. Schéma cible

```
        Facebook / Instagram      TikTok        LinkedIn (Page)      WhatsApp (Président)
              │  inbox             │  DM          │  messages          │  conversations
              └───── notifications par e-mail ───┴────────────────────┘
                                    │
                                    ▼
                    contact@upl-gabon.com   ← boîte de référence (Private Email / Namecheap)
                    · alias entrants (§ 4A) · réception Gmail via IMAP (§ 4C)
                                    │
                     étiquettes par objet (§ 5) : Pré-inscription · MBA · Partenariat ·
                     Abonnement · Presse · Paiement/réclamation
                                    │
                                    ▼
                    réponse sous 48 h ouvrées — texte P10 (TEXTES_A_VALIDER.md)
```

Ce qui est **déjà** en place : le site (formulaire + boutons du bandeau d'action) envoie déjà vers
`contact@` avec un **objet préfixé** (`Candidature MBA`, `Partenariat`, `Abonnement actualités`, …) —
c'est exactement ce que les étiquettes § 5 exploitent. Rien à changer côté site pour router.

---

## 3. Le compte Google ouvert avec l'adresse UPL : ce qu'il est, ce qu'il n'est pas

Ce qui a été fait (bon réflexe) : un **compte Google ordinaire**, ouvert avec une adresse de l'école.
Il donne Gmail, Drive, YouTube et la **fiche d'établissement Google** — sans créer de doublon avec une
Page Facebook ou une Page LinkedIn, qui sont d'autres objets, sur d'autres réseaux.

| | Le compte Google UPL | Une « Page » sur un réseau social |
|---|---|---|
| Rôle | outil de travail + annuaire (fiche d'établissement, YouTube, Drive) | vitrine avec abonnés et commentaires |
| Audience | ceux qui cherchent l'école sur Google | la communauté UPL |
| Ce qu'il faut y coller | la description § 4.7 de `BIOS_RESEAUX_2026.md` | la bio du réseau concerné |

**Les quatre fragilités d'un compte « particulier », et la parade :**

| Risque | Parade (à faire cette semaine) |
|---|---|
| Compte au nom d'une **personne physique** : si le compte est déclaré comme personnel, Google peut le bloquer au nom de l'usurpation d'identité | créer le compte au **nom de l'institution** (Prénom = « Université Privée », Nom = « de Libreville ») avec le mail `contact@`, et ne jamais y faire semblant d'être un élève ou un enseignant identifié |
| **Un seul détenteur** de mot de passe : mot de passe perdu ou personne partie = Drive, chaîne YouTube et fiche d'établissement perdus | 2ᵉ accès : ajouter un second utilisateur **propriétaire du compte** (Google : « Ajouter une personne de confiance » / reprise de compte) + 2ᵉ **gestionnaire** sur la fiche d'établissement |
| **Récupération** branchée sur un Gmail personnel | e-mail et téléphone de récupération = **boîte `contact@` et numéro UPL**, jamais un Gmail privé |
| Récupération du compte **impossible** si la boîte `contact@` est elle-même fermée un jour | le compte registrar (Namecheap) et la boîte `contact@` doivent avoir **2 admins UPL** ; codes de secours 2FA dans une enveloppe au secrétariat (pas dans GitHub, pas dans un chat) |

**Passage à une vraie messagerie d'établissement (plus tard, pas maintenant) :** quand l'UPL aura
3 boîtes ou plus à faire tourner, un **Google Workspace Business Starter** ou **Zoho Mail** sur le même
domaine règle d'un coup l'annuaire, les aliases, la co-administration et la récupération de compte.
Décision à prendre par le Président (coût par utilisateur et par mois, domaine et MX à déplacer en
conséquence) — **après** la campagne, pas pendant.

---

## 4. Rediriger concrètement — trois niveaux, à activer dans cet ordre

### A. Alias dans Private Email (recommandé, zéro risque sur les MX)

1. Interface admin Private Email → **Mailboxes** → la boîte `contact@` → **Aliases** → *Add alias*.
2. Créer selon les besoins réels du secrétariat : `secretariat@upl-gabon.com`, `mba@upl-gabon.com`.
3. Un alias **ne reçoit pas pour son propre compte** : il livre dans la boîte `contact@`, et les
   réponses partent de `contact@`. C'est exactement ce qu'on veut : rien ne se perd, une seule boîte.
4. Activer l'**alias « catch-all »** du domaine si l'option est disponible (un parent qui écrit
   `contact@upl-gabon.ga`, `upl@…`, `info@…` arrive quand même dans la boîte UPL).
5. **Publication :** l'alias n'apparaît nulle part avant qu'un envoi de test depuis un autre
   fournisseur n'ait été reçu, et que le Président n'ait validé. En pratique : publier `contact@`,
   garder les alias pour l'interne et les signatures.

### B. Lire (et répondre) depuis le compte Google — transfert

1. Gmail → Paramètres → **Transfert et POP/IMAP** → ajouter une adresse de transfert.
2. **Relevé systématique** du courrier : dans Private Email, activer la redirection vers l'adresse
   Gmail **en conservant une copie dans la boîte d'origine** (jamais de redirection « sèche » :
   la boîte `contact@` doit rester l'archive légale de l'école).
3. Pour **répondre en tant que** `contact@upl-gabon.com` depuis Gmail : *Comptes et importation →
   Envoyer un e-mail en tant que* → SMTP `mail.privateemail.com`, port **465** (SSL) ou **587**,
   identifiants de la boîte `contact@`. Si le relais SMTP est refusé, on répond depuis le webmail
   Private Email — on n'utilise **jamais** une adresse personnelle pour répondre à un candidat.
4. Vérifier après coup : un mail envoyé doit passer **SPF + DKIM** (sinon il part en spam chez
   les entreprises et les écoles partenaires). Test : s'écrire depuis Gmail à soi-même, ouvrir
   « Afficher l'original », chercher `spf=pass` et `dkim=pass`.

### C. Alternative plus robuste : IMAP depuis Gmail (pas de transfert)

Private Email → IMAP activé → Gmail *Consulter le courrier d'autres comptes* :
`mail.privateemail.com`, port **993**, SSL, boîte `contact@`, case « toujours utiliser une adresse
de secours » cochée avec le SMTP du § B.3. Avantage : Gmail n'est qu'un **poste de consultation**,
la messagerie de référence reste celle de l'école ; supprimer l'accès IMAP suffit à couper le lien,
sans rien perdre.

> À retenir pour le secrétariat : **la boîte `contact@` est la mémoire de l'école.** Gmail, WhatsApp,
> la Page Facebook : ce sont des vitrines. Tout ce qui a de la valeur (dossier candidat, reçu,
> convention, échange partenaire) doit être **archivé dans `contact@`** et dans le Drive de l'institution.

---

## 5. Router sans créer de boîte : étiquettes par objet

Le site et les posts utilisent déjà des objets fixes. Chaque objet = une étiquette, un responsable, un
délai. À configurer en 10 minutes dans Gmail (*Filtres → Créer un filtre → critères « sujet:… » →
Appliquer l'étiquette + Ne jamais envoyer dans Spam*) ou dans les filtres Private Email.

| Objet reçu | Étiquette | À qui c'est transmis | Délai promis |
|---|---|---|---|
| `Pré-inscription 2026-2027` | **Pré-inscriptions** | secrétariat | 48 h ouvrées, accusé P10 |
| `Candidature MBA` | **MBA** | secrétariat + Président (hebdo) | 48 h ouvrées |
| `Demande de rendez-vous` | **RDV** | secrétariat, puis validation d'un créneau | 48 h ouvrées |
| `Partenariat` | **Partenariats** | Président seul décide | réponse d'intérêt sous 7 jours |
| `Abonnement actualités` | **Lettre d'info** | secrétariat (liste de diffusion WhatsApp + tableur) | accusé simple |
| `Paiement` / `Reçu` / réclamation | **Scolarité** | secrétariat, copie Président | sous 24 h — sujet sensible |
| Presse, télévision, institution | **Presse** | Président, via secrétariat | pas d'engagement sans lui |

Deux règles de tenue : **un mail classé = un mail répondu** (une étiquette « en attente » par
dossier, vidée chaque vendredi), et **aucun dossier d'inscription dans une boîte personnelle** —
les pièces des candidats restent dans la boîte de l'école et le Drive de l'institution.

---

## 6. Les boîtes de réception des réseaux, elles aussi, rentrent dans `contact@`

| Réseau | Où arrivent les messages | Réglage à faire | Règle d'écriture |
|---|---|---|---|
| Facebook + Instagram (Meta) | **Boîte de réception Meta Business Suite** | Notifications par e-mail **vers `contact@`**, réponses depuis la Page (jamais depuis le profil) | chaque échange avec un candidat est **copié** dans un mail `Pré-inscription — {nom}` |
| TikTok | Messages du compte Pro | e-mail de notification sur `contact@` | réponse courte + bascule vers WhatsApp ou mail |
| LinkedIn (Page) | Messages de la Page + notifications | recevoir les notifs sur `contact@` | objet `Candidature MBA` pour les cadres |
| WhatsApp Business (Président) | téléphone du secrétariat | réponses rapides P10 / P6 / P7 ; étiquettes par formation | **jamais** d'engagement tarifaire écrit hors grille du site |
| Fiche d'établissement Google | questions / avis | répondre sous 7 jours, ton sobre | on ne promet ni date de rentrée ni bourse |

**Le geste qui évite tous les trous :** dans les 24 h, tout contact reçu sur un réseau est
**recopié par e-mail** vers `contact@` avec l'objet de l'étiquette correspondante (nom, téléphone,
formation souhaitée, ce qui a été répondu). Un stagiaire, un appui ponctuel ou un prestataire peut
partir : le lead, lui, reste dans la boîte de l'école.

---

## 7. Accusé de réception — le seul texte à copier-coller

Utiliser la pièce **P10** de `TEXTES_A_VALIDER.md` (accusé de réception secrétariat), et la signature
du § 3 de `BIOS_RESEAUX_2026.md`. Ni « bienvenue à bord », ni promesse, ni délai non tenable.

---

## 8. À faire cette semaine (une séance de 45 minutes)

- [ ] Alias créés dans Private Email (`secretariat@`, puis `mba@`) — **non publiés** (étape A)
- [ ] Catch-all du domaine activé si disponible
- [ ] IMAP ou transfert configuré pour lire `contact@` depuis le compte Google, **avec copie conservée**
- [ ] Test « Envoyer en tant que » depuis Gmail → un mail à une adresse extérieure → vérifier `spf=pass dkim=pass`
- [ ] 7 étiquettes + 7 filtres créés (§ 5)
- [ ] Notifications e-mail activées sur Meta, TikTok, LinkedIn → `contact@` (§ 6)
- [ ] Compte Google : e-mail + téléphone de récupération = UPL ; personne de confiance ajoutée (§ 3)
- [ ] 2FA par application sur les 6 comptes + codes de secours sous enveloppe au secrétariat

## 9. Ce qu'on ne fait pas

- Pas de **chaîne d'envoi** ni de publipostage sauvage vers des adresses achetées (liste de diffusion
  = uniquement des personnes qui ont écrit à l'UPL, sur WhatsApp ou par e-mail).
- Pas d'auto-réponse commerciale, pas de « promo », pas de compte de secours perso pour dépanner.
- Pas de réponse depuis `calvin…@gmail` ou tout Gmail d'un tiers, même ponctuellement.
- Pas de publication d'une nouvelle adresse avant le test de réception et l'accord écrit du Président.
