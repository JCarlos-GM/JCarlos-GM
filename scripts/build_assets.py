"""Genera los SVG del perfil (assets/).

Uso:  python scripts/build_assets.py
Estilo: negro / blanco / rojo, línea fina, animación mínima.
"""
import math
import re
from pathlib import Path
from xml.sax.saxutils import escape as esc

OUT = Path(__file__).resolve().parent.parent / "assets"
OUT.mkdir(exist_ok=True)
ICONS = Path(__file__).resolve().parent / "icons"  # Simple Icons (CC0), viewBox 24×24

BLACK = "#0a0a0a"
PANEL = "#111111"
LINE = "#242424"
LINE2 = "#3a3a3a"
WHITE = "#f5f5f5"
GRAY = "#8c8c8c"
DIM = "#5c5c5c"
RED = "#e3262e"

SANS = "'Segoe UI','Helvetica Neue',Helvetica,Arial,sans-serif"
MONO = "'JetBrains Mono','Cascadia Code','SF Mono',Consolas,'Liberation Mono',monospace"


def svg(w, h, body, title, rx=14):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
        f'role="img" aria-label="{esc(title)}"><title>{esc(title)}</title>'
        f'<rect x=".5" y=".5" width="{w - 1}" height="{h - 1}" rx="{rx}" fill="{BLACK}" stroke="{LINE}"/>'
        f"{body}</svg>\n"
    )


def write(name, content):
    (OUT / name).write_text(content, encoding="utf-8")
    print(f"  assets/{name}  ({len(content) / 1024:.1f} KB)")


def text(x, y, s, size=14, fill=WHITE, mono=False, weight=400, anchor="start", spacing=0):
    fam = MONO if mono else SANS
    ls = f' letter-spacing="{spacing}"' if spacing else ""
    return (
        f'<text x="{x}" y="{y}" font-family="{fam}" font-size="{size}" font-weight="{weight}" '
        f'fill="{fill}" text-anchor="{anchor}"{ls}>{esc(s)}</text>'
    )


def icon(slug, x, y, size, fill):
    """Logo de Simple Icons incrustado como <path> (los SVG en <img> no cargan recursos externos)."""
    f = ICONS / f"{slug}.svg"
    if not f.exists():
        return f'<rect x="{x + size * .3:.1f}" y="{y + size * .3:.1f}" width="{size * .4:.1f}" height="{size * .4:.1f}" fill="none" stroke="{fill}"/>'
    d = re.search(r' d="([^"]+)"', f.read_text(encoding="utf-8")).group(1)
    return f'<path transform="translate({x:.1f} {y:.1f}) scale({size / 24:.4f})" d="{d}" fill="{fill}"/>'


def mover(path_id, dur, r=3, fill=RED, begin=0):
    return (
        f'<circle r="{r}" fill="{fill}"><animateMotion dur="{dur}s" begin="{begin}s" repeatCount="indefinite">'
        f'<mpath href="#{path_id}"/></animateMotion></circle>'
    )


def wave(x0, x1, y, amp, wl, step=6):
    pts = []
    x = x0
    while x <= x1 + 0.01:
        pts.append(f"{x:.0f},{y - amp * math.sin((x - x0) / wl * math.tau):.1f}")
        x += step
    return "L" + " L".join(pts)


# ── Hero ─────────────────────────────────────────────────────────────────
def hero():
    W, H = 1200, 380
    b = []
    # retícula de puntos (zona derecha)
    for gx in range(660, 1170, 24):
        for gy in range(48, 300, 24):
            b.append(f'<circle cx="{gx}" cy="{gy}" r="1" fill="#262626"/>')

    # circuito → onda
    y = 210
    d = f"M660,{y} H716 V150 H780 V{y} H820 " + wave(820, 1150, y, 34, 165)
    b.append(f'<path id="sig" d="{d}" fill="none" stroke="{WHITE}" stroke-width="1.5" stroke-linejoin="round"/>')
    for px, py in [(716, y), (716, 150), (780, 150), (780, y)]:
        b.append(f'<rect x="{px - 4}" y="{py - 4}" width="8" height="8" fill="{BLACK}" stroke="{WHITE}" stroke-width="1.5"/>')
    b.append(f'<rect x="652" y="{y - 8}" width="16" height="16" fill="{RED}"/>')
    b.append(mover("sig", 6, r=4))
    b.append(text(660, 270, "hardware", 12, DIM, mono=True))
    b.append(text(1150, 270, "software", 12, DIM, mono=True, anchor="end"))

    # texto
    b.append(text(64, 92, "FULL STACK  ·  IOT  ·  FIRMWARE", 13, RED, mono=True, spacing=2))
    b.append(text(60, 168, "Juan Carlos", 66, WHITE, weight=700, spacing=-1.5))
    b.append(
        f'<text x="60" y="240" font-family="{SANS}" font-size="66" font-weight="700" letter-spacing="-1.5" fill="{WHITE}">'
        f'Govea Magaña<tspan fill="{RED}">.</tspan></text>'
    )
    b.append(text(64, 284, "Ing. en Sistemas Computacionales · TecNM La Piedad", 17, GRAY))

    b.append(f'<line x1="60" y1="322" x2="1140" y2="322" stroke="{LINE}"/>')
    b.append(text(64, 350, "La Piedad, Michoacán — México", 12, DIM, mono=True))
    b.append(text(1140, 350, "nexaqua.com.mx   polenshoes.com   ressly.com.mx", 12, DIM, mono=True, anchor="end"))
    write("hero.svg", svg(W, H, "".join(b), "Juan Carlos Govea Magaña — Full Stack, IoT, Firmware"))


# ── Ecosistema NexAquA ───────────────────────────────────────────────────
def ecosystem():
    W, H = 1200, 470
    NW, NH = 196, 62
    top, bottom = 200, 370
    nodes = {
        "sens": (130, top, "Sensores", "válvulas en campo"),
        "esp": (365, top, "Nodos ESP32", "maestro / esclavo"),
        "mqtt": (600, top, "Broker MQTT", "TLS · ESP-NOW"),
        "api": (835, top, "API REST", "Node · Supabase"),
        "notif": (1070, top, "Alertas", "push · correo · Telegram"),
        "hmi": (250, bottom, "HMI Raspberry Pi", "táctil · gestos · voz"),
        "aria": (485, bottom, "ARIA", "asistente de voz"),
        "dash": (720, bottom, "Dashboard", "React · Recharts"),
        "app": (955, bottom, "App Android", "Java · Firebase"),
    }
    b = []
    b.append(text(40, 52, "NEXAQUA", 13, RED, mono=True, weight=700, spacing=2))
    b.append(text(140, 52, "flujo de datos", 13, GRAY, mono=True))
    b.append(f'<circle cx="1036" cy="48" r="4" fill="{RED}"><animate attributeName="opacity" values="1;.25;1" dur="2s" repeatCount="indefinite"/></circle>')
    b.append(text(1160, 52, "EN PRODUCCIÓN", 12, WHITE, mono=True, anchor="end", spacing=1.5))

    def h_link(a, c):
        (ax, ay, *_), (cx, cy, *_) = nodes[a], nodes[c]
        return f"M{ax + NW / 2},{ay} H{cx - NW / 2}"

    def v_link(a, c):
        (ax, ay, *_), (cx, cy, *_) = nodes[a], nodes[c]
        mid = (ay + NH / 2 + cy - NH / 2) / 2
        return f"M{ax},{ay + NH / 2} V{mid} H{cx} V{cy - NH / 2}"

    links = [h_link("sens", "esp"), h_link("esp", "mqtt"), h_link("mqtt", "api"), h_link("api", "notif"),
             v_link("mqtt", "hmi"), v_link("mqtt", "aria"), v_link("api", "dash"), v_link("api", "app")]
    for i, d in enumerate(links):
        b.append(f'<path id="l{i}" d="{d}" fill="none" stroke="{LINE2}" stroke-width="1.2"/>')
        b.append(mover(f"l{i}", 2.6, r=2.4, fill=WHITE, begin=-i * 0.4))

    # lazo de Defensa Activa
    sx, ex = nodes["esp"][0], nodes["sens"][0]
    ty = top - NH / 2
    loop = f"M{sx},{ty} V{ty - 46} H{ex} V{ty}"
    b.append(f'<path id="loop" d="{loop}" fill="none" stroke="{RED}" stroke-width="1.5"/>')
    b.append(f'<path d="M{ex - 5},{ty - 9} L{ex},{ty - 1} L{ex + 5},{ty - 9}" fill="none" stroke="{RED}" stroke-width="1.5"/>')
    b.append(mover("loop", 1.2, r=3.5))
    b.append(text((sx + ex) / 2, ty - 56, "Defensa Activa · cierre de válvula < 250 ms", 12, RED, mono=True, anchor="middle"))

    for key, (x, y, t, sub) in nodes.items():
        accent = RED if key == "esp" else LINE2
        b.append(f'<rect x="{x - NW / 2}" y="{y - NH / 2}" width="{NW}" height="{NH}" rx="6" fill="{PANEL}" stroke="{accent}"/>')
        b.append(text(x - NW / 2 + 18, y - 3, t, 16, WHITE, weight=600))
        b.append(text(x - NW / 2 + 18, y + 17, sub, 11.5, GRAY, mono=True))

    b.append(f'<line x1="40" y1="428" x2="1160" y2="428" stroke="{LINE}"/>')
    b.append(text(40, 452, "+ PCB propia en KiCad   + carcasa en Blender   + gemelo digital 3D del invernadero", 12, DIM, mono=True))
    write("nexaqua-flow.svg", svg(W, H, "".join(b), "Flujo de datos de NexAquA"))


# ── Tarjetas ─────────────────────────────────────────────────────────────
FLOWER = "".join(
    f'<ellipse cx="0" cy="-13" rx="6.5" ry="13" transform="rotate({a})" fill="none" stroke="{WHITE}" stroke-width="1.4"/>'
    for a in range(0, 360, 60)
) + f'<circle r="5" fill="{RED}"/>'

HOUSE = (
    f'<path d="M-22,0 L0,-20 L22,0" fill="none" stroke="{WHITE}" stroke-width="1.5" stroke-linejoin="round"/>'
    f'<path d="M-16,-5 V20 H16 V-5" fill="none" stroke="{WHITE}" stroke-width="1.5" stroke-linejoin="round"/>'
    f'<rect x="-5" y="6" width="10" height="14" fill="{RED}"/>'
)


def card(name, kicker, title, lines, stats, stack_lines, url, status, icon):
    W, H = 590, 430
    b = [f'<g transform="translate({W - 70} 72)">{icon}</g>']
    b.append(text(36, 52, kicker, 12, RED, mono=True, spacing=2))
    b.append(text(34, 100, title, 42, WHITE, weight=700, spacing=-1))
    y = 136
    for ln in lines:
        b.append(text(36, y, ln, 15, GRAY))
        y += 23
    y += 18
    b.append(f'<line x1="36" y1="{y}" x2="{W - 36}" y2="{y}" stroke="{LINE}"/>')
    colw = (W - 72) / len(stats)
    for i, (big, small) in enumerate(stats):
        x = 36 + i * colw
        if i:
            b.append(f'<line x1="{x:.0f}" y1="{y + 16}" x2="{x:.0f}" y2="{y + 64}" stroke="{LINE}"/>')
        pad = 0 if i == 0 else 18
        b.append(text(x + pad, y + 44, big, 22, WHITE, weight=700))
        b.append(text(x + pad, y + 64, small, 11, GRAY, mono=True))
    y += 82
    b.append(f'<line x1="36" y1="{y}" x2="{W - 36}" y2="{y}" stroke="{LINE}"/>')
    y += 32
    for ln in stack_lines:
        b.append(text(36, y, ln, 12.5, DIM, mono=True))
        y += 22
    b.append(f'<line x1="36" y1="{H - 68}" x2="{W - 36}" y2="{H - 68}" stroke="{LINE}"/>')
    b.append(f'<rect x="36" y="{H - 41}" width="7" height="7" fill="{GRAY}"/>')
    b.append(text(52, H - 34, status, 12, GRAY, mono=True))
    b.append(text(W - 36, H - 34, f"{url} →", 12.5, WHITE, mono=True, anchor="end"))
    write(name, svg(W, H, "".join(b), f"{title} — {kicker}"))


def cards():
    card(
        "card-polen.svg", "ECOMMERCE · GUATEMALA", "Polen",
        ["Tienda de sneakers y panel de administración", "para un cliente: catálogo, checkout con",
         "comprobante, envíos y devoluciones."],
        [("FEL", "factura SAT GT"), ("3 apps", "tienda/admin/API"), ("CI", "en cada push")],
        ["Next.js 15 / TypeScript / Prisma / PostgreSQL", "Turborepo / Zod / pnpm"],
        "polenshoes.com", "proyecto finalizado", FLOWER,
    )
    card(
        "card-ressly.svg", "GESTIÓN RESIDENCIAL", "Ressly",
        ["Plataforma para condominios y fraccionamientos:", "accesos, pagos y comunicación entre",
         "administración, vecinos y guardias."],
        [("5", "repositorios"), ("2", "apps Android"), ("3", "roles de usuario")],
        ["React / Node.js / Express / PostgreSQL", "Java / Android / Vercel"],
        "ressly.com.mx", "proyecto finalizado", HOUSE,
    )


# ── Stack ────────────────────────────────────────────────────────────────
def stack():
    layers = [
        ("IA y voz", [("DeepSeek", None), ("Llama · Groq", "meta"), ("Ollama", "ollama"), ("Whisper", "openai"),
                      ("Kokoro", None), ("XTTS v2", None), ("MediaPipe", "mediapipe")]),
        ("Interfaces", [("React", "react"), ("Next.js", "nextdotjs"), ("TypeScript", "typescript"), ("Tailwind", "tailwindcss"),
                        ("shadcn/ui", "shadcnui"), ("Three.js", "threedotjs"), ("Android", "android")]),
        ("Despliegue", [("Vercel", "vercel"), ("Render", "render"), ("Turborepo", "turborepo"), ("pnpm", "pnpm"),
                        ("Actions", "githubactions"), ("Vitest", "vitest"), ("Cloudinary", "cloudinary")]),
        ("Backend y datos", [("Node.js", "nodedotjs"), ("Express", "express"), ("PostgreSQL", "postgresql"), ("Prisma", "prisma"),
                             ("Supabase", "supabase"), ("Firebase", "firebase"), ("Zod", "zod")]),
        ("Comunicación", [("MQTT/TLS", "mqtt"), ("Mosquitto", "eclipsemosquitto"), ("HiveMQ", "hivemq"),
                          ("ESP-NOW", "espressif"), ("REST", None)]),
        ("Firmware", [("ESP32", "espressif"), ("C/C++", "cplusplus"), ("FreeRTOS", None), ("LVGL", None),
                      ("Arduino", "arduino"), ("Raspberry Pi", "raspberrypi")]),
        ("Hardware", [("KiCad", "kicad"), ("Blender", "blender"), ("sensores", None), ("válvulas", None)]),
    ]
    W, RH, top = 1200, 54, 84
    H = top + RH * len(layers) + 30
    b = [text(40, 52, "STACK", 13, RED, mono=True, weight=700, spacing=2),
         text(1160, 52, "de la pantalla al circuito", 12, DIM, mono=True, anchor="end")]
    rail = f"M48,{top + RH * len(layers) - RH / 2} V{top + RH / 2}"
    b.append(f'<path id="rail" d="{rail}" stroke="{LINE2}" fill="none"/>')
    for i, (name, items) in enumerate(layers):
        y = top + i * RH
        cy = y + RH / 2
        b.append(f'<line x1="80" y1="{y}" x2="1160" y2="{y}" stroke="{LINE}"/>')
        b.append(f'<rect x="44" y="{cy - 4}" width="8" height="8" fill="{BLACK}" stroke="{GRAY}"/>')
        b.append(text(80, cy + 5, name, 15, WHITE, weight=600))
        x = 270
        for label, slug in items:
            b.append(icon(slug, x, cy - 8, 16, WHITE))
            b.append(text(x + 24, cy + 5, label, 13, GRAY))
            x += 24 + len(label) * 7.2 + 26
        assert x < 1180, f"la fila {name} no cabe ({x:.0f}px)"
    b.append(f'<line x1="80" y1="{top + RH * len(layers)}" x2="1160" y2="{top + RH * len(layers)}" stroke="{LINE}"/>')
    b.append(mover("rail", 5, r=3.5))
    write("stack.svg", svg(W, H, "".join(b), "Stack técnico por capas"))


if __name__ == "__main__":
    hero()
    ecosystem()
    cards()
    stack()
