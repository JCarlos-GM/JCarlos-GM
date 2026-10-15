"""Genera assets/langs.svg con los lenguajes de TODOS los repos propios (públicos y privados).

Solo se publican porcentajes agregados: ningún nombre de repo ni cantidad de código.

Uso:  GITHUB_TOKEN=<token con scope repo> python scripts/build_langs.py
      (en local, si no hay GITHUB_TOKEN, usa `gh auth token`)
"""
import json
import os
import subprocess
import sys
import urllib.request
from collections import Counter

from build_assets import BLACK, DIM, GRAY, LINE, RED, WHITE, icon, svg, text, write

TOP = 6
SHADES = [RED, WHITE, "#c4c4c4", "#9a9a9a", "#707070", "#4d4d4d", "#2e2e2e"]
SLUGS = {
    "Python": "python", "TypeScript": "typescript", "Java": "openjdk", "JavaScript": "javascript",
    "C": "c", "C++": "cplusplus", "CSS": "css3", "HTML": "html5", "Shell": "gnubash",
}


def token():
    t = os.environ.get("GITHUB_TOKEN")
    if t:
        return t
    return subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, check=True).stdout.strip()


def get(url, tok):
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {tok}", "Accept": "application/vnd.github+json"})
    with urllib.request.urlopen(req) as r:
        return json.load(r)


def languages(tok):
    totals = Counter()
    seen = {"públicos": 0, "privados": 0}
    page = 1
    while True:
        repos = get(f"https://api.github.com/user/repos?affiliation=owner&per_page=100&page={page}", tok)
        if not repos:
            break
        for repo in repos:
            if not repo["fork"]:
                seen["privados" if repo["private"] else "públicos"] += 1
                totals.update(get(repo["languages_url"], tok))
        page += 1
    print(f"Repos analizados: {seen['públicos']} públicos, {seen['privados']} privados")
    return totals


def render(totals):
    total = sum(totals.values())
    top = totals.most_common(TOP)
    rows = [(name, n / total) for name, n in top]
    rest = 1 - sum(p for _, p in rows)
    if rest > 0.0005:
        rows.append(("Otros", rest))

    W, H = 495, 195
    b = [text(28, 38, "LENGUAJES", 12, RED, mono=True, weight=700, spacing=2),
         text(W - 28, 38, "públicos + privados", 11, DIM, mono=True, anchor="end")]

    # barra segmentada
    x, bw = 28, W - 56
    b.append(f'<clipPath id="bar"><rect x="28" y="56" width="{bw}" height="8" rx="4"/></clipPath><g clip-path="url(#bar)">')
    for i, (_, p) in enumerate(rows):
        w = bw * p
        b.append(f'<rect x="{x:.1f}" y="56" width="{w + 0.6:.1f}" height="8" fill="{SHADES[i]}"/>')
        x += w
    b.append("</g>")

    # leyenda en 2 columnas
    colw = (W - 56) / 2
    for i, (name, p) in enumerate(rows):
        cx = 28 + (i // 4) * colw
        cy = 96 + (i % 4) * 26
        b.append(f'<rect x="{cx}" y="{cy - 9}" width="8" height="8" fill="{SHADES[i]}" stroke="{LINE}"/>')
        slug = SLUGS.get(name)
        tx = cx + 18
        if slug:
            b.append(icon(slug, tx, cy - 12, 14, GRAY))
            tx += 22
        b.append(text(tx, cy, name, 13, WHITE))
        b.append(text(cx + colw - 22, cy, f"{p * 100:.1f}%", 12, GRAY, mono=True, anchor="end"))
    write("langs.svg", svg(W, H, "".join(b), "Lenguajes más usados (repos públicos y privados)", rx=10))


if __name__ == "__main__":
    try:
        tok = token()
    except Exception:
        print("Sin token (GITHUB_TOKEN o gh). No se regenera langs.svg.")
        sys.exit(0)
    render(languages(tok))
