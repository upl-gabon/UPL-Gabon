#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Deux documents UPL — édition du 31 août 2026 (remise ce matin) :
  1. UPL_BANQUE_Dossier_Ecobank_260M.pdf  — dossier complet banque, style analyste, or soyeux
  2. UPL_INTERNE_Vision_500_Direction.pdf — plan de conquête interne, ambition 500 étudiants
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle, PageBreak, KeepTogether, Image)
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.lib.utils import ImageReader

from generer_livrables import LOGO

HERE = os.path.dirname(os.path.abspath(__file__))
OUT1 = os.path.join(HERE, "UPL_BANQUE_Dossier_Ecobank_260M.pdf")
OUT2 = os.path.join(HERE, "UPL_INTERNE_Vision_500_Direction.pdf")

# ------------------------------------------------ charte (or soyeux + bleu nuit)
NAVY = colors.HexColor("#0B2A5B")
NAVY_DK = colors.HexColor("#081E42")
GOLD = colors.HexColor("#C9A227")
GOLD_DK = colors.HexColor("#A8871F")
GOLD_SILK = colors.HexColor("#F7F0DC")     # soie dorée claire
GOLD_PALE = colors.HexColor("#FCF8EE")
GREY = colors.HexColor("#33383F")
LINE = colors.HexColor("#D8C58A")
ZEBRA = colors.HexColor("#FBF7EC")

W = A4[0] - 4*cm            # largeur utile (marges 2 cm) — tableaux pleine largeur, bien centrés

# ------------------------------------------------ styles
ST = {}
ST["titre"] = ParagraphStyle("titre", fontName="Helvetica-Bold", fontSize=17, leading=22,
                             textColor=NAVY, alignment=TA_CENTER)
ST["soustitre"] = ParagraphStyle("soustitre", fontName="Helvetica", fontSize=11.5, leading=15,
                                 textColor=GOLD_DK, alignment=TA_CENTER)
ST["corps"] = ParagraphStyle("corps", fontName="Helvetica", fontSize=9.6, leading=14,
                             alignment=TA_JUSTIFY, textColor=GREY, spaceAfter=6)
ST["corpsc"] = ParagraphStyle("corpsc", parent=ST["corps"], alignment=TA_CENTER)
ST["h1"] = ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=12.5, leading=16,
                          textColor=NAVY, alignment=TA_CENTER, spaceBefore=4, spaceAfter=2)
ST["h2"] = ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=10.5, leading=13.5,
                          textColor=NAVY_DK)
ST["cell"] = ParagraphStyle("cell", fontName="Helvetica", fontSize=8.8, leading=11.4, textColor=GREY)
ST["cellb"] = ParagraphStyle("cellb", parent=ST["cell"], fontName="Helvetica-Bold", textColor=NAVY_DK)
ST["c"] = ParagraphStyle("c", parent=ST["cell"], alignment=TA_CENTER)
ST["cb"] = ParagraphStyle("cb", parent=ST["c"], fontName="Helvetica-Bold", textColor=NAVY_DK)
ST["head"] = ParagraphStyle("head", fontName="Helvetica-Bold", fontSize=8.8, leading=11.4,
                            textColor=NAVY_DK, alignment=TA_CENTER)
ST["sign"] = ParagraphStyle("sign", fontName="Helvetica", fontSize=9.6, leading=13.5,
                            textColor=GREY, alignment=TA_CENTER)
ST["corpsl"] = ParagraphStyle("corpsl", parent=ST["corps"], alignment=TA_LEFT)
ST["corpsr"] = ParagraphStyle("corpsr", parent=ST["corps"], alignment=TA_RIGHT)
ST["note"] = ParagraphStyle("note", fontName="Helvetica-Oblique", fontSize=8.6, leading=11.5,
                            textColor=colors.HexColor("#6E6455"), alignment=TA_CENTER)
ST["toch0"] = ParagraphStyle("toch0", parent=ST["h1"])
ST["toch1"] = ParagraphStyle("toch1", parent=ST["h1"])
ST["toc0"] = ParagraphStyle("toc0", fontName="Helvetica-Bold", fontSize=10.5, leading=20,
                            textColor=NAVY)
ST["toc1"] = ParagraphStyle("toc1", fontName="Helvetica", fontSize=9.6, leading=17,
                            textColor=GREY, leftIndent=16)

def P(t, s="corps"): return Paragraph(t, ST[s])

def gold_rule(width=W, thick=1.2):
    t = Table([[""]], colWidths=[width], rowHeights=[thick])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), GOLD),
                           ("TOPPADDING", (0, 0), (-1, -1), 0),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 0)]))
    t._is_rule = True
    return t

def titre_doc(txt):
    p = P(txt.upper(), "toch0"); p._toctxt = txt
    return [p, gold_rule(9*cm, 1.0), Spacer(1, 10)]

def ht1(txt, rule=4.6*cm):
    p = P(txt, "toch1"); p._toctxt = txt
    return [p, gold_rule(rule, 0.8), Spacer(1, 6)]

def anti_coupure(story):
    """Un titre n'est jamais orphelin en bas de page ; un tableau n'est jamais coupé."""
    out = []
    for f in story:
        if isinstance(f, Table) and getattr(f, "_is_data", False) and out:
            grp, pris = [f], 0
            while out and pris < 4:
                q = out[-1]
                if isinstance(q, PageBreak) or (isinstance(q, Table) and getattr(q, "_is_data", False)):
                    break
                if isinstance(q, (Paragraph, Spacer)) or (isinstance(q, Table) and getattr(q, "_is_rule", False)):
                    grp.insert(0, out.pop()); pris += 1
                else:
                    break
            out.append(KeepTogether(grp))
        else:
            out.append(f)
    return out

def sec(txt):
    return [Spacer(1, 6), P(txt, "h1"), gold_rule(7*cm, 0.9), Spacer(1, 8)]

def sec2(txt):
    return [Spacer(1, 5), P(txt, "h2"), Spacer(1, 3)]

def T(data, aligns=None, header=True, total_rows=0, zebra=True, fs=8.8):
    """Tableau pleine largeur, centré. aligns: liste 'l'/'c' par colonne."""
    n = len(data[0])
    aligns = aligns or ["l"] * n
    rows = []
    for i, r in enumerate(data):
        row = []
        for j, cell in enumerate(r):
            if i == 0 and header:
                row.append(Paragraph(str(cell), ST["head"]))
            elif aligns[j] == "c":
                row.append(Paragraph(str(cell), ST["cb" if i >= len(data) - total_rows else "c"]))
            else:
                row.append(Paragraph(str(cell), ST["cellb" if i >= len(data) - total_rows else "cell"]))
        rows.append(row)
    t = Table(rows, colWidths=[W/n]*n, hAlign="CENTER", repeatRows=1 if header else 0)
    cmds = [("GRID", (0, 0), (-1, -1), 0.5, LINE),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("LEFTPADDING", (0, 0), (-1, -1), 5), ("RIGHTPADDING", (0, 0), (-1, -1), 5),
            ("TOPPADDING", (0, 0), (-1, -1), 3.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5)]
    if header:
        cmds += [("BACKGROUND", (0, 0), (-1, 0), GOLD_SILK),
                 ("LINEBELOW", (0, 0), (-1, 0), 0.9, GOLD_DK)]
    if zebra:
        for i in range(1 if header else 0, len(rows)):
            if (i - (1 if header else 0)) % 2 == 1:
                cmds.append(("BACKGROUND", (0, i), (-1, i), GOLD_PALE))
    for k in range(1, total_rows + 1):
        cmds += [("BACKGROUND", (0, len(rows) - k), (-1, len(rows) - k), GOLD_SILK),
                 ("LINEABOVE", (0, len(rows) - k), (-1, len(rows) - k), 0.9, GOLD_DK)]
    t.setStyle(TableStyle(cmds))
    t._is_data = True
    return t

# ------------------------------------------------ gabarits
class DocS(BaseDocTemplate):
    """Dossier banque — blanc, filets or, sobre."""
    def __init__(self, path, bandeau, **kw):
        super().__init__(path, pagesize=A4, leftMargin=2*cm, rightMargin=2*cm,
                         topMargin=2.5*cm, bottomMargin=2.1*cm, **kw)
        self.bandeau = bandeau
        fr = Frame(self.leftMargin, self.bottomMargin, self.width, self.height, id="m")
        self.addPageTemplates([PageTemplate(id="p", frames=[fr], onPage=self._pg)])

    def _pg(self, c, doc):
        w, h = A4
        c.saveState()
        # en-tête : filet or double + titre courant
        c.setStrokeColor(GOLD); c.setLineWidth(1.1)
        c.line(2*cm, h-1.55*cm, w-2*cm, h-1.55*cm)
        c.setStrokeColor(GOLD_DK); c.setLineWidth(0.5)
        c.line(2*cm, h-1.42*cm, w-2*cm, h-1.42*cm)
        c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 8.2)
        c.drawCentredString(w/2, h-1.28*cm, self.bandeau)
        if os.path.exists(LOGO):
            c.drawImage(LOGO, 2*cm, h-2.32*cm, width=1.28*cm, height=0.81*cm,
                        mask="auto", preserveAspectRatio=True)
        # pied
        c.setStrokeColor(GOLD); c.setLineWidth(0.8)
        c.line(2*cm, 1.55*cm, w-2*cm, 1.55*cm)
        c.setFillColor(colors.HexColor("#7A7264")); c.setFont("Helvetica", 7.6)
        c.drawCentredString(w/2, 1.15*cm, f"— {doc.page} —")
        c.restoreState()

    def afterFlowable(self, f):
        if isinstance(f, Paragraph) and f.style.name in ("toch0", "toch1"):
            txt = getattr(f, "_toctxt", f.getPlainText())
            if txt == "Sommaire":
                return
            lvl = 0 if f.style.name == "toch0" else 1
            self.notify("TOCEntry", (lvl, txt, self.page))

def fmt(n): return f"{int(round(n)):,}".replace(",", " ")

# ================================================================
#  DONNÉES HARMONISÉES (devis révisé + crédit 260 M)
# ================================================================
TRAV, FG = 177_540_000, 8_877_000
HT, TVA, TTC = 186_417_000, 33_555_060, 219_972_060
MENS, TOT_INT, TOT_PAY = 3_660_458, 161_300_000, 421_300_000
EMPLOI = [("Construction du bâtiment pédagogique R+2 — 504 m2 (devis négocié, TTC)", TTC),
          ("Équipements informatiques et audiovisuels", 10_000_000),
          ("Communication et recrutement étudiants — campagne 12 mois", 15_000_000),
          ("Renforcement de l'équipe (appui administratif et 2 commerciaux)", 5_000_000),
          ("Fonds de roulement", 10_000_000),
          ("Frais bancaires et aléas de démarrage", 27_940)]
assert sum(m for _, m in EMPLOI) == 260_000_000
LOTS = [("Études, installation de chantier", 3_000_000),
        ("Fondations et infrastructures", 12_470_000),
        ("Structure métallique (métré optimisé)", 53_835_000),
        ("Planchers et galeries de circulation", 14_672_000),
        ("Escaliers métalliques", 7_200_000),
        ("Façades et vitrerie", 19_130_000),
        ("Cloisons et portes intérieures", 6_450_000),
        ("Faux plafonds et isolation", 7_308_000),
        ("Toiture et acrotère", 3_970_000),
        ("Évacuation des eaux pluviales", 1_800_000),
        ("Revêtements de sol", 5_040_000),
        ("Électricité — courants forts", 7_305_000),
        ("Courants faibles et réseaux numériques", 5_000_000),
        ("Climatisation — 9 salles", 6_120_000),
        ("Plomberie et sanitaires", 4_500_000),
        ("Sécurité incendie", 2_000_000),
        ("Peinture et finitions", 3_200_000),
        ("Garde-corps", 2_240_000),
        ("Aménagements extérieurs", 2_800_000),
        ("Essais, nettoyage, réception (DOE)", 1_000_000),
        ("Mobilier pédagogique des 9 salles", 8_500_000)]
assert sum(m for _, m in LOTS) == TRAV

# ================================================================
#  DOCUMENT 1 — BANQUE
# ================================================================
def doc_banque():
    st = []
    # ---------- Page de couverture
    def _logo(w=3.6*cm):
        if os.path.exists(LOGO):
            iw, ih = ImageReader(LOGO).getSize()
            return Image(LOGO, width=w, height=w*ih/iw)
        return Spacer(1, w)
    st += [Spacer(1, 1.0*cm), _logo(), Spacer(1, 0.7*cm)]
    st += [P("UNIVERSITÉ PRIVÉE DE LIBREVILLE", "titre"), gold_rule(10*cm, 1.4),
           Spacer(1, 14),
           P("DOSSIER DE DEMANDE DE FINANCEMENT", "titre"),
           P("Crédit d'investissement — deux cent soixante millions (260 000 000) FCFA", "soustitre"),
           Spacer(1, 26)]
    st += [T([["Établissement", "Université Privée de Libreville (UPL) — SAS"],
              ["Président-Fondateur", "M. Serge Patrick MINANG"],
              ["Banque sollicitée", "ECOBANK GABON"],
              ["Objet", "Construction du bâtiment pédagogique R+2, équipements et lancement des six filières"],
              ["Montant sollicité", "260 000 000 FCFA"],
              ["Durée", "120 mois, dont 12 mois de différé sur le capital"],
              ["Siège", "Sablière, face Résidence de l'Ambassade d'Arabie Saoudite — Libreville"],
              ["Contact", "062 62 19 78 / 077 35 95 72 — contact@upl-gabon.com"],
              ["Date du dossier", "Libreville, le 31 août 2026"]],
            aligns=["c", "l"], header=False, zebra=True)]
    st += [Spacer(1, 24), P("Conducteur d'échange établi conformément à la trame ECOBANK", "note"),
           Spacer(1, 8), P("DOCUMENT RÉSERVÉ À L'USAGE BANCAIRE", "note"), PageBreak()]

    # ---------- Sommaire
    toc = TableOfContents()
    toc.levelStyles = [ST["toc0"], ST["toc1"]]
    toc.dotsMinLevel = 0
    st += titre_doc("Sommaire") + [Spacer(1, 10), toc, PageBreak()]

    # ---------- Lettre
    st += titre_doc("Lettre de demande de financement")
    st += [P("Libreville, le 31 août 2026", "corpsr"), Spacer(1, 8),
           P("À Monsieur le Directeur des Engagements Entreprises<br/>ECOBANK GABON<br/>Libreville", "corpsl"), Spacer(1, 8),
           P("<b>Objet : Demande de crédit d'investissement — 260 000 000 FCFA</b>", "corpsl"), Spacer(1, 8),
           P("<b>Monsieur le Directeur,</b>", "corpsl"),
           P("Depuis quatre années, l'Université Privée de Libreville forme les cadres et dirigeants "
             "gabonais : près de quatre-vingts auditeurs ont suivi son programme Executive MBA, conduit "
             "avec l'ESSEC de Douala — École Supérieure des Sciences Économiques et Commerciales, dixième business school d'Afrique francophone. L'établissement est autofinancé, ne porte aucune dette "
             "bancaire et dégage un résultat d'exploitation positif depuis l'origine."),
           P("Six filières structurantes ouvrent à la rentrée 2026-2027. Les locaux actuels ne "
             "permettant pas d'accueillir cette montée en charge, un devis ferme et négocié de "
             "219 972 060 FCFA TTC couvre la construction d'un bâtiment pédagogique R+2 de 504 m2 — "
             "neuf salles climatisées et meublées — dont la livraison est attendue sous deux mois, la "
             "première tranche étant réceptionnée à six semaines pour accueillir les cours dès "
             "septembre."),
           P("En conséquence, j'ai l'honneur de solliciter de votre établissement un crédit "
             "d'investissement de <b>deux cent soixante millions (260 000 000) FCFA</b>, sur "
             "120 mois dont 12 mois de différé sur le capital. Les fonds couvrent la construction, "
             "les équipements, la campagne de recrutement, le renforcement de l'équipe et le fonds de "
             "roulement, conformément au plan d'emploi détaillé au présent dossier."),
           P("Le présent dossier reprend, en la complétant, la trame du conducteur d'échange établi par "
             "votre établissement ; les annexes financières, juridiques et le plan d'investissement "
             "l'accompagnent. Le plan de remboursement, établi sur des hypothèses mesurées, fait "
             "ressortir un ratio de couverture du service de la dette constamment supérieur au seuil "
             "de 1,3 x."),
           P("Je reste à la disposition de la banque pour tout complément d'analyse, visite de site ou "
             "entretien, et vous prie d'agréer, Monsieur le Directeur, l'expression de ma "
             "considération distinguée."),
           Spacer(1, 16),
           P("<b>Serge Patrick MINANG</b>", "sign"),
           P("Président-Fondateur — Université Privée de Libreville", "sign"), PageBreak()]

    # ---------- Conducteur
    st += titre_doc("Conducteur d'échange — ECOBANK S.A")
    st += [P("Trame ECOBANK complétée par l'UPL — Libreville, 31 août 2026", "note"), Spacer(1, 6)]

    st += ht1("Identité et actionnariat", 4.6*cm)
    st += sec2("• Nom de la structure :")
    st += [P("Université Privée de Libreville (UPL)")]
    st += sec2("• Forme juridique de la société :")
    st += [P("SAS — Société par Actions Simplifiée (enseignement supérieur privé)")]
    st += sec2("• Montant du capital :")
    st += [P("20 000 000 FCFA (vingt millions de francs CFA), entièrement libéré.")]
    st += sec2("• Principaux actionnaires et part du capital :")
    st += [T([["Actionnaire", "Qualité", "Part"],
              ["Serge Patrick MINANG", "Président-Fondateur", "60 %"],
              ["Blandine ENGONGA", "Épouse du fondateur", "15 %"],
              ["Stan MINANG", "Enfant du fondateur", "5 %"],
              ["Vianney Aldrin MINANG", "Enfant du fondateur", "5 %"],
              ["Calvin Blanchard MINANG", "Enfant du fondateur", "5 %"],
              ["Cléanne MINANG", "Enfant du fondateur", "5 %"],
              ["Diamant Eudalia MINANG", "Enfant du fondateur", "5 %"],
              ["TOTAL", "Capital détenu à 100 % par la famille du fondateur", "100 %"]],
            aligns=["l", "l", "c"], total_rows=1),
           P("En cas d'écart avec les statuts enregistrés, les statuts font foi.", "note")]

    st += [PageBreak()] + ht1("Management et organisation", 5.4*cm)
    st += [P("<b>Président-Fondateur :</b> Serge Patrick MINANG, depuis 2022. Ingénieur et MBA, docteur "
             "en administration des affaires (DBA) en instance de soutenance ; fonctionnaire du "
             "Ministère des Travaux Publics. Exerce la direction "
             "générale de l'UPL : pilotage institutionnel, pédagogique et commercial ; sélection des "
             "enseignants ; relation avec l'ESSEC de Douala. CV joint.", "corps"),
           P("<b>Directeur Commercial et Marketing :</b> fonction assurée par le Président-Fondateur "
             "depuis 2022 (réseaux, prescription, développement). Le renforcement de l'équipe — deux "
             "commerciaux recruteurs et un appui administratif — est prévu au plan de développement, "
             "sous son autorité. Profils à transmettre à l'embauche.", "corps"),
           P("<b>Direction financière :</b> fonction assurée par la direction générale, avec l'appui "
             "d'un ingénieur financier diplômé du Programme Grande École de SKEMA Business School et "
             "du MSc Corporate Financial Management. La direction s'attachera, en tant que de "
             "besoin, les services d'un expert-comptable de place.", "corps"),
           P("<b>Directeur Pédagogique :</b> Dr MENGUE Urielle. Assure, sous la direction du "
             "Président-Fondateur, la coordination pédagogique des programmes, le suivi des "
             "enseignants et le contrôle de la qualité académique, en lien avec la convention "
             "conclue avec l'ESSEC de Douala. CV disponible sur demande.", "corps")]

    st += [PageBreak()] + ht1("Activités du client", 4.3*cm)
    st += [P("<b>• Date d'entrée en activité :</b> 2022 (première promotion Executive MBA). "
             "Activité principale : enseignement supérieur privé — formation de cadres et dirigeants. "
             "Historique : 2022 lancement du MBA avec l'ESSEC de Douala ; 2022-2025 "
             "consolidation (une vingtaine d'auditeurs par an, près de 80 cadres formés), VAE et "
             "conseil ; 2026-2027 ouverture de six filières : Gouvernance et Management, Économie "
             "Numérique et Intelligence Artificielle, Économie Bleue, Droit, Assurance Maladie et "
             "Sécurité Sociale, Classes Préparatoires aux Grandes Écoles — aux côtés du MBA et du DBA."),
           P("<b>• Produits et services commercialisés</b> (part dans le chiffre d'affaires récurrent 2025) :"),
           T([["Produit", "Part"],
              ["Executive MBA (20 auditeurs × 4 000 000 FCFA)", "83,8 %"],
              ["Validation des Acquis de l'Expérience (VAE)", "7,9 %"],
              ["Accompagnement et conseil", "6,3 %"],
              ["Frais de dossier et d'inscription", "2,1 %"],
              ["TOTAL — CA récurrent 2025 : 95 500 000 FCFA", "100 %"]],
             aligns=["l", "c"], total_rows=1),
           P("Hors champ récurrent, l'UPL conduit des séminaires de formation pour le compte "
             "d'administrations et d'entreprises — notamment le Ministère des Mines et des "
             "Hydrocarbures — inscrits au titre des prestations exceptionnelles.", "note"),
           P("<b>• Effectif :</b> permanents : 2 (Président-Fondateur ; secrétariat — Mme Blandine "
             "ENGONGA) ; appui financier ponctuel d'un actionnaire non salarié ; "
             "enseignants vacataires par session ; auditeurs 2025 : une vingtaine en MBA actif."),
           P("<b>• Chiffre d'affaires et résultats sur les trois dernières années :</b>"),
           T([["En FCFA", "2023", "2024", "2025"],
              ["Chiffre d'affaires", "≈ 80 000 000", "≈ 80 000 000", "95 500 000"],
              ["Résultat net", "n.d.", "n.d.", "17 900 000"]],
             aligns=["l", "c", "c", "c"]),
           P("<b>• Commissaires aux comptes :</b> la désignation interviendra conformément aux seuils "
             "et usages en vigueur. L'UPL prendra attache, en tant que de besoin, avec un "
             "expert-comptable établi à Libreville."),
           P("<b>• Prévisions de l'entreprise :</b>"),
           T([["Indicateur", "2026", "2027", "2028", "2029", "2030"],
              ["Effectifs UPL", "80", "120", "170", "210", "230"],
              ["CA (M FCFA)", "119,5", "164,0", "206,9", "242,8", "252,8"],
              ["EBE (M FCFA)", "50,0", "79,0", "106,0", "127,0", "132,0"],
              ["CAF (M FCFA)", "33,5", "42,3", "62,1", "78,1", "83,2"],
              ["Service de la dette (M FCFA)", "6,5", "30,5", "43,9", "43,9", "43,9"],
              ["DSCR", "5,15 x", "1,39 x", "1,41 x", "1,78 x", "1,90 x"]],
             aligns=["l", "c", "c", "c", "c", "c"]),
           P("Crédit sollicité : 260 000 000 FCFA ; 120 mois ; différé de 12 mois sur le capital ; "
             "taux indicatif 10 %. Mensualité en différé : 2 166 667 FCFA (intérêts seuls) ; "
             "mensualité en régime : 3 660 458 FCFA.", "note")]

    st += [PageBreak()] + ht1("Relations bancaires", 3.6*cm)
    st += [P("<b>• Banques en relation avec le client :</b>"),
           T([["Banque", "Nature de la relation", "Engagement de crédit"],
              ["UGB", "Compte de fonctionnement principal de l'UPL", "Aucun crédit en cours"],
              ["ECOBANK GABON", "Banque sollicitée pour le présent dossier", "Demande en instruction — 260 M FCFA"]],
             aligns=["l", "l", "l"]),
           P("<b>• Engagements en cours :</b> néant. L'UPL ne porte aucune dette bancaire ; le présent "
             "crédit constituerait sa première relation de crédit institutionnelle."),
           P("<b>• Besoins bancaires actuels justifiés :</b> crédit d'investissement de "
             "260 000 000 FCFA au titre du plan de développement 2026-2027 :"),
           T([["Poste", "Montant (FCFA)"]] + [[l, fmt(m)] for l, m in EMPLOI] +
             [["TOTAL", fmt(260_000_000)]], aligns=["l", "c"], total_rows=1),
           P("Devis de la construction : négocié et joint (219 972 060 FCFA TTC) ; équipements "
             "engagés selon le calendrier du projet.", "note"),
           P("<b>• Principaux actifs de la société :</b>"),
           T([["Type d'actif", "Valeur", "Localisation", "Âge", "Nanti"],
              ["Aménagements et équipements pédagogiques", "≈ 12 à 15 M FCFA (brut 2025)", "Sablière, Libreville", "2022-2025", "Non"],
              ["Créances étudiants (MBA)", "≈ 8 M FCFA (≈ 10 % du CA MBA)", "Libreville", "Courant", "Non"],
              ["Trésorerie", "≈ 5 M FCFA (bilan 2025)", "Compte UGB", "—", "Non"],
              ["Convention ESSEC de Douala", "Actif immatériel non valorisé", "—", "Depuis 2022", "Non"],
              ["Bâtiment R+2 (en cours de réalisation)", "219 972 060 FCFA TTC — devis ferme", "Sablière, Libreville", "Neuf", "À constituer"]],
             aligns=["l", "l", "l", "c", "c"])]

    st += [PageBreak()] + ht1("Clients et marché", 3.4*cm)
    st += [P("<b>• Principaux clients</b> (auditeurs et étudiants) :"),
           T([["Famille de clients", "Part dans les ventes"],
              ["Cadres et dirigeants du secteur public — MBA", "≈ 50 à 60 %"],
              ["Cadres et dirigeants du secteur privé — MBA / executive", "≈ 25 à 35 %"],
              ["Particuliers et professionnels (VAE, conseil)", "≈ 10 à 15 %"],
              ["Ministère des Mines et des Hydrocarbures — séminaires de formation sur mesure", "en développement"],
              ["Ministère de la Fonction Publique — agents publics en formation", "en développement"],
              ["ANBG — boursiers nationaux (l'État accompagne la scolarisation par les bourses)", "en développement"],
              ["Bacheliers — nouvelles filières (à compter de 2026)", "à construire"]],
             aligns=["l", "c"]),
           P("Sept familles de clients au total, dont trois relais de croissance publique : "
             "administrations, Fonction Publique et boursiers ANBG.", "note"),
           P("<b>• Délais moyens de paiement :</b> auditeurs MBA — virement, chèque ou espèces en "
             "FCFA, paiement à l'inscription puis par échéancier sur l'année académique ; VAE et "
             "conseil — 0 à 30 jours ; entreprises (formations sur mesure) — 30 à 60 jours sur "
             "facture ; administrations (séminaires sur mesure) — virement, 30 à 60 jours sur facture ; "
             "boursiers ANBG — paiement public sur notification de bourse. "
             "Les créances représentent environ 10 % du CA MBA ; un encaissement par "
             "mobile money et un prélèvement automatique sont mis en place à la rentrée."),
           P("<b>• Principaux fournisseurs et délais :</b> vacataires enseignants (pédagogie — part "
             "prépondérante des achats — virement, 0 à 15 jours, fin de session) ; bailleur "
             "immobilier (loyer de Sablière — mensuel) ; prestataires de communication (sur devis) ; "
             "fournisseurs IT, mobilier et BTP au titre du présent investissement (paiement selon "
             "devis : 25 % à la commande, 50 % à mi-chantier, 25 % à la livraison)."),
           P("<b>• Situation de la concurrence et position sur le marché :</b> l'UPL est reconnue "
             "comme offrant le meilleur MBA de la place, appréciation portée autant par le marché "
             "que par les concurrents eux-mêmes. Le comparatif des scolarités conforte cette "
             "position :"),
           T([["Établissement", "Offre MBA", "Scolarité (FCFA)", "Observation"],
              ["UPL", "Executive MBA avec l'ESSEC de Douala", "4 000 000", "Meilleur rapport qualité-prix de la place"],
              ["BBS", "MBA dispensé en anglais", "5 000 000", "Formation en anglais, peu adaptée au marché local"],
              ["Université Internationale de Libreville (UIL)", "MBA", "9 000 000", "Tarif élevé"],
              ["Autres acteurs", "Universités Mundiapolis, de Nice, etc.", "—", "Présence limitée — formats à distance ou partenariats"]],
             aligns=["l", "l", "c", "l"]),
           P("Sur les autres segments — licences et masters, classes préparatoires, assurance — "
             "l'offre locale reste restreinte (université Omar Bongo, USTM, rares privés) ; "
             "aucune CPGE privée et peu de formations spécialisées en assurance maladie : l'UPL "
             "y fait son entrée à la rentrée 2026.", "note"),
           P("<b>• Points de vente :</b> Sablière, Libreville — site pédagogique loué ; chiffre "
             "d'affaires moyen mensuel 2025 : ≈ 8 000 000 FCFA. Le bâtiment R+2 construit sur ce "
             "même site porte la capacité à environ 400 étudiants par jour."),
           P("<b>• Points forts / points de vigilance :</b>"),
           T([["Points forts", "Points de vigilance"],
              ["Meilleur MBA de la place — près de 80 cadres formés depuis 2022", "Poursuite de la structuration de la fonction financière"],
              ["CA récurrent et EBE positifs en 2025", "Organisation concentrée sur le fondateur"],
              ["Aucune dette bancaire", "Créances étudiants ≈ 10 % du CA MBA"],
              ["Convention avec l'ESSEC de Douala", "Habilitation et autorisation des filières par l'Enseignement Supérieur en cours"],
              ["Crédit dimensionné : couverture du service de la dette ≥ 1,39 x", "Montée en charge des filières à confirmer par les inscriptions"]],
             aligns=["l", "l"])]
    st += [Spacer(1, 30),
           P("Fait à Libreville, le 31 août 2026", "corpsc"), Spacer(1, 22),
           Table([[P("<b>Serge Patrick MINANG</b><br/>Président-Fondateur<br/><br/><br/>Signature et cachet", "sign")]],
                 colWidths=[9*cm], hAlign="CENTER",
                 style=TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                                   ("TOPPADDING", (0, 0), (-1, -1), 8)])),
           Spacer(1, 12), P("ECOBANK GABON", "note"), PageBreak()]

    # ---------- Annexe financière
    st += titre_doc("Annexe financière")
    st += [P("<b>Hypothèses retenues — scénario :</b> effectifs MBA de 20 à 32 sur cinq ans ; "
             "grille tarifaire officielle 2026-2027 (Licence 1 000 000 à 1 200 000 ; Master 1 500 000 "
             "à 2 000 000 ; CPGE 2 200 000 ; MBA 4 000 000 ; DBA 4 500 000 FCFA) ; neuf salles "
             "disponibles dès la livraison du bâtiment ; impôt sur les sociétés à 30 % ; créances "
             "étudiantes ≈ 10 % du CA MBA ; traitements publics du fondateur et de son épouse "
             "(≈ 8 et 12 M FCFA par an), tous deux fonctionnaires, non intégrés au calcul du "
             "ratio de couverture."),
           P("<b>Compte de résultat prévisionnel</b> (millions de FCFA) :"),
           T([["Rubrique", "2025", "2026", "2027", "2028", "2029", "2030"],
              ["Chiffre d'affaires", "95,5", "119,5", "164,0", "206,9", "242,8", "252,8"],
              ["Charges d'exploitation", "-69,9", "-69,5", "-85,0", "-101,0", "-116,0", "-121,0"],
              ["Excédent brut d'exploitation", "25,6", "50,0", "79,0", "106,0", "127,0", "132,0"],
              ["Dotations aux amortissements", "0,0", "-10,0", "-17,5", "-17,5", "-17,5", "-17,5"],
              ["Charges financières", "0,0", "-2,7", "-15,8", "-10,1", "-4,9", "-1,4"],
              ["Résultat net", "17,9", "27,5", "35,0", "58,0", "76,0", "82,5"],
              ["Capacité d'autofinancement", "17,9", "33,5", "42,3", "62,1", "78,1", "83,2"]],
             aligns=["l"] + ["c"]*6, total_rows=1),
           P("<b>Plan d'amortissement du crédit</b> — 260 000 000 FCFA, 120 mois, différé de 12 mois, "
             "taux indicatif 10 % ; décaissement en octobre 2026 ; mensualité en régime de "
             "3 660 458 FCFA ; coût total du crédit ≈ 421,3 M FCFA dont ≈ 161,3 M FCFA d'intérêts :"),
           T([["Année", "Service annuel (FCFA)", "Dont intérêts", "Dont capital", "Capital restant dû"],
              ["2026 (3 mois)", "6 500 000", "6 500 000", "0", "260 000 000"],
              ["2027", "30 497 000", "25 925 000", "4 572 000", "255 428 000"],
              ["2028", "43 930 000", "23 530 000", "20 400 000", "235 028 000"],
              ["2029", "43 930 000", "21 320 000", "22 610 000", "212 418 000"],
              ["2030", "43 930 000", "19 030 000", "24 900 000", "187 518 000"],
              ["2031", "43 930 000", "16 560 000", "27 370 000", "160 148 000"],
              ["2032 à 2036", "160 523 000", "48 435 000", "160 148 000", "0"]],
             aligns=["c", "c", "c", "c", "c"], total_rows=1),
           P("<b>Ratio de couverture du service de la dette</b> (CAF / service annuel) : "
             "5,15 x en 2026 ; 1,39 x en 2027 ; 1,41 x en 2028 ; 1,78 x en 2029 ; 1,90 x en 2030 — "
             "constamment supérieur au seuil bancaire de référence de 1,3 x."),
           P("<b>Épreuve de solidité — exercice 2028</b> (année pleine d'amortissement) :"),
           T([["Indicateur (M FCFA)", "Base", "CA - 25 %", "CA - 40 %", "Choc RH + 30 %"],
              ["Chiffre d'affaires", "206,9", "155,2", "124,1", "206,9"],
              ["Excédent brut", "106,0", "70,8", "49,7", "94,0"],
              ["CAF", "62,1", "30,5", "13,6", "51,3"],
              ["Service de la dette", "43,9", "43,9", "43,9", "43,9"],
              ["DSCR", "1,41 x", "0,69 x", "0,31 x", "1,17 x"]],
             aligns=["l", "c", "c", "c", "c"]),
           P("Il ressort de l'analyse que l'épreuve dégradée est absorbée par la trésorerie "
             "constituée dès 2026 — fonds de roulement de 10 M FCFA et CAF cumulée 2026-2027 de "
             "75,8 M FCFA — ainsi que par les ressources personnelles du fondateur et de son épouse "
             "(≈ 8 et 12 M FCFA par an), non intégrées au calcul. Le scénario de crise conduirait "
             "à un aménagement d'échéancier avec la banque, "
             "que la structure du crédit — différé de douze mois — permet d'anticiper."),
           P("<b>Plan d'emploi des fonds</b> : tel que détaillé au conducteur d'échange — "
             "construction 219 972 060 FCFA TTC ; équipements 10 M ; communication 15 M ; équipe "
             "5 M ; fonds de roulement 10 M ; frais et aléas 27 940 FCFA — total "
             "260 000 000 FCFA, dont 88,5 % d'actifs physiques."), PageBreak()]

    # ---------- Annexe juridique
    st += titre_doc("Annexe juridique — bordereau des pièces")
    pieces = ["Statuts de l'UPL — original enregistré", "Extrait RCCM à jour",
              "Convention avec l'ESSEC de Douala",
              "Habilitation et autorisations des filières — Ministère de l'Enseignement Supérieur",
              "Grille tarifaire officielle 2026-2027", "Supports de communication et flyers",
              "Liste des auditeurs MBA et état des créances", "États financiers 2022-2025",
              "Relevés bancaires UGB — 12 à 24 mois",
              "Devis de construction négocié — 219 972 060 FCFA TTC",
              "Plan de communication 2026-2027", "Attestations fiscales et sociales",
              "CV du Président-Fondateur et de l'équipe", "Répartition du capital"]
    statuts = ["Disponible", "Disponible", "Disponible", "En cours", "Disponible",
               "Disponible", "Disponible", "Disponible", "Disponibles",
               "Joint au présent dossier", "Joint", "Sur demande",
               "Disponible", "Disponible"]
    st += [T([["N°", "Pièce", "Statut"]] +
             [[str(i+1), p, s] for i, (p, s) in enumerate(zip(pieces, statuts))],
             aligns=["c", "l", "c"]), PageBreak()]

    # ---------- Plan d'investissement
    st += titre_doc("Plan d'investissement 2026-2027")
    st += [P("<b>Construction du bâtiment pédagogique R+2</b> — Sablière, Libreville ; environ "
             "504 m2 sur trois niveaux ; neuf salles de cours climatisées et meublées ; blocs "
             "sanitaires par niveau ; salle informatique ; réseaux numériques et vidéosurveillance ; "
             "sécurité incendie ; aménagements extérieurs. Devis négocié après mise en "
             "concurrence, en repli de 46,3 % sur la première proposition :"),
           T([["Lot", "Montant HT (FCFA)"]] + [[l, fmt(m)] for l, m in LOTS] +
             [["Total des travaux", fmt(TRAV)],
              ["Frais généraux et aléas (5 %)", fmt(FG)],
              ["Montant total hors taxes", fmt(HT)],
              ["TVA 18 %", fmt(TVA)],
              ["MONTANT TOTAL TTC", fmt(TTC)]],
             aligns=["l", "c"], total_rows=5),
           P("<b>Conditions du marché</b> : délai d'exécution de deux mois au plus, réception "
             "partielle de la tranche A (rez-de-chaussée) à six semaines afin d'accueillir les cours "
             "dès la rentrée ; paiement de 25 % à la commande, 50 % à mi-chantier et 25 % à la "
             "livraison ; pénalités de retard de un millième par jour calendaire, plafonnées à 10 %."),
           P("<b>Calendrier</b> : septembre 2026 — rentrée dans les locaux actuels de Sablière et "
             "lancement de la campagne de recrutement ; septembre à novembre 2026 — travaux en "
             "cadence renforcée, réception partielle à six semaines, réception complète sous deux "
             "mois ; novembre 2026 à premier trimestre 2027 — équipement informatique et audiovisuel, "
             "transfert de l'ensemble des cours, montée en charge des six filières."),
           P("<b>Capacité</b> : le bâtiment porte la capacité d'accueil à environ 400 étudiants par "
             "jour, soit le premier palier de 300 étudiants et la trajectoire vers 500 étudiants "
             "portée par le Master Plan Campus (horizon 2028-2035, enveloppe indicative d'environ "
             "3,5 milliards FCFA, financement multi-acteurs, hors de la présente demande)."),
           Spacer(1, 22),
           P("Fait à Libreville, le 31 août 2026", "corpsc"),
           P("<b>Serge Patrick MINANG</b><br/>Président-Fondateur — Université Privée de Libreville", "sign")]
    d = DocS(OUT1, "UNIVERSITÉ PRIVÉE DE LIBREVILLE — DOSSIER BANCAIRE ECOBANK — 260 000 000 FCFA")
    d.multiBuild(anti_coupure(st))
    return d

# ================================================================
#  DOCUMENT 2 — INTERNE (ambition 500)
# ================================================================
def doc_interne():
    st = []
    st += [Spacer(1, 1.5*cm),
           P("DOCUMENT INTERNE — DIRECTION DE L'UPL", "soustitre"), gold_rule(6*cm, 1.2),
           Spacer(1, 14),
           P("PLAN DE CONQUÊTE", "titre"),
           P("Objectif : 500 étudiants", "titre"),
           P("Vision du Président-Fondateur — édition du 31 août 2026", "soustitre"),
           Spacer(1, 22),
           T([["Capacité après livraison", "9 salles — ≈ 400 étudiants/jour"],
              ["Objectif de la direction", "300 inscrits à la fin 2026, 500 à l'horizon juin 2027"],
              ["Moyens engagés", "Bâtiment 219,97 M TTC livré sous 2 mois · campagne 15 M FCFA · 3 recrutements"],
              ["Terrain", "Libreville — Akanda, lycées, entreprises, églises, CEMAC"]],
             aligns=["l", "l"], header=False, zebra=True),
           Spacer(1, 26), P("DIFFUSION RÉSERVÉE À LA DIRECTION — NE PAS TRANSMETTRE À LA BANQUE", "note"),
           PageBreak()]

    st += titre_doc("1. La vision du Président")
    st += [P("Le Président-Fondateur fixe le cap : <b>500 étudiants</b>. Le bâtiment se construit en "
             "soixante jours ; la conquête se mène sur le même rythme. Cette page n'engage que la "
             "direction de l'UPL : elle démultiplie le dossier présenté à la banque, dont le "
             "scénario prudent reste la seule base de remboursement."),
           P("Le raisonnement tient en trois chiffres. <b>Neuf salles</b> disponibles dès novembre. "
             "<b>Deux mille cinq cent mille</b> Gabonais ont moins de vingt-cinq ans, dont une "
             "majorité urbaine à Libreville et Akanda. <b>Zéro</b> offre concurrente de CPGE privée "
             "et d'école d'assurance maladie dans le pays. La demande existe ; il faut aller la "
             "chercher, salle par salle, lycée par lycée, entreprise par entreprise.")]

    st += titre_doc("2. Le potentiel commercial")
    st += [T([["Levier", "Donnée", "Conséquence"],
              ["Population", "2,57 millions d'habitants — âge médian 21,5 ans — 91 % urbains", "Cœur de cible jeune, concentré sur Libreville"],
              ["Numérique", "1,84 million d'internautes — 782 000 comptes sociaux — 3,19 millions de lignes mobiles", "WhatsApp, Facebook et TikTok touchent la majorité des familles"],
              ["Capacité physique", "9 salles — ≈ 400 places par jour en deux rotations", "300 étudiants immédiatement, 500 avec le rythme du soir"],
              ["Prix", "Licence à 1 000 000 FCFA — MBA à 4 000 000 FCFA payables en 8 échéances", "Trois à dix fois moins cher qu'une scolarité à l'étranger"],
              ["Prescription", "≈ 80 cadres formés, administrations et entreprises partenaires", "Le bouche-à-oreille est l'actif commercial n°1"]],
             aligns=["l", "l", "l"])]

    st += titre_doc("3. La bataille des soixante jours")
    st += [T([["Semaine", "Offensive"],
              ["S0", "Comptes officiels actifs — kit imprimé — Moov Money ouvert à côté d'Airtel Money — tableau de suivi des leads"],
              ["S1", "Pré-inscriptions ouvertes sur tous les canaux ; présence physique devant les 10 principaux lycées et centres de résultats du bac"],
              ["S2", "Grille tarifaire et offre des six pôles affichées ; paiement en tranches et mobile money expliqué aux familles"],
              ["S3", "Tournée des proviseurs et des entreprises ; le Président en radio ; visites du chantier en casque UPL pour les parents"],
              ["S4", "Première journée portes ouvertes à Sablière — cours ouverts, salle informatique allumée, inscription sur place"],
              ["S5", "Affichage 4×3 sur les axes passants ; encarts presse ; phoning de qualification — trois appels par prospect"],
              ["S6", "Seconde journée portes ouvertes ; relance générale des pré-inscrits ; groupes WhatsApp par lycée animés par les ambassadeurs"],
              ["S7", "Rentrée officielle dans le nouveau bâtiment — cérémonie, presse, témoignages, remerciements publics"],
              ["S8+", "Rythme de croisière : deux à trois publications par semaine, chaque lead traité sous 48 heures, reporting hebdomadaire à la Présidence"]],
             aligns=["c", "l"]),
           P("En parallèle, la chasse aux cohortes d'entreprise : vingt rendez-vous DRH en trente "
             "jours — banques, port, administrations, compagnies d'assurance. Une seule cohorte de "
             "dix cadres rapporte 40 M FCFA, soit l'équivalent d'une promotion entière de Licence.")]

    st += titre_doc("4. Le budget de la conquête — 15 000 000 FCFA")
    st += [T([["Poste", "Détail", "Montant", "Part"],
              ["Affichage et médias", "4×3 Libreville-Akanda 1,9 M · radio 1,2 M · presse 0,9 M", "4 000 000", "27 %"],
              ["Digital", "Publicités sociales 2,0 M · contenus 1,0 M · site et référencement 0,5 M", "3 500 000", "23 %"],
              ["Terrain et phoning", "Portes ouvertes 1,0 M · lycées et salons 1,0 M · crédits d'appel 1,0 M", "3 000 000", "20 %"],
              ["Influence et relations publiques", "Ambassadeurs alumni · interviews · film de rentrée", "2 000 000", "13 %"],
              ["Animation des réseaux", "Community management — 12 mois", "1 500 000", "10 %"],
              ["Événementiel", "Cérémonie de rentrée · kakémonos · tracts", "1 000 000", "7 %"],
              ["TOTAL", "", "15 000 000", "100 %"]],
             aligns=["l", "l", "c", "c"], total_rows=1),
           P("Soixante pour cent de ce budget travaille même en cas de perturbation des réseaux : "
             "radio, presse, affichage, terrain et phoning ne dépendent d'aucune connexion.")]

    st += titre_doc("5. Ce que 500 étudiants rapportent")
    st += [T([["Palier", "Effectif", "Chiffre d'affaires annuel indicatif", "Marge brute cible"],
              ["Rentrée 2026", "100 inscrits", "≈ 150 M FCFA", "≈ 40 %"],
              ["Fin 2026", "300 inscrits", "≈ 420 M FCFA", "≈ 45 %"],
              ["Mi-2027", "500 inscrits", "≈ 795 M FCFA", "≈ 50 %"]],
             aligns=["l", "c", "c", "c"]),
           P("Au palier de 500, l'UPL dégage une capacité d'autofinancement supérieure à "
             "300 M FCFA par an : de quoi financer la tranche suivante du campus — deux hectares, "
             "amphithéâtre, résidence — sans nouvel endettement lourd. Le crédit de 260 M FCFA "
             "souffle alors que l'établissement a déjà doublé de taille."),
           P("Trajectoire suivie chaque lundi matin en comité de direction : inscrits, pré-inscrits, "
             "appels passés, taux de conversion, encaissements mobile money rapprochés des reçus.")]

    st += titre_doc("6. Les partenariats internationaux")
    st += [P("La campagne de prise de contact est lancée : <b>57 institutions</b> ciblées en France, "
             "en Belgique, au Québec et au Sénégal — écoles de commerce et d'ingénieurs, prépas "
             "privées, facultés de médecine, instituts d'études politiques, dont plusieurs "
             "interlocuteurs directement responsables du développement en Afrique. Objectif de la "
             "direction : <b>trois accords cadres signés avant décembre 2026</b> — jumelage de "
             "prépa, voie d'accès vers un master, programme exécutif conjoint."),
           P("Chaque signature transforme le recrutement : un étudiant UPL sait où son diplôme peut "
             "le conduire ; une école partenaire amène ses étudiants, ses professeurs et sa "
             "réputation. L'UPL devient la plateforme d'Afrique centrale de ses partenaires — "
             "personne d'autre ne tient cette position à Libreville.")]

    st += titre_doc("7. Les risques, et comment la direction les tient")
    st += [T([["Risque", "Parade engagée"],
              ["Remplissage au-dessous de l'objectif", "Phoning en trois touches, tournée des lycées, commissions d'ambassadeurs, places de la première promotion à tarif fondateur"],
              ["Retard de chantier", "Tranche A livrée à six semaines, pénalités contractuelles, réception partielle avant réception complète"],
              ["Perturbation des réseaux", "60 % du budget hors connexion ; kit imprimé ; SMS ; radio ; accueil renforcé au secrétariat"],
              ["Trésorerie de la rentrée", "Échéanciers jusqu'à huit tranches, encaissement Airtel Money et Moov Money, reçus numérotés, rapprochement mensuel"]],
             aligns=["l", "l"])]

    st += titre_doc("8. Décisions demandées au Président")
    st += [T([["N°", "Décision", "Avis de la direction"],
              ["1", "Lancement de la bataille des soixante jours dès acceptation du devis", "GO"],
              ["2", "Budget de conquête de 15 M FCFA tel que ventilé ci-dessus", "GO"],
              ["3", "Recrutement immédiat des deux commerciaux et de l'appui administratif", "GO"],
              ["4", "Ouverture de Moov Money en complément d'Airtel Money", "GO"],
              ["5", "Campagne partenariats — relances et déplacements France de septembre", "GO"]],
             aligns=["c", "l", "c"]),
           Spacer(1, 18),
           P("Libreville, le 31 août 2026", "corpsc"),
           P("<b>Serge Patrick MINANG</b><br/>Président-Fondateur — Direction de l'UPL", "sign")]
    d = DocS(OUT2, "UPL — DOCUMENT INTERNE — PLAN DE CONQUÊTE 500 ÉTUDIANTS — DIFFUSION RESTREINTE")
    d.build(anti_coupure(st))
    return d

if __name__ == "__main__":
    d1 = doc_banque()
    d2 = doc_interne()
    for p, d in ((OUT1, d1), (OUT2, d2)):
        print("OK", os.path.basename(p), "-", d.page, "pages -", f"{os.path.getsize(p)/1024:.0f} Ko")
