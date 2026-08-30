#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Présentation UPL (slides paysage) — à joindre aux emails de partenariat pour déclencher la réponse."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle, PageBreak)

from generer_livrables import (P, S, styled_table, LOGO,
                               BLUE, BLUE_DK, GOLD, GOLD_LT, BLUE_LT, GREY, LINE, ZEBRA)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "UPL_Presentation_Partenariats.pdf")
PAGE = landscape(A4)          # 29.7 x 21 cm

S["kicker"] = ParagraphStyle("kicker", fontName="Helvetica-Bold", fontSize=10,
                             textColor=GOLD, leading=13)
S["h1"] = ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=20, leading=24,
                         textColor=BLUE, spaceAfter=4)
S["lead"] = ParagraphStyle("lead", fontName="Helvetica", fontSize=11.5, leading=16,
                           textColor=GREY, alignment=TA_JUSTIFY)
S["big"] = ParagraphStyle("big", fontName="Helvetica-Bold", fontSize=30, leading=34,
                          textColor=colors.white, alignment=TA_CENTER)
S["coverSub"] = ParagraphStyle("coverSub", fontName="Helvetica", fontSize=14, leading=19,
                               textColor=GOLD, alignment=TA_CENTER)
S["coverNote"] = ParagraphStyle("coverNote", fontName="Helvetica", fontSize=10.5, leading=14,
                                textColor=colors.HexColor("#C6D2E8"), alignment=TA_CENTER)
S["stat"] = ParagraphStyle("stat", fontName="Helvetica-Bold", fontSize=19, leading=22,
                           textColor=BLUE, alignment=TA_CENTER)
S["statl"] = ParagraphStyle("statl", fontName="Helvetica", fontSize=8.6, leading=11,
                            textColor=GREY, alignment=TA_CENTER)
S["cardt"] = ParagraphStyle("cardt", fontName="Helvetica-Bold", fontSize=12.5, leading=15,
                            textColor=BLUE)
S["cardb"] = ParagraphStyle("cardb", fontName="Helvetica", fontSize=9.6, leading=13,
                            textColor=GREY, alignment=TA_JUSTIFY)

class Deck(BaseDocTemplate):
    def __init__(self, path, **kw):
        super().__init__(path, pagesize=PAGE, leftMargin=1.7*cm, rightMargin=1.7*cm,
                         topMargin=2.1*cm, bottomMargin=1.55*cm, **kw)
        fr = Frame(self.leftMargin, self.bottomMargin, self.width, self.height, id="s")
        self.addPageTemplates([
            PageTemplate(id="cover", frames=[Frame(1.7*cm, 1.55*cm, PAGE[0]-3.4*cm, PAGE[1]-3.1*cm, id="c")], onPage=self._cover),
            PageTemplate(id="slide", frames=[fr], onPage=self._slide)])

    def _cover(self, c, doc):
        w, h = PAGE
        c.saveState()
        c.setFillColor(BLUE); c.rect(0, 0, w, h, stroke=0, fill=1)
        c.setFillColor(BLUE_DK); c.rect(0, 0, w, 6.2*cm, stroke=0, fill=1)
        c.setFillColor(GOLD); c.rect(0, 6.2*cm, w, 0.22*cm, stroke=0, fill=1)
        if os.path.exists(LOGO):
            c.drawImage(LOGO, w/2 - 2.1*cm, h - 5.6*cm, width=4.2*cm, height=2.67*cm,
                        mask="auto", preserveAspectRatio=True)
        c.setFillColor(GOLD); c.setFont("Helvetica-Bold", 8.8)
        c.drawCentredString(w/2, 1.85*cm, "EXCELLENCE   ·   INNOVATION   ·   LEADERSHIP")
        c.setFillColor(colors.HexColor("#9FB2D6")); c.setFont("Helvetica", 8.6)
        c.drawCentredString(w/2, 1.25*cm, "Sablière, face Résidence de l'Ambassade d'Arabie Saoudite - Libreville (Gabon)   ·   contact@upl-gabon.com   ·   www.upl-gabon.com")
        c.restoreState()

    def _slide(self, c, doc):
        w, h = PAGE
        c.saveState()
        c.setFillColor(BLUE); c.rect(0, h-1.35*cm, w, 1.35*cm, stroke=0, fill=1)
        c.setFillColor(GOLD); c.rect(0, h-1.47*cm, w, 0.12*cm, stroke=0, fill=1)
        c.setFillColor(colors.white); c.setFont("Helvetica-Bold", 8.3)
        c.drawString(1.7*cm, h-0.9*cm, "UPL  ·  Proposition de coopération académique  ·  Gabon / CEMAC")
        if os.path.exists(LOGO):
            c.drawImage(LOGO, w-2.35*cm, h-1.22*cm, width=1.05*cm, height=0.67*cm,
                        mask="auto", preserveAspectRatio=True)
        c.setStrokeColor(GOLD); c.setLineWidth(0.7)
        c.line(1.7*cm, 1.15*cm, w-1.7*cm, 1.15*cm)
        c.setFillColor(colors.HexColor("#6B7382")); c.setFont("Helvetica", 7.4)
        c.drawString(1.7*cm, 0.8*cm, "Université Privée de Libreville - Serge Patrick MINANG, Président-Fondateur - +241 062 62 19 78 - contact@upl-gabon.com")
        c.drawRightString(w-1.7*cm, 0.8*cm, f"{doc.page}")
        c.restoreState()

def slide(st, kicker, title, content):
    st += [Paragraph(kicker, S["kicker"]), Paragraph(title, S["h1"]), Spacer(1, 6)] + content + [PageBreak()]
    return st

def stat_row(items):
    cells = [[P(n, "stat"), P(l, "statl")] for n, l in items]
    t = Table([cells], colWidths=[(PAGE[0]-3.4*cm)/len(items)]*len(items))
    t.setStyle(TableStyle([
        ("BOX", (0, 0), (-1, -1), 0.9, GOLD),
        ("INNERGRID", (0, 0), (-1, -1), 0.45, GOLD),
        ("BACKGROUND", (0, 0), (-1, -1), GOLD_LT),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 9),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6)]))
    return t

def build():
    W = PAGE[0] - 3.4*cm
    st = []

    # ---- 1. COUVERTURE
    st += [Spacer(1, 2.2*cm),
           Paragraph("UNIVERSITÉ PRIVÉE DE LIBREVILLE", S["big"]),
           Spacer(1, 0.5*cm),
           Paragraph("Présentation institutionnelle et proposition de coopération académique", S["coverSub"]),
           Spacer(1, 1.1*cm),
           Paragraph("Gabon  ·  Afrique centrale  ·  zone CEMAC", S["coverNote"]),
           Paragraph("Executive MBA depuis 2022 avec l'Université de Douala  ·  six filières à la rentrée 2026", S["coverNote"]),
           Spacer(1, 1.5*cm),
           Paragraph("Présenté par Serge Patrick MINANG, Président-Fondateur<br/>Libreville, août 2026", S["coverNote"]),
           PageBreak()]

    # ---- 2. UPL EN 30 SECONDES
    st = slide(st, "Qui sommes-nous", "L'UPL en 30 secondes", [
        Paragraph("Établissement d'enseignement supérieur privé fondé en 2022 à Libreville par "
                  "M. Serge Patrick MINANG (ingénieur, MBA, doctorant DBA, fonctionnaire du Ministère "
                  "des Travaux Publics), l'Université Privée de Libreville forme les cadres et "
                  "dirigeants du Gabon. Établissement familial, autofinancé, sans dette bancaire, "
                  "à l'abri des pressions commerciales.", S["lead"]),
        Spacer(1, 12),
        stat_row([("2022", "année de fondation"),
                  ("80", "cadres et dirigeants formés (Executive MBA)"),
                  ("6", "filières ouvertes à la rentrée 2026"),
                  ("504 m2", "bâtiment pédagogique R+2 en réalisation")]),
        Spacer(1, 12),
        Paragraph("Notre conviction : l'Afrique centrale francophone mérite des parcours de niveau "
                  "international, accessibles sur place, construits avec de grandes institutions "
                  "exigeantes.", S["lead"])])

    # ---- 3. OFFRE ACADEMIQUE
    st = slide(st, "L'offre", "Une offre académique complète à la rentrée 2026", [
        styled_table([
            [P("Programme", "cellb"), P("Contenu", "cellb"), P("Public", "cellb")],
            [P("Executive MBA (socle historique)", "cellb"), P("Soirées 17 h - 21 h, partenariat Université de Douala, jusqu'à 8 échéances", "cell"), P("Cadres et dirigeants", "cell")],
            [P("Gouvernance, Leadership et Management", "cell"), P("Licence, Master, MBA, DBA", "cell"), P("Futurs cadres et executives", "cell")],
            [P("Économie Numérique et Intelligence Artificielle", "cell"), P("Data, numérique appliqué, transformation", "cell"), P("Étudiants et professionnels", "cell")],
            [P("Économie Bleue, Gestion Portuaire et Développement Durable", "cell"), P("Adossée au port en eau profonde de Libreville-Owendo", "cell"), P("Métiers maritimes et logistiques", "cell")],
            [P("Droit et Sciences Politiques", "cell"), P("Droit des affaires, action publique", "cell"), P("Juristes, cadres publics", "cell")],
            [P("École d'Assurance Maladie et de Sécurité Sociale", "cell"), P("Couverture maladie universelle, protection sociale", "cell"), P("Métiers de la santé et de la protection sociale", "cell")],
            [P("Classes Préparatoires aux Grandes Écoles (CPGE)", "cell"), P("Préparation intensive aux concours", "cell"), P("Bacheliers excellents", "cell")],
        ], [7.3*cm, 11.2*cm, 6.1*cm])])

    # ---- 4. POURQUOI LE GABON
    st = slide(st, "Le marché", "Pourquoi le Gabon, pourquoi maintenant", [
        styled_table([
            [P("Un marché francophone sous-couvert", "cardt"),
             P("Aucune grande école internationale n'est implantée à Libreville. L'Afrique centrale francophone est le dernier grand espace francophone sans plateforme académique de référence.", "cardb")],
            [P("Une zone CEMAC de 50 millions d'habitants", "cardt"),
             P("Cameroun, Congo, Guinée équatoriale, Tchad, Centrafrique : Libreville est un hub régional naturel (aéroport international, port en eau profonde, francophonie, monnaie FCFA).", "cardb")],
            [P("Un pays urbain et solvable", "cardt"),
             P("Plus de 90 % de population urbaine, un pouvoir d'achat parmi les plus élevés d'Afrique centrale, une demande forte des familles pour des diplômes internationaux.", "cardb")],
            [P("Des besoins massifs en compétences", "cardt"),
             P("Transformation numérique, économie bleue, financement du développement, couverture maladie universelle, gouvernance publique : les chantiers du pays appellent des formations de haut niveau.", "cardb")],
        ], [8.6*cm, 16.0*cm], header=False, zebra=False,
            extra=[("BACKGROUND", (0, 0), (0, -1), BLUE_LT),
                   ("VALIGN", (0, 0), (-1, -1), "TOP"),
                   ("TOPPADDING", (0, 0), (-1, -1), 6),
                   ("BOTTOMPADDING", (0, 0), (-1, -1), 6)]),
        Spacer(1, 8),
        Paragraph("Le premier partenaire qui s'installe à Libreville prend position sur tout un "
                  "espace régional - avant les autres.", S["lead"])])

    # ---- 5. CAMPUS
    st = slide(st, "Les moyens", "Un campus qui se construit maintenant", [
        styled_table([
            [P("Étape", "cellb"), P("Contenu", "cellb"), P("Calendrier", "cellb")],
            [P("Bâtiment pédagogique R+2", "cellb"), P("504 m2, 9 salles climatisées et meublées, salle informatique, réseaux numériques, vidéosurveillance - devis négocié de 219,97 M FCFA", "cell"), P("Livraison rapide - rentrée 2026", "cell")],
            [P("Montée en charge", "cell"), P("Équipements informatiques et audiovisuels, équipe commerciale renforcée, campagne de recrutement régionale", "cell"), P("2026 - 2027", "cell")],
            [P("Master Plan Campus", "cellb"), P("Campus dédié de 2 hectares : 2 bâtiments d'enseignement, amphithéâtre 300 places, bibliothèque, Centre IA, laboratoires, résidence étudiante - enveloppe indicative 3,5 milliards FCFA, financement multi-acteurs", "cell"), P("Horizon 2028 - 2035", "cell")],
        ], [5.6*cm, 14.5*cm, 4.5*cm]),
        Spacer(1, 6),
        stat_row([("9 salles", "dès la rentrée 2026"),
                  ("2 ha", "assiette du futur campus"),
                  ("3,5 Mds FCFA", "programme immobilier long terme"),
                  ("400 ét./jour", "capacité cible en rotations")])])

    # ---- 6. CREDIBILITE
    st = slide(st, "La preuve", "Une institution crédible, pas un projet sur le papier", [
        styled_table([
            [P("Un partenariat international qui fonctionne depuis 2022", "cardt"),
             P("Executive MBA conduit avec l'Université de Douala (Cameroun) : ingénierie pédagogique, reconnaissance des crédits universitaires, enseignants croisés. Nous savons faire vivre une convention académique.", "cardb")],
            [P("80 cadres formés, autofinancement, zéro dette", "cardt"),
             P("Quatre années d'exploitation positive, sans subvention ni endettement : la croissance est financée par l'activité. Un programme d'investissement de 260 M FCFA est engagé pour 2026-2027.", "cardb")],
            [P("Un dirigeant connu et stabilisé", "cardt"),
             P("Serge Patrick MINANG, ingénieur, MBA, doctorant DBA, fonctionnaire du Ministère des Travaux Publics : ancrage institutionnel, réseau administratif et économique, réputation personnelle engagée.", "cardb")],
            [P("Des autorisations en bonne voie", "cardt"),
             P("Autorisations ministérielles d'ouverture disponibles ou en cours de finalisation, filière par filière, conformément à la réglementation gabonaise de l'enseignement supérieur privé.", "cardb")],
        ], [8.6*cm, 16.0*cm], header=False, zebra=False,
            extra=[("BACKGROUND", (0, 0), (0, -1), BLUE_LT),
                   ("VALIGN", (0, 0), (-1, -1), "TOP"),
                   ("TOPPADDING", (0, 0), (-1, -1), 6),
                   ("BOTTOMPADDING", (0, 0), (-1, -1), 6)]),
        Spacer(1, 8),
        Paragraph("Nous ne demandons pas un accord diplômant immédiat : nous proposons de "
                  "construire la preuve, étape par étape.", S["lead"])])

    # ---- 7. TROIS FORMATS
    st = slide(st, "La proposition", "Trois formats de coopération, un premier pas", [
        Table([[
            [Paragraph("A", ParagraphStyle("fa", fontName="Helvetica-Bold", fontSize=22, textColor=colors.white, alignment=TA_CENTER)),
             Paragraph("Implantation progressive", S["cardt"]),
             Paragraph("Un programme ou une implantation académique construits pas à pas à Libreville : module conjoint, puis programme labellisé, puis campus délocalisé, selon les exigences d'accréditation de votre institution.", S["cardb"])],
            [Paragraph("B", ParagraphStyle("fb", fontName="Helvetica-Bold", fontSize=22, textColor=colors.white, alignment=TA_CENTER)),
             Paragraph("Cycle UPL de trois ans", S["cardt"]),
             Paragraph("Un parcours UPL construit selon des standards définis conjointement, préparant à une candidature sélective vers vos cursus de niveau Master.", S["cardb"])],
            [Paragraph("C", ParagraphStyle("fc", fontName="Helvetica-Bold", fontSize=22, textColor=colors.white, alignment=TA_CENTER)),
             Paragraph("Voie d'accès dédiée", S["cardt"]),
             Paragraph("Une candidature spécifique pour les meilleurs diplômés UPL - sans admission automatique - avec cours hybrides et évaluations académiques conformes à vos critères.", S["cardb"])]],
        ], colWidths=[(PAGE[0]-3.4*cm)/3.0]*3),
        Spacer(1, 8),
        Paragraph("Le premier jalon peut rester modeste : cohorte pilote, école d'été, module "
                  "conjoint ou mission d'étude sur les besoins de compétences en Afrique centrale.",
                  S["lead"])])

    # ---- 8. CE QUE LE PARTENAIRE Y GAGNE
    st = slide(st, "L'équilibre", "Un partenariat gagnant-gagnant", [
        styled_table([
            [P("Ce que l'UPL apporte", "cellb"), P("Ce que votre établissement y gagne", "cellb")],
            [P("Ancrage local : équipe, campus, relations avec administrations et entreprises gabonaises", "cell"),
             P("Une porte d'entrée immédiate sur le Gabon et la zone CEMAC, sans investissement ni risque fixe", "cell")],
            [P("Expérience éprouvée du partenariat académique (convention Douala depuis 2022)", "cell"),
             P("Un partenaire qui connaît les exigences d'accréditation, de sélection et de qualité, et les accepte", "cell")],
            [P("Capacité de recrutement régional d'étudiants et professionnels qualifiés", "cell"),
             P("Un vivier de candidats pré-sélectionnés pour vos programmes sélectifs (Master, spécialisations)", "cell")],
            [P("Organisation complète sur place : accueil, logistique, encadrement, visibilité", "cell"),
             P("Un terrain pour vos étudiants : stages, études de terrain, missions encadrées, projets entrepreneuriaux au Gabon", "cell")],
            [P("Communication conjointe et image pionnière en Afrique centrale", "cell"),
             P("Un positionnement de pionnier face aux écoles internationales - avant la concurrence", "cell")],
        ], [11.1*cm, 13.5*cm])])

    # ---- 9. JALONS
    st = slide(st, "Le chemin", "Des premiers jalons réalistes", [
        styled_table([
            [P("Jalon", "cellb"), P("Description", "cellb"), P("Horizon", "cellb")],
            [P("Premier échange", "cellb"), P("Réunion confidentielle de 20 minutes par Microsoft Teams (ou en personne en France à partir du 9 septembre)", "cell"), P("Sous 15 jours", "cell")],
            [P("Accord cadre de principe", "cell"), P("Lettre d'intention fixant le périmètre, la confidentialité et les prochaines étapes - sans engagement diplômant", "cell"), P("Automne 2026", "cell")],
            [P("Mission d'étude ou module conjoint", "cell"), P("Étude des besoins de compétences en Afrique centrale ou module court (finance durable, entrepreneuriat, numérique, santé publique)", "cell"), P("Rentrée 2027", "cell")],
            [P("Cohorte pilote / école d'été", "cellb"), P("Première expérience d'enseignement conjoint à Libreville, mesurée et documentée", "cell"), P("Été 2027", "cell")],
            [P("Accueil de vos étudiants", "cell"), P("Stages, études de terrain, missions encadrées et projets entrepreneuriaux au Gabon", "cell"), P("Dès l'accord cadre", "cell")],
        ], [5.4*cm, 14.6*cm, 4.6*cm])])

    # ---- 10. CTA
    st += [Spacer(1, 1.0*cm),
           Paragraph("Prochain pas", S["kicker"]),
           Paragraph("Un échange de 20 minutes cette semaine ?", ParagraphStyle(
               "h1c", parent=S["h1"], fontSize=24, alignment=TA_CENTER, textColor=BLUE)),
           Spacer(1, 14),
           Table([[P("Réunion Microsoft Teams de 20 minutes avec M. le Président Serge Patrick MINANG<br/>"
                     "ou rencontre en personne : <b>France, à partir du 9 septembre</b>", "lead")]],
                 colWidths=[PAGE[0]-3.4*cm],
                 style=TableStyle([("BOX", (0, 0), (-1, -1), 1.0, GOLD),
                                   ("BACKGROUND", (0, 0), (-1, -1), GOLD_LT),
                                   ("TOPPADDING", (0, 0), (-1, -1), 12),
                                   ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
                                   ("LEFTPADDING", (0, 0), (-1, -1), 14),
                                   ("RIGHTPADDING", (0, 0), (-1, -1), 14)])),
           Spacer(1, 16),
           Table([[P("<b>Serge Patrick MINANG</b><br/>Président-Fondateur<br/>"
                     "+241 062 62 19 78 / +241 077 35 95 72<br/>contact@upl-gabon.com", "bodyc"),
                   P("<b>Université Privée de Libreville</b><br/>Sablière, face Résidence de "
                     "l'Ambassade d'Arabie Saoudite<br/>Libreville - Gabon<br/>www.upl-gabon.com", "bodyc"),
                   P("<b>Excellence · Innovation · Leadership</b><br/>Executive MBA avec l'Université "
                     "de Douala<br/>6 filières - rentrée 2026<br/>Campus en expansion", "bodyc")]],
                 colWidths=[(PAGE[0]-3.4*cm)/3.0]*3,
                 style=TableStyle([("BACKGROUND", (0, 0), (-1, -1), BLUE_LT),
                                   ("BOX", (0, 0), (-1, -1), 0.8, GOLD),
                                   ("INNERGRID", (0, 0), (-1, -1), 0.4, GOLD),
                                   ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                                   ("TOPPADDING", (0, 0), (-1, -1), 10),
                                   ("BOTTOMPADDING", (0, 0), (-1, -1), 10)]))]

    doc = Deck(OUT)
    doc.build(st)
    return doc

if __name__ == "__main__":
    d = build()
    print("OK", OUT, "-", d.page, "pages -", f"{os.path.getsize(OUT)/1024:.0f} Ko")
