#!/usr/bin/env python3
"""Génère le pack Facebook UPL (hors site public)."""
from pathlib import Path
from PIL import Image
from fpdf import FPDF

ROOT = Path(__file__).resolve().parents[3]
PACK = Path(__file__).resolve().parent
VIS = ROOT / "docs/com/visuels"
LOGO = ROOT / "assets/img/logo-upl.png"
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONTB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONTS = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
NAVY = (11, 42, 91)
GOLD = (201, 162, 39)

POSTS = [
    {
        "id": "01-preinscriptions",
        "img": "01-preinscriptions-carre.png",
        "title": "Pré-inscriptions 2026-2027",
        "caption": """Université Privée de Libreville — pré-inscriptions 2026-2027

Licence · Master · CPGE · Executive MBA · DBA

La pré-inscription est gratuite et sans engagement. Le secrétariat vous rappelle pour les modalités et les places disponibles.

Executive MBA : inscriptions ouvertes depuis 2022.

Site : https://upl-gabon.com
E-mail : contact@upl-gabon.com
Tél. : +241 02 62 19 78 · +241 07 35 95 72
Sablière, Libreville""",
        "pdf_lines": [
            "Pré-inscriptions 2026-2027",
            "Licence · Master · CPGE · Executive MBA · DBA",
            "",
            "La pré-inscription est gratuite et sans engagement.",
            "Le secrétariat vous rappelle pour les modalités",
            "et les places disponibles.",
            "",
            "Executive MBA : inscriptions ouvertes depuis 2022.",
        ],
    },
    {
        "id": "02-licence1",
        "img": "02-licence1-carre.png",
        "title": "Licence 1",
        "caption": """Licence 1 — Université Privée de Libreville

Droits de scolarité 2026-2027 :
• 1 000 000 FCFA pour les 50 premières inscriptions
• 1 200 000 FCFA ensuite

Frais d'inscription exigibles au dépôt du dossier : 200 000 FCFA (50 premières) ou 300 000 FCFA (inscriptions normales). Solde en 6 tranches. Un reçu est délivré pour tout paiement.

Pré-inscription gratuite, sans engagement — places limitées.

https://upl-gabon.com
contact@upl-gabon.com
+241 02 62 19 78 · +241 07 35 95 72""",
        "pdf_lines": [
            "Licence 1 — droits de scolarité 2026-2027",
            "",
            "1 000 000 FCFA — 50 premières inscriptions",
            "1 200 000 FCFA — inscriptions normales",
            "",
            "Frais d'inscription au dépôt du dossier :",
            "200 000 FCFA (50 premières) ou 300 000 FCFA.",
            "Solde en 6 tranches. Reçu pour tout paiement.",
        ],
    },
    {
        "id": "03-mba",
        "img": "03-mba-carre.png",
        "title": "Executive MBA",
        "caption": """Executive MBA — Université Privée de Libreville

Programme ouvert depuis 2022, à Libreville, avec l'appui académique de l'Université de Douala.

• Public : cadres et dirigeants en activité
• Cours du soir, 17h–21h, Sablière
• Promotion d'environ 20 auditeurs
• Près de 80 cadres formés
• Scolarité : 4 000 000 FCFA l'année, payable en tranches (jusqu'à huit échéances)

Candidature : CV, parcours et diplômes
contact@upl-gabon.com — objet « Candidature MBA »

https://upl-gabon.com/mba.html""",
        "pdf_lines": [
            "Executive MBA — ouvert depuis 2022",
            "",
            "Cadres et dirigeants en activité.",
            "Cours du soir 17h–21h, Sablière.",
            "Promotion d'environ 20 auditeurs.",
            "Près de 80 cadres formés.",
            "Appui académique : Université de Douala.",
            "",
            "Scolarité : 4 000 000 FCFA l'année,",
            "payable en tranches (jusqu'à huit échéances).",
        ],
    },
    {
        "id": "04-tarifs",
        "img": "04-tarifs-carre.png",
        "title": "Droits de scolarité",
        "caption": """Droits de scolarité — rentrée 2026-2027

Licence 1     1 000 000 FCFA (50 premières) / 1 200 000 FCFA
Master 1      1 500 000 FCFA
Master 2      2 000 000 FCFA
CPGE          2 200 000 FCFA
Executive MBA 4 000 000 FCFA (ouvert depuis 2022)
DBA           Sur dossier

Pré-inscriptions : gratuites, sans engagement.
Paiement en tranches selon la formation. Reçu à chaque versement.
Airtel Money : conservez le justificatif — la confirmation de l'UPL est indispensable.

https://upl-gabon.com
contact@upl-gabon.com""",
        "pdf_lines": [
            "Droits de scolarité 2026-2027",
            "",
            "Licence 1     1 000 000 FCFA (50 premières)",
            "              / 1 200 000 FCFA",
            "Master 1      1 500 000 FCFA",
            "Master 2      2 000 000 FCFA",
            "CPGE          2 200 000 FCFA",
            "Executive MBA 4 000 000 FCFA",
            "DBA           Sur dossier",
        ],
    },
    {
        "id": "05-poles",
        "img": "06-poles-carre.png",
        "title": "Cinq pôles",
        "caption": """Les formations de la rentrée 2026-2027 s'organisent autour de cinq pôles, plus les classes préparatoires :

1. Gouvernance, Leadership et Management
2. Économie Numérique et Intelligence Artificielle
3. Économie Bleue, Gestion Portuaire et Développement Durable
4. Droit et Sciences Politiques
5. Assurance Maladie et Sécurité Sociale
+ Classes préparatoires aux Grandes Écoles (CPGE)

Pré-inscriptions ouvertes. Places limitées.

https://upl-gabon.com""",
        "pdf_lines": [
            "Cinq pôles d'enseignement",
            "",
            "1. Gouvernance, Leadership et Management",
            "2. Économie Numérique et Intelligence Artificielle",
            "3. Économie Bleue, Gestion Portuaire",
            "    et Développement Durable",
            "4. Droit et Sciences Politiques",
            "5. Assurance Maladie et Sécurité Sociale",
            "+ Classes préparatoires (CPGE)",
        ],
    },
    {
        "id": "06-contact",
        "img": "05-contact-story.png",
        "title": "Contact",
        "caption": """Pré-inscription 2026-2027 — trois étapes

1. Écrire à contact@upl-gabon.com (objet « Pré-inscription 2026-2027 »)
   Nom, téléphone, formation souhaitée, dernier diplôme.
2. Le secrétariat vous rappelle et vous remet la liste des pièces.
3. Après validation du profil : inscription et règlement auprès du secrétariat.

La pré-inscription est gratuite et sans engagement.

Tél. : +241 02 62 19 78 · +241 07 35 95 72
Sablière, Libreville
https://upl-gabon.com""",
        "pdf_lines": [
            "Nous écrire",
            "",
            "contact@upl-gabon.com",
            "+241 02 62 19 78",
            "+241 07 35 95 72",
            "",
            "Sablière, Libreville",
            "https://upl-gabon.com",
        ],
    },
]


def cover():
    src = Image.open(PACK / "couverture-source.png").convert("RGB")
    # Facebook cover recommended 1640 × 624
    out = src.resize((1640, 624), Image.Resampling.LANCZOS)
    out.save(PACK / "couverture-facebook-1640x624.jpg", quality=92, optimize=True)
    src.save(PACK / "couverture-facebook.png")


def make_pdf(post, dest: Path):
    pdf = FPDF(format="A4", unit="mm")
    pdf.set_auto_page_break(auto=True, margin=18)
    pdf.add_page()
    pdf.add_font("DejaVu", "", FONT)
    pdf.add_font("DejaVu", "B", FONTB)
    pdf.add_font("DejaVuS", "", FONTS)
    pdf.set_fill_color(*NAVY)
    pdf.rect(0, 0, 210, 42, "F")
    pdf.set_fill_color(*GOLD)
    pdf.rect(0, 42, 210, 1.6, "F")
    if LOGO.exists():
        pdf.image(str(LOGO), 12, 7, h=28)
    pdf.set_xy(48, 10)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("DejaVu", "B", 13)
    pdf.cell(0, 8, "Université Privée de Libreville", new_x="LMARGIN", new_y="NEXT")
    pdf.set_x(48)
    pdf.set_font("DejaVu", "", 10)
    pdf.set_text_color(*GOLD)
    pdf.cell(0, 6, "Excellence  ·  Innovation  ·  Leadership")
    pdf.set_y(52)
    pdf.set_text_color(*NAVY)
    pdf.set_font("DejaVuS", "", 18)
    pdf.multi_cell(0, 9, post["title"])
    pdf.set_fill_color(*GOLD)
    pdf.rect(10, pdf.get_y() + 1, 40, 0.8, "F")
    pdf.ln(8)
    pdf.set_font("DejaVu", "", 12)
    pdf.set_text_color(20, 20, 20)
    for line in post["pdf_lines"][1:]:
        pdf.set_x(12)
        pdf.multi_cell(186, 7, line)
    img = VIS / post["img"]
    if img.exists():
        y = pdf.get_y() + 6
        # keep visual on page
        if y < 180:
            pdf.image(str(img), x=55, y=y, w=100)
    pdf.set_y(272)
    pdf.set_fill_color(*NAVY)
    pdf.rect(0, 275, 210, 22, "F")
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("DejaVu", "", 9)
    pdf.set_xy(12, 280)
    pdf.cell(0, 5, "contact@upl-gabon.com   ·   +241 02 62 19 78   ·   upl-gabon.com")
    pdf.set_xy(12, 286)
    pdf.set_text_color(*GOLD)
    pdf.cell(0, 5, "Sablière, Libreville  ·  Pré-inscription gratuite, sans engagement")
    pdf.output(str(dest))


def main():
    out_img = PACK / "posts"
    out_pdf = PACK / "pdf"
    out_txt = PACK / "textes"
    for d in (out_img, out_pdf, out_txt):
        d.mkdir(exist_ok=True)
    cover()
    for p in POSTS:
        src = VIS / p["img"]
        if src.exists():
            im = Image.open(src).convert("RGB")
            im.save(out_img / f"{p['id']}.jpg", quality=90, optimize=True)
        (out_txt / f"{p['id']}.txt").write_text(p["caption"].strip() + "\n", encoding="utf-8")
        make_pdf(p, out_pdf / f"{p['id']}.pdf")
    readme = PACK / "00-PUBLIER.txt"
    readme.write_text(
        """UPL — pack Facebook (page neuve)
================================
Site upl-gabon.com NON modifié.
Anciennes pages agences : ignorées.

1. COUVERTURE (tout de suite)
   Remplacer la bannière « 66 ans / indépendance » par :
   couverture-facebook-1640x624.jpg
   (Photo de profil : garder le logo UPL)

2. PUBLICATIONS (image JPG + coller le texte .txt)
   Ordre, pas tout le même jour :
   a) 01-preinscriptions  → épingler en haut de la Page
   b) 02-licence1
   c) 03-mba
   d) 04-tarifs
   e) 05-poles
   f) 06-contact

   Les PDF (dossier pdf/) : à joindre en document si besoin.
   Facebook met mieux en avant les JPG.

3. NE PAS PUBLIER (Drive)
   Dossier Ecobank / 80 M / annexes bancaires
   Cours complets MBA (sauf extrait autorisé plus tard)
   Facture Namecheap
   Vidéo Rentrée 2024

4. Films TV autorisés (lien YouTube, pas de fichier)
   https://youtu.be/jh_iCTJuLKA
   https://youtu.be/FAKHfv8nN7I
""",
        encoding="utf-8",
    )
    print("pack built", PACK)


if __name__ == "__main__":
    main()
