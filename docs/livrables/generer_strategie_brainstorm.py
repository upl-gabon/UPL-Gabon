#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Stratégie de communication « offensive » — support de brainstorm pour le Président.
Idées classées par famille, avec pitch, coût, risque, impact et ce qui peut mal tourner.
Document de travail INTERNE Présidence — ne pas diffuser.
"""
import os
from reportlab.lib.units import cm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle

from generer_livrables import (Doc, P, S, section, styled_table,
                               BLUE, BLUE_DK, GOLD, GOLD_LT, BLUE_LT, GREY, RED, GREEN)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "UPL_Strategie_Com_Brainstorm_President.pdf")

S["pitch"] = ParagraphStyle("pitch", parent=S["body"], fontSize=9.0, leading=12.6,
                            alignment=TA_JUSTIFY, spaceAfter=3)
S["idea"] = ParagraphStyle("idea", fontName="Helvetica-Bold", fontSize=9.6,
                           leading=12, textColor=BLUE)
S["tag"] = ParagraphStyle("tag", fontName="Helvetica-Bold", fontSize=7.8, leading=10,
                          textColor=GREY, alignment=TA_CENTER)

def card(num, titre, pitch, cout, delai, risque, impact, danger):
    head = Table([[P(num, "tag"), P(titre, "idea"),
                   P(f"Risque {risque}/5", "tag"), P(f"Impact {impact}/5", "tag")]],
                 colWidths=[1.0*cm, 11.6*cm, 2.4*cm, 2.2*cm],
                 style=TableStyle([
                     ("BACKGROUND", (0, 0), (0, 0), GOLD),
                     ("BACKGROUND", (2, 0), (-1, 0), BLUE_LT),
                     ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                     ("BOX", (0, 0), (-1, -1), 0.4, GOLD),
                     ("LEFTPADDING", (0, 0), (-1, -1), 4),
                     ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                     ("TOPPADDING", (0, 0), (-1, -1), 3),
                     ("BOTTOMPADDING", (0, 0), (-1, -1), 3)]))
    meta = Table([[P(f"<b>Coût :</b> {cout}", "cell"), P(f"<b>Délai :</b> {delai}", "cell"),
                   P(f"<b>Si ça dérape :</b> {danger}", "cell")]],
                 colWidths=[3.6*cm, 3.4*cm, 10.2*cm],
                 style=TableStyle([
                     ("VALIGN", (0, 0), (-1, -1), "TOP"),
                     ("LEFTPADDING", (0, 0), (-1, -1), 4),
                     ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                     ("TOPPADDING", (0, 0), (-1, -1), 2),
                     ("BOTTOMPADDING", (0, 0), (-1, -1), 2)]))
    from reportlab.platypus import KeepTogether
    return KeepTogether([head, Spacer(1, 2), P(pitch, "pitch"), meta, Spacer(1, 7)])

def build():
    st = []
    st += [P("Document de travail interne - Présidence uniquement - ne pas diffuser", "kicker"),
           P("Stratégie de communication 2026-2027", "h1"),
           P("Boîte à idées pour le brainstorm du Président - version offensive, sans langue de "
             "bois. Rien ici n'est décidé : chaque idée se note, se challenge, se retient ou se "
             "jette. Objectif : remplir les 9 salles du nouveau bâtiment et faire de l'UPL "
             "l'école dont tout Libreville parle avant décembre 2026.", "body"),
           Spacer(1, 4)]

    # 0. Lire le terrain
    st += section("0. Le terrain, dit franchement")
    st += [P("<b>Ce qui joue contre nous :</b> personne ne connaît l'UPL hors des cercles MBA ; "
             "« université privée » rime avec « usine à diplômes » dans la tête des parents ; "
             "les gens doutent de tout ce qui n'est pas Omar Bongo ; le budget (15 M) est 10 fois "
             "plus petit que celui des banques, pas des écoles."),
           P("<b>Ce qui joue pour nous :</b> un Président fonctionnaire crédible et propre ; un "
             "partenaire réel (Université de Douala) ; 80 cadres formés qui parlent de nous ; un "
             "bâtiment NEUF qui se construit sous les yeux de la ville en 60 jours — c'est une "
             "arme marketing en soi ; des prix 3 à 10 fois inférieurs aux écoles qui envoient "
             "leurs étudiants en France ; le mobile money pour encaisser sans friction."),
           P("<b>Les 3 lois de la campagne :</b> (1) <b>La preuve bat la promesse</b> — on montre "
             "le chantier, les élèves, les reçus signés, pas des renders. (2) <b>La vitesse bat "
             "la taille</b> — on réagit en 24 h, les gros ne réagissent jamais. (3) <b>Le réseau "
             "bat la pub</b> — un pasteur, un DRH ou un proviseur qui recommande vaut 100 panneaux.")]

    # A. Jeunesse / bac
    st += section("A. Attaque sur le marché des bacheliers (le gros volume)")
    st += [card("A1", "Le jour du bac, on est partout",
                "Le jour de la publication des résultats, des équipes UPL avec tee-shirts et flyers "
                "sont physiquement devant les 10 principaux lycées et centres d'examen de "
                "Libreville/Akanda, plus un message WhatsApp massif : « Ton bac est là. Et "
                "maintenant ? 90 places seulement pour la première promotion Licence à 1 000 000 F "
                "(50 premières places). » On capte l'émotion au moment exact où elle existe.",
                "1,5 M (équipes, tee-shirts, flyers, crédit tel.)", "Jour J + 2 semaines",
                "3/5", "5/5",
                "bousculade devant les lycées, réaction de l'administration : demander les "
                "autorisations de quartier et rester courtois."),
           card("A2", "Rareté assumée : « 90 places, pas une de plus »",
                "Au lieu de supplier les étudiants, on inverse : c'est l'UPL qui choisit. Processus "
                "d'admission avec entretien de motivation (10 minutes, gratuit) et dossier. La "
                "sélection crée le désir. Slogan : « Sans sélection, pas d'excellence. » Le jour "
                "où un candidat est refusé, sa mère en parle à cinq autres mamans.",
                "0,3 M (formation jury d'entretiens)", "Immédiat", "2/5", "4/5",
                "si l'entretien refuse trop de monde en début d'année, remplir les salles devient "
                "dur : fixer un taux de refus maximum (15 %)."),
           card("A3", "TikTok : les vérités qui fâchent sur l'emploi",
                "Série courte « Vérités sur le marché de l'emploi gabonais » : chiffres chocs sur "
                "les diplômés sans emploi, les métiers qui recrutent vraiment (port, numérique, "
                "assurance), l'IA qui arrive. Ton cash, 30 secondes, visage réel ou voix off sur "
                "images. Controversé = partagé. Fin de chaque épisode : « Et toi, tu fais quoi "
                "l'an prochain ? »",
                "0,8 M (tournage smartphone + montage)", "2 semaines", "3/5", "5/5",
                "un chiffre contesté ou un ton trop négatif : sourcer chaque chiffre et toujours "
                "finir sur une solution (nos filières)."),
           card("A4", "Ambassadeurs-lycée commissionnés",
                "Dans chaque grand lycée, un « ambassadeur UPL » (enseignant respecté ou élève "
                "leader) reçoit 10 000 F par étudiant inscrit venu de son établissement, plafonné. "
                "Il distribue les flyers, répond aux questions, crée le groupe WhatsApp du lycée. "
                "L'argent ne parle pas, il remercie.",
                "1 M (commissions sur résultats)", "3 semaines", "4/5", "4/5",
                "dérive type « vente pyramidale » : plafonner, payer sur inscription EFFECTIVE et "
                "facturée, et interdire toute promesse de note."),
           card("A5", "Parrainage familial : « ramène ton frère »",
                "Chaque étudiant inscrit qui amène un inscrit reçoit 100 000 F de réduction sur sa "
                "tranche suivante. Au Gabon, la famille paie les études : on transforme les mamans "
                "en force de vente. Simple, mesurable, immédiat.",
                "1,5 M (réductions accordées)", "Immédiat", "2/5", "4/5",
                "cannibalisation du prix : plafonner à 2 parrainages par étudiant et par an."),
           card("A6", "La première tranche offerte aux 20 premiers",
                "Pour créer l'urgence réelle : les 20 premiers pré-inscrits confirmés de Licence 1 "
                "ne paient pas les frais d'inscription (200 000 F). Compte à rebours public sur "
                "WhatsApp et Facebook. C'est vrai (offre limitée), donc légal, et ça débloque les "
                "indécis.",
                "0,4 M", "Immédiat", "1/5", "3/5",
                "effet d'aubaine : les 20 premiers partent vite, donc l'offre s'arrête vite — "
                "prévoir la variante « 2e vague » à 50 %.")]

    # B. MBA / entreprises
    st += section("B. Le MBA : aller chercher l'argent là où il est (entreprises et institutions)")
    st += [card("B1", "Raid RH : 20 rendez-vous, 20 cohortes potentielles",
                "Le Président + un commercial prennent 20 RDV en 30 jours avec les DRH/DG des "
                "banques (BGFI, Ecobank, BICIG, UGB, BOA), compagnies (pétrole, ports, Caisse "
                "Nationale de Sécurité Sociale), et ministères. Offre cohorte : « 10 cadres formés "
                "ensemble, tarif entreprise, facture unique, planning aménagé. » Une seule "
                "signature = 40 M de chiffre d'affaires — plus que toute une promo Étudiants.",
                "0,5 M (déplacements, présentations imprimées)", "30 jours", "2/5", "5/5",
                "aucun : au pire on apprend pourquoi ça bloque. Ne jamais céder sur le prix "
                "affiché, négocier sur les services."),
           card("B2", "Le MBA vendu comme un réseau, pas comme des cours",
                "Les cadres paient 4 M pour le diplôme ET pour la salle à côté d'eux. On assume : "
                "aprèswork networking mensuel (cocktail + intervenant de marque), annuaire des "
                "alumni par promotion, badge « UPL Business Club ». Le cours devient l'entrée "
                "d'un club. Personne d'autre ne le vend comme ça à Libreville.",
                "1,2 M (6 événements/an)", "1 mois", "1/5", "4/5",
                "coût des cocktails : partenaires (brasserie, traiteur) sollicités en échange de "
                "visibilité — ne rien promettre à un partenaire non signé."),
           card("B3", "Masterclass gratuite d'une pointure",
                "Faire venir UNE personnalité régionale connue (prof d'Abidjan/Douala, dirigeant "
                "respecté) pour une masterclass gratuite sur 2 heures, accès sur inscription. "
                "Salle pleine garantie, 300 leads qualifiés cadres, presse locale invitée. La "
                "masterclass EST la publicité.",
                "2,5 M (déplacement + salle + organisation)", "6 à 8 semaines", "2/5", "5/5",
                "invité qui annule : toujours un plan B local (le Président + un DBA)."),
           card("B4", "Facture entreprise payée = remise rapide",
                "Toute formation entreprise payée intégralement sous 15 jours : remise de 5 %. "
                "Les directions financières adorent arrondir leur budget. Encaisse vite, évite "
                "les créances qui pourrissent le bilan (déjà 8 M de créances MBA).",
                "0 F (manque à gagner marginale)", "Immédiat", "1/5", "3/5",
                "usage immodéré de la remise : la plafonner et la retirer dès que le carnet est plein.")]

    # C. Réseaux de confiance
    st += section("C. Les réseaux de confiance : églises, associations, WhatsApp, phoning")
    st += [card("C1", "La tournée des églises et des associations de parents",
                "Au Gabon, la recommandation d'un responsable religieux ou d'une association de "
                "femmes vaut tous les médias. Le Président demande 10 minutes dans 15 églises et "
                "5 associations après le culte ou la réunion : présentation de l'UPL, invitation "
                "à la porte ouverte, fiches distribuées. Sensible, mais c'est le canal de confiance "
                "n°1 du pays.",
                "0,3 M (impression, déplacements)", "4 semaines", "4/5", "4/5",
                "mélange religion/commerce mal perçu : parler éducation et avenir des jeunes, "
                "jamais de politique, jamais de promesse divine."),
           card("C2", "L'armée WhatsApp structurée",
                "Un groupe WhatsApp par cible (parents, bacheliers, cadres, diaspora), animés par "
                "des règles : 3 messages par semaine maximum, toujours utiles (dates, tarifs, "
                "photos réelles), réponse en moins de 2 heures. Chaque membre du personnel UPL "
                "relaye dans ses 10 groupes personnels. 0 F de budget, effet de ruissellement.",
                "0,2 M (crédits téléphoniques)", "1 semaine", "2/5", "4/5",
                "spam = blocage en masse : varier les formats (photo, voix, texte) et jamais "
                "d'envoi après 21 h."),
           card("C3", "Phoning agressif et organisé",
                "Le fichier des pré-inscrits et des contacts lycées est appelé 3 fois : J+0 "
                "(qualification), J+7 (invitation porte ouverte), veille de rentrée (rappel "
                "final). Créneaux 18 h - 21 h en semaine, samedi matin. Script court, honnête, "
                "avec rappel des numéros officiels. Le téléphone convertit 3 fois plus que la pub.",
                "1 M (12 mois de crédits + primes appel)", "Immédiat", "2/5", "4/5",
                "réputation de harcèlement : 3 appels maximum par prospect, retrait immédiat sur "
                "demande."),
           card("C4", "Les alumni en chasse",
                "Les 80 cadres formés reçoivent un statut : « Ambassadeur UPL ». Celui qui amène "
                "un inscrit MBA reçoit une remise de 200 000 F sur son DBA (ou un accès gratuit au "
                "Business Club). Tableau d'honneur publié chaque trimestre. Ils ont vécu le "
                "produit : ce sont nos meilleurs vendeurs.",
                "0,5 M", "3 semaines", "1/5", "4/5",
                "jalousie entre promotions : critères publics et identiques pour tous.")]

    # D. Coups d'éclat
    st += section("D. Les coups d'éclat : faire parler sans budget média")
    st += [card("D1", "Le défi « 60 jours » : le chantier en spectacle",
                "On transforme la contrainte (livraison en 2 mois) en storytelling : compte à "
                "rebours public « UPL construit votre avenir en 60 jours », time-lapse hebdo du "
                "chantier sur TikTok/Facebook, visites du chantier en casque UPL pour parents et "
                "proviseurs, cérémonie de « première pierre » avec presse et autorités. Le "
                "bâtiment devient le meilleur spot publicitaire du pays — et il est gratuit.",
                "0,8 M (casques, signalétique, photographe)", "Immédiat (chantier en cours)", "2/5", "5/5",
                "retard de chantier = propagande négative : ne lancer le compte à rebours public "
                "qu'une la tranche A (RDC) sécurisée à 6 semaines."),
           card("D2", "L'émission radio du Président",
                "Acheter ou négocier un créneau hebdo de 30 minutes « Les métiers de demain » sur "
                "une radio populaire : le Président répond en direct aux appels des parents. Un "
                "recteur ne répond jamais au téléphone à la radio ; le Président, si. Différenciation "
                "totale, coût ridicule.",
                "1,8 M (12 émissions)", "3 semaines", "2/5", "4/5",
                "dérapage en direct sur un sujet politique : ne parler QUE formation, emploi, "
                "campus. Aucun commentaire politique, quelle que soit la question."),
           card("D3", "La publicité comparative (à manier avec gants)",
                "Affiche et post « Comparez avant de payer » : grille factuelle et vérifiable "
                "(prix, taille des classes, partenariat, emploi du temps) entre l'UPL et les "
                "alternatives à Libreville, sources publiques. Interdit de dénigrer, autorisé "
                "d'informer. Extrêmement percutant, juridiquement sensible.",
                "0,6 M", "2 semaines", "5/5", "4/5",
                "procès en dénigrement : chaque chiffre doit être public et daté, faire relire "
                "l'affiche par un juriste avant diffusion, et garder une version sans noms."),
           card("D4", "Un spot TV pendant le journal du soir",
                "Les deux films institutionnels UPL existent déjà. Les diffuser en spot court "
                "(15 s) autour du journal de 20 h pendant 3 semaines, au moment où les parents "
                "décident de l'inscription. C'est le créneau des décideurs familiaux.",
                "2,5 M (3 semaines)", "4 semaines", "1/5", "3/5",
                "coût élevé pour la portée : tester 1 semaine d'abord, mesurer les appels, "
                "arrêter si pas d'effet."),
           card("D5", "La porte ouverte « ton fils teste l'université »",
                "Portes ouvertes avec vrais cours ouverts : un cours magistral public, la salle "
                "informatique allumée, un atelier « rédige ta lettre de motivation ». Les "
                "visiteurs repartent avec une photo DANS la salle. Un parent qui a vu l'intérieur "
                "n'envoie pas son enfant ailleurs.",
                "0,7 M", "3 semaines", "1/5", "4/5",
                "fréquentation faible la 1re fois : coupler avec les églises (C1) et les "
                "proviseurs pour remplir la salle.")]

    # E. Idées dangereuses
    st += section("E. Zone rouge : idées à haut rendement potentiel, à ne déclencher QU'APRÈS décision écrite du Président")
    st += [P("Ces idées sont listées parce qu'elles marchent partout en Afrique de l'Ouest et "
             "centrale. Elles comportent un risque réel (juridique, réputationnel, politique). "
             "Elles ne se lancent que sur décision écrite du Président, avec un avocat ou un "
             "conseil en communication, et jamais « pour voir ».", "body"),
           card("E1", "La garantie « réussi ou remboursé »",
                "Remboursement partiel (30 %) de la scolarité si l'étudiant assidu ne valide pas "
                "sa 1re année. Signal de confiance maximal, personne ne le fait. Démonte "
                "l'objection « usine à diplômes » en une phrase.",
                "provision 1 M/an", "1 mois", "4/5", "4/5",
                "coût si échec massif : conditions strictes (assiduité 90 %, notes suivies, "
                "remboursement en crédit de scolarité, pas en espèces)."),
           card("E2", "Attaquer frontalement les « écoles fantômes »",
                "Campagne « Méfiez-vous des écoles qui ne montrent rien » : demander à voir les "
                "salles, les profs, les reçus — partout. Sans citer personne, tout le monde "
                "comprend. Positionne l'UPL en transparence totale (visites, reçus numérotés, "
                "prix affichés).",
                "0,4 M", "2 semaines", "4/5", "4/5",
                "guerre avec le secteur privé de l'enseignement : rester 100 % implicite, ne "
                "jamais nommer, sinon dénigrement."),
           card("E3", "Recruter 2 « profs stars » à prix d'or",
                "Proposer à 2 personnalités gabonaises très connues (ex-dirigeant, consultant "
                "réputé) d'intervenir au MBA contre cachet élevé. Leur nom sur l'affiche remplit "
                "la promo. On achète de la crédibilité instantanée.",
                "2 M (cachets)", "6 semaines", "3/5", "4/5",
                "dépendance à une personne : contrat d'un module, pas d'une année entière, et "
                "toujours 2 intervenants sur chaque module star."),
           card("E4", "Le concours national « Bourse d'Excellence UPL »",
                "Concours ouvert à tous les bacheliers du pays : 10 bourses totales (scolarité "
                "offerte) tirées au sort des meilleurs dossiers, remises par le Président avec "
                "presse et autorités. Coût réel : 10 x 1 M étalés sur 3 ans, mais retour en "
                "notoriété nationale immédiat et immense.",
                "2 M la 1re année (à trouver hors budget com)", "8 semaines", "3/5", "5/5",
                "promesse lourde sur 3 ans : budgéter les bourses AVANT l'annonce, jamais "
                "l'inverse."),
           card("E5", "Occuper le débat public sur l'emploi des jeunes",
                "Tribunes et interviews du Président sur le thème « Le Gabon forme-t-il les "
                "métiers de demain ? » dans la presse et les radios. L'UPL devient LA voix "
                "écoutée sur le sujet, et le recrutement suit. Toujours en apport de solution, "
                "jamais en critique du pouvoir.",
                "0,2 M", "2 semaines", "4/5", "4/5",
                "récupération politique : rester sur le terrain technique (compétences, "
                "économie bleue, IA) et décliner toute question polémique.")]

    # F. Sélection
    st += section("F. Pour le brainstorm : la matrice de décision")
    st += [P("Mon avis tranché, à contester librement : si on ne devait retenir que <b>cinq</b> "
             "idées pour septembre-décembre, je prends <b>A1 (jour du bac), B1 (raid RH), C1 "
             "(églises/associations), D1 (défi 60 jours) et D2 (radio Président)</b> — environ "
             "4,9 M, tout tient dans le budget de 15 M, et chaque idée est mesurable en "
             "inscriptions. Les idées E ne se décident pas à chaud.", "pitch"),
           styled_table([
               [P("Idée", "cellb"), P("Coût", "cellrb"), P("Risque", "cellrb"), P("Impact", "cellrb"), P("Décision du Président", "cellb")],
               [P("A1 - Jour du bac", "cell"), P("1,5 M", "cellr"), P("3/5", "cellr"), P("5/5", "cellr"), P("GO / NON / PLUS TARD", "cellc")],
               [P("A2 - Sélection assumée (90 places)", "cell"), P("0,3 M", "cellr"), P("2/5", "cellr"), P("4/5", "cellr"), P("GO / NON / PLUS TARD", "cellc")],
               [P("A3 - TikTok « vérités »", "cell"), P("0,8 M", "cellr"), P("3/5", "cellr"), P("5/5", "cellr"), P("GO / NON / PLUS TARD", "cellc")],
               [P("A4 - Ambassadeurs lycées", "cell"), P("1,0 M", "cellr"), P("4/5", "cellr"), P("4/5", "cellr"), P("GO / NON / PLUS TARD", "cellc")],
               [P("A5 - Parrainage familial", "cell"), P("1,5 M", "cellr"), P("2/5", "cellr"), P("4/5", "cellr"), P("GO / NON / PLUS TARD", "cellc")],
               [P("A6 - Frais offerts 20 premiers", "cell"), P("0,4 M", "cellr"), P("1/5", "cellr"), P("3/5", "cellr"), P("GO / NON / PLUS TARD", "cellc")],
               [P("B1 - Raid RH entreprises", "cell"), P("0,5 M", "cellr"), P("2/5", "cellr"), P("5/5", "cellr"), P("GO / NON / PLUS TARD", "cellc")],
               [P("B2 - MBA = Business Club", "cell"), P("1,2 M", "cellr"), P("1/5", "cellr"), P("4/5", "cellr"), P("GO / NON / PLUS TARD", "cellc")],
               [P("B3 - Masterclass pointure", "cell"), P("2,5 M", "cellr"), P("2/5", "cellr"), P("5/5", "cellr"), P("GO / NON / PLUS TARD", "cellc")],
               [P("B4 - Remise paiement rapide", "cell"), P("0 F", "cellr"), P("1/5", "cellr"), P("3/5", "cellr"), P("GO / NON / PLUS TARD", "cellc")],
               [P("C1 - Églises et associations", "cell"), P("0,3 M", "cellr"), P("4/5", "cellr"), P("4/5", "cellr"), P("GO / NON / PLUS TARD", "cellc")],
               [P("C2 - Armée WhatsApp", "cell"), P("0,2 M", "cellr"), P("2/5", "cellr"), P("4/5", "cellr"), P("GO / NON / PLUS TARD", "cellc")],
               [P("C3 - Phoning 3 touches", "cell"), P("1,0 M", "cellr"), P("2/5", "cellr"), P("4/5", "cellr"), P("GO / NON / PLUS TARD", "cellc")],
               [P("C4 - Alumni en chasse", "cell"), P("0,5 M", "cellr"), P("1/5", "cellr"), P("4/5", "cellr"), P("GO / NON / PLUS TARD", "cellc")],
               [P("D1 - Défi 60 jours (chantier)", "cell"), P("0,8 M", "cellr"), P("2/5", "cellr"), P("5/5", "cellr"), P("GO / NON / PLUS TARD", "cellc")],
               [P("D2 - Radio du Président", "cell"), P("1,8 M", "cellr"), P("2/5", "cellr"), P("4/5", "cellr"), P("GO / NON / PLUS TARD", "cellc")],
               [P("D3 - Pub comparative", "cell"), P("0,6 M", "cellr"), P("5/5", "cellr"), P("4/5", "cellr"), P("GO / NON / PLUS TARD", "cellc")],
               [P("D4 - Spot TV journal 20 h", "cell"), P("2,5 M", "cellr"), P("1/5", "cellr"), P("3/5", "cellr"), P("GO / NON / PLUS TARD", "cellc")],
               [P("D5 - Porte ouverte « teste »", "cell"), P("0,7 M", "cellr"), P("1/5", "cellr"), P("4/5", "cellr"), P("GO / NON / PLUS TARD", "cellc")],
               [P("E1 - Réussi ou remboursé", "cell"), P("provision 1 M", "cellr"), P("4/5", "cellr"), P("4/5", "cellr"), P("ZONE ROUGE - décision écrite", "cellc")],
               [P("E2 - « Écoles fantômes »", "cell"), P("0,4 M", "cellr"), P("4/5", "cellr"), P("4/5", "cellr"), P("ZONE ROUGE - décision écrite", "cellc")],
               [P("E3 - Profs stars", "cell"), P("2,0 M", "cellr"), P("3/5", "cellr"), P("4/5", "cellr"), P("ZONE ROUGE - décision écrite", "cellc")],
               [P("E4 - Bourses d'excellence", "cell"), P("2,0 M", "cellr"), P("3/5", "cellr"), P("5/5", "cellr"), P("ZONE ROUGE - décision écrite", "cellc")],
               [P("E5 - Tribune emploi des jeunes", "cell"), P("0,2 M", "cellr"), P("4/5", "cellr"), P("4/5", "cellr"), P("ZONE ROUGE - décision écrite", "cellc")],
           ], [6.4*cm, 2.2*cm, 1.7*cm, 1.7*cm, 4.8*cm], fontsize=7.6),
           P("Arbitrage budget : les idées retenues se financent par réaffectation à l'intérieur "
             "des 15 M du plan de communication (crédit 260 M) — la publicité TV et les médias "
             "classiques réduits si le terrain rapporte plus. Toute idée à coût nouveau hors "
             "enveloppe (bourses E4) doit trouver son financement AVANT annonce.", "note"),
           Spacer(1, 8),
           P("Document de travail interne - Présidence UPL - 30 août 2026. Idées à arbitrer par "
             "Serge Patrick MINANG, Président-Fondateur. Les mentions de risques ne sont pas des "
             "conseils juridiques : faire relire les actions de la zone rouge (avocat / conseil "
             "en communication) avant tout lancement.", "note")]
    doc = Doc(OUT, "UPL - Stratégie com offensive - brainstorm Président - INTERNE")
    doc.build(st)
    return doc

if __name__ == "__main__":
    d = build()
    print("OK", OUT, "-", d.page, "pages")
