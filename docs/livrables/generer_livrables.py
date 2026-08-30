#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Génère les deux livrables UPL :
  1. Contre-proposition de devis (réponse au devis MATRIX GROUP du 01/09/2026)
  2. Plan de communication rentrée 2026-2027
Charte UPL : bleu #0B2A5B · or #C9A227 · blanc
"""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_RIGHT, TA_LEFT
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle, Image, KeepTogether,
                                PageBreak)

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))          # racine du repo
LOGO = os.path.join(ROOT, "assets", "img", "logo-upl.png")
OUT1 = os.path.join(HERE, "UPL_Contre-proposition_Devis_Campus_MATRIX_GROUP_REV3.pdf")
OUT2 = os.path.join(HERE, "UPL_Plan_de_Communication_Rentree_2026-2027.pdf")

# ---------------------------------------------------------------- charte
BLUE = colors.HexColor("#0B2A5B")
BLUE_DK = colors.HexColor("#081E42")
GOLD = colors.HexColor("#C9A227")
GOLD_LT = colors.HexColor("#F5EEDA")
BLUE_LT = colors.HexColor("#E8EDF5")
ZEBRA = colors.HexColor("#F4F6FA")
GREY = colors.HexColor("#3A3F47")
LINE = colors.HexColor("#C9D2E0")
RED = colors.HexColor("#8C1D18")
GREEN = colors.HexColor("#1E5B2E")

def fmt(n):
    return f"{int(round(n)):,}".replace(",", " ")

# ---------------------------------------------------------------- styles
S = {}
S["body"] = ParagraphStyle("body", fontName="Helvetica", fontSize=9.3, leading=13,
                           alignment=TA_JUSTIFY, textColor=GREY, spaceAfter=5)
S["bodyc"] = ParagraphStyle("bodyc", parent=S["body"], alignment=TA_CENTER)
S["small"] = ParagraphStyle("small", parent=S["body"], fontSize=8, leading=10.5)
S["note"] = ParagraphStyle("note", parent=S["small"], textColor=colors.HexColor("#5A6070"),
                           alignment=TA_LEFT)
S["h1"] = ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=15.5, leading=19,
                         textColor=BLUE, alignment=TA_LEFT, spaceAfter=2)
S["h2"] = ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=11.5, leading=14.5,
                         textColor=colors.white, alignment=TA_LEFT)
S["kicker"] = ParagraphStyle("kicker", fontName="Helvetica-Bold", fontSize=8.5,
                             textColor=GOLD, leading=11)
S["cell"] = ParagraphStyle("cell", fontName="Helvetica", fontSize=8.1, leading=10.3,
                           textColor=GREY, alignment=TA_LEFT)
S["cellb"] = ParagraphStyle("cellb", parent=S["cell"], fontName="Helvetica-Bold")
S["cellr"] = ParagraphStyle("cellr", parent=S["cell"], alignment=TA_RIGHT)
S["cellrb"] = ParagraphStyle("cellrb", parent=S["cellr"], fontName="Helvetica-Bold")
S["cellc"] = ParagraphStyle("cellc", parent=S["cell"], alignment=TA_CENTER)
S["lotrow"] = ParagraphStyle("lotrow", fontName="Helvetica-Bold", fontSize=8.1,
                             leading=10.3, textColor=colors.white)

def P(txt, st="body"):
    return Paragraph(txt, S[st])

def section(title, subtitle=""):
    inner = Paragraph(title, S["h2"]) if not subtitle else \
        Table([[Paragraph(title, S["h2"])],
               [Paragraph(subtitle, ParagraphStyle("sub", fontName="Helvetica",
                    fontSize=8, textColor=colors.HexColor("#DCE4F2"), leading=10))]],
              colWidths=[None], style=TableStyle([
                  ("LEFTPADDING", (0, 0), (-1, -1), 0),
                  ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                  ("TOPPADDING", (0, 0), (-1, -1), 0),
                  ("BOTTOMPADDING", (0, 0), (-1, -1), 1)]))
    t = Table([[ "", inner ]], colWidths=[0.28*cm, 17.2*cm],
              rowHeights=None)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, -1), GOLD),
        ("BACKGROUND", (1, 0), (1, -1), BLUE),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (1, 0), (1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5)]))
    return [Spacer(1, 10), t, Spacer(1, 7)]

# ---------------------------------------------------------------- gabarit
class Doc(BaseDocTemplate):
    def __init__(self, path, band_text, **kw):
        super().__init__(path, pagesize=A4, leftMargin=1.7*cm, rightMargin=1.7*cm,
                         topMargin=3.35*cm, bottomMargin=1.9*cm, **kw)
        self.band_text = band_text
        fr = Frame(self.leftMargin, self.bottomMargin, self.width, self.height, id="main")
        self.addPageTemplates([
            PageTemplate(id="first", frames=[fr], onPage=self._first),
            PageTemplate(id="later", frames=[fr], onPage=self._later)])

    def _first(self, c, doc):
        c.saveState()
        w, h = A4
        c.setFillColor(BLUE); c.rect(0, h-3.05*cm, w, 3.05*cm, stroke=0, fill=1)
        c.setFillColor(GOLD); c.rect(0, h-3.22*cm, w, 0.17*cm, stroke=0, fill=1)
        if os.path.exists(LOGO):
            c.drawImage(LOGO, 1.05*cm, h-2.72*cm, width=2.62*cm, height=1.67*cm,
                        mask="auto", preserveAspectRatio=True)
        c.setFillColor(colors.white)
        c.setFont("Helvetica-Bold", 14.5)
        c.drawString(4.1*cm, h-1.62*cm, "UNIVERSITÉ PRIVÉE DE LIBREVILLE")
        c.setFillColor(GOLD); c.setFont("Helvetica-Bold", 8.6)
        c.drawString(4.1*cm, h-2.05*cm, "UPL  ·  EXCELLENCE  ·  INNOVATION  ·  LEADERSHIP")
        c.setFillColor(colors.HexColor("#C6D2E8")); c.setFont("Helvetica", 7.6)
        c.drawString(4.1*cm, h-2.52*cm, "Sablière, face Résidence de l'Ambassade d'Arabie Saoudite - Libreville (Gabon)")
        c.drawString(4.1*cm, h-2.78*cm, "Tél. +241 02 62 19 78 / +241 07 35 95 72   ·   contact@upl-gabon.com   ·   www.upl-gabon.com")
        self._footer(c, doc)
        c.restoreState()

    def _later(self, c, doc):
        c.saveState()
        w, h = A4
        c.setFillColor(BLUE); c.rect(0, h-1.12*cm, w, 1.12*cm, stroke=0, fill=1)
        c.setFillColor(GOLD); c.rect(0, h-1.24*cm, w, 0.12*cm, stroke=0, fill=1)
        c.setFillColor(colors.white); c.setFont("Helvetica-Bold", 8)
        c.drawString(1.7*cm, h-0.74*cm, self.band_text)
        if os.path.exists(LOGO):
            c.drawImage(LOGO, w-2.5*cm, h-0.98*cm, width=1.15*cm, height=0.73*cm,
                        mask="auto", preserveAspectRatio=True)
        self._footer(c, doc)
        c.restoreState()

    def _footer(self, c, doc):
        w, h = A4
        c.setStrokeColor(GOLD); c.setLineWidth(0.7)
        c.line(1.7*cm, 1.35*cm, w-1.7*cm, 1.35*cm)
        c.setFillColor(colors.HexColor("#6B7382")); c.setFont("Helvetica", 6.9)
        c.drawString(1.7*cm, 1.0*cm, "Université Privée de Libreville - document confidentiel - usage Présidence / négociation")
        c.drawRightString(w-1.7*cm, 1.0*cm, f"Page {doc.page}")

# ---------------------------------------------------------------- tableaux
def styled_table(data, widths, header=True, zebra=True, fontsize=8.1,
                 align_right_cols=(), header_bg=BLUE, extra=None):
    t = Table(data, colWidths=widths, repeatRows=1 if header else 0)
    cmds = [
        ("GRID", (0, 0), (-1, -1), 0.4, LINE),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]
    if header:
        cmds += [("BACKGROUND", (0, 0), (-1, 0), header_bg),
                 ("LINEBELOW", (0, 0), (-1, 0), 0.8, GOLD)]
    if zebra:
        start = 1 if header else 0
        for i in range(start, len(data)):
            if (i - start) % 2 == 1:
                cmds.append(("BACKGROUND", (0, i), (-1, i), ZEBRA))
    if extra:
        cmds += extra
    t.setStyle(TableStyle(cmds))
    return t

# ================================================================ DOC 1
# Contre-DQE : (n°, désignation, unité, qté, PU_matrix, PU_upl) ; montant = qté*PU_upl
LOT_HEADERS = {}
dq = [
    ("LOT 01", "ÉTUDES, INSTALLATION DE CHANTIER ET PRÉPARATION", [
        ("01.01", "Études architecturales d'exécution et plans de structure métallique", "Forfait", 1, 1_500_000, 1_200_000),
        ("01.02", "Études fluides (plomberie, électricité, CVC, SSI) et synthèse", "Forfait", 1, 1_000_000, 800_000),
        ("01.03", "Installation de chantier, gardiennage, signalisation et repli", "Forfait", 1, 2_000_000, 1_000_000)]),
    ("LOT 02", "FONDATIONS ET INFRASTRUCTURES", [
        ("02.01", "Implantation topographique et terrassements généraux", "Forfait", 1, 500_000, 500_000),
        ("02.02", "Fouilles en rigoles et en puits", "m3", 40, 25_000, 20_000),
        ("02.03", "Béton de propreté dosé à 150 kg/m3", "m3", 6, 150_000, 120_000),
        ("02.04", "Béton armé semelles/longrines dosé 350 kg/m3", "m3", 35, 255_000, 230_000),
        ("02.05", "Platines d'ancrage, goujons et boulons de scellement", "Ens.", 1, 3_200_000, 2_400_000)]),
    ("LOT 03", "STRUCTURE MÉTALLIQUE PRINCIPALE (métré optimisé : 47 kg/m2)", [
        ("03.01", "Ossature principale profilés acier S275 (poteaux HEA/HEB, poutres IPN)", "kg", 16_600, 4_300, 2_100),
        ("03.02", "Poutres secondaires, solives et contreventements", "kg", 7_250, 4_300, 2_100),
        ("03.03", "Traitement anticorrosion (primaire + finition polyuréthane)", "m2", 750, 6_500, 5_000)]),
    ("LOT 04", "PLANCHERS ET GALERIES DE CIRCULATION", [
        ("04.01", "Platelage contreplaqué structural phénolique ép. 19 mm", "m2", 504, 19_000, 13_500),
        ("04.02", "Galeries simple appui (suppression des porte-à-faux 1,60 m)", "kg", 2_800, 4_400, 2_150),
        ("04.03", "Platelage et étanchéité technique des galeries extérieures", "m2", 84, 32_000, 22_000)]),
    ("LOT 05", "ESCALIERS MÉTALLIQUES EXTÉRIEURS", [
        ("05.01", "Escalier métallique apparent (limons, marches, paliers)", "U", 3, 4_200_000, 2_400_000)]),
    ("LOT 06", "FAÇADES ET VITRERIE EXTÉRIEURE", [
        ("06.01", "Châssis aluminium pour façades vitrées et ouvrants", "m2", 160, 115_000, 63_000),
        ("06.02", "Vitrage de sécurité feuilleté (classe ajustée aux standards locaux)", "m2", 160, 82_000, 47_000),
        ("06.03", "Portes vitrées d'accès avec quincaillerie", "U", 9, 280_000, 170_000)]),
    ("LOT 07", "CLOISONS INTÉRIEURES ACOUSTIQUES", [
        ("07.01", "Cloisons bois double parement (cp 8 mm + ossature + laine)", "m2", 340, 24_000, 15_000)]),
    ("LOT 08", "PORTES INTÉRIEURES", [
        ("08.01", "Blocs-portes bois/stratifié pour salles de classe", "U", 9, 250_000, 150_000)]),
    ("LOT 09", "FAUX PLAFONDS ET ISOLATION ACOUSTIQUE", [
        ("09.01", "Faux plafonds suspendus modulaires sur ossature métallique", "m2", 504, 19_500, 10_000),
        ("09.02", "Laine de verre acoustique déroulée au-dessus du faux plafond", "m2", 504, 8_000, 4_500)]),
    ("LOT 10", "TOITURE ET ACROTÈRE", [
        ("10.01", "Charpente secondaire toiture et tôles bac acier nervurées", "m2", 168, 22_000, 15_000),
        ("10.02", "Acrotère périphérique h. 0,80 m (structure, parement, étanchéité)", "ml", 58, 38_000, 25_000)]),
    ("LOT 11", "ÉVACUATION DES EAUX PLUVIALES (EP)", [
        ("11.01", "Gouttières, naissances, descentes EP et raccordement", "Ens.", 1, 2_400_000, 1_800_000)]),
    ("LOT 12", "REVÊTEMENTS DE SOL", [
        ("12.01", "Revêtement de sol PVC acoustique U4P3 et plinthes assorties", "m2", 504, 17_500, 10_000)]),
    ("LOT 13", "ÉLECTRICITÉ - COURANTS FORTS", [
        ("13.01", "TGBT, tableaux divisionnaires, câblage et chemins de câbles", "Ens.", 1, 5_500_000, 4_200_000),
        ("13.02", "Appareillage complet (prises, interrupteurs) et luminaires LED", "Ens.", 1, 4_800_000, 3_105_000)]),
    ("LOT 14", "COURANTS FAIBLES ET RÉSEAUX NUMÉRIQUES", [
        ("14.01", "Réseau informatique RJ45, baie de brassage, bornes Wi-Fi", "Ens.", 1, 3_800_000, 2_800_000),
        ("14.02", "Vidéosurveillance, contrôle d'accès, pré-équipement audiovisuel", "Ens.", 1, 3_500_000, 2_200_000)]),
    ("LOT 15", "CLIMATISATION - RÉTABLIE INTÉGRALEMENT DANS LE MARCHÉ", [
        ("15.01", "Climatiseurs split inverter par salle : fourniture, pose, accessoires, protections électriques, évacuations et mise en service", "U", 9, 680_000, 680_000)]),
    ("LOT 16", "PLOMBERIE ET SANITAIRES", [
        ("16.01", "Réseaux EF, évacuations EU/EV et blocs sanitaires complets", "Ens.", 1, 6_500_000, 4_500_000)]),
    ("LOT 17", "SÉCURITÉ INCENDIE (SSI)", [
        ("17.01", "Extincteurs, BAES, blocs d'alarme autonome, signalétique", "Ens.", 1, 2_800_000, 2_000_000)]),
    ("LOT 18", "PEINTURE ET FINITIONS", [
        ("18.01", "Enduits et peinture murs/plafonds (intérieur et extérieur)", "Ens.", 1, 4_800_000, 3_200_000)]),
    ("LOT 19", "BRANDING - SORTI DU MARCHÉ (réalisé par le prestataire graphique de l'UPL)", [
        ("19.01", "Films adhésifs, logos et signalétique directionnelle", "Ens.", 1, 3_500_000, 0)]),
    ("LOT 20", "GARDE-CORPS MÉTALLIQUES", [
        ("20.01", "Garde-corps contemporains pour galeries et escaliers", "ml", 80, 48_000, 28_000)]),
    ("LOT 21", "AMÉNAGEMENTS EXTÉRIEURS", [
        ("21.01", "Nivellement des abords, dallage piéton, caniveau, éclairage", "Ens.", 1, 4_500_000, 2_800_000)]),
    ("LOT 22", "MOBILIER PÉDAGOGIQUE DES 9 SALLES - RÉTABLI DANS LE MARCHÉ", [
        ("22.01", "Tables, chaises étudiants, bureau enseignant et tableaux pour 9 salles", "Ens.", 1, 8_500_000, 8_500_000)]),
    ("LOT 23", "ESSAIS, NETTOYAGE ET RÉCEPTION", [
        ("23.01", "Nettoyage de fin de chantier, essais techniques et DOE", "Ens.", 1, 1_200_000, 1_000_000)]),
]

lot_totals = []
grand = 0
rows = [[P("N°", "cellc"), P("Désignation des ouvrages et prestations", "cell"),
         P("U.", "cellc"), P("Qté", "cellr"), P("PU initial<br/>HT", "cellr"),
         P("PU UPL<br/>HT", "cellr"), P("Montant UPL<br/>HT", "cellrb")]]
for code, title, lines in dq:
    rows.append([P(f"{code} - {title}", "lotrow"), "", "", "", "", "", ""])
    st = 0
    for (n, des, u, q, pu0, pu1) in lines:
        m = q * pu1
        st += m
        rows.append([P(n, "cellc"), P(des, "cell"), P(u, "cellc"),
                     P(fmt(q), "cellr"), P(fmt(pu0) if pu0 else "-", "cellr"),
                     P(fmt(pu1) if pu1 else "hors marché", "cellr"),
                     P(fmt(m) if m else "-", "cellrb")])
    rows.append(["", P(f"Sous-total {code}", "cellb"), "", "", "", "",
                 P(fmt(st), "cellrb")])
    lot_totals.append((code, title, st))
    grand += st

TRAVAUX = grand
FG = round(TRAVAUX * 0.05)
TOT_HT = TRAVAUX + FG
TVA = round(TOT_HT * 0.18)
TTC = TOT_HT + TVA
assert TRAVAUX == 177_540_000, f"Travaux HT inattendus: {TRAVAUX}"
assert FG == 8_877_000, f"FG inattendu: {FG}"
assert TOT_HT == 186_417_000, f"Total HT inattendu: {TOT_HT}"
assert TVA == 33_555_060, f"TVA inattendue: {TVA}"
assert TTC == 219_972_060, f"TTC inattendu: {TTC}"
rows.append(["", P("MONTANT TOTAL TRAVAUX RÉVISÉS HT", "cellb"), "", "", "", "",
             P(fmt(TRAVAUX), "cellrb")])
rows.append(["", P("Frais généraux et aléas (5 %)", "cellb"), "", "", "", "",
             P(fmt(FG), "cellrb")])
rows.append(["", P("MONTANT TOTAL HORS TAXES (HT)", "cellb"), "", "", "", "",
             P(fmt(TOT_HT), "cellrb")])
rows.append(["", P("TVA Gabon 18 %", "cellb"), "", "", "", "", P(fmt(TVA), "cellrb")])
rows.append(["", P("MONTANT TOTAL TTC (FCFA)", "cellb"), "", "", "", "",
             P(fmt(TTC), "cellrb")])

dq_extra = [
    ("BACKGROUND", (0, len(rows)-5), (-1, len(rows)-1), GOLD_LT),
    ("LINEABOVE", (0, len(rows)-5), (-1, len(rows)-5), 0.9, GOLD),
    ("SPAN", (0, len(rows)-5), (5, len(rows)-5)), ("SPAN", (0, len(rows)-4), (5, len(rows)-4)),
    ("SPAN", (0, len(rows)-3), (5, len(rows)-3)), ("SPAN", (0, len(rows)-2), (5, len(rows)-2)),
    ("SPAN", (0, len(rows)-1), (5, len(rows)-1)),
]
for i, r in enumerate(rows):
    if r[1] == "" and r[0] != "":
        dq_extra += [("SPAN", (0, i), (-1, i)), ("BACKGROUND", (0, i), (-1, i), BLUE_DK),
                     ("TOPPADDING", (0, i), (-1, i), 3.5), ("BOTTOMPADDING", (0, i), (-1, i), 3.5)]
    if isinstance(r[1], Paragraph) and str(r[1].text).startswith("Sous-total"):
        dq_extra += [("BACKGROUND", (0, i), (-1, i), BLUE_LT)]

def build_doc1():
    st = []
    st += [P("Négociation de marché de travaux - proposition révisée n° 3 (délai d'exécution 2 mois - décision de la Présidence)", "kicker"),
           P("Contre-proposition de devis - révisée", "h1"),
           P("Bâtiment universitaire R+2 - environ 504 m2 - campus UPL de Sablière, Libreville", "body"),
           Spacer(1, 4)]
    st += [styled_table([
        [P("Émetteur", "cellb"), P("Université Privée de Libreville (UPL) - Présidence", "cell"),
         P("Votre référence", "cellb"), P("Devis quantitatif et estimatif « DEVIS CAMPUS UPL - MATRIX GROUP » du 01/09/2026", "cell")],
        [P("Destinataire", "cellb"), P("MATRIX GROUP, Libreville", "cell"),
         P("Notre référence", "cellb"), P("UPL/DC/2026-08-30/C03 (révision n° 3)", "cell")],
        [P("Objet", "cellb"), P("Contre-proposition révisée et conditions de marché", "cell"),
         P("Date", "cellb"), P("Libreville, le 30 août 2026", "cell")],
    ], [2.1*cm, 6.4*cm, 2.1*cm, 6.4*cm], header=False, zebra=False,
        extra=[("BACKGROUND", (0, 0), (0, -1), BLUE_LT),
               ("BACKGROUND", (2, 0), (2, -1), BLUE_LT),
               ("VALIGN", (0, 0), (-1, -1), "TOP")])]
    st += [Spacer(1, 6)]

    # 1. Résumé exécutif
    st += section("1. Résumé exécutif")
    st += [P("L'UPL prend acte du devis quantitatif et estimatif (DQE) établi le 01/09/2026 pour la "
             "construction de son bâtiment universitaire R+2 d'environ 504 m2 à Sablière (Libreville), "
             "arrêté à <b>409 672 872 FCFA TTC</b>. Après examen détaillé et arbitrage de la "
             "Présidence, l'enveloppe validée est portée à <b>220 000 000 FCFA TTC maximum</b>. La "
             "présente révision n° 2 rétablit intégralement dans le marché la climatisation des "
             "9 salles (fourniture, pose et mise en service) et le mobilier pédagogique complet, "
             "et s'établit à <b>219 972 060 FCFA TTC</b>, soit une économie de "
             "<b>189 700 812 FCFA (-46,3 %)</b> sur le devis initial, en conservant l'intégralité "
             "du programme fonctionnel : 9 salles de cours climatisées et meublées, blocs "
             "sanitaires, salles techniques et numériques, aménagements extérieurs.")]
    st += [styled_table([
        [P("Rubrique", "cellb"), P("Devis reçu", "cellb"), P("Révision n° 2 (UPL)", "cellb"), P("Écart", "cellb")],
        [P("Travaux HT", "cell"), P("330 648 000 FCFA", "cellr"),
         P("177 540 000 FCFA", "cellr"), P("- 46,3 %", "cellr")],
        [P("Frais généraux et aléas (5 %)", "cell"), P("16 532 400 FCFA", "cellr"),
         P("8 877 000 FCFA (base recalibrée)", "cellr"), P("- 46,3 %", "cellr")],
        [P("Montant total HT", "cell"), P("347 180 400 FCFA", "cellr"),
         P("186 417 000 FCFA", "cellr"), P("- 46,3 %", "cellr")],
        [P("TVA 18 %", "cell"), P("62 492 472 FCFA", "cellr"),
         P("33 555 060 FCFA", "cellr"), P("", "cellr")],
        [P("MONTANT TOTAL TTC", "cellb"), P("409 672 872 FCFA", "cellrb"),
         P("<b>219 972 060 FCFA</b>", "cellrb"), P("<b>- 189 700 812 FCFA</b>", "cellrb")],
        [P("Ratio total HT / m2 (504 m2)", "cell"), P("689 000 FCFA/m2", "cellr"),
         P("370 000 FCFA/m2", "cellr"), P("- 46,3 %", "cellr")],
        [P("Marge sous le plafond de 220 000 000 FCFA TTC", "cellb"), P("", "cellr"),
         P("27 940 FCFA", "cellrb"), P("", "cellr")],
    ], [5.0*cm, 3.9*cm, 4.7*cm, 3.4*cm],
        extra=[("BACKGROUND", (0, 5), (-1, 5), GOLD_LT),
               ("LINEABOVE", (0, 5), (-1, 5), 0.9, GOLD),
               ("BACKGROUND", (0, 7), (-1, 7), GOLD_LT),
               ("LINEABOVE", (0, 7), (-1, 7), 0.9, GOLD)])]
    st += [P("Décision de la Présidence du 30 août 2026 : le délai d'exécution est fixé à <b>2 mois "
             "maximum</b>, avec réception partielle de la tranche A (RDC) à 6 semaines, afin que les "
             "cours puissent démarrer dès septembre dans une partie du bâtiment. Le détail des 23 "
             "lots figure en section 4 ; la contre-proposition est transmise pour acceptation sous "
             "10 jours ouvrés.", "note")]

    # 2. Structure du devis reçu
    st += section("2. Rappel de la structure du devis reçu")
    st += [styled_table([
        [P("Poste (DQE du 01/09/2026)", "cell"), P("Montant HT (FCFA)", "cellrb"), P("Observation UPL", "cell")],
        [P("Total HT travaux (lots 01 à 23)", "cell"), P("330 648 000", "cellr"),
         P("Base de calcul conservée pour la comparaison ligne à ligne", "cell")],
        [P("Frais généraux et aléas (5 %)", "cell"), P("16 532 400", "cellr"),
         P("Admis dans la révision n° 3 à 5 % d'une base recalibrée : 8 877 000", "cell")],
        [P("Montant total HT", "cell"), P("347 180 400", "cellr"), P("", "cell")],
        [P("TVA 18 %", "cell"), P("62 492 472", "cellr"), P("Taux conforme à la législation gabonaise", "cell")],
        [P("Montant total TTC", "cellb"), P("409 672 872", "cellrb"),
         P("Dépassement de l'enveloppe Présidence de 209,7 M FCFA (+105 %)", "cell")],
    ], [6.6*cm, 3.3*cm, 7.1*cm],
        extra=[("BACKGROUND", (0, 5), (-1, 5), GOLD_LT)])]

    # 3. Analyse des écarts
    st += section("3. Analyse des écarts au regard des prix de référence au Gabon",
                  "Les références citées sont des bases de prix publiques gabonaises et des textes officiels ; chaque ligne reste négociable sur justificatifs.")
    st += [styled_table([
        [P("Poste", "cellb"), P("Référence Gabon", "cellb"), P("Devis reçu", "cellb"), P("Écart", "cellb")],
        [P("Acier S275JR profilés laminés, travaillé en atelier et monté (lots 03)", "cell"),
         P("<b>env. 1 135 FCFA/kg</b> posé (base de prix publique CYPE Gabon, prix-construction.info, 2025)", "cell"),
         P("4 300 FCFA/kg", "cellr"), P("× 3,8<br/>soit + 53,3 M FCFA sur le seul lot 03", "cellr")],
        [P("Main-d'œuvre charpentier métal", "cell"),
         P("env. 4 000 FCFA/h compagnon CP2 (même base)", "cell"),
         P("non détaillé", "cellr"), P("détail à produire", "cellr")],
        [P("Ciment CEM II 42,5", "cell"),
         P("sac 50 kg plafonné à <b>5 000 FCFA</b> Libreville/Akanda (arrêté n° 0001-23)", "cell"),
         P("inclus au m3", "cellr"), P("poste béton à recalibrer", "cellr")],
        [P("Métré structure (lots 03)", "cell"),
         P("28 000 kg pour 504 m2 = 55,6 kg/m2", "cell"),
         P("55,6 kg/m2", "cellr"), P("optimisable à 47 kg/m2 par étude d'exécution, sans réduction de portée ni de sécurité", "cellr")],
        [P("Frais généraux 5 %", "cell"),
         P("usage local : 5 % admis, calculés sur une base de travaux recalibrée", "cell"),
         P("16 532 400 FCFA", "cellr"), P("ramenés à 8 877 000 FCFA", "cellr")],
    ], [4.0*cm, 6.2*cm, 3.2*cm, 3.6*cm])]
    st += [Spacer(1, 4),
           P("<b>Ce que la révision n° 2 conserve intégralement :</b> la surface développée de "
             "504 m2, les 9 salles de cours, l'ossature acier S275 avec traitement anticorrosion, la "
             "climatisation par salle (9 splits inverter, 6 120 000 FCFA HT, fourniture, pose, "
             "accessoires, protections électriques, évacuations et mise en service comprises), le "
             "mobilier complet des 9 salles (8 500 000 FCFA HT), les réseaux informatiques et la "
             "vidéosurveillance, la sécurité incendie, les aménagements extérieurs et la livraison "
             "avec dossier des ouvrages exécutés. "
             "<b>Ce qu'elle ajuste :</b> (i) le prix de l'acier au niveau d'un double de la base "
             "publique, intégrant import, finition et marge d'entrepreneur ; (ii) le métré structurel, "
             "optimisé par l'étude d'exécution ; (iii) les porte-à-faux de 1,60 m remplacés par des "
             "galeries sur simple appui, à surface de circulation équivalente ; (iv) le classement du "
             "vitrage ajusté aux standards locaux ; (v) le lot 19 (branding), seul, reste traité en "
             "direct par le prestataire graphique de l'UPL ; (vi) les frais généraux et aléas "
             "maintenus à 5 %, mais calculés sur la base de travaux recalibrée (8 877 000 FCFA "
             "au lieu de 16 532 400 FCFA).")]

    # 4. DQE contre-proposition
    st += section("4. Devis quantitatif et estimatif - contre-proposition UPL",
                  "Prix unitaires cibles en FCFA hors taxes. Quantités ajustées après optimisation du métré (notes en tête de lot).")
    st += [styled_table(rows, [1.25*cm, 6.15*cm, 0.95*cm, 1.35*cm, 1.75*cm, 1.75*cm, 2.1*cm],
                        extra=dq_extra)]
    st += [P("Montant total TTC de la révision n° 3 : <b>219 972 060 FCFA</b> "
             "(travaux révisés 177 540 000 FCFA HT + frais généraux et aléas 5 % : 8 877 000 FCFA, "
             "soit 186 417 000 FCFA HT + TVA 18 %), laissant une marge de <b>27 940 FCFA</b> sous le "
             "plafond de 220 000 000 FCFA TTC validé par la Présidence. Le lot 19 (branding) seul "
             "reste hors marché et est traité directement par l'UPL ; la climatisation (lot 15) et le "
             "mobilier des 9 salles (lot 22) sont rétablis intégralement.", "small"),
           P("Nota : l'UPL étudie avec son conseil fiscal l'éligibilité du projet à des régimes "
             "d'exonération (enseignement supérieur privé, code des investissements). Le montant "
             "ci-dessus intègre la TVA à 18 % en l'état actuel de la réglementation.", "note")]

    # 5. Variante phasage
    st += section("5. Variante de phasage (si préférence pour une exécution en deux temps)")
    st += [styled_table([
        [P("Phase", "cellb"), P("Contenu", "cellb"), P("Travaux HT (FCFA)", "cellrb"), P("TTC indicatif (FCFA)", "cellrb")],
        [P("Phase 1 - reprise 2026/2027", "cell"),
         P("RDC + R+1 entièrement achevés, meublés et climatisés (6 salles, sanitaires, locaux "
           "techniques), structure calculée pour recevoir le R+2 ultérieurement - tranche A (RDC) "
           "réceptionnée en priorité à 6 semaines", "cell"),
         P("127 500 000", "cellr"), P("157 972 500", "cellrb")],
        [P("Phase 2 - croissance", "cell"),
         P("Achèvement du R+2 (3 salles complémentaires), finitions et vitrages définitifs", "cell"),
         P("50 040 000", "cellr"), P("61 999 560", "cellrb")],
        [P("TOTAL phasé", "cellb"), P("Identique au programme complet", "cellb"),
         P("177 540 000", "cellr"), P("219 972 060", "cellrb")],
    ], [3.4*cm, 8.3*cm, 2.8*cm, 2.9*cm], extra=[("BACKGROUND", (0, 3), (-1, 3), GOLD_LT)])]

    # 6. Conditions
    st += section("6. Conditions de marché proposées par l'UPL")
    st += [styled_table([
        [P("Délai d'exécution", "cellb"), P("<b>2 mois maximum</b> à compter de l'ordre de service, en cadence renforcée (double équipe, 6 jours sur 7) : réception partielle de la tranche A (RDC, 4 à 6 salles) à <b>6 semaines</b> pour permettre la tenue des cours dès la rentrée de septembre, réception complète à 2 mois ; pénalités de retard de 1/1000 du montant TTC par jour calendaire, plafonnées à 10 %", "cell")],
        [P("Modalités de paiement", "cellb"), P("<b>25 %</b> d'avance de démarrage à la commande (contre garantie bancaire de bonne exécution de 10 %) · <b>50 %</b> à mi-chantier · <b>25 %</b> à la livraison", "cell")],
        [P("Avantages offerts à l'entreprise", "cellb"), P("Paiements ponctuels par virement ou mobile money professionnel, accès permanent au chantier, interlocuteur unique (Présidence), perspective d'un marché de maintenance pluriannuel et d'un accès prioritaire à la phase 2 si le présent marché est exécuté dans les délais et le budget", "cell")],
        [P("Réponse attendue", "cellb"), P("Acceptation ou contre-offre argumentée ligne à ligne sous <b>10 jours ouvrés</b>", "cell")],
    ], [4.1*cm, 13.1*cm], header=False, zebra=False,
        extra=[("BACKGROUND", (0, 0), (0, -1), BLUE_LT), ("VALIGN", (0, 0), (-1, -1), "TOP")])]

    st += [Spacer(1, 10),
           P("L'UPL souhaite vivement aboutir avec MATRIX GROUP, dont le dossier technique a retenu "
             "notre attention. La présente révision n° 2, arrêtée à 219 972 060 FCFA TTC après "
             "arbitrage de la Présidence, rétablit la climatisation et le mobilier dans le marché et "
             "a pour seul objectif de conclure dans l'enveloppe validée tout en sécurisant "
             "l'entreprise sur ses paiements et son carnet de commandes. Nous restons à "
             "disposition pour une réunion de chantier à Sablière dans la semaine suivant la réception."),
           Spacer(1, 14)]
    st += [Table([[P("Le Président-Fondateur de l'UPL", "bodyc"),
                   P("", "bodyc")], [P("<b>Serge Patrick MINANG</b>", "bodyc"), P("", "bodyc")]],
                 colWidths=[8.6*cm, 8.6*cm],
                 style=TableStyle([("LINEABOVE", (0, 0), (0, 0), 0.6, GREY)]))]
    st += [Spacer(1, 8),
           P("Sources des références de prix : base de prix publique CYPE / prix-construction.info "
             "(éditions Gabon 2025) ; arrêté n° 0001-23 fixant les prix plafonds du ciment ; "
             "annuaires professionnels du BTP au Gabon (Filao, AfricanNuaire). "
             "Document établi le 30 août 2026 - valable 21 jours.", "note")]

    doc = Doc(OUT1, "UPL - Contre-proposition de devis, révision n° 2 - campus de Sablière - confidentiel")
    st = [x for x in st]
    doc.build(st)
    return doc

# ================================================================ DOC 2
def build_doc2():
    st = []
    st += [P("Document de pilotage - à valider par le Président avant exécution", "kicker"),
           P("Plan de communication - rentrée 2026-2027", "h1"),
           P("Pré-inscriptions, ouverture des six filières et Executive MBA - budget intégré au crédit d'investissement de 260 M FCFA sollicité auprès d'Ecobank - adapté aux réalités "
             "du Gabon : réseaux parfois bloqués, paiements par mobile money, importance du terrain "
             "et du phoning.", "body"), Spacer(1, 4)]

    # 1 Contexte & objectifs
    st += section("1. Contexte et objectifs de campagne")
    st += [P("La rentrée 2026-2027 marque le changement d'échelle de l'UPL : ouverture de six filières "
             "(Gouvernance et Management · Économie Numérique et IA · Économie Bleue · Droit · "
             "Assurance et Sécurité Sociale · CPGE) aux côtés de l'Executive MBA délivré avec "
             "l'Université de Douala. Objectifs alignés sur le plan de développement validé dans le "
             "dossier de financement :")]
    st += [styled_table([
        [P("Objectif sur 12 mois", "cellb"), P("Cible", "cellrb")],
        [P("Contacts qualifiés générés (tunnel commercial)", "cell"), P("3 000", "cellr")],
        [P("Pré-inscriptions issues du tunnel", "cell"), P("500", "cellr")],
        [P("Étudiants inscrits, toutes filières (premier palier)", "cell"), P("100 et plus", "cellr")],
        [P("Coût d'acquisition maximum par étudiant inscrit", "cell"), P("150 000 FCFA", "cellr")],
        [P("Délai de réponse à chaque lead (phoning / WhatsApp)", "cell"), P("moins de 48 h ouvrées", "cellr")],
    ], [11.5*cm, 5.7*cm])]
    st += [P("Calendrier immobilier : la rentrée 2026 démarre dans les locaux actuels de Sablière ; les cours basculent dans le nouveau bâtiment pédagogique R+2 (tranche A livrée à 6 semaines, bâtiment complet sous 2 mois) au fil des réceptions partielles.<br/>Message central validé : <b>« UPL - Formez-vous aujourd'hui aux métiers de demain. »</b> "
             "Aucune date de rentrée n'est communiquée tant qu'elle n'est pas confirmée par la Présidence.", "note")]

    # 2 Le Gabon en chiffres
    st += section("2. Le Gabon en chiffres - ce que cela impose au plan",
                  "Sources : DataReportal / GSMA Intelligence « Digital 2025 - Gabon » ; ARCEP Gabon, observatoire du marché mobile, 1er trimestre 2025.")
    st += [styled_table([
        [P("Indicateur", "cellb"), P("Valeur", "cellrb"), P("Conséquence pour l'UPL", "cellb")],
        [P("Population / âge médian", "cell"), P("2,57 M hab. / 21,5 ans", "cellr"),
         P("Cœur de cible jeune : bacheliers et 18-24 ans (11,8 % de la population)", "cell")],
        [P("Population urbaine", "cell"), P("91,4 %", "cellr"),
         P("Concentration Libreville / Akanda : affichage et terrain très rentables", "cell")],
        [P("Utilisateurs d'internet", "cell"), P("1,84 M (71,9 %)", "cellr"),
         P("Digital utile, mais jamais seul canal", "cell")],
        [P("Comptes sur les réseaux sociaux", "cell"), P("782 000 (30,5 %)", "cellr"),
         P("Facebook / WhatsApp / TikTok prioritaires ; LinkedIn pour les cadres", "cell")],
        [P("Connexions mobiles", "cell"), P("3,19 M (124 %), 88 % en 3G/4G", "cellr"),
         P("Tout le contenu doit être « mobile first », léger, en vidéo courte", "cell")],
        [P("Répartition opérateurs", "cell"), P("Moov 51,1 % / Airtel 48,9 %", "cellr"),
         P("Encaissements : accepter Airtel Money ET Moov Money", "cell")],
    ], [4.3*cm, 4.2*cm, 8.7*cm])]
    st += [P("Lecture stratégique : même avec 71,9 % d'internautes, le risque de blocage ou de "
             "ralentissement des réseaux (attesté ces dernières années au Gabon) impose qu'au moins "
             "la moitié du budget soit « hors data » : radio, presse, affichage, terrain et phoning.",
             "note")]

    # 3 Contraintes
    st += section("3. Contraintes spécifiques et réponses du plan")
    st += [styled_table([
        [P("Contrainte constatée", "cellb"), P("Réponse prévue", "cellb")],
        [P("Blocage ou bridage des réseaux internet et sociaux ; recours généralisé aux VPN", "cell"),
         P("Plan de continuité (section 9) : canaux hors data (radio, presse L'Union, affichage, SMS, terrain) toujours actifs en parallèle ; contenus préparés à l'avance et programmables ; équipe dotée de connexions des deux opérateurs", "cell")],
        [P("Refus / faible usage de la carte bancaire ; l'argent mobile domine (inverse de la France)", "cell"),
         P("Airtel Money déjà intégré au site (avec justificatif + confirmation UPL) ; activation de Moov Money ; espèces acceptées uniquement au secrétariat contre reçu numéroté ; virement possible ; aucune demande de paiement par carte", "cell")],
        [P("Préférence pour la relation directe et la parole de confiance", "cell"),
         P("Phoning structuré (section 6), journées portes ouvertes à Sablière, ambassadeurs alumni (env. 80 cadres formés), mot du Président en rendez-vous physiques", "cell")],
        [P("Presse et radio restent des médias de référence", "cell"),
         P("Encarts dans L'Union, passages radio (invitations du Président en interview), épisodes TV avec les deux films institutionnels déjà produits", "cell")],
    ], [6.3*cm, 10.9*cm])]

    # 4 Cibles & messages
    st += section("4. Cibles, messages et offres")
    st += [styled_table([
        [P("Cible", "cellb"), P("Message", "cellb"), P("Canaux principaux", "cellb")],
        [P("Bacheliers et parents (Libreville, Akanda, Estuaire)", "cell"),
         P("Six filières d'avenir à Sablière ; tarifs verrouillés et affichés ; pré-inscription simple ; paiement en tranches", "cell"),
         P("WhatsApp · Facebook · TikTok · affichage · lycées · radio", "cell")],
        [P("Cadres et dirigeants (public, parapublic, privé)", "cell"),
         P("Executive MBA en soirées (17 h - 21 h), partenariat Université de Douala, jusqu'à 8 échéances ; 4 000 000 FCFA", "cell"),
         P("LinkedIn · WhatsApp · phoning · rendez-vous d'entreprise", "cell")],
        [P("Entreprises et institutions", "cell"),
         P("Formations sur mesure, partenariats de recherche et de recrutement - sur rendez-vous, sans annonce de partenariats non signés", "cell"),
         P("LinkedIn · e-mail contact@ · visites de la Présidence", "cell")],
        [P("Diaspora et sous-région (Cameroun, Congo, Guinée Équatoriale)", "cell"),
         P("Un campus à Libreville, des diplômes reconnus, un accompagnement à l'installation", "cell"),
         P("Facebook · WhatsApp · site bilingue FR/EN", "cell")],
    ], [4.2*cm, 8.4*cm, 4.6*cm])]

    # 5 Dispositif par canal
    st += section("5. Dispositif par canal")
    st += [styled_table([
        [P("Canal", "cellb"), P("Rôle et actions", "cellb"), P("Règles", "cellb")],
        [P("WhatsApp Business (n° Président)", "cell"),
         P("Hub central : réponse aux leads sous 48 h, diffusion des fiches programme, relances, confirmation des paiements mobile money", "cell"),
         P("Fiche alignée sur le site ; compte unique existant ; aucun second numéro", "cell")],
        [P("Facebook + Instagram", "cell"),
         P("Vitrine quotidienne : annonces pré-inscriptions, tarifs, pôles, événement rentrée épinglé ; publicité ciblée Libreville/Akanda", "cell"),
         P("Pages officielles via contact@upl-gabon.com ; 2 administrateurs UPL minimum", "cell")],
        [P("TikTok (@upl.gabon)", "cell"),
         P("Formats courts pour bacheliers : campus, métiers, témoignages alumni, réponses aux questions fréquentes", "cell"),
         P("Vraies images et visuels validés uniquement - pas de visages générés par IA", "cell")],
        [P("LinkedIn", "cell"),
         P("Executive MBA, DBA, partenariats entreprises, publication des contenus B2B et du mot du Président", "cell"),
         P("Publications moins fréquentes mais irréprochables (références réelles)", "cell")],
        [P("Site upl-gabon.com + SEO", "cell"),
         P("Page officielle des tarifs et de la pré-inscription ; version anglaise ; formulaire de contact", "cell"),
         P("Site figé : toute modification validée par la Présidence", "cell")],
        [P("Radio (locales Libreville)", "cell"),
         P("Spots de pré-inscription + interviews du Président (rentrée, métiers d'avenir)", "cell"),
         P("Contrats courts, renouvelables selon audience constatée", "cell")],
        [P("Presse écrite - L'Union", "cell"),
         P("Encarts « pré-inscriptions ouvertes » et annonce d'ouverture des filières ; interview de rentrée", "cell"),
         P("Caler la parution sur les journées portes ouvertes", "cell")],
        [P("Affichage 4x3", "cell"),
         P("Axes passants Libreville / Akanda : Sablière, Mont-Bouët, PK, carrefours scolaires", "cell"),
         P("Visuel unique et numéro WhatsApp unique", "cell")],
        [P("TV", "cell"),
         P("Diffusion des deux films institutionnels déjà produits lors des créneaux familiaux", "cell"),
         P("Pas de production nouvelle cette année", "cell")],
        [P("Terrain", "cell"),
         P("2 journées portes ouvertes à Sablière ; tournées des lycées et centres d'examen ; présence aux salons étudiants ; relais églises et associations de parents", "cell"),
         P("Équipe : 2 commerciaux recruteurs financés par le plan de développement", "cell")],
        [P("Phoning", "cell"),
         P("Fichier des pré-inscrits et des contacts lycées : appel de qualification, invitation à la porte ouverte, relance à J+7 ; créneaux 18 h - 21 h en semaine, 10 h - 13 h le samedi", "cell"),
         P("Script court validé ; mention systématique des numéros officiels UPL", "cell")],
    ], [3.3*cm, 9.5*cm, 4.4*cm], fontsize=7.9)]

    # 6 Encaissement
    st += section("6. Encaissement des frais - procédure sécurisée (sans carte bancaire)")
    st += [styled_table([
        [P("Étape", "cellb"), P("Détail", "cellb")],
        [P("1. Pré-inscription", "cell"), P("Gratuite : formulaire papier au secrétariat ou fiche WhatsApp / site. Renseignée dans le tableau de suivi (date, nom, téléphone, formation, relance)", "cell")],
        [P("2. Paiement", "cell"), P("Frais d'inscription et tranches (jusqu'à 8 échéances pour le MBA) réglés par Airtel Money ou Moov Money aux numéros officiels UPL, ou en espèces au secrétariat, ou par virement", "cell")],
        [P("3. Justificatif", "cell"), P("L'étudiant conserve et transmet son justificatif mobile money (capture ou SMS) par WhatsApp au secrétariat", "cell")],
        [P("4. Confirmation UPL", "cell"), P("Le secrétariat vérifie l'encaissement, délivre un reçu numéroté et la confirmation officielle (contact@upl-gabon.com) qui valide le dossier", "cell")],
    ], [3.4*cm, 13.8*cm], header=False, zebra=False,
        extra=[("BACKGROUND", (0, 0), (0, -1), BLUE_LT)])]
    st += [P("Règles anti-fraude : numéros de paiement communiqués uniquement sur les documents "
             "officiels UPL ; aucun intermédiaire itinérant n'est habilité à encaisser ; la confirmation "
             "ne vient jamais d'une adresse personnelle. Ajouter Moov Money (51 % des abonnés mobiles) "
             "à l'offre existante Airtel Money est un chantier prioritaire de la semaine 0.", "note")]

    # 7 Calendrier
    st += section("7. Calendrier d'exécution (8 semaines puis rythme de croisière)",
                  "Reprend le kit éditorial existant (pièces P1 à P10). Aucune publication sans validation préalable du Président.")
    st += [styled_table([
        [P("Semaine", "cellb"), P("Objectif", "cellb"), P("Actions clés", "cellb")],
        [P("S0", "cellrb"), P("Préparation", "cell"),
         P("Activation des comptes officiels (contact@upl-gabon.com, 2FA, 2 admins UPL) ; validation des textes et visuels ; activation Moov Money ; impression du kit hors-ligne (flyers, affiches, fiches tarifs) ; formation de l'équipe au tableau de suivi", "cell")],
        [P("S1", "cellrb"), P("Présence", "cell"),
         P("P1 annonce des pré-inscriptions (tous canaux) · P2 Licence 1 · P3 Executive MBA (LinkedIn) · P6 comment se pré-inscrire · P8 replay TV", "cell")],
        [P("S2", "cellrb"), P("Offre", "cell"),
         P("P4 grille tarifaire · P5 les six pôles · P7 paiement (tranches, mobile money, justificatif) · relance de P1", "cell")],
        [P("S3", "cellrb"), P("Preuve et B2B", "cell"),
         P("Modules du MBA (reprise exacte du site) · P9 partenariats entreprises (LinkedIn) · mot du Président si photo réelle fournie", "cell")],
        [P("S4", "cellrb"), P("Terrain - vague 1", "cell"),
         P("1re journée portes ouvertes à Sablière · tournée des lycées · démarrage du phoning · interviews radio du Président", "cell")],
        [P("S5", "cellrb"), P("Médias", "cell"),
         P("Pose de l'affichage 4x3 · encarts L'Union · spots radio · diffusion TV des films", "cell")],
        [P("S6", "cellrb"), P("Dernière ligne droite", "cell"),
         P("Relances téléphoniques des pré-inscrits · 2e journée portes ouvertes · diffusions WhatsApp groupées", "cell")],
        [P("S7", "cellrb"), P("Rentrée", "cell"),
         P("Cérémonie de rentrée · couverture photo et vidéo (images réelles) · témoignages · remerciements publics aux partenaires signés", "cell")],
        [P("S8+", "cellrb"), P("Croisière", "cell"),
         P("2 à 3 publications par semaine tirées du kit ; chaque lead traité sous 48 h ; reporting hebdomadaire à la Présidence", "cell")],
    ], [1.6*cm, 3.4*cm, 12.2*cm], fontsize=7.9)]

    # 8 Budget
    st += section("8. Budget : 15 000 000 FCFA (12 mois)",
                  "Poste « communication et marketing » du plan d'emploi du crédit d'investissement de 260 000 000 FCFA sollicité auprès d'Ecobank Gabon.")
    st += [styled_table([
        [P("Poste", "cellb"), P("Détail", "cellb"), P("Montant (FCFA)", "cellrb"), P("Part", "cellrb")],
        [P("Affichage et médias hors digital", "cell"), P("Affichage 4x3 Libreville/Akanda (1,9 M) · spots radio (1,2 M) · encarts presse L'Union (0,9 M)", "cell"), P("4 000 000", "cellr"), P("27 %", "cellr")],
        [P("Digital et réseaux sociaux", "cell"), P("Publicités Facebook/Instagram/TikTok/LinkedIn (2,0 M) · production de contenus (1,0 M) · site et SEO (0,5 M)", "cell"), P("3 500 000", "cellr"), P("23 %", "cellr")],
        [P("Terrain et prospection", "cell"), P("Journées portes ouvertes (1,0 M) · tournées lycées et salons (1,0 M) · crédits téléphoniques phoning (1,0 M)", "cell"), P("3 000 000", "cellr"), P("20 %", "cellr")],
        [P("Influence et relations publiques", "cell"), P("Programme ambassadeurs alumni · interviews radio/TV · vidéo de rentrée", "cell"), P("2 000 000", "cellr"), P("13 %", "cellr")],
        [P("Community management", "cell"), P("Animation quotidienne des comptes et production éditoriale (12 mois)", "cell"), P("1 500 000", "cellr"), P("10 %", "cellr")],
        [P("Événementiel et PLV", "cell"), P("Cérémonie de rentrée · kakémonos · flyers · trousses commerciales", "cell"), P("1 000 000", "cellr"), P("7 %", "cellr")],
        [P("TOTAL", "cellb"), P("", "cell"), P("15 000 000", "cellrb"), P("100 %", "cellrb")],
    ], [4.1*cm, 8.0*cm, 3.0*cm, 2.1*cm],
        extra=[("BACKGROUND", (0, 7), (-1, 7), GOLD_LT), ("LINEABOVE", (0, 7), (-1, 7), 0.9, GOLD)])]
    st += [P("Répartition « hors data » : 60 % du budget (affichage/médias, terrain, influence, "
             "événementiel) restent actifs même en cas de blocage des réseaux ; 40 % (digital, "
             "community management) accélèrent lorsque les réseaux sont ouverts.", "note")]

    # 9 Continuité
    st += section("9. Plan de continuité en cas de blocage des réseaux")
    st += [styled_table([
        [P("Scénario", "cellb"), P("Bascule immédiate", "cellb"), P("Responsable", "cellb")],
        [P("Réseaux sociaux bridés / coupés", "cell"),
         P("SMS aux pré-inscrits (les deux opérateurs) · phoning intensifié · radio · affichage · relais physiques (lycées, églises, associations de parents)", "cell"),
         P("Secrétariat + commerciaux", "cell")],
        [P("Internet mobile coupé", "cell"),
         P("Le kit hors-ligne déjà imprimé prend le relais : flyers, fiches tarifs, affiches ; accueil renforcé au secrétariat de Sablière ; au besoin, passages radio du Président", "cell"),
         P("Présidence", "cell")],
        [P("Réseaux ouverts mais lents (VPN)", "cell"),
         P("Contenus légers (texte + image) privilégiés ; publication différée programmée ; WhatsApp en messages courts", "cell"),
         P("Community manager", "cell")],
        [P("Fichier de suivi", "cell"),
         P("Double saisie quotidienne : registre papier au secrétariat + tableur hors ligne ; aucune perte de lead en cas de coupure", "cell"),
         P("Secrétariat", "cell")],
    ], [3.9*cm, 10.3*cm, 3.0*cm])]

    # 10 Gouvernance
    st += section("10. Organisation et gouvernance")
    st += [styled_table([
        [P("Rôle", "cellb"), P("Responsabilité", "cellb")],
        [P("Président (Serge Patrick MINANG)", "cell"), P("Valide textes, visuels, budget et calendrier avant toute publication ou dépense ; porte-parole en radio/TV/presse", "cell")],
        [P("Secrétariat (présidence)", "cell"), P("Tableau de suivi des leads, reçus numérotés, confirmations d'inscription, coordination des appels", "cell")],
        [P("2 commerciaux recruteurs terrain", "cell"), P("Phoning, tournées lycées, portes ouvertes, salons - plan de développement (poste « renforcement équipe »)", "cell")],
        [P("Community manager", "cell"), P("Animation quotidienne, veille, remontée des leads vers le tableau de suivi sous 24 h", "cell")],
        [P("Règles de sécurité des comptes", "cell"), P("E-mail officiel contact@upl-gabon.com pour tous les comptes ; double authentification sur téléphones UPL ; 2 administrateurs UPL minimum ; jamais de prestataire unique propriétaire", "cell")],
    ], [5.2*cm, 12.0*cm], header=False, zebra=False,
        extra=[("BACKGROUND", (0, 0), (0, -1), BLUE_LT)])]

    # 11 KPI
    st += section("11. Indicateurs de pilotage et reporting")
    st += [styled_table([
        [P("Indicateur", "cellb"), P("Fréquence", "cellb"), P("Cible", "cellb")],
        [P("Leads enregistrés (tous canaux)", "cell"), P("Hebdomadaire", "cell"), P("3 000 sur 12 mois (env. 60/semaine)", "cell")],
        [P("Pré-inscriptions", "cell"), P("Hebdomadaire", "cell"), P("500 sur 12 mois", "cell")],
        [P("Inscriptions confirmées et encaissées", "cell"), P("Mensuelle", "cell"), P("100 et plus (premier palier)", "cell")],
        [P("Coût par inscription", "cell"), P("Mensuelle", "cell"), P("150 000 FCFA max.", "cell")],
        [P("Délai de réponse aux leads", "cell"), P("Hebdomadaire", "cell"), P("< 48 h ouvrées", "cell")],
        [P("Publications réalisées / prévues", "cell"), P("Hebdomadaire", "cell"), P("2 à 3 par semaine", "cell")],
        [P("Encaissements mobile money rapprochés", "cell"), P("Mensuelle", "cell"), P("100 % des reçus émis", "cell")],
    ], [6.2*cm, 3.4*cm, 7.6*cm])]

    # 12 Décision
    st += section("12. Décision attendue du Président")
    st += [styled_table([
        [P("N°", "cellc"), P("Décision à valider", "cellb"), P("Oui / Non / Ajuster", "cellc")],
        [P("1", "cellc"), P("Budget de communication de 15 000 000 FCFA et sa répartition", "cell"), P("", "cellc")],
        [P("2", "cellc"), P("Activation de Moov Money en complément d'Airtel Money pour les encaissements", "cell"), P("", "cellc")],
        [P("3", "cellc"), P("Lancement de la semaine 0 (comptes officiels, kit hors-ligne, équipe)", "cell"), P("", "cellc")],
        [P("4", "cellc"), P("Commande des médias : affichage, radio, encarts L'Union, spots TV", "cell"), P("", "cellc")],
        [P("5", "cellc"), P("Plan de continuité réseau et procédure d'encaissement ci-dessus", "cell"), P("", "cellc")],
    ], [1.1*cm, 12.1*cm, 4.0*cm])]
    st += [Spacer(1, 10),
           P("Document de travail établi le 30 août 2026 pour la Présidence de l'UPL. Chiffres "
             "Gabon : DataReportal / GSMA Intelligence (Digital 2025 - Gabon) et ARCEP Gabon "
             "(observatoire mobile T1 2025). Objectifs et budget alignés sur le dossier de crédit "
             "d'investissement de 260 000 000 FCFA (V12) présenté à Ecobank Gabon.", "note")]

    doc = Doc(OUT2, "UPL - Plan de communication rentrée 2026-2027 - à valider par le Président")
    doc.build(st)
    return doc

if __name__ == "__main__":
    os.makedirs(HERE, exist_ok=True)
    d1 = build_doc1()
    d2 = build_doc2()
    print("OK")
    print(" 1:", OUT1)
    print("    pages:", d1.page)
    print(" 2:", OUT2)
    print("    pages:", d2.page)
    print(f" Totaux doc1 : HT {fmt(grand)} · TVA {fmt(TVA)} · TTC {fmt(TTC)}")
