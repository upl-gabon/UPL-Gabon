#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Génère les 4 documents bancaires V12 — crédit d'investissement 260 M FCFA :
  1. Dossier bancaire UPL 260M (principal)
  2. Annexes financières
  3. Annexes juridiques
  4. Master Plan Campus (repositionné)
Réutilise la charte UPL de generer_livrables.py.
"""
import os
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_RIGHT
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, PageBreak

from generer_livrables import (Doc, P, S, section, styled_table, fmt,
                               BLUE, BLUE_DK, GOLD, GOLD_LT, BLUE_LT, ZEBRA,
                               GREY, LINE)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = [os.path.join(HERE, n) for n in [
    "UPL_1_Dossier_Bancaire_260M_V12.pdf",
    "UPL_2_Annexes_Financieres_V12.pdf",
    "UPL_3_Annexes_Juridiques_V12.pdf",
    "UPL_4_Master_Plan_Campus_V12.pdf",
]]

# ================================================================ MODELE FINANCIER
P_CREDIT = 260_000_000
RATE = 0.10
IM = RATE / 12
N_MONTHS = 120          # 10 ans
DIFFERE = 12            # 12 mois intérêts seuls
START_YEAR, START_MONTH = 2026, 10   # décaissement octobre 2026

# mensualité constante après différé (n = 108)
MENS = P_CREDIT * IM / (1 - (1 + IM) ** (-(N_MONTHS - DIFFERE)))

def schedule():
    """Retourne (rows, yearly) : mensualités et agrégats par année civile."""
    rows, bal, yearly = [], P_CREDIT, {}
    for m in range(1, N_MONTHS + 1):
        if m <= DIFFERE:
            interest, capital = bal * IM, 0.0
            pay = interest
        else:
            interest = bal * IM
            capital = min(MENS - interest, bal)
            pay = interest + capital
        bal -= capital
        y = START_YEAR + (START_MONTH - 1 + m - 1) // 12
        d = yearly.setdefault(y, {"pay": 0.0, "int": 0.0, "cap": 0.0, "end": 0.0})
        d["pay"] += pay; d["int"] += interest; d["cap"] += capital; d["end"] = bal
        rows.append((m, pay, interest, capital, bal))
    return rows, yearly

ROWS_DEBT, YEARLY = schedule()
TOTAL_INT = sum(r[2] for r in ROWS_DEBT)
TOTAL_PAID = sum(r[1] for r in ROWS_DEBT)

# --- compte de résultat prudent (M FCFA)
REV = {  # programme: 2025..2031
    "Executive MBA":            [80.0, 96.0, 108.0, 116.0, 128.0, 128.0, 128.0],
    "DBA":                      [0.0, 4.5, 9.0, 13.5, 18.0, 18.0, 18.0],
    "Licence / Master (filières nouvelles)": [0.0, 12.0, 40.0, 66.0, 85.0, 95.0, 95.0],
    "CPGE":                     [0.0, 4.4, 4.4, 8.8, 8.8, 8.8, 8.8],
    "VAE":                      [7.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    "Accompagnement / conseil": [6.0, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6],
    "Frais de dossier et inscription": [2.0, 1.0, 1.0, 1.0, 1.4, 1.4, 1.4],
}
CHARGES = [69.9, 69.5, 85.0, 101.0, 116.0, 121.0, 121.0]
DOT = [0.0, 10.0, 17.5, 17.5, 17.5, 17.5, 17.5]     # dotations amortissements
YEARS = [2025, 2026, 2027, 2028, 2029, 2030, 2031]

CA = [round(sum(v[i] for v in REV.values()), 1) for i in range(7)]
EBE = [round(CA[i] - CHARGES[i], 1) for i in range(7)]
INT_Y = [YEARLY.get(y, {"int": 0.0})["int"] / 1e6 for y in YEARS]
RAI = [round(EBE[i] - DOT[i] - round(INT_Y[i], 1), 1) for i in range(7)]
IS = [round(max(RAI[i], 0) * 0.30, 1) for i in range(7)]
RN = [round(RAI[i] - IS[i], 1) for i in range(7)]
CAF = [round(RN[i] + DOT[i], 1) for i in range(7)]
SERV = [round(YEARLY.get(y, {"pay": 0.0})["pay"] / 1e6, 1) for y in YEARS]
DSCR = [round(CAF[i] / SERV[i], 2) if SERV[i] else None for i in range(7)]

assert abs(CA[1] - 119.5) < 0.01 and abs(CA[2] - 164.0) < 0.01
assert min(d for d in DSCR[1:6] if d) >= 1.30, f"DSCR min: {DSCR}"
DEVIS_TTC = 219_972_060
EMPLOI = [
    ("Construction du bâtiment universitaire R+2, 504 m2 (devis révisé TTC - MATRIX GROUP)", DEVIS_TTC),
    ("Équipements informatiques et audiovisuels (salle informatique, vidéoprojecteurs)", 10_000_000),
    ("Communication et marketing — plan de communication 12 mois (document joint)", 15_000_000),
    ("Renforcement de l'équipe (responsable administratif + 2 commerciaux, 12 mois)", 5_000_000),
    ("Fonds de roulement (cycle universitaire)", 10_000_000),
    ("Provision frais bancaires et aléas de démarrage", 27_940),
]
assert sum(m for _, m in EMPLOI) == P_CREDIT

def M(v):
    return f"{v:,.1f}".replace(",", " ").replace(".", ",")

# ================================================================ DOC 1
def build_dossier():
    st = []
    st += [P("Crédit d'investissement - 260 000 000 FCFA", "kicker"),
           P("Dossier de demande de financement", "h1"),
           P("Excellence - Innovation - Leadership", "body"), Spacer(1, 4)]
    st += [styled_table([
        [P("Établissement", "cellb"), P("Université Privée de Libreville (UPL)", "cell"),
         P("Banque sollicitée", "cellb"), P("Ecobank Gabon", "cell")],
        [P("Objet", "cellb"), P("Construction du bâtiment pédagogique R+2, équipement et lancement commercial des six filières", "cell"),
         P("Montant", "cellb"), P("260 000 000 FCFA", "cell")],
        [P("Durée", "cellb"), P("120 mois, dont 12 mois de différé sur le capital", "cell"),
         P("Date du dossier", "cellb"), P("Libreville, août 2026", "cell")],
    ], [2.6*cm, 7.6*cm, 2.9*cm, 4.1*cm], header=False, zebra=False,
        extra=[("BACKGROUND", (0, 0), (0, -1), BLUE_LT), ("BACKGROUND", (2, 0), (2, -1), BLUE_LT),
               ("VALIGN", (0, 0), (-1, -1), "TOP")]),
        Spacer(1, 8)]

    st += [P("Serge Patrick MINANG - Président-Fondateur - Université Privée de Libreville", "small"),
           P("Sablière, en face de la Résidence de l'Ambassade d'Arabie Saoudite - Libreville - Tél. 062 62 19 78 / 077 35 95 72 - contact@upl-gabon.com - www.upl-gabon.com", "note"),
           Spacer(1, 8)]

    st += section("1. Lettre de demande de financement")
    st += [P("Libreville, le 30 août 2026", "small"), Spacer(1, 4),
           P("Monsieur le Directeur des Engagements Entreprises, Ecobank Gabon, Libreville", "small"),
           P("<b>Objet : Demande de crédit d'investissement - 260 000 000 FCFA</b>", "body"),
           P("Monsieur le Directeur,", "body"),
           P("Depuis quatre années, l'Université Privée de Libreville développe son activité au service "
             "de la formation des cadres et dirigeants gabonais. Fondée en 2022, elle a délivré son "
             "programme Executive MBA à près de 80 auditeurs, majoritairement issus de "
             "l'administration, des entreprises publiques et du secteur privé. L'établissement est "
             "autofinancé, sans dette bancaire, et dégage un résultat d'exploitation positif depuis "
             "l'origine."),
           P("Pour la rentrée 2026-2027, l'UPL ouvre six filières structurantes - Gouvernance et "
             "Management, Économie Numérique et Intelligence Artificielle, Économie Bleue, Droit, "
             "Assurance et Sécurité Sociale, Classes Préparatoires - aux côtés de l'Executive MBA et "
             "du DBA. Les locaux actuels ne permettent pas d'accueillir cette montée en charge : "
             "après mise en concurrence, un devis ferme et négocié de <b>219 972 060 FCFA TTC</b> "
             "(révision n° 2, soit -46 % sur la première proposition) couvre la construction d'un "
             "bâtiment pédagogique R+2 d'environ 504 m2 - 9 salles climatisées et meublées - livrable "
             "en <b>deux mois</b>, afin que les cours puissent débuter dès septembre dans les locaux "
             "actuels puis basculer progressivement dans le nouveau bâtiment dès la réception "
             "partielle."),
           P("J'ai l'honneur de solliciter un crédit d'investissement de <b>260 000 000 FCFA</b> sur "
             "120 mois, avec 12 mois de différé sur le capital, couvrant la construction, "
             "l'équipement informatique, le plan de communication de lancement (15 M FCFA, document "
             "joint), le renforcement de l'équipe commerciale et le fonds de roulement. Le plan de "
             "remboursement, établi sur un scénario prudent - sans intégrer le salaire public du "
             "fondateur - présente un ratio de couverture du service de la dette (DSCR) compris entre "
             f"<b>{M(min(d for d in DSCR[1:6] if d))} x et {M(max(d for d in DSCR[1:6] if d))} x</b> "
             "sur la période d'exécution, au-delà du seuil bancaire habituel de 1,3 x."),
           P("Le présent dossier détaille l'établissement, sa situation financière, l'emploi précis "
             "des fonds, le plan commercial et les projections associées. Les états financiers, "
             "échéanciers et pièces justificatives figurent dans les annexes séparées. Je souhaite "
             "inscrire ce financement dans une relation bancaire durable avec Ecobank Gabon et me "
             "tiens à votre disposition pour toute présentation complémentaire ou visite de site."),
           P("Je vous prie d'agréer, Monsieur le Directeur, l'expression de ma considération "
             "distinguée."), Spacer(1, 6),
           P("<b>Serge Patrick MINANG</b><br/>Président-Fondateur - Université Privée de Libreville", "bodyc"),
           Spacer(1, 6)]

    st += section("2. Présentation institutionnelle de l'UPL")
    st += [styled_table([
        [P("Dénomination", "cellb"), P("Université Privée de Libreville (UPL), fondée en 2022", "cell")],
        [P("Dirigeant", "cellb"), P("Serge Patrick MINANG, ingénieur, MBA, doctorant DBA, fonctionnaire du Ministère des Travaux Publics", "cell")],
        [P("Siège", "cellb"), P("Quartier Sablière, Libreville - face Résidence de l'Ambassade d'Arabie Saoudite", "cell")],
        [P("Capital", "cellb"), P("Détenu à 100 % par la famille du fondateur : M. MINANG (60 %), Mme Blandine ENGONGA (15 %), cinq enfants (5 % chacun)", "cell")],
        [P("Programme socle", "cellb"), P("Executive MBA en partenariat avec l'Université de Douala - près de 80 cadres formés - scolarité 4 000 000 FCFA", "cell")],
        [P("Ouverture 2026-2027", "cellb"), P("Six filières : Gouvernance et Management · Économie Numérique et IA · Économie Bleue · Droit · Assurance et Sécurité Sociale · CPGE", "cell")],
    ], [3.6*cm, 13.6*cm], header=False, zebra=False,
        extra=[("BACKGROUND", (0, 0), (0, -1), BLUE_LT), ("VALIGN", (0, 0), (-1, -1), "TOP")]),
        Spacer(1, 4),
           P("Le corps professoral associe enseignants permanents, vacataires universitaires et "
             "intervenants professionnels. L'ouverture effective de chaque filière est conditionnée "
             "aux autorisations ministérielles correspondantes, disponibles ou en cours de "
             "finalisation. Le positionnement est complémentaire de l'Université Omar Bongo, de "
             "l'USTM et des établissements privés existants, sur les créneaux du management exécutif, "
             "du numérique appliqué, de la gouvernance et des métiers de la protection sociale.")]

    st += section("3. Plan de développement 2026-2027")
    st += [styled_table([
        [P("Objectif", "cellb"), P("Détail", "cell")],
        [P("Capacité d'accueil", "cell"), P("Construire en 2 mois un bâtiment pédagogique R+2 de 504 m2 (9 salles) portant la capacité à environ 400 étudiants/jour, pour atteindre le premier palier de 300 étudiants puis l'horizon stratégique de 500", "cell")],
        [P("Rentrée 2026", "cell"), P("Cours maintenus dès septembre dans les locaux actuels de Sablière ; réception partielle du nouveau bâtiment à 6 semaines (tranche A - RDC) puis réception complète sous 2 mois ; transfert progressif des cours", "cell")],
        [P("Offre", "cell"), P("Ouvrir les six filières nouvelles à la rentrée 2026-2027 aux côtés de l'Executive MBA et du DBA", "cell")],
        [P("Structuration", "cell"), P("Professionnaliser les fonctions financière et commerciale ; préparer l'accès aux financements long terme du campus (Master Plan joint en document 4)", "cell")],
    ], [3.6*cm, 13.6*cm], header=False, zebra=False,
        extra=[("BACKGROUND", (0, 0), (0, -1), BLUE_LT), ("VALIGN", (0, 0), (-1, -1), "TOP")]),
        Spacer(1, 4),
           P("Calendrier opérationnel :", "cellb"),
           styled_table([
               [P("Période", "cellb"), P("Étape", "cellb")],
               [P("Sept. 2026", "cell"), P("Rentrée dans les locaux actuels ; signature du marché de travaux ; lancement de la campagne de communication")],
               [P("Sept.-nov. 2026", "cell"), P("Travaux du bâtiment R+2 en cadence renforcée : réception partielle (tranche A - RDC) à 6 semaines, réception complète à 2 mois")],
               [P("Nov. 2026 - T1 2027", "cell"), P("Équipement informatique et audiovisuel ; transfert de l'intégralité des cours ; montée en charge des six filières")],
               [P("2027-2028", "cell"), P("Consolidation des effectifs ; reporting mensuel à la banque ; préparation du financement long terme du campus")],
           ], [3.6*cm, 13.6*cm])]

    st += section("4. Plan marketing et commercial")
    st += [P("Message central : <b>« UPL - Formez-vous aujourd'hui aux métiers de demain. »</b> Le "
             "développement commercial était resté informel (bouche-à-oreille, réseaux du fondateur). "
             "L'ouverture de six filières et la livraison du nouveau bâtiment imposent une "
             "structuration professionnelle, détaillée dans le <b>plan de communication 2026-2027 "
             "joint au dossier</b> (12 mois, budget 15 M FCFA, intégré au présent financement) : "
             "digital (Facebook, TikTok, LinkedIn, WhatsApp Business), radio, presse, affichage "
             "4x3, terrain (portes ouvertes, lycées), phoning et encaissement par mobile money "
             "(Airtel Money et Moov Money), adaptés aux réalités du marché gabonais."),
           styled_table([
               [P("Objectif 12 mois", "cellb"), P("Cible", "cellrb")],
               [P("Contacts qualifiés générés (tunnel commercial)", "cell"), P("3 000", "cellr")],
               [P("Pré-inscriptions issues du tunnel", "cell"), P("500", "cellr")],
               [P("Étudiants inscrits, toutes filières (premier palier)", "cell"), P("100 et plus", "cellr")],
               [P("Coût moyen d'acquisition par étudiant inscrit", "cell"), P("max. 150 000 FCFA", "cellr")],
           ], [11.5*cm, 5.7*cm])]

    st += section("5. Emploi des 260 000 000 FCFA")
    st += [styled_table(
        [[P("Poste", "cellb"), P("Montant (FCFA)", "cellrb"), P("Part", "cellrb"), P("Justificatif", "cellb")]] +
        [[P(p, "cell"), P(fmt(m), "cellr"), P(f"{m/P_CREDIT*100:.1f} %".replace(".", ","), "cellr"), P(j, "cell")]
         for (p, m), j in zip(EMPLOI, [
             "Devis révisé MATRIX GROUP du 30/08/2026 (révision n° 2 négociée)",
             "Devis distributeurs IT - à joindre avant décaissement",
             "Plan de communication 2026-2027 (document joint)",
             "Contrats et bulletins - à joindre",
             "Décalages d'encaissement du cycle universitaire",
             "Frais de dossier bancaires et imprévus de démarrage"])] +
        [[P("TOTAL", "cellb"), P(fmt(P_CREDIT), "cellrb"), P("100 %", "cellrb"), P("", "cell")]],
        [6.6*cm, 3.2*cm, 1.6*cm, 5.8*cm],
        extra=[("BACKGROUND", (0, 7), (-1, 7), GOLD_LT), ("LINEABOVE", (0, 7), (-1, 7), 0.9, GOLD)]),
           P("Postes physiques : 230 M FCFA (88,5 %) - construction et équipements. Postes immatériels "
             "et trésorerie : 30 M FCFA (11,5 %). Décaissement possible en tranches contre devis et "
             "factures : tranche travaux à la signature du marché, puis équipements, communication et "
             "trésorerie sur justificatifs.", "note")]

    st += section("6. Prévisionnel financier et remboursement")
    st += [styled_table([
        [P("Paramètre", "cellb"), P("Valeur", "cell")],
        [P("Montant", "cellb"), P("260 000 000 FCFA")],
        [P("Durée", "cellb"), P("120 mois (10 ans), dont 12 mois de différé sur le capital")],
        [P("Taux indicatif retenu", "cellb"), P("10 % annuel (à négocier)")],
        [P("Mensualité en différé (mois 1 à 12)", "cellb"), P(f"env. {fmt(P_CREDIT*RATE/12)} FCFA (intérêts seuls)")],
        [P("Mensualité en régime (mois 13 à 120)", "cellb"), P(f"env. {fmt(MENS)} FCFA")],
        [P("Total intérêts", "cellb"), P(f"env. {M(TOTAL_INT/1e6)} M FCFA")],
        [P("Coût total du crédit", "cellb"), P(f"env. {M(TOTAL_PAID/1e6)} M FCFA")],
    ], [6.2*cm, 11.0*cm], header=False, zebra=False,
        extra=[("BACKGROUND", (0, 0), (0, -1), BLUE_LT)]),
        Spacer(1, 4),
           P("Capacité de remboursement - scénario prudent (DSCR = CAF / service annuel de la "
             "dette), sans intégrer le salaire public du fondateur (env. 8 M FCFA/an), ressource "
             "complémentaire mobilisable :", "body"),
           styled_table([[P("Indicateur (M FCFA)", "cellb")] + [P(str(y), "cellc") for y in YEARS[1:6]]] + [
               [P("CAF (scénario prudent)", "cell")] + [P(M(CAF[i]), "cellr") for i in range(1, 6)],
               [P("Service annuel de la dette", "cell")] + [P(M(SERV[i]), "cellr") for i in range(1, 6)],
               [P("DSCR", "cellb")] + [P(f"{M(DSCR[i])} x", "cellrb") for i in range(1, 6)],
               [P("Seuil bancaire de référence", "cell")] + [P("1,3 x", "cellc") for _ in range(5)],
           ], [5.4*cm] + [2.36*cm]*5),
           P("Le crédit est intégralement remboursé en septembre 2036. Le stress test de l'année "
             "pleine 2028 figure en annexes financières : le scénario dégradé (-25 % de CA) est "
             "couvert par la trésorerie constituée dès 2026 (fonds de roulement + CAF cumulée) et par "
             "le salaire du fondateur ; le scénario de crise (-40 %) appellerait un aménagement "
             "d'échéancier avec la banque.", "note")]

    st += section("7. Analyse financière synthétique")
    st += [styled_table([
        [P("Rubrique 2025 (activité récurrente)", "cellb"), P("Montant (FCFA)", "cellrb")],
        [P("Chiffre d'affaires récurrent (Executive MBA 80 M · VAE 7,5 M · conseil 6 M · frais 2 M)", "cell"), P("95 500 000", "cellr")],
        [P("Charges d'exploitation", "cell"), P("- 69 900 000", "cellr")],
        [P("EBE indicatif (marge env. 26,8 %)", "cellb"), P("25 600 000", "cellrb")],
    ], [11.0*cm, 6.2*cm], header=False, zebra=False,
        extra=[("BACKGROUND", (0, 0), (0, -1), BLUE_LT)]),
           P("Les états financiers 2022-2025 sont issus des déclarations du fondateur, non certifiés ; "
             "une revue ONECCA est en cours d'organisation (détail en annexes). L'établissement ne "
             "porte aucune dette bancaire : sa capacité d'endettement est entière et ce crédit "
             "constituerait sa première relation de crédit institutionnelle. Les créances étudiants "
             "représentent env. 10 % du CA MBA ; un mécanisme de prélèvement et d'encaissement par "
             "mobile money est prévu dès la rentrée.")]

    st += section("8. Garanties, pièces et reporting")
    st += [P("Les garanties définitives seront arrêtées lors de l'instruction conformément à la "
             "politique de risque d'Ecobank : le fondateur est disposé à examiner l'ensemble des "
             "dispositifs usuels (hypothèque sur le bâtiment financé, caution personnelle, "
             "assurance-vie dirigeant, blocage de comptes). Le détail des 16 pièces du dossier figure "
             "en annexes juridiques (document 3), dont le devis révisé et le marché de travaux "
             "MATRIX GROUP. Reporting proposé : trimestriel (effectifs, CA encaissé, charges), "
             "états financiers annuels dans les 4 mois de la clôture, point annuel de gestion et "
             "communication immédiate de tout événement significatif."),
           Spacer(1, 10),
           P("<b>Serge Patrick MINANG</b><br/>Président-Fondateur - Université Privée de Libreville", "bodyc"),
           Spacer(1, 6),
           P("Pièces jointes : document 2 - annexes financières · document 3 - annexes juridiques · "
             "document 4 - Master Plan Campus · plan de communication 2026-2027 · devis révisé "
             "MATRIX GROUP.", "note")]
    doc = Doc(OUT[0], "UPL - Dossier bancaire 260 M FCFA - Ecobank Gabon - V12")
    doc.build(st)
    return doc

# ================================================================ DOC 2
def build_annexes_fin():
    st = []
    st += [P("Document 2 - états prévisionnels et analyse de risque", "kicker"),
           P("Annexes financières", "h1"),
           P("Dossier bancaire UPL / Ecobank Gabon - 260 M FCFA - scénario prudent (base du DSCR) - "
             "horizon 2025-2031 - Libreville, août 2026", "body"), Spacer(1, 6)]

    st += section("1. Hypothèses de construction du prévisionnel")
    st += [styled_table([
        [P("Hypothèse", "cellb"), P("Valeur", "cellb"), P("Commentaire", "cellb")],
        [P("Effectifs MBA (référence)", "cell"), P("20 à 32 sur 5 ans", "cellr"), P("Base historique 2022-2025 stable", "cell")],
        [P("Prix MBA / DBA", "cell"), P("4 000 000 / 4 500 000 FCFA", "cellr"), P("Grille officielle 2026-2027", "cell")],
        [P("Prix Master 1 / Master 2", "cell"), P("1 500 000 / 2 000 000 FCFA", "cellr"), P("Grille officielle 2026-2027", "cell")],
        [P("Prix Licence (1re promotion)", "cell"), P("1 000 000 puis 1 200 000 FCFA", "cellr"), P("1 M pour les 50 premières inscriptions", "cell")],
        [P("Prix CPGE", "cell"), P("2 200 000 FCFA", "cellr"), P("Grille officielle 2026-2027", "cell")],
        [P("Capacité physique", "cell"), P("9 salles (bâtiment R+2, 504 m2)", "cellr"), P("Livré sous 2 mois - devis révisé MATRIX GROUP", "cell")],
        [P("Taux IS retenu", "cell"), P("30 %", "cellr"), P("Régime standard", "cell")],
        [P("Dotations aux amortissements", "cell"), P("17,5 M FCFA/an à partir de 2027", "cellr"), P("Bâtiment sur 25 ans, équipements sur 3-5 ans", "cell")],
        [P("Charges variables / fixes", "cell"), P("env. 70 % / 30 %", "cellr"), P("Hypothèse retenue pour le stress test", "cell")],
        [P("Créances clients", "cell"), P("env. 10 % du CA MBA", "cellr"), P("Observé 2024-2025", "cell")],
        [P("Salaire du fondateur (fonctionnaire)", "cell"), P("env. 8 M FCFA/an", "cellr"), P("Non intégré au calcul du DSCR", "cell")],
    ], [5.0*cm, 5.2*cm, 7.0*cm])]

    st += section("2. Compte de résultat prévisionnel - scénario prudent (M FCFA)")
    lines = []
    for prog, vals in REV.items():
        lines.append([P(prog, "cell")] + [P(M(v), "cellr") for v in vals])
    tbl = [[P("Rubrique", "cellb")] + [P(str(y), "cellc") for y in YEARS]] + lines + [
        [P("CHIFFRE D'AFFAIRES", "cellb")] + [P(f"<b>{M(CA[i])}</b>", "cellrb") for i in range(7)],
        [P("Charges d'exploitation", "cell")] + [P(M(-CHARGES[i]), "cellr") for i in range(7)],
        [P("EBE", "cellb")] + [P(M(EBE[i]), "cellrb") for i in range(7)],
        [P("Dotations aux amortissements", "cell")] + [P(M(-DOT[i]), "cellr") for i in range(7)],
        [P("Charges financières (crédit)", "cell")] + [P(M(-round(INT_Y[i], 1)), "cellr") for i in range(7)],
        [P("Résultat avant impôt", "cell")] + [P(M(RAI[i]), "cellr") for i in range(7)],
        [P("Impôt sur les sociétés (30 %)", "cell")] + [P(M(-IS[i]), "cellr") for i in range(7)],
        [P("Résultat net", "cellb")] + [P(M(RN[i]), "cellrb") for i in range(7)],
        [P("CAF", "cellb")] + [P(f"<b>{M(CAF[i])}</b>", "cellrb") for i in range(7)],
    ]
    st += [styled_table(tbl, [5.4*cm] + [1.83*cm]*7, fontsize=7.6),
           P("Lecture : la construction en propre remplace le loyer et les charges d'immobilier ; "
             "la marge EBE progresse de 42 % (2026) à 52 % (2030) par effet d'échelle.", "note")]

    st += section("3. Flux de trésorerie prévisionnels (M FCFA)")
    inv_2026 = -(DEVIS_TTC + 10_000_000) / 1e6
    st += [styled_table([
        [P("Flux", "cellb")] + [P(str(y), "cellc") for y in YEARS[1:6]],
        [P("CAF", "cell")] + [P(M(CAF[i]), "cellr") for i in range(1, 6)],
        [P("Variation BFR", "cell")] + [P(M(v), "cellr") for v in (-2.0, -2.5, -2.0, -1.5, 0.0)],
        [P("Flux d'exploitation", "cell")] + [P(M(CAF[i] + v), "cellr") for i, v in zip(range(1, 6), (-2.0, -2.5, -2.0, -1.5, 0.0))],
        [P("Investissements (travaux + équipements)", "cell")] + [P(M(inv_2026) if i == 1 else "0,0", "cellr") for i in range(1, 6)],
        [P("Décaissement du crédit", "cell")] + [P(M(260.0) if i == 1 else "0,0", "cellr") for i in range(1, 6)],
        [P("Service de la dette (intérêts + capital)", "cell")] + [P(M(-SERV[i]), "cellr") for i in range(1, 6)],
        [P("Variation de trésorerie", "cellb")] + [P(M(CAF[i] + v + (inv_2026 if i == 1 else 0) + (260.0 if i == 1 else 0) - SERV[i]), "cellrb") for i, v in zip(range(1, 6), (-2.0, -2.5, -2.0, -1.5, 0.0))],
    ], [6.4*cm] + [2.16*cm]*5),
        P("La trésorerie reste positive chaque année : le pic d'investissement 2026 (env. 240 M FCFA) "
          "est intégralement couvert par le crédit, et le fonds de roulement de 10 M FCFA sécurise "
          "les décalages d'encaissement du cycle universitaire.", "note")]

    st += section("4. Plan d'amortissement - 260 M FCFA / 120 mois / différé 12 mois / 10 %")
    st += [P(f"Mensualité en régime : <b>{fmt(MENS)} FCFA</b> (mois 13 à 120). Décaissement "
             f"octobre 2026 ; première mensualité à intérêts seuls en octobre 2026 ; dernière "
             f"échéance en septembre 2036. Total des intérêts : env. {M(TOTAL_INT/1e6)} M FCFA ; coût "
             f"total du crédit : env. {M(TOTAL_PAID/1e6)} M FCFA.", "body")]
    yr_rows = [[P("Année civile", "cellb"), P("Service annuel (FCFA)", "cellrb"),
                P("Dont intérêts", "cellrb"), P("Dont capital", "cellrb"),
                P("Capital restant dû fin d'année", "cellrb")]]
    for y in range(2026, 2037):
        d = YEARLY.get(y)
        if not d:
            continue
        yr_rows.append([P(str(y), "cellc"), P(fmt(d["pay"]), "cellr"), P(fmt(d["int"]), "cellr"),
                        P(fmt(d["cap"]), "cellr"), P(fmt(d["end"]), "cellr")])
    yr_rows.append([P("TOTAL", "cellb"), P(fmt(TOTAL_PAID), "cellrb"), P(fmt(TOTAL_INT), "cellrb"),
                    P(fmt(P_CREDIT), "cellrb"), P("", "cell")])
    st += [styled_table(yr_rows, [2.4*cm, 3.9*cm, 3.6*cm, 3.6*cm, 3.7*cm], fontsize=7.9,
                        extra=[("BACKGROUND", (0, len(yr_rows)-1), (-1, len(yr_rows)-1), GOLD_LT)]),
           P("Échéancier mensuel détaillé disponible sur demande (tableur). Années 2027 : intérêts "
             "seuls jusqu'en septembre, puis remboursement du capital à compter d'octobre 2027.", "note")]

    st += section("5. Ratio de couverture du service de la dette (DSCR)")
    st += [styled_table([[P("Indicateur (M FCFA)", "cellb")] + [P(str(y), "cellc") for y in YEARS[1:6]]] + [
        [P("CAF", "cell")] + [P(M(CAF[i]), "cellr") for i in range(1, 6)],
        [P("Service annuel de la dette", "cell")] + [P(M(SERV[i]), "cellr") for i in range(1, 6)],
        [P("DSCR", "cellb")] + [P(f"{M(DSCR[i])} x", "cellrb") for i in range(1, 6)],
        [P("Position vs seuil 1,3 x", "cell")] + [P("> seuil", "cellc") for _ in range(5)],
    ], [5.4*cm] + [2.36*cm]*5),
        P("Le salaire fonctionnaire du fondateur (env. 8 M FCFA/an) n'est pas intégré : il constitue "
          "une réserve de couverture supplémentaire d'environ 20 % du service annuel de la dette.", "note")]

    st += section("6. Stress test - année 2028 (année pleine d'amortissement)")
    base_ca, base_ebe = CA[3], EBE[3]
    serv28 = SERV[3]
    def stress(pct):
        ca = base_ca * (1 - pct)
        ebe = base_ebe - 0.68 * (base_ca * pct)
        rai = ebe - DOT[3] - round(INT_Y[3], 1)
        rn = rai - max(rai, 0) * 0.30
        caf = rn + DOT[3]
        return ca, ebe, caf
    s25 = stress(0.25); s40 = stress(0.40)
    rh_ebe = base_ebe - 0.30 * CHARGES[3] * 0.40
    rh_rai = rh_ebe - DOT[3] - round(INT_Y[3], 1)
    rh_caf = (rh_rai - max(rh_rai, 0) * 0.3) + DOT[3]
    st += [styled_table([
        [P("Indicateur (M FCFA)", "cellb"), P("BASE", "cellb"), P("Dégradé -25 % CA", "cellb"), P("Crise -40 % CA", "cellb"), P("Choc RH +30 %", "cellb")],
        [P("Chiffre d'affaires", "cell"), P(M(base_ca), "cellr"), P(M(s25[0]), "cellr"), P(M(s40[0]), "cellr"), P(M(base_ca), "cellr")],
        [P("EBE", "cell"), P(M(base_ebe), "cellr"), P(M(s25[1]), "cellr"), P(M(s40[1]), "cellr"), P(M(rh_ebe), "cellr")],
        [P("CAF", "cell"), P(M(CAF[3]), "cellr"), P(M(s25[2]), "cellr"), P(M(s40[2]), "cellr"), P(M(rh_caf), "cellr")],
        [P("Service annuel de la dette", "cell")] + [P(M(serv28), "cellr")] * 4,
        [P("DSCR", "cellb")] + [P(f"{M(v)} x", "cellrb") for v in
                                (CAF[3]/serv28, s25[2]/serv28, s40[2]/serv28, rh_caf/serv28)],
    ], [4.6*cm, 3.1*cm, 3.1*cm, 3.1*cm, 3.1*cm]),
        P("Lecture : en scénario dégradé (-25 % de CA), le service de la dette reste honoré grâce à "
          "la trésorerie constituée dès 2026 (fonds de roulement + CAF cumulée 2026-2027 env. 45 M "
          "FCFA) et au salaire du fondateur ; un réaménagement léger d'échéancier suffirait. En "
          "scénario de crise (-40 %), l'UPL solliciterait un aménagement de 6 à 12 mois avec la "
          "banque, la structure du crédit (différé 12 mois) absorbant le premier choc. Le choc RH "
          "est absorbé.", "note")]

    st += section("7. Scénario cible indicatif - trajectoire 500 étudiants")
    st += [styled_table([
        [P("Indicateur", "cellb"), P("2026", "cellc"), P("2027", "cellc"), P("2028", "cellc"), P("2029", "cellc"), P("2030", "cellc")],
        [P("Effectifs totaux UPL (fourchette)", "cell")] + [P(v, "cellr") for v in ("80-100", "150-220", "250-350", "350-450", "env. 500")],
        [P("Chiffre d'affaires (M FCFA, fourchette)", "cell")] + [P(v, "cellr") for v in ("160-200", "300-420", "490-650", "650-780", "env. 795")],
        [P("Investissements complémentaires nécessaires", "cell")] + [P(v, "cellr") for v in ("—", "20-40 M", "50-90 M", "80-150 M", "100-200 M")],
    ], [6.0*cm] + [2.24*cm]*5),
        P("Scénario indicatif, non retenu pour le DSCR. Avec 9 salles (contre 4 aujourd'hui), le "
          "bâtiment financé porte à lui seul le premier palier de 300 étudiants ; la trajectoire 500 "
          "passe par le Master Plan campus (document 4).", "note")]

    st += section("8. Principaux ratios financiers - scénario prudent")
    end_bal = [YEARLY.get(y, {"end": 0.0})["end"] / 1e6 for y in YEARS]
    propres = [28.0, 75.0, 118.0, 172.0, 232.0, 297.0, 363.0]
    st += [styled_table([
        [P("Ratio", "cellb")] + [P(str(y), "cellc") for y in YEARS[1:6]],
        [P("Marge EBE / CA", "cell")] + [P(f"{M(EBE[i]/CA[i]*100)} %", "cellr") for i in range(1, 6)],
        [P("Résultat net / CA", "cell")] + [P(f"{M(RN[i]/CA[i]*100)} %", "cellr") for i in range(1, 6)],
        [P("Endettement / capitaux propres", "cell")] + [P(f"{M(end_bal[i]/propres[i])} x", "cellr") for i in range(1, 6)],
        [P("Endettement / EBE", "cell")] + [P(f"{M(end_bal[i]/EBE[i])} x", "cellr") for i in range(1, 6)],
        [P("DSCR", "cellb")] + [P(f"{M(DSCR[i])} x", "cellrb") for i in range(1, 6)],
    ], [5.8*cm] + [2.24*cm]*5, fontsize=7.9)]

    st += section("9. Plan d'emploi des 260 000 000 FCFA")
    st += [styled_table([[P("Poste", "cellb"), P("Montant (FCFA)", "cellrb"), P("Part", "cellrb")]] +
        [[P(p, "cell"), P(fmt(m), "cellr"), P(f"{m/P_CREDIT*100:.1f} %".replace(".", ","), "cellr")] for p, m in EMPLOI] +
        [[P("TOTAL", "cellb"), P(fmt(P_CREDIT), "cellrb"), P("100 %", "cellrb")]],
        [10.2*cm, 4.0*cm, 3.0*cm],
        extra=[("BACKGROUND", (0, 7), (-1, 7), GOLD_LT)])]

    st += section("10. Grille tarifaire officielle 2026-2027")
    st += [styled_table([
        [P("Programme", "cellb"), P("Frais annuels (FCFA)", "cellrb"), P("Frais d'inscription", "cellrb")],
        [P("Licence 1 (50 premières places)", "cell"), P("1 000 000", "cellr"), P("200 000", "cellr")],
        [P("Licence 1 (tarif normal)", "cell"), P("1 200 000", "cellr"), P("300 000", "cellr")],
        [P("Master 1", "cell"), P("1 500 000", "cellr"), P("300 000", "cellr")],
        [P("Master 2", "cell"), P("2 000 000", "cellr"), P("300 000", "cellr")],
        [P("CPGE", "cell"), P("2 200 000", "cellr"), P("300 000", "cellr")],
        [P("Executive MBA", "cell"), P("4 000 000", "cellr"), P("300 000", "cellr")],
        [P("DBA", "cell"), P("4 500 000", "cellr"), P("300 000", "cellr")],
    ], [8.0*cm, 4.6*cm, 4.6*cm]),
           Spacer(1, 8),
           P("<b>Serge Patrick MINANG</b><br/>Président-Fondateur - Université Privée de Libreville", "bodyc")]
    doc = Doc(OUT[1], "UPL - Annexes financières - dossier 260 M FCFA - V12")
    doc.build(st)
    return doc

# ================================================================ DOC 3
def build_annexes_jur():
    st = []
    st += [P("Document 3 - bordereau et fiches descriptives", "kicker"),
           P("Annexes juridiques et pièces justificatives", "h1"),
           P("Dossier bancaire UPL / Ecobank Gabon - 260 M FCFA - Libreville, août 2026", "body"),
           P("Sablière, en face de la Résidence de l'Ambassade d'Arabie Saoudite - Libreville - "
             "Tél. 062 62 19 78 / 077 35 95 72 - contact@upl-gabon.com - www.upl-gabon.com", "note"),
           Spacer(1, 6)]

    st += section("1. Bordereau de situation documentaire")
    pieces = [
        ("1", "Statuts de l'UPL", "Disponible"),
        ("2", "Registre du Commerce et du Crédit Mobilier (RCCM)", "Disponible"),
        ("3", "Convention de partenariat avec l'Université de Douala", "Disponible"),
        ("4", "Autorisations ministérielles par filière", "Disponible / en cours"),
        ("5", "Grille tarifaire officielle 2026-2027", "Disponible"),
        ("6", "Supports de communication (flyers filières)", "Disponible"),
        ("7", "Liste étudiants MBA et état des créances", "Disponible"),
        ("8", "États financiers 2022-2025 (reconstitués)", "Disponible"),
        ("9", "Relevés bancaires 12 à 24 mois", "À produire"),
        ("10", "Devis révisé MATRIX GROUP et contrat de travaux du bâtiment R+2", "Devis disponible - contrat à joindre"),
        ("11", "Devis équipements informatiques et audiovisuels", "À produire avant décaissement"),
        ("12", "Plan de communication 2026-2027 et devis médias", "Disponible (document joint)"),
        ("13", "Attestations fiscales et sociales à jour", "À produire"),
        ("14", "Bulletins de salaire et attestation employeur du fondateur", "Disponible"),
        ("15", "CV du fondateur et de l'équipe dirigeante", "Disponible"),
        ("16", "Répartition du capital (actionnariat familial)", "Disponible"),
    ]
    st += [styled_table([[P("N°", "cellc"), P("Pièce", "cellb"), P("Statut", "cellb")]] +
        [[P(n, "cellc"), P(p, "cell"), P(s, "cell")] for n, p, s in pieces],
        [1.2*cm, 11.0*cm, 5.0*cm])]

    st += section("2. Fiches descriptives par pièce")
    fiches = [
        ("Pièce n° 1 - Statuts de l'UPL",
         "Statuts constitutifs de l'Université Privée de Libreville précisant l'objet social "
         "(enseignement supérieur privé), la forme juridique, le siège social (Sablière, Libreville) "
         "et la répartition du capital. Original signé et enregistré."),
        ("Pièce n° 2 - RCCM",
         "Extrait à jour du Registre du Commerce et du Crédit Mobilier de Libreville, attestant "
         "l'immatriculation et l'existence légale de l'établissement."),
        ("Pièce n° 3 - Convention avec l'Université de Douala",
         "Convention académique liant l'UPL à l'Université de Douala (Cameroun) pour l'ingénierie "
         "pédagogique du programme Executive MBA, la reconnaissance des crédits universitaires et la "
         "participation croisée d'enseignants. Partenariat constituant un actif immatériel majeur du "
         "dossier."),
        ("Pièce n° 4 - Autorisations ministérielles",
         "Autorisations délivrées par le Ministère de l'Enseignement supérieur gabonais pour "
         "l'ouverture des filières. Les autorisations des nouvelles filières 2026-2027 sont "
         "disponibles ou en cours de finalisation, filière par filière ; leur obtention conditionne "
         "l'ouverture effective de chaque cursus."),
        ("Pièce n° 5 - Grille tarifaire officielle 2026-2027",
         "Grille tarifaire publiée par l'UPL détaillant les frais de scolarité et d'inscription pour "
         "chaque programme (Licence, Master, CPGE, MBA, DBA)."),
        ("Pièce n° 6 - Supports de communication",
         "Flyers officiels par filière (Gouvernance, Numérique et IA, Économie Bleue, Droit, École "
         "d'Assurance et de Sécurité Sociale, CPGE) et formulaires de pré-inscription."),
        ("Pièce n° 7 - Liste étudiants MBA et créances",
         "Liste nominative des auditeurs MBA en cours de formation, avec état des montants encaissés "
         "et des créances résiduelles (env. 10 % du CA MBA, soit env. 8 M FCFA). Un mécanisme "
         "d'encaissement par mobile money et prélèvement est prévu dès la rentrée 2026."),
        ("Pièce n° 8 - États financiers 2022-2025",
         "Comptes de résultat et bilans reconstitués sur 2022-2025 à partir des données du "
         "fondateur. Non certifiés à ce jour ; revue par un expert-comptable ONECCA en cours "
         "d'organisation."),
        ("Pièce n° 9 - Relevés bancaires",
         "Relevés sur 12 à 24 mois de l'ensemble des comptes de l'établissement, à produire à "
         "l'analyste crédit pour validation des flux d'encaissement."),
        ("Pièce n° 10 - Devis révisé MATRIX GROUP et contrat de travaux",
         "Devis quantitatif et estimatif initial du 01/09/2026 (409 672 872 FCFA TTC) et "
         "contre-proposition négociée de l'UPL arrêtée à 219 972 060 FCFA TTC (révision n° 2, "
         "-46,3 %), couvrant la construction du bâtiment pédagogique R+2 de 504 m2 : 9 salles "
         "climatisées et meublées, sanitaires, réseaux informatiques, sécurité incendie, "
         "aménagements extérieurs. Délai d'exécution : 2 mois maximum, avec réception partielle à "
         "6 semaines pour permettre la rentrée. Le contrat de travaux signé sera joint avant "
         "décaissement de la tranche travaux."),
        ("Pièce n° 11 - Devis équipements informatiques et audiovisuels",
         "Devis nominatifs des distributeurs IT pour la salle informatique, les vidéoprojecteurs et "
         "les écrans (enveloppe 10 M FCFA), remis avant décaissement de la tranche équipements."),
        ("Pièce n° 12 - Plan de communication et devis médias",
         "Plan de communication 2026-2027 (document joint) : budget 15 M FCFA sur 12 mois - digital, "
         "radio, presse, affichage, terrain et phoning - avec devis des régies et prestataires à "
         "joindre avant décaissement de la tranche communication."),
        ("Pièce n° 13 - Attestations fiscales et sociales",
         "Attestations à jour de la Direction Générale des Impôts et de la Caisse Nationale de "
         "Sécurité Sociale."),
        ("Pièce n° 14 - Bulletins de salaire du fondateur",
         "Bulletins de salaire et attestation d'employeur de M. Serge Patrick MINANG, fonctionnaire "
         "du Ministère des Travaux Publics (env. 8 M FCFA/an), ressource complémentaire non intégrée au "
         "calcul du DSCR."),
        ("Pièce n° 15 - CV du fondateur et de l'équipe",
         "Curriculum vitae du fondateur (ingénieur, MBA, doctorant DBA) et des principaux "
         "collaborateurs, dont le responsable administratif et les deux commerciaux recruteurs "
         "financés par le crédit."),
        ("Pièce n° 16 - Actionnariat",
         "Répartition du capital : M. MINANG (60 %), Mme Blandine ENGONGA, épouse (15 %), et les "
         "cinq enfants (5 % chacun). Actionnariat familial intégral."),
    ]
    for title, body in fiches:
        st += [P(f"<b>{title}</b>", "cellb"), P(body, "cell"), Spacer(1, 3)]

    st += section("3. Reporting proposé pendant la durée du crédit")
    st += [P("- Reporting trimestriel : effectifs par filière, CA encaissé, principaux postes de "
             "charges, avancement des travaux puis occupation du bâtiment.", "cell"),
           P("- États financiers annuels transmis à Ecobank dans les 4 mois de la clôture.", "cell"),
           P("- Point annuel de gestion avec le chargé d'affaires Ecobank.", "cell"),
           P("- Communication immédiate de tout événement significatif (litige, autorisation, "
             "changement de gouvernance).", "cell"),
           Spacer(1, 10),
           P("Fait à Libreville, le 30 août 2026", "small"),
           P("<b>Serge Patrick MINANG</b><br/>Président-Fondateur - Université Privée de Libreville", "bodyc")]
    doc = Doc(OUT[2], "UPL - Annexes juridiques - dossier 260 M FCFA - V12")
    doc.build(st)
    return doc

# ================================================================ DOC 4
def build_master_plan():
    st = []
    st += [P("Vision stratégique long terme - horizon 2028-2035", "kicker"),
           P("Master Plan Campus UPL", "h1"),
           P("Enveloppe indicative : env. 3 500 000 000 FCFA - financement multi-acteurs par tranches "
             "successives - Libreville, août 2026", "body"), Spacer(1, 6)]

    st += section("1. Vision du fondateur")
    st += [P("La vocation de l'UPL est de devenir à terme une référence universitaire privée du "
             "Gabon et d'Afrique centrale. Ce Master Plan traduit cette vocation en un programme "
             "d'aménagement, de construction et d'équipement à l'échelle d'un campus universitaire "
             "complet de 2 hectares, à horizon 5 à 10 ans."),
           P("Il s'appuie sur une première étape immédiate : le <b>bâtiment pédagogique R+2 de "
             "504 m2</b> financé par le crédit de 260 M FCFA sollicité aujourd'hui, qui porte "
             "immédiatement la capacité d'accueil à environ 400 étudiants par jour et préfigure le "
             "campus. La rentrée 2026-2027 démarre dans les locaux actuels de Sablière, puis "
             "bascule dans le nouveau bâtiment livré sous 2 mois.")]

    st += section("2. La tranche immédiate - bâtiment pédagogique R+2 (crédit 260 M FCFA)")
    st += [styled_table([
        [P("Caractéristique", "cellb"), P("Détail", "cellb")],
        [P("Programme", "cell"), P("Bâtiment universitaire R+2 d'environ 504 m2 : 9 salles de cours climatisées et meublées, blocs sanitaires par niveau, salles techniques et numériques, galeries de circulation, aménagements extérieurs")],
        [P("Structure", "cell"), P("Ossature acier S275 (métré optimisé 47 kg/m2), platelage structural, façades largement vitrées, conforme aux études d'exécution")],
        [P("Coût", "cell"), P("219 972 060 FCFA TTC - devis négocié MATRIX GROUP (révision n° 2, -46,3 % sur la proposition initiale de 409,7 M FCFA TTC)")],
        [P("Délai", "cell"), P("2 mois maximum en cadence renforcée ; réception partielle (tranche A - RDC) à 6 semaines pour accueillir les cours dès la rentrée")],
        [P("Capacité", "cell"), P("env. 400 étudiants/jour en 2 rotations - premier palier de 300 étudiants, horizon 500 avec le campus complet")],
        [P("Financement", "cell"), P("Crédit d'investissement Ecobank 260 M FCFA : bâtiment (220 M) + équipements IT (10 M) + communication (15 M) + équipe (5 M) + fonds de roulement (10 M)")],
    ], [3.4*cm, 13.8*cm], header=False, zebra=False,
        extra=[("BACKGROUND", (0, 0), (0, -1), BLUE_LT), ("VALIGN", (0, 0), (-1, -1), "TOP")])]

    st += section("3. Programme immobilier long terme - 23 postes (env. 3,5 Md FCFA)")
    posts = [
        ("Terrain (2 ha)", 150), ("Frais fonciers, notariés, taxes", 15),
        ("Préparation du site (nivellement, terrassement)", 45),
        ("Voiries et parkings", 100), ("Clôture et sécurisation périmétrique", 30),
        ("Réseaux (eau, assainissement, télécoms)", 75),
        ("Raccordement et distribution électrique", 65),
        ("Installation solaire (autonomie partielle)", 60), ("Groupe électrogène", 40),
        ("Bâtiment A - Enseignement (Licence/Master)", 400),
        ("Bâtiment B - Enseignement (MBA/DBA/Executive)", 400),
        ("Amphithéâtre 300 places", 280), ("Bibliothèque universitaire", 180),
        ("Centre d'Intelligence Artificielle", 160),
        ("Laboratoires (numérique, économie bleue)", 110),
        ("Bâtiment administratif", 130), ("Centre d'orientation et carrière", 65),
        ("Salle de conférences 200 places", 140), ("Cafétéria / restauration", 90),
        ("Espaces vie étudiante", 115), ("Résidence étudiante (30 chambres)", 260),
        ("Mobilier et équipements pédagogiques", 250),
        ("Imprévus et honoraires (études, MOE)", 340),
    ]
    half = 12
    left = posts[:13]; right = posts[13:] + [("", 0)]
    rows = []
    for (a, va), (b, vb) in zip(left, right):
        rows.append([P(a, "cell"), P(f"{va}", "cellr") if va else "",
                     P(b, "cell") if b else "", P(f"{vb}", "cellr") if vb else ""])
    st += [styled_table([[P("Poste", "cellb"), P("M FCFA", "cellrb"), P("Poste", "cellb"), P("M FCFA", "cellrb")]] + rows,
                        [5.6*cm, 1.6*cm, 5.9*cm, 1.6*cm], fontsize=7.6),
           P("Hypothèses : foncier env. 7 500 FCFA/m2 en périphérie de Libreville (fourchette 3 000 à "
             "15 000 F) ; construction env. 400 000 FCFA/m2 ; imprévus et honoraires env. 10 %. Montants "
             "indicatifs, à préciser lors des études techniques préalables.", "note")]

    st += section("4. Découpage en tranches")
    st += [styled_table([
        [P("Tranche", "cellb"), P("Périmètre", "cellb"), P("Enveloppe indicative", "cellrb")],
        [P("Tranche 0 (2026 - en cours)", "cell"),
         P("Bâtiment pédagogique R+2 de 504 m2 sur Libreville - financé par le crédit 260 M FCFA - livré sous 2 mois", "cell"),
         P("220 M FCFA", "cellr")],
        [P("Tranche 1 (années 1-2)", "cell"),
         P("Foncier, VRD, Bâtiment A, réseaux, énergie", "cell"), P("env. 1 000 M FCFA", "cellr")],
        [P("Tranche 2 (années 3-4)", "cell"),
         P("Bâtiment B, amphithéâtre, bibliothèque, administration", "cell"), P("env. 1 200 M FCFA", "cellr")],
        [P("Tranche 3 (années 5-6)", "cell"),
         P("Laboratoires, Centre IA, vie étudiante, résidence", "cell"), P("env. 900 M FCFA", "cellr")],
        [P("Tranche 4 (finalisation)", "cell"),
         P("Équipements, mobilier, aménagements complémentaires", "cell"), P("env. 400 M FCFA", "cellr")],
    ], [3.6*cm, 10.0*cm, 3.6*cm],
        extra=[("BACKGROUND", (0, 1), (-1, 1), GOLD_LT)])]

    st += section("5. Stratégie de financement multi-acteurs")
    st += [styled_table([
        [P("Source de financement", "cellb"), P("Rôle envisagé", "cellb"), P("Part indicative", "cellrb")],
        [P("Autofinancement UPL (CAF cumulée)", "cell"), P("Apport propre", "cell"), P("env. 10 %", "cellr")],
        [P("Pool bancaire gabonais (Ecobank, BGFI, BICIG, UGB, BOA)", "cell"), P("Financement long terme structuré", "cell"), P("env. 40 %", "cellr")],
        [P("Bailleurs de développement (BOAD, BDEAC, IFC, Proparco, AFD)", "cell"), P("Financement concessionnel long terme", "cell"), P("env. 35 %", "cellr")],
        [P("Investisseurs stratégiques et partenaires académiques", "cell"), P("Prise de participation ou apports en compte courant", "cell"), P("env. 10 %", "cellr")],
        [P("Subventions publiques et mécénat", "cell"), P("Cofinancement d'équipements", "cell"), P("env. 5 %", "cellr")],
    ], [6.4*cm, 7.6*cm, 3.2*cm])]

    st += section("6. Feuille de route indicative")
    st += [styled_table([
        [P("Horizon", "cellb"), P("Étape", "cellb")],
        [P("2026", "cell"), P("Tranche 0 : crédit 260 M FCFA - construction du bâtiment R+2 en 2 mois, équipement, campagne de communication, rentrée des six filières")],
        [P("2027", "cell"), P("Consolidation institutionnelle et financière ; remboursement du crédit selon échéancier ; identification foncière ; premiers contacts partenaires")],
        [P("2028", "cell"), P("Structuration juridique et financière du campus ; études de faisabilité ; recherche de terrain")],
        [P("2029", "cell"), P("Acquisition foncière ; permis de construire ; bouclage du financement Tranche 1")],
        [P("2030-2031", "cell"), P("Construction Tranche 1 (Bâtiment A, VRD, réseaux, énergie)")],
        [P("2032-2033", "cell"), P("Livraison Tranche 1 ; mise en service partielle ; lancement Tranche 2")],
        [P("2034-2035", "cell"), P("Construction Tranches 2 et 3 ; ouverture progressive du campus complet")],
    ], [2.6*cm, 14.6*cm])]

    st += section("7. Positionnement par rapport au crédit de 260 M FCFA")
    st += [P("Le crédit de 260 000 000 FCFA sollicité auprès d'Ecobank porte sur le développement "
             "immédiat 2026-2027 : construction du bâtiment pédagogique R+2 (219,97 M FCFA TTC, "
             "devis négocié), équipements informatiques, plan de communication de lancement et "
             "renforcement de l'équipe. Il finance la « Tranche 0 » du campus et est intégralement "
             "couvert par les capacités d'exploitation de l'établissement (DSCR prudent supérieur à 1,3 x)."),
           P("Le Master Plan Campus (env. 3,5 Md FCFA) est un projet distinct, à horizon 5 à 10 ans, "
             "qui ne conditionne ni ne dépend du remboursement du crédit sollicité. Il est présenté "
             "à la banque à titre informatif, pour positionner la trajectoire de l'établissement et "
             "la relation bancaire durable recherchée.")]

    st += section("8. Illustration du futur campus")
    st += [P("Un environnement moderne, stimulant et connecté pour former les leaders de demain : "
             "salles de cours, salle informatique, bibliothèque / learning center, vie de campus, "
             "amphithéâtre. Formations : Économie Bleue, Gestion Portuaire et Développement Durable "
             "· Économie Numérique et Intelligence Artificielle · Droit et Sciences Politiques · "
             "Gouvernance, Leadership et Management · École d'Assurance Maladie et de Sécurité "
             "Sociale · CPGE · Executive MBA · DBA. Illustration non contractuelle - à caractère "
             "prospectif.", "bodyc"),
           Spacer(1, 10),
           P("Fait à Libreville, le 30 août 2026", "small"),
           P("<b>Serge Patrick MINANG</b><br/>Président-Fondateur - Université Privée de Libreville", "bodyc")]
    doc = Doc(OUT[3], "UPL - Master Plan Campus - tranche 0 financée par le crédit 260 M - V12")
    doc.build(st)
    return doc

if __name__ == "__main__":
    print(f"Mensualité régime : {fmt(MENS)} FCFA | intérêts totaux env. {M(TOTAL_INT/1e6)} M | coût total env. {M(TOTAL_PAID/1e6)} M")
    print("CA   :", [M(v) for v in CA])
    print("CAF  :", [M(v) for v in CAF])
    print("SERV :", [M(v) for v in SERV])
    print("DSCR :", DSCR)
    assert min(d for d in DSCR[1:6] if d) >= 1.30
    ds = [build_dossier(), build_annexes_fin(), build_annexes_jur(), build_master_plan()]
    for path, d in zip(OUT, ds):
        print("OK", os.path.basename(path), "-", d.page, "pages")
