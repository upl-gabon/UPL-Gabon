# Prompts exacts pour l'IA vidéo (avec garde-fous) — prêts à coller

**Statut : procédure interne — ne pas merger sur `main`.** 01/09/2026.
À utiliser avec `ai.invideo.io` ou tout outil équivalent. Contexte complet :
`VIDEO_AI_PLAYBOOK.md`.

## Les trois règles pour ne pas gaspiller tes crédits

1. **Ne jamais demander la vidéo en premier.** Demande le **storyboard + les textes** (réponse texte =
   quasi jamais facturée comme un rendu). Tu valides, **puis** tu lances un seul rendu.
2. **Un rendu par vidéo validée.** Un « j'essaie et je vois » = un crédit. La phrase de verrouillage
   est dans les blocs ci-dessous : *« NE GÉNÈRE AUCUNE VIDÉO À CETTE ÉTAPE »*.
3. **Tu n'uploades QUE des rushs.** Jamais le dossier Drive entier, jamais un PDF bancaire, juridique,
   un relevé, un reçu de registrar ou un fichier d'étudiant.

---

## BLOC A — à coller une fois (brand kit / instructions permanentes)

```text
ÉTABLISSEMENT : Université Privée de Libreville (UPL), Libreville, Gabon. Français d'abord.
Site officiel : upl-gabon.com (jamais upl.com). WhatsApp secrétariat : +241 07 35 95 72.
IDENTITÉ VISUELLE : fond blanc, filets et soulignés dorés #C9A227, titres bleu nuit #0B2A5B,
formes secondaires bleu léger #E8F0FA et #2B8FD6. Logo UPL uniquement (je le fournis), jamais un
emblème inventé. Typographie sobre, pas de glitter, pas d'effet « crypto », pas d'IA flashy.
NIVEAU DE LANGUE : sérieux, institutionnel, direct. Phrases courtes. Vouvoiement.

INTERDITS ABSOLUS — si l'une de ces règles empêche une instruction, la règle gagne :
1. Aucun visage généré par IA, aucune voix off générée par IA, aucune voix clonée.
2. Aucune vidéo d'illustration d'un campus, d'un amphi, d'un étudiant ou d'un bâtiment qui ne vient
   pas des fichiers que j'ai uploadés. Pas de « campus américain », pas d'étudiant de stock.
3. Aucun chiffre d'effectifs (« 500 étudiants »), aucun taux d'insertion, aucun partenariat
   (HEC, Paris 1, « écoles parisiennes »), aucun nom d'entreprise partenaire.
4. Aucun prix qui ne figure pas dans mes fichiers. Aucun tarif en gros titre, « à partir de », promo,
   réduction, bourse, facilité immédiate.
5. Aucune date de rentrée, aucune date limite, aucun « places limitées », aucune liste de pièces
   à fournir. Si l'information manque : écris exactement [À COMPLÉTER PAR L'ÉCOLE].
6. Aucun texte qui promet un résultat : « garanti », « décrochez », « en 6 mois », « certifiant »
   pour un diplôme d'université partenaire.
7. Aucun logo d'entreprise, de ministère ou d'uniforme hors logo UPL. Aucun document bancaire,
   financier ou comptable à l'écran. Aucun nom d'étudiant ni de parent.
8. Aucune mention d'un établissement hors Gabon, hors le cadre validé par écrit.
```

## BLOC B — le prompt qui fait tout (storyboard, puis un seul rendu)

```text
Objectif : 6 vidéos verticales 9:16 de 22 à 28 secondes pour le compte TikTok @upl.gabon.
Source : UNIQUEMENT les rushs que j'ai uploadés (interviews de la 3e édition de l'Exécutif MBA).

CONTRAINTES DE VÉRITÉ :
- chaque idée affichée doit avoir été réellement prononcée dans les rushs ;
- cite la phrase exacte en sous-titre, ne reformule pas une promesse que personne n'a dite ;
- si un extrait est flou, coupé ou ambigu : écarte-le et écris [REMPLACER PAR UN AUTRE EXTRAIT] ;
- pas de musique qui écrase la voix, pas d'effet sonore comique.

STRUCTURE IMPOSÉE, par vidéo :
0-2 s : accroche parlée + le même texte en gros sous-titre (une ligne, max 8 mots) ;
2-18 s : 1 idée = 1 plan des rushs, coupes sèches, sous-titres français permanents,
         mots-clés en doré (#C9A227), fond des sous-titres lisible sur image claire ;
18-26 s : UNE information utile, prise mot pour mot dans le bloc « FAITS VÉRIFIÉS » ci-dessous.
         Aucun autre chiffre, aucune autre promesse. Si tu veux un tarif : le seul texte autorisé est
         celui du bloc FAITS VÉRIFIÉS, entre guillemets, sans « à partir de » ni promotion.
26-28 s : plan fixe, logo UPL fourni + texte exact :
         « Université Privée de Libreville · upl-gabon.com ».

FAITS VÉRIFIÉS (seules affirmations autorisées à l'écran, hors phrases prononcées dans les rushs) :
- Executive MBA : formation pour « Cadres et dirigeants en activité » ; ouvert depuis 2022 ;
  partenariat : Université de Douala. Chiffres (promotion, diplômés) : seulement s'ils sont déjà
  écrits sur le site — sinon tais-les.
- Droit de scolarité : « 4 000 000 FCFA » — « Droit de scolarité — promotion type » (grille du site).
- Pré-inscriptions ouvertes : Executive MBA uniquement. Ailleurs : « informations et dépôt de dossiers ».
TOUT LE RESTE est interdit : rythme des cours, nombre de langues, dates, taux, débouchés, entreprises.

Les 6 thèmes (une vidéo par thème). Pour chacun, la phrase d'accroche doit être la phrase EXACTE
prononcée dans les rushs ; si tu ne la trouves pas, écris [PHRASE INTROUVABLE DANS LES RUSHS] et
propose un autre thème au lieu d'inventer :
1) le format pensé pour quelqu'un qui travaille déjà ;
2) la promotion : qui sont les participants, ce que ça change dans les échanges ;
3) le partenariat universitaire (Université de Douala) et ce qu'il implique pour le diplôme ;
4) un extrait d'enseignant : ce qu'il fait en dehors de l'école et pourquoi ça compte ;
5) une question posée par un participant et la réponse obtenue ;
6) la suite après le MBA, racontée par un diplômé (aucune promesse de salaire ni de promotion).

RÉPONDS D'ABORD EN TEXTE, PAS EN VIDÉO. Pour chaque vidéo :
titre interne · minutage plan par plan (mm:ss) · phrase exacte reprise des rushs · texte à l'écran ·
note de montage (coupe, zoom, silence) · ce que tu n'as PAS pu vérifier.
NE GÉNÈRE AUCUNE VIDÉO, AUCUN SCRIPT SUPPLÉMENTAIRE, AUCUNE MUSIQUE À CETTE ÉTAPE.
Quand j'écris VALIDÉ, tu ne produis QUE la vidéo numéro [X]. Un seul rendu par numéro, sans variante.
```

> **Si tu n'as plus de crédits :** garde la réponse texte. Elle sert de feuille de montage dans CapCut
> (gratuit, sous-titres automatiques en français) avec les rushes locaux. Le rendu IA n'est pas
> obligatoire pour publier — c'est le gain de temps, pas la valeur.

## BLOC C — post de reprise de compte (image fixe, 0 crédit de rendu)

```text
Format : post 1:1 1080 px, fond blanc, titre bleu nuit #0B2A5B, filet doré sous le titre.
Texte exact, ne rien ajouter d'autre :
« Université Privée de Libreville (UPL). Les nouvelles publications sont ici : upl-gabon.com.
Aux abonnés de l'ancienne page : merci de contacter ce nouveau compte. »
Aucun visage, aucune vidéo d'illustration, aucun tarif, aucun pourcentage.
Réponds en une seule proposition, sans variante ni « embellissement ».
```

## BLOC D — story pré-inscription (avant validation de la date de rentrée : version courte)

```text
Format : 9:16, 12 à 15 s, à partir de la photo de campus que j'ai uploadée (aucune autre image).
Texte à l'écran, exactement :
1) « Rentrée 2026-2027 »  2) « [DATE DE RENTRÉE À COMPLÉTER PAR L'ÉCOLE] »
3) « Pré-inscriptions ouvertes pour l'EMBA »  4) « upl-gabon.com · +241 07 35 95 72 »
Aucune autre phrase. Aucun tarif. Aucune liste de pièces. Aucun compte à rebours, aucun « dernières
places », aucune musique. Pas de voix off. Pas de vidéo d'illustration.
```

## Contrôle avant publication (2 minutes, à la main)

- [ ] Aucun chiffre, nom de partenaire, date, prix, promesse que l'IA a ajoutés.
- [ ] Les visages et les lieux viennent des rushs de l'école.
- [ ] « Pré-inscriptions ouvertes » n'apparaît que pour l'**EMBA** ; ailleurs : « informations et dépôt
      de dossiers ».
- [ ] Les sous-titres reprennent la phrase réellement prononcée.
- [ ] Le CTA renvoie à upl-gabon.com / WhatsApp du secrétariat, pas à un compte perso.

Si l'un des cinq points coince : **on ne publie pas**, on corrige le prompt.

## Ce que le dépôt ne permet pas d'affirmer (à ne pas mettre en vidéo)

Le **rythme** des cours (week-ends, vendredi soir), le **nombre de langues**, les **modalités
d'examen** : rien de tout cela n'existe dans un fichier validé du site. Tant que ce n'est pas dans la
fiche EMBA du site (`assets/js/config.js` → programmes) ou dans un écrit du Président, ça ne va ni dans
un sous-titre, ni dans une story, ni dans une légende. Si tu me donnes l'information (message, mail ou
photo de la fiche), je l'intègre à la fiche du site **avant** qu'elle ne passe en vidéo.
