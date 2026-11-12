#!/usr/bin/env python3
"""Assemble index.html (la page GitHub Pages) à partir de apps-script/Code.gs.

Code.gs contient toute la page dans la variable PAGE_HTML. Ce script la reprend
telle quelle et y ajoute seulement :
  - le titre et les balises meta que doGet() pose côté Apps Script ;
  - le pont web/pont.html, juste avant le script de l'appli.

À relancer après toute modification de apps-script/ ou web/ :  python3 build.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).parent
START = "var PAGE_HTML = "

lines = [l for l in (ROOT / "apps-script/Code.gs").read_text(encoding="utf-8").split("\n") if l.startswith(START)]
assert len(lines) == 1, "ligne PAGE_HTML introuvable dans Code.gs"
page = json.loads(lines[0][len(START):].rstrip().rstrip(";"))

# Ce que doGet() ajoute côté Apps Script, plus l'icône de l'appli.
HEAD = """
  <title>Suivi muscu</title>
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no, viewport-fit=cover">
  <meta name="mobile-web-app-capable" content="yes">
  <!-- Icône et installation sur l'écran d'accueil (propre à la version GitHub Pages). -->
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-title" content="Suivi muscu">
  <meta name="theme-color" content="#08090b">
  <link rel="apple-touch-icon" href="icons/icon-180.png">
  <link rel="icon" type="image/png" sizes="192x192" href="icons/icon-192.png">
  <link rel="manifest" href="manifest.webmanifest">"""

def insert(text, anchor, addition, before=False):
    assert text.count(anchor) == 1, f"repère introuvable ou en double : {anchor!r}"
    return text.replace(anchor, addition + anchor if before else anchor + addition)

out = insert(page, '<meta charset="utf-8">', HEAD)
out = insert(out, "<head>", "\n  <!-- Fichier généré par build.py : ne pas modifier à la main. -->")
out = insert(out, "  <script>", (ROOT / "web/pont.html").read_text(encoding="utf-8"), before=True)
(ROOT / "index.html").write_text(out, encoding="utf-8")
print("index.html généré")
