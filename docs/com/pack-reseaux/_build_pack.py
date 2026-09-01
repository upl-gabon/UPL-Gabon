#!/usr/bin/env python3
"""Pack visuels réseaux UPL — blanc · or · bleu léger (campagne 2026-2027).

    /tmp/fv/bin/python docs/com/pack-reseaux/_build_pack.py
    (venv : python3 -m venv /tmp/fv && /tmp/fv/bin/pip install pillow)

Le contenu n'est jamais recopié ici : il vient de docs/com/flyers/data/flyers.json
lui-même généré depuis assets/js/config.js (npm run flyers:data). Les légende/postes
suivent les textes validés de docs/com/pack-facebook/textes/.

L'emblème du dépôt (assets/img/logo-upl.png) ne fait que 256x163 px : il est **redessiné
en vectoriel** (mêmes motifs : lauriers or, bonnet bleu, livre ouvert, 3 étoiles) pour
rester net de 500 px à 1640 px.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent / "2026-09"
DATA = json.loads((ROOT / "docs/com/flyers/data/flyers.json").read_text(encoding="utf-8"))

F = "/usr/share/fonts/truetype/dejavu"
SERIF, SERIF_B = f"{F}/DejaVuSerif.ttf", f"{F}/DejaVuSerif-Bold.ttf"
SANS, SANS_B = f"{F}/DejaVuSans.ttf", f"{F}/DejaVuSans-Bold.ttf"

BLANC = (255, 255, 255)
IVOIRE = (250, 251, 253)
BLEU_LEGER = (232, 240, 250)
BLEU_FILET = (205, 222, 242)
OR = (201, 162, 39)
OR_PALE = (233, 211, 138)
BLEU_BONNET = (43, 143, 214)
BLEU_BONNET_F = (24, 116, 189)
NUIT = (11, 42, 91)
ENCRE = (26, 38, 58)
GRIS = (92, 105, 125)

_font_cache = {}


def font(path, size):
    key = (path, int(size))
    if key not in _font_cache:
        _font_cache[key] = ImageFont.truetype(path, int(size))
    return _font_cache[key]


# ---------------------------------------------------------------- primitives
class Sheet:
    """Canevas + draw, avec un texte centré qui respecte l'interlettrage."""

    def __init__(self, w, h, bg=BLANC):
        self.im = Image.new("RGBA", (int(w), int(h)), bg)
        self.d = ImageDraw.Draw(self.im, "RGBA")
        self.w, self.h = int(w), int(h)

    def tw(self, txt, f, spacing=0):
        if not spacing:
            return self.d.textlength(txt, font=f)
        return sum(self.d.textlength(c, font=f) + spacing for c in txt) - spacing

    def txt(self, x, y, s, f, fill=ENCRE, spacing=0, cx=None, anchor="la"):
        if cx is not None:
            x = cx - self.tw(s, f, spacing) / 2
        if spacing:
            for ch in s:
                self.d.text((x, y), ch, font=f, fill=fill, anchor=anchor)
                x += self.d.textlength(ch, font=f) + spacing
        else:
            self.d.text((x, y), s, font=f, fill=fill, anchor=anchor)
        return y + int(f.size * 1.42)

    def para(self, x, y, s, f, fill, max_w, lh=1.42, cx=None):
        for para in s.split("\n"):
            line = ""
            for word in para.split(" "):
                trial = (line + " " + word).strip()
                if self.tw(trial, f) <= max_w or not line:
                    line = trial
                else:
                    y = self.txt(x, y, line, f, fill, cx=cx)
                    line = word
            y = self.txt(x, y, line, f, fill, cx=cx)
        return y

    def fit(self, s, path, max_w, max_size, min_size=16):
        size = int(max_size)
        while size > min_size:
            f = font(path, size)
            if all(self.tw(l, f) <= max_w for l in s.split("\n")):
                return f
            size -= 2
        return font(path, min_size)

    def rule(self, x0, y0, x1, y1, color=OR, width=3):
        self.d.line([(x0, y0), (x1, y1)], fill=color, width=width)

    def save(self, name):
        OUT.mkdir(parents=True, exist_ok=True)
        self.im.convert("RGB").save(OUT / name, "PNG", optimize=True)
        print(f"  {name:48s} {self.w}x{self.h}")


# ------------------------------------------------------------------ emblème
def star(dr, cx, cy, r, fill):
    pts = []
    for i in range(10):
        ang = math.radians(-90 + i * 36)
        rad = r if i % 2 == 0 else r * 0.45
        pts.append((cx + rad * math.cos(ang), cy + rad * math.sin(ang)))
    dr.polygon(pts, fill=fill)


def leaf(sheet, cx, cy, length, width, angle_deg, fill):
    """Feuille de laurier = ellipse allongée pivotée (base arrondie, pointe fine)."""
    pad = int(length + width) + 4
    im = Image.new("RGBA", (pad * 2, pad * 2), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    c = pad
    d.ellipse([c - length, c - width, c + length, c + width], fill=fill)
    d.polygon([(c + length, c), (c + length * 0.45, c - width * 0.95),
               (c + length * 0.45, c + width * 0.95)], fill=fill)
    im = im.rotate(-angle_deg, resample=Image.Resampling.BICUBIC, center=(c, c))
    sheet.im.alpha_composite(im, (int(cx - c), int(cy - c)))


def laurel_branch(sheet, cx, cy, s, side=1, fill=OR):
    """Branche de laurier en coupe : feuilles effilées le long d'une courbe, trait fin."""
    d = sheet.d
    pts = []
    for i in range(41):
        t = i / 40
        x = cx + side * (s * 0.30 + s * 0.56 * t - s * 0.10 * t * t)
        y = cy + s * 0.74 - s * 1.10 * t + s * 0.30 * t * t
        pts.append((x, y, t))
    d.line([(x, y) for x, y, _ in pts], fill=fill, width=max(2, int(s * 0.022)))
    for i in range(0, 40, 4):
        x, y, t = pts[i]
        x2, y2, _ = pts[min(i + 3, 40)]
        ang = math.degrees(math.atan2(-(y2 - y), (x2 - x) * side))
        ln = s * (0.24 - 0.07 * t)
        leaf(sheet, x, y, ln, ln * 0.30, ang + 34, fill)
        if i > 0:
            leaf(sheet, x, y, ln * 0.82, ln * 0.26, ang - 30, fill)
    x, y, t = pts[-1]
    leaf(sheet, x, y, s * 0.20, s * 0.06, 90 - 20 * side * side, fill)


def emblem(sheet, cx, cy, s):
    """Lauriers (fond), puis livre, bonnet et étoiles. s = demi-encombrement."""
    d = sheet.d
    for side in (-1, 1):
        laurel_branch(sheet, cx, cy, s, side=side)
    # livre ouvert, posé sous le bonnet
    by = cy + s * 0.46
    bw = s * 1.02
    for sign in (-1, 1):
        d.polygon([(cx + sign * bw / 2, by + s * 0.04), (cx + sign * s * 0.05, by - s * 0.10),
                   (cx + sign * s * 0.05, by + s * 0.20), (cx + sign * bw / 2, by + s * 0.34)], fill=OR)
        for k in range(3):
            d.line([(cx + sign * (s * 0.14 + k * s * 0.11), by - s * 0.01 + k * s * 0.05),
                    (cx + sign * (bw / 2 - s * 0.05), by + s * 0.08 + k * s * 0.065)],
                   fill=BLANC, width=max(2, int(s * 0.024)))
    # bonnet carré
    capy = cy - s * 0.14
    d.polygon([(cx, capy - s * 0.22), (cx + s * 0.52, capy), (cx, capy + s * 0.22),
               (cx - s * 0.52, capy)], fill=BLEU_BONNET)
    d.polygon([(cx - s * 0.23, capy + s * 0.08), (cx + s * 0.23, capy + s * 0.08),
               (cx + s * 0.18, capy + s * 0.30), (cx - s * 0.18, capy + s * 0.30)], fill=BLEU_BONNET_F)
    d.line([(cx + s * 0.42, capy + s * 0.02), (cx + s * 0.47, capy + s * 0.34)], fill=OR,
           width=max(2, int(s * 0.028)))
    d.ellipse([cx + s * 0.43, capy + s * 0.32, cx + s * 0.51, capy + s * 0.40], fill=OR)
    # étoiles
    for dx, dy in ((-s * 0.34, -s * 0.60), (0, -s * 0.70), (s * 0.34, -s * 0.60)):
        star(d, cx + dx, cy + dy, s * 0.125, OR)


def wordmark(sheet, cx, top, s, name_lines=("UNIVERSITÉ", "PRIVÉE DE LIBREVILLE"),
              tagline=True, color=NUIT, sub_color=BLEU_BONNET_F):
    y = top
    if name_lines:
        y = sheet.txt(0, y, name_lines[0], font(SANS_B, int(s * 0.50)), color, cx=cx)
        y = sheet.txt(0, y - int(s * 0.10), name_lines[1], font(SANS_B, int(s * 0.21)),
                      sub_color, spacing=s * 0.075, cx=cx)
        y += int(s * 0.10)
    if tagline:
        ft = font(SANS, int(s * 0.20))
        tag = "Excellence · Innovation · Leadership"
        half = sheet.tw(tag, ft) / 2 + s * 0.16        # filets hors du texte, jamais dessus
        sheet.rule(cx - half - s * 0.14, y + s * 0.13, cx - half, y + s * 0.13, OR, max(2, int(s * 0.03)))
        sheet.rule(cx + half, y + s * 0.13, cx + half + s * 0.14, y + s * 0.13, OR, max(2, int(s * 0.03)))
        sheet.txt(0, y, tag, ft, GRIS, cx=cx)
        y += int(s * 0.36)
    return y


def lockup(sheet, cx, top, s, name=True, tagline=True):
    emblem_h = s * 1.15
    emblem(sheet, cx, top + emblem_h * 0.55, s * 0.46)
    return wordmark(sheet, cx, top + emblem_h, s,
                    name_lines=("UNIVERSITÉ", "PRIVÉE DE LIBREVILLE") if name else None,
                    tagline=tagline)


# --------------------------------------------------------------------- gabarits
C = DATA["contact"]
CONTACT2 = [C["addressShort"], " · ".join(C["phones"]) + "   ·   " + C["email"]]


def contact_bar(sheet, y, h, bg=BLEU_LEGER, txt_color=NUIT, rule=OR, site=True):
    """Bandeau du bas : téléphones + e-mail à gauche, domaine à droite — jamais superposés."""
    d = sheet.d
    d.rectangle([0, y, sheet.w, sheet.h], fill=bg)
    d.rectangle([0, y, sheet.w, y + max(3, int(h * 0.012))], fill=rule)
    m = int(sheet.w * 0.055)
    pad = int(sheet.w * 0.03)
    site = C["siteShort"]
    size_site = int(sheet.w * 0.036)
    fs = font(SANS_B, size_site)
    if site:
        while sheet.tw(site, fs) > sheet.w * 0.26 and size_site > 18:
            size_site -= 2
            fs = font(SANS_B, size_site)
        site_w = sheet.tw(site, fs)
    else:
        site_w = 0
    maxw = sheet.w - 2 * m - site_w - pad
    f1s, f2s = int(sheet.w * 0.034), int(sheet.w * 0.030)
    l1 = " · ".join(C["phones"])
    while sheet.tw(l1, font(SANS_B, f1s)) > maxw and f1s > 16:
        f1s -= 1
    f1 = font(SANS_B, f1s)
    l2 = C["email"]
    while sheet.tw(l2, font(SANS, f2s)) > maxw and f2s > 15:
        f2s -= 1
    f2 = font(SANS, f2s)
    sheet.txt(m, y + h * 0.19, l1, f1, txt_color)
    sheet.txt(m, y + h * 0.55, l2, f2, txt_color)
    if site:
        sheet.txt(sheet.w - m, y + h * 0.34, site, fs, OR, anchor="ra")


def corners(sheet, m, color=OR, ln=None, width=4):
    ln = ln or int(sheet.w * 0.035)
    W, H = sheet.w, sheet.h
    for (x, y, sx, sy) in ((m, m, 1, 1), (W - m, m, -1, 1), (m, H - m, 1, -1), (W - m, H - m, -1, -1)):
        sheet.rule(x, y, x + sx * ln, y, color, width)
        sheet.rule(x, y, x, y + sy * ln, color, width)


# ---------------------------------------------------------------------- fichiers
def build_logos():
    for size, name in ((1024, "00-emblem-vectoriel-1024.png"), (512, "00-emblem-vectoriel-512.png")):
        sh = Sheet(size, size, (0, 0, 0, 0))
        emblem(sh, size / 2, size / 2, size * 0.30)
        sh.save(name)
    sh = Sheet(1200, 760, BLANC)
    lockup(sh, 600, 70, 150)
    sh.save("01-verrou-marque-blanc-1200x760.png")
    sh = Sheet(1200, 760, (11, 42, 91, 255))
    wordmark(sh, 600, 470, 150, color=BLANC, sub_color=OR_PALE, tagline=True)
    emblem(sh, 600, 250, 165)
    sh.save("02-verrou-marque-sur-bleu-1200x760.png")
    src = ROOT / "assets/img/logo-upl.png"
    if src.exists():
        o = Image.open(src).convert("RGB")
        o = o.resize((o.width * 4, o.height * 4), Image.Resampling.LANCZOS)
        o = o.filter(ImageFilter.UnsharpMask(radius=1.6, percent=90, threshold=2))
        o.save(OUT / "03-logo-original-256px-agrandi.png")
        print("  03-logo-original-256px-agrandi.png             1024x652  (netteté limitée : source 256 px)")


def avatar(w=1024, circle=False):
    sh = Sheet(w, w, BLANC if not circle else (0, 0, 0, 0))
    d = sh.d
    if circle:
        d.ellipse([20, 20, w - 20, w - 20], fill=BLANC)
        d.ellipse([20, 20, w - 20, w - 20], outline=OR, width=int(w * 0.012))
    else:
        d.rectangle([int(w * 0.05), int(w * 0.05), w - int(w * 0.05), w - int(w * 0.05)],
                    outline=BLEU_FILET, width=3)
        corners(sh, int(w * 0.05), OR, int(w * 0.055), 5)
    yend = lockup(sh, w / 2, w * 0.135, w * 0.155, name=True, tagline=True)
    sh.rule(w * 0.33, yend + w * 0.035, w * 0.67, yend + w * 0.035, OR, 4)
    sh.txt(0, yend + w * 0.058, "LIBREVILLE · GABON", font(SANS_B, int(w * 0.033)), GRIS,
           spacing=w * 0.013, cx=w / 2)
    return sh


def build_avatars():
    avatar(1024).save("10-avatar-carre-1024.png")
    a = avatar(500)
    a.im.resize((500, 500), Image.Resampling.LANCZOS).convert("RGB").save(OUT / "10-avatar-carre-500.png")
    print(f"  {'10-avatar-carre-500.png':48s} 500x500")
    avatar(1024, circle=True).save("11-avatar-cercle-1024.png")


def cover(w, h, campaign, title, sub, note, file_name):
    sh = Sheet(w, h, BLANC)
    d = sh.d
    left_w = w * 0.30
    d.rectangle([0, 0, left_w, h], fill=BLEU_LEGER)
    d.rectangle([left_w, 0, left_w + max(3, h * 0.008), h], fill=OR)
    lockup(sh, left_w / 2, h * 0.14, h * 0.150, name=True, tagline=True)
    x = left_w + w * 0.045
    maxw = int(w - x - w * 0.05)
    y = h * 0.14
    y = sh.txt(x, y, campaign.upper(), font(SANS_B, int(h * 0.042)), OR, spacing=h * 0.010)
    f = sh.fit(title, SERIF_B, maxw, int(h * 0.135), int(h * 0.062))
    y = sh.txt(x, y, title, f, NUIT)
    y += int(h * 0.02)
    sh.rule(x, y, x + maxw * 0.42, y, NUIT, max(2, int(h * 0.005)))
    y += int(h * 0.05)
    fs = sh.fit(sub, SERIF, maxw, int(h * 0.072), int(h * 0.045))
    y = sh.txt(x, y, sub, fs, ENCRE)
    fnote = sh.fit(note, SANS, maxw, int(h * 0.050), int(h * 0.030))
    y = sh.para(x, h * 0.70, note, fnote, GRIS, maxw)
    f = sh.fit(" · ".join(C["phones"]) + "   ·   " + C["email"] + "   ·   " + C["siteShort"],
               SANS_B, maxw, int(h * 0.052), int(h * 0.032))
    sh.txt(x, h * 0.855, " · ".join(C["phones"]) + "   ·   " + C["email"] + "   ·   " + C["siteShort"],
           f, NUIT)
    sh.save(file_name)


def build_covers():
    cover(1640, 624, "Campagne 2026-2027", "Pré-inscriptions 2026-2027",
          "Licence · Master · CPGE · Executive MBA · DBA",
          "Executive MBA ouvert depuis 2022 — appui académique de l'Université de Douala",
          "20-couverture-facebook-1640x624.png")
    cover(1584, 396, "Université Privée de Libreville", "Pré-inscriptions 2026-2027",
          "Licence · Master · CPGE · MBA · DBA", "Sablière, Libreville — Gabon",
          "21-couverture-linkedin-page-1584x396.png")
    cover(1500, 500, "Compte officiel réservé", "Université Privée de Libreville",
          "Libreville · Gabon", "upl-gabon.com",
          "22-couverture-x-1500x500.png")
    sh = Sheet(1584, 396, BLANC)
    sh.d.rectangle([0, 0, 1584, 396], fill=BLEU_LEGER)
    sh.d.rectangle([0, 330, 1584, 336], fill=OR)
    lockup(sh, 250, 60, 60, name=False, tagline=False)
    sh.txt(430, 108, "Secrétariat — Université Privée de Libreville", font(SERIF_B, 52), NUIT)
    sh.txt(430, 180, "Pré-inscriptions 2026-2027 · contact@upl-gabon.com · upl-gabon.com",
           font(SANS, 32), GRIS)
    sh.save("23-couverture-linkedin-profil-1584x396.png")


def post(file_name, kicker, title, lines, note="", w=1080, h=1350, table=False):
    sh = Sheet(w, h, BLANC)
    d = sh.d
    m = int(w * 0.07)
    mx = m + int(w * 0.025)
    d.rectangle([m, m, w - m, h - m - int(h * 0.135)], outline=BLEU_FILET, width=2)
    corners(sh, m, OR, int(w * 0.045), 4)
    lockup(sh, w / 2, int(h * 0.035), int(w * 0.058), name=True, tagline=False)
    y = int(h * 0.235)
    fk = sh.fit(kicker.upper(), SANS_B, w - 2 * m - int(w * 0.05), int(w * 0.030), int(w * 0.020))
    y = sh.para(mx, y, kicker.upper(), fk, OR, w - 2 * m - int(w * 0.05))
    y -= int(h * 0.012)
    f = sh.fit(title, SERIF_B, w - 2 * m - int(w * 0.06), int(w * 0.105), int(w * 0.05))
    y = sh.txt(mx, y, title, f, NUIT)
    y += int(h * 0.008)
    sh.rule(mx, y, m + int(w * 0.19), y, OR, 4)
    y += int(h * 0.028)
    if table:
        fb = font(SANS, int(w * 0.033))
        fp = font(SANS_B, int(w * 0.033))
        fb0, fp0 = font(SANS, int(w * 0.032)), font(SANS_B, int(w * 0.033))
        base_r, sub_r = int(w * 0.060), int(w * 0.040)
        rows_h = sum(base_r + (sub_r if sub else 0) for _, _, sub in lines)
        limit = h - int(h * 0.135) - (int(h * 0.085) if note else int(h * 0.02))
        if y + rows_h > limit:
            k = max(0.62, (limit - y) / rows_h)
            base_r, sub_r = int(base_r * k), int(sub_r * k)
        row_h = base_r
        for idx, (label, price, sub) in enumerate(lines):
            row_h = base_r + (sub_r if sub else 0)
            d.rectangle([mx, y - 6, w - m - int(w * 0.025), y + row_h],
                         fill=BLANC if idx % 2 == 0 else IVOIRE)
            sh.txt(mx + int(w * 0.015), y + int(base_r * 0.28), label, fb0, ENCRE)
            sh.txt(w - m - int(w * 0.045), y + int(base_r * 0.26), price, fp0, NUIT, anchor="ra")
            if sub:
                sh.txt(mx + int(w * 0.015), y + int(base_r * 0.95), sub, font(SANS, int(w * 0.0235)), GRIS)
            y += row_h
    else:
        fb = font(SANS, int(w * 0.036))
        ind = int(w * 0.028)
        for line in lines:
            y0 = y
            y = sh.para(mx + ind, y, line, fb, ENCRE, w - mx - m - ind)
            r = int(fb.size * 0.16)
            d.ellipse([mx, y0 + int(fb.size * 0.44) - r, mx + 2 * r, y0 + int(fb.size * 0.44) + r], fill=OR)
            y += int(h * 0.006)
    if note:
        fn = font(SANS, int(w * 0.0245))
        nl = 0
        for para in note.split("\n"):
            cur = ""
            for word in para.split(" "):
                trial = (cur + " " + word).strip()
                if sh.tw(trial, fn) <= w - 2 * m - int(w * 0.055) or not cur:
                    cur = trial
                else:
                    nl += 1; cur = word
            nl += 1
        while y + int(nl * fn.size * 1.34) > h - int(h * 0.135) - int(h * 0.045) and fn.size > 15:
            fn = font(SANS, fn.size - 1)
        sh.para(mx, y + int(h * 0.018), note, fn, GRIS, w - 2 * m - int(w * 0.055))
    contact_bar(sh, h - int(h * 0.135), int(h * 0.135))
    sh.save(file_name)


def build_posts():
    post("30-post-1080x1350-preinscriptions.png", "Libreville · depuis 2022", "Pré-inscriptions",
         ["Licence · Master · CPGE · Executive MBA · DBA",
          "Pré-inscription gratuite et sans engagement.",
          "Le secrétariat rappelle chaque candidat pour les pièces du dossier et les places disponibles."],
         note=DATA["copy"]["places"])
    post("31-post-1080x1350-licence1.png", "Rentrée 2026-2027", "Licence 1",
         DATA["copy"]["l1Lignes"],
         note="Un reçu est délivré pour tout paiement. Solde en 6 tranches — l'échéancier est remis par le secrétariat.")
    post("32-post-1080x1350-mba.png", "Depuis 2022 · appui Université de Douala", "Executive MBA",
         DATA["copy"]["mbaLignes"])
    post("33-post-1080x1350-poles.png", "Rentrée 2026-2027", "Cinq pôles d'enseignement",
         DATA["poles"])
    post("34-post-1080x1350-contact.png", "Se pré-inscrire", "Trois étapes",
         DATA["copy"]["etapes"],
         note="Écrire à contact@upl-gabon.com, objet « Pré-inscription 2026-2027 » — ou déposer le dossier au secrétariat, Sablière.")
    # grille tarifaire en tableau
    import re
    SHORT = {"Classes préparatoires aux Grandes Écoles (CPGE)": "CPGE — classes préparatoires",
             "Executive MBA": "Executive MBA", "Licence 1": "Licence 1"}
    rows = []
    for t in DATA["tarifs"]:
        amounts = [a.strip() for a in re.findall(r"[\d][\d   ]*FCFA", t["price"])]
        paren = re.findall(r"\(([^)]*)\)", t["price"])
        price = amounts[0] if amounts else t["price"]
        extra = amounts[1:]
        sub = " · ".join(paren + [("ensuite " + e) for e in extra])
        if t["id"] == "exec-mba":
            sub = (sub + " · " if sub else "") + "ouvert depuis 2022"
        rows.append((SHORT.get(t["label"], t["label"]), price, sub))
    post("35-post-1080x1350-tarifs-table.png", "Droits de scolarité annuels", "Grille 2026-2027",
         rows, note=DATA["copy"]["note"], table=True)


def build_stories():
    for name, kick, title, lines in (
        ("40-story-1080x1920-preinscriptions.png", "Campagne 2026-2027", "Pré-inscriptions",
         ["Licence · Master · CPGE", "Executive MBA · DBA", "Gratuit, sans engagement",
          "Le secrétariat vous rappelle"]),
        ("41-story-1080x1920-contact.png", "Secrétariat · Sablière", "Écrire à l'UPL",
         [C["email"], " · ".join(C["phones"]), "WhatsApp " + C["whatsappDisplay"], "upl-gabon.com"]),
    ):
        w, h = 1080, 1920
        sh = Sheet(w, h, BLANC)
        sh.d.rectangle([0, 0, w, int(h * 0.40)], fill=BLEU_LEGER)
        sh.d.rectangle([0, int(h * 0.40) - 8, w, int(h * 0.40)], fill=OR)
        lockup(sh, w / 2, int(h * 0.055), int(w * 0.082), name=True, tagline=True)
        y = int(h * 0.44)
        y = sh.txt(0, y, kick.upper(), font(SANS_B, int(w * 0.030)), OR, spacing=int(w * 0.010), cx=w / 2)
        f = sh.fit(title, SERIF_B, w - 160, int(w * 0.118), int(w * 0.07))
        y = sh.txt(0, y + 12, title, f, NUIT, cx=w / 2)
        sh.rule(w * 0.36, y + 14, w * 0.64, y + 14, OR, 5)
        y += 48
        for line in lines:
            fb = sh.fit(line, SANS, w - 190, int(w * 0.046), int(w * 0.030))
            y = sh.para(0, y, line, fb, ENCRE, w - 190, cx=w / 2)
            y += 12
        # encart bas, dans la zone sûre au-dessus de l'UI
        box = (int(w * 0.14), int(h * 0.775), int(w * 0.86), int(h * 0.845))
        sh.d.rectangle(box, fill=BLANC, outline=OR, width=4)
        sh.txt(0, int(h * 0.795), "upl-gabon.com", font(SANS_B, int(w * 0.046)), NUIT, cx=w / 2)
        sh.txt(0, int(h * 0.885), "Université Privée de Libreville — Sablière, Libreville (Gabon)",
               font(SANS, int(w * 0.026)), GRIS, cx=w / 2)
        sh.save(name)


def build_extras():
    w = 1080
    sh = Sheet(w, w, BLANC)
    sh.d.rectangle([0, 0, w, int(w * 0.30)], fill=BLEU_LEGER)
    sh.d.rectangle([0, int(w * 0.30) - 6, w, int(w * 0.30)], fill=OR)
    lockup(sh, w / 2, int(w * 0.04), int(w * 0.072), name=True, tagline=True)
    f = sh.fit("Pré-inscriptions 2026-2027", SERIF_B, w - 140, 76)
    sh.txt(0, int(w * 0.42), "Pré-inscriptions 2026-2027", f, NUIT, cx=w / 2)
    y = int(w * 0.50)
    for line in ["Licence · Master · CPGE · Executive MBA · DBA", "Gratuit, sans engagement — places limitées."]:
        y = sh.txt(0, y, line, font(SANS, 44), ENCRE, cx=w / 2)
    sh.txt(0, int(w * 0.68), C["email"], font(SANS_B, 46), OR, cx=w / 2)
    sh.d.rectangle([0, int(w * 0.845), w, w], fill=BLEU_LEGER)
    sh.d.rectangle([0, int(w * 0.845), w, int(w * 0.845) + 4], fill=OR)
    sh.txt(0, int(w * 0.895), " · ".join(C["phones"]), font(SANS_B, 40), NUIT, cx=w / 2)
    sh.save("50-whatsapp-carre-1080-preinscriptions.png")

    for name, t1, t2 in (("51-miniature-youtube-1280x720-presentation.png",
                         "L'UPL à la télévision", "Présentation institutionnelle"),
                        ("52-miniature-youtube-1280x720-mba.png",
                         "Executive MBA", "L'interview du programme, à Libreville")):
        w, h = 1280, 720
        sh = Sheet(w, h, BLANC)
        sh.d.rectangle([0, 0, int(w * 0.30), h], fill=BLEU_LEGER)
        sh.d.rectangle([int(w * 0.30), 0, int(w * 0.30) + 5, h], fill=OR)
        lockup(sh, int(w * 0.15), int(h * 0.16), int(h * 0.10), name=False, tagline=False)
        sh.txt(0, int(h * 0.66), "U.P.L", font(SANS_B, 34), NUIT, spacing=8, cx=int(w * 0.15))
        x = int(w * 0.36)
        sh.txt(x, int(h * 0.30), t1, sh.fit(t1, SERIF_B, w - x - 60, 72), NUIT)
        sh.txt(x, int(h * 0.30) + 96, t2, font(SANS, 40), GRIS)
        sh.rule(x, int(h * 0.30) + 82, x + int(w * 0.16), int(h * 0.30) + 82, OR, 4)
        sh.txt(x, int(h * 0.74), "Université Privée de Libreville · upl-gabon.com", font(SANS_B, 30), NUIT)
        sh.save(name)


def build_docs():
    (OUT / "MODE-EMPLOI.txt").write_text("""PACK RÉSEAUX UPL — blanc · or · bleu léger (campagne 2026-2027)
Généré par docs/com/pack-reseaux/_build_pack.py. Contenu repris de assets/js/config.js
via docs/com/flyers/data/flyers.json : aucun tarif recopié à la main.

OÙ METTRE CHAQUE FICHIER
  00-emblem-vectoriel-*.png .............. emblème redessiné, fond transparent (usage libre)
  01/02-verrou-marque-*.png .............. bloc de marque complet (emblème + UNIVERSITÉ + devise)
  03-logo-original-256px-agrandi.png ..... comparaison : le fichier du dépôt ne fait que 256 px
  10-avatar-carre-500 / 1024 ............. photo de profil : Facebook (Page), LinkedIn (Page + profil), X
  11-avatar-cercle-1024 .................. Instagram et TikTok (rognés en rond)
  20-couverture-facebook-1640x624 ........ couverture de la Page Facebook
  21-couverture-linkedin-page ............ bannière de la Page entreprise LinkedIn (1584x396)
  22-couverture-x ........................ compte X réservé (1500x500)
  23-couverture-linkedin-profil .......... bannière du profil de travail du secrétariat
  30 à 35-post-1080x1350 ................. publications fil Facebook / Instagram / LinkedIn (4:5)
  35-...-tarifs-table ..................... la grille en tableau : la plus lisible sur mobile
  40 / 41-story-1080x1920 ................ Story Instagram et Facebook, statut WhatsApp
  50-whatsapp-carre-1080 ................ envoi WhatsApp (conversation, listes de diffusion)
  51 / 52-miniature-youtube ............... miniatures des deux films TV (1280x720)

PALETTE
  blanc #FFFFFF · ivoire #FAFBFD · bleu léger #E8F0FA · filet #CDDEF2
  or #C9A227 · or pâle #E9D38A · bleu du bonnet #2B8FD6
  bleu nuit #0B2A5B : texte et filets uniquement, plus de grands aplats (demande du Président)

AVANT DE PUBLIER
  1. Faire valider les visuels avec les textes : pièces P1, P11 et P12 de docs/com/TEXTES_A_VALIDER.md.
  2. Fournir le logo en haute définition (SVG ou PNG >= 1200 px) : celui du dépôt fait 256x163 et ne
     tient pas l'impression. Le pack utilise un emblème redessiné en attendant — le jour où le vrai
     fichier vectoriel arrive, on remplace `emblem()` et on régénère tout.
  3. Photos réelles du campus / des promotions : les insérer dans la partie haute des posts 30 à 35,
     en gardant le bandeau de contact. Aucune image générée, aucun visage IA (règle du playbook).
  4. Un tarif qui bouge se corrige dans assets/js/config.js, puis `npm run flyers:data` et ce script.
     `npm test` casse si un flyer contredit le site.

ZONES SÛRES
  Stories et Reels : ~250 px libres en haut, ~320 px en bas (nom du compte, barre de réponse, bouton
  d'envoi). Les visuels 40/41 les respectent déjà.
  Facebook recadre les couvertures sur mobile : l'essentiel reste dans les 60 % centraux.

© Université Privée de Libreville — Sablière, Libreville (Gabon).
""", encoding="utf-8")
    (OUT / "palette.txt").write_text("\n".join(
        f"{n:<16}#{''.join(f'{c:02X}' for c in v)}" for n, v in [
            ("blanc", BLANC), ("ivoire", IVOIRE), ("bleu-leger", BLEU_LEGER), ("bleu-filet", BLEU_FILET),
            ("or", OR), ("or-pale", OR_PALE), ("bleu-bonnet", BLEU_BONNET), ("bleu-nuit", NUIT),
            ("encre", ENCRE), ("gris", GRIS)]), encoding="utf-8")
    print("  MODE-EMPLOI.txt + palette.txt")


if __name__ == "__main__":
    print("Pack réseaux UPL — blanc · or · bleu léger\n")
    build_logos()
    build_avatars()
    build_covers()
    build_posts()
    build_stories()
    build_extras()
    build_docs()
    print(f"\n{OUT}")
