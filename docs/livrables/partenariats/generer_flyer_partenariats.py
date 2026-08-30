#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
"""Flyer UPL « coopération académique » — PDF léger à joindre aux emails de partenariat."""
import os
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, PageBreak

from generer_livrables import (Doc, P, S, section, styled_table, LOGO,
                               BLUE, BLUE_DK, GOLD, GOLD_LT, BLUE_LT, GREY, LINE, ZEBRA)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "UPL_Flyer_Partenariats.pdf")

S["big"] = ParagraphStyle("big", fontName="Helvetica-Bold", fontSize=17, leading=21,
                          textColor=BLUE, alignment=TA_CENTER)
S["sub"] = ParagraphStyle("sub", fontName="Helvetica", fontSize=10.5, leading=14,
                          textColor=GREY, alignment=TA_CENTER)
S["stat"] = ParagraphStyle("stat", fontName="Helvetica-Bold", fontSize=13.5, leading=16,
                           textColor=BLUE, alignment=TA_CENTER)
S["statl"] = ParagraphStyle("statl", fontName="Helvetica", fontSize=7.6, leading=9.5,
                            textColor=GREY, alignment=TA_CENTER)

def stat_bloc(n, label):
    return [P(n, "stat"), P(label, "statl")]

def build():
    st = []
    # ---------------- PAGE 1
    st += [Spacer(1, 6),
           P("Proposition de coopération académique", "kicker"),
           P("Université Privée de Libreville", "big"),
           P("Gabon · Afrique centrale · zone CEMAC — Libreville, août 2026", "sub"),
           Spacer(1, 10)]

    st += section("L'établissement")
    st += [P("Fondée en 2022 à Libreville par M. Serge Patrick MINANG, ingénieur, MBA, doctorant "
             "DBA, fonctionnaire du Ministère des Travaux Publics, l'UPL est un établissement "
             "d'enseignement supérieur privé familial, autofinancé et sans dette. Elle conduit "
             "depuis 2022 un Executive MBA en partenariat avec l'Université de Douala "
             "(Cameroun) : près de 80 cadres et dirigeants formés, issus de l'administration, "
             "des entreprises publiques et du secteur privé.")]

    st += section("L'UPL en chiffres")
    st += [Table([[stat_bloc("2022", "année de fondation"),
                   stat_bloc("80", "cadres formés (Executive MBA)"),
                   stat_bloc("6", "filières ouvertes à la rentrée 2026"),
                   stat_bloc("504 m2", "bâtiment pédagogique R+2 en cours de réalisation")]],
                 colWidths=[4.3*cm]*4,
                 style=TableStyle([
                     ("BOX", (0, 0), (-1, -1), 0.8, GOLD),
                     ("INNERGRID", (0, 0), (-1, -1), 0.4, GOLD),
                     ("BACKGROUND", (0, 0), (-1, -1), GOLD_LT),
                     ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                     ("TOPPADDING", (0, 0), (-1, -1), 8),
                     ("BOTTOMPADDING", (0, 0), (-1, -1), 8)])),
           Spacer(1, 8)]

    st += section("Offre académique 2026-2027")
    st += [styled_table([
        [P("Programme", "cellb"), P("Description", "cellb")],
        [P("Executive MBA (socle historique)", "cell"), P("Soirées 17h-21h, partenariat Université de Douala, scolarité 4 000 000 FCFA, jusqu'à 8 échéances", "cell")],
        [P("Gouvernance, Leadership et Management", "cell"), P("Licence · Master · MBA · DBA", "cell")],
        [P("Économie Numérique et Intelligence Artificielle", "cell"), P("Data, numérique appliqué, transformation", "cell")],
        [P("Économie Bleue, Gestion Portuaire et Développement Durable", "cell"), P("Adossée au port en eau profonde de Libreville-Owendo", "cell")],
        [P("Droit et Sciences Politiques", "cell"), P("Droit des affaires, action publique", "cell")],
        [P("École d'Assurance Maladie et de Sécurité Sociale", "cell"), P("Couverture maladie universelle, protection sociale", "cell")],
        [P("Classes Préparatoires aux Grandes Écoles (CPGE)", "cell"), P("Préparation aux concours des grandes écoles", "cell")],
    ], [7.2*cm, 10.0*cm])]

    st += section("Pourquoi le Gabon, pourquoi Libreville")
    st += [P("Le Gabon est un pays francophone stable, urbanisé à plus de 90 %, doté d'infrastructures "
             "régionales (port en eau profonde, aéroport international) et d'un pouvoir d'achat "
             "parmi les plus élevés d'Afrique centrale. L'Afrique centrale francophone reste "
             "pourtant très peu couverte par les grandes écoles internationales : il n'existe pas "
             "de plateforme académique de référence à Libreville. L'UPL entend occuper cette "
             "position et servir non seulement le Gabon, mais l'ensemble de la zone CEMAC "
             "(Cameroun, Congo, Guinée équatoriale, Tchad, Centrafrique) - un bassin de plus de "
             "50 millions d'habitants."),
           P("Le programme immobilier est engagé : bâtiment pédagogique immédiat de 504 m2 "
             "(9 salles climatisées, salle informatique, livraison rapide), puis master plan "
             "campus à horizon 2028-2035 (enveloppe indicative d'environ 3,5 milliards FCFA, "
             "financement multi-acteurs).")]

    st += [PageBreak()]
    # ---------------- PAGE 2
    st += [P("Formats de coopération proposés", "kicker"),
           P("Trois chemins, un premier pas", "big"),
           Spacer(1, 8)]

    st += section("1. Trois formats possibles")
    st += [styled_table([
        [P("Format", "cellb"), P("Contenu", "cellb")],
        [P("A. Implantation progressive", "cellb"),
         P("Un programme ou une implantation académique construits pas à pas à Libreville : module conjoint, puis programme labellisé, puis campus délocalisé selon les exigences d'accréditation de votre institution.", "cell")],
        [P("B. Cycle UPL de trois ans", "cellb"),
         P("Un parcours UPL construit selon des standards définis conjointement avec votre établissement, préparant à une candidature sélective vers vos cursus de niveau Master.", "cell")],
        [P("C. Voie d'accès dédiée", "cellb"),
         P("Une candidature spécifique pour les meilleurs diplômés UPL - sans admission automatique - accompagnée de cours hybrides et d'évaluations académiques conformes à vos critères.", "cell")],
    ], [4.4*cm, 12.8*cm])]

    st += section("2. Premiers jalons réalistes")
    st += [styled_table([
        [P("Jalon", "cellb"), P("Horizon", "cellb")],
        [P("Cohorte pilote ou école d'été à Libreville", "cell"), P("Été 2027", "cell")],
        [P("Module conjoint (finance durable, entrepreneuriat, numérique, santé publique)", "cell"), P("Rentrée 2027", "cell")],
        [P("Mission d'étude conjointe sur les besoins de compétences en Afrique centrale", "cell"), P("2027", "cell")],
        [P("Accueil de vos étudiants au Gabon : stages, études de terrain, missions encadrées, projets entrepreneuriaux", "cell"), P("Dès la signature d'un accord cadre", "cell")],
    ], [12.2*cm, 5.0*cm])]

    st += section("3. Ce que l'UPL apporte au partenariat")
    st += [P("- <b>Un ancrage local</b> : équipe, campus, relations avec les administrations, entreprises "
             "et institutions gabonaises ; les autorisations ministérielles d'ouverture des filières "
             "sont disponibles ou en cours de finalisation."),
           P("- <b>Une expérience éprouvée</b> du partenariat académique international : la convention "
             "avec l'Université de Douala fonctionne depuis 2022 (ingénierie pédagogique, crédits "
             "universitaires, enseignants croisés)."),
           P("- <b>Un recrutement régional</b> : capacité d'attirer des étudiants et professionnels du "
             "Gabon et de la CEMAC vers des programmes sélectifs."),
           P("- <b>Une volonté de rigueur</b> : nous connaissons les exigences d'accréditation, de "
             "sélection et de qualité pédagogique, et acceptons un cadrage complet avant tout "
             "engagement diplômant.")]

    st += section("4. Prochain pas")
    st += [P("Un premier échange confidentiel de 20 minutes, par Microsoft Teams ou en personne. "
             "M. le Président Serge Patrick MINANG sera en France à partir du 9 septembre et se "
             "tient à la disposition de vos équipes (direction des relations internationales, "
             "direction des partenariats) pour une rencontre."),
           Spacer(1, 10)]

    st += [Table([[P("<b>Serge Patrick MINANG</b><br/>Président-Fondateur<br/>"
                     "+241 062 62 19 78 / +241 077 35 95 72<br/>"
                     "contact@upl-gabon.com<br/>www.upl-gabon.com", "bodyc"),
                   P("<b>Université Privée de Libreville</b><br/>Sablière, face Résidence de "
                     "l'Ambassade d'Arabie Saoudite<br/>Libreville - Gabon<br/>"
                     "Excellence · Innovation · Leadership", "bodyc")]],
                 colWidths=[8.6*cm, 8.6*cm],
                 style=TableStyle([
                     ("BACKGROUND", (0, 0), (-1, -1), BLUE_LT),
                     ("BOX", (0, 0), (-1, -1), 0.8, GOLD),
                     ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                     ("TOPPADDING", (0, 0), (-1, -1), 10),
                     ("BOTTOMPADDING", (0, 0), (-1, -1), 10)]))]

    doc = Doc(OUT, "UPL - Proposition de coopération académique - Libreville, Gabon")
    doc.build(st)
    return doc, OUT

if __name__ == "__main__":
    d, path = build()
    size = os.path.getsize(path)
    print("OK", path, "-", d.page, "pages -", f"{size/1024:.0f} Ko")
