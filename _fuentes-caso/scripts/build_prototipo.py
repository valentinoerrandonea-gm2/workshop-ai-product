#!/usr/bin/env python3
"""Construye el prototipo de referencia (backup de la demo de Val):
referencia/design-original/ (Tutorial + Kit-Detalle aplanados) y
referencia/prototipo/ (web-actual + sección Cursos integrada)."""
import json
import re
import shutil
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
CAPTURA = BASE / "captura"
CASO = BASE.parent / "caso-makerlab"
WEB = CASO / "web-actual"
REF = CASO / "outcome-esperado" / "referencia"
ORIG = REF / "design-original"
PROTO = REF / "prototipo"

CTA_SVG = (
    '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" '
    'stroke-width="1.75" stroke-linecap="round"><path d="M5 12h14M13 6l6 6-6 6"></path></svg>'
)

# ── canon ──────────────────────────────────────────────────────────────────
CURSOS = [
    {
        "slug": "Curso-Semaforo.html", "nombre": "Semáforo inteligente",
        "nivel": "Inicial", "badge": "badge--accent", "clases": 4, "horas": 6,
        "precio": "$89.900", "media": "SEMÁFORO ARMADO · LEDS ENCENDIDOS",
        "blurb": "Tu primer circuito real: un semáforo con botón peatonal y modo "
                 "nocturno. De cero, sin experiencia previa.",
        "kit": [
            ("ARD-UNO-R3", "Arduino UNO R3"),
            ("PRT-830", "Protoboard 830 puntos"),
            ("LED-5MM-X10", "Pack 10 LEDs 5mm surtidos"),
            ("RES-220-X25", "Pack 25 resistencias 220 ohm"),
            ("BTN-12MM", "Pulsador táctil 12mm"),
            ("JMP-MM-40", "Jumpers macho-macho x40"),
        ],
        "temario": [
            ("Tu primer circuito", "Qué es Arduino, el protoboard, encender un LED."),
            ("El semáforo básico", "Tres LEDs, resistencias, tiempos con millis()."),
            ("El botón peatonal", "Entradas digitales, pull-up, antirrebote."),
            ("Proyecto final", "Semáforo completo con cruce peatonal y modo nocturno."),
        ],
    },
    {
        "slug": None, "nombre": "Estación meteorológica IoT",
        "nivel": "Intermedio", "badge": "badge--led", "clases": 6, "horas": 10,
        "precio": "$149.900", "media": "ESTACIÓN METEOROLÓGICA · LCD ENCENDIDO",
        "blurb": "Medí temperatura y humedad, mostralas en un display y publicalas "
                 "por WiFi para verlas desde el celular.",
    },
    {
        "slug": None, "nombre": "Robot evita-obstáculos",
        "nivel": "Avanzado", "badge": "badge--hot", "clases": 8, "horas": 14,
        "precio": "$189.900", "media": "ROBOT 2WD · EN MOVIMIENTO",
        "blurb": "Un robot con dos motores que detecta obstáculos con ultrasonido "
                 "y decide solo hacia dónde moverse.",
    },
]


def card_curso(c: dict, destacado: bool = False) -> str:
    extra = " kit-card--featured" if destacado else ""
    cta = (f'<a class="btn btn--primary btn--sm" href="{c["slug"]}">Ver curso {CTA_SVG}</a>'
           if c["slug"] else
           '<span class="btn btn--ghost btn--sm" aria-disabled="true">Inscripción próximamente</span>')
    return f'''<article class="kit-card card{extra}">
<div class="kit-card__media ph" aria-hidden="true">{c["media"]}<span class="badge {c["badge"]} kit-card__level">● {c["nivel"]}</span></div>
<div class="kit-card__body">
<div class="kit-card__meta mono"><span>{c["clases"]} clases</span><span>·</span><span>{c["horas"]} hs</span><span>·</span><span>online en vivo</span></div>
<h3 class="kit-card__name">{c["nombre"]}</h3>
<p class="kit-card__blurb">{c["blurb"]}</p>
<div class="kit-card__foot">
<div class="kit-card__price"><div class="mono kit-card__price-label">Curso + kit incluido</div><div class="kit-card__price-value">{c["precio"]}</div></div>
<div class="kit-card__ctas">{cta}</div>
</div></div></article>'''


def main_cursos() -> str:
    cards = card_curso(CURSOS[0], destacado=True) + "".join(card_curso(c) for c in CURSOS[1:])
    return f'''<main>
<section class="section">
<div class="container">
<div class="eyebrow">// MakerLab Academy</div>
<h1 style="margin-top: 14px; max-width: 22ch;">Aprendé robótica. <span class="accent">El kit va incluido.</span></h1>
<p style="margin-top: 18px; max-width: 58ch; color: var(--ink-soft); font-size: 18px;">
Cursos online en vivo donde no mirás: <b>armás</b>. Te inscribís, te llega el kit
con todos los componentes a tu casa, y construís el proyecto clase a clase con
un instructor que te acompaña. Un solo precio, cero vueltas.</p>
<div class="kit-card__meta mono" style="margin-top: 16px;"><span>✓ Kit a domicilio</span><span>·</span><span>✓ Clases grabadas para siempre</span><span>·</span><span>✓ Sin conocimientos previos (nivel inicial)</span></div>
</div>
</section>
<section class="section section--alt">
<div class="container">
<div class="eyebrow">// Primera camada</div>
<h2 style="margin-top: 14px;">Tres cursos, una progresión.</h2>
<div class="kits-grid" style="margin-top: 28px;">{cards}</div>
</div>
</section>
</main>'''


def main_semaforo() -> str:
    c = CURSOS[0]
    temario = "".join(
        f'''<div class="card" style="padding: 18px 22px; display: flex; gap: 18px; align-items: baseline;">
<div class="mono" style="color: var(--accent); white-space: nowrap;">Clase {i + 1:02d} ───</div>
<div><h3 style="font-size: 17px; margin: 0;">{titulo}</h3>
<p style="margin: 4px 0 0; color: var(--ink-soft); font-size: 14px;">{desc}</p></div></div>'''
        for i, (titulo, desc) in enumerate(c["temario"]))
    bom = "".join(
        f'<li style="display: flex; gap: 14px; padding: 10px 0; border-bottom: 1px dashed var(--line, #ddd);">'
        f'<span class="mono" style="color: var(--ink-mute); min-width: 130px;">{sku}</span>'
        f'<span>{nombre}</span></li>'
        for sku, nombre in c["kit"])
    otros = "".join(card_curso(x) for x in CURSOS[1:])
    return f'''<main>
<section class="section">
<div class="container" style="display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 48px; align-items: start;">
<div>
<div class="eyebrow">// MakerLab Academy · <a href="Cursos.html" style="border-bottom: 1px solid currentColor;">Cursos</a> / Semáforo inteligente</div>
<span class="badge {c["badge"]}" style="margin-top: 16px; display: inline-block;">● Nivel {c["nivel"].lower()} — tu primer Arduino</span>
<h1 style="margin-top: 12px;">Semáforo inteligente</h1>
<p style="margin-top: 16px; max-width: 56ch; color: var(--ink-soft); font-size: 18px;">
Armá un semáforo real con botón peatonal y modo nocturno, y de paso aprendé lo
que importa: leer un circuito, escribir tu primer programa y entender por qué
funciona. Sin experiencia previa, de cero.</p>
<div class="kit-card__meta mono" style="margin-top: 18px;"><span>{c["clases"]} clases</span><span>·</span><span>{c["horas"]} horas</span><span>·</span><span>online en vivo</span><span>·</span><span>queda grabado</span></div>
</div>
<aside class="card" style="padding: 26px; position: sticky; top: 90px;">
<div class="mono" style="font-size: 12px; color: var(--ink-mute);">CURSO + KIT INCLUIDO</div>
<div style="font-size: 38px; font-weight: 700; margin: 6px 0 2px;" class="mono">{c["precio"]}</div>
<p style="font-size: 13px; color: var(--ink-soft); margin: 0 0 16px;">Precio final. Incluye las clases, el kit completo de componentes y el envío a todo el país.</p>
<a class="btn btn--primary btn--lg" href="Carrito.html" style="width: 100%; justify-content: center;">Inscribirme — kit incluido {CTA_SVG}</a>
<p class="mono" style="font-size: 11px; color: var(--ink-mute); margin-top: 12px;">✓ El kit se despacha al inscribirte · ✓ Cupo: 25 alumnos</p>
</aside>
</div>
</section>
<section class="section section--alt">
<div class="container">
<div class="eyebrow">// Temario</div>
<h2 style="margin-top: 14px;">Clase a clase, hasta que funciona.</h2>
<div style="display: grid; gap: 14px; margin-top: 28px; max-width: 760px;">{temario}</div>
</div>
</section>
<section class="section">
<div class="container">
<div class="eyebrow">// Tu kit incluido</div>
<h2 style="margin-top: 14px;">Todo lo que llega a tu casa.</h2>
<div class="card" style="padding: 26px; margin-top: 28px; max-width: 760px;">
<ul style="list-style: none; margin: 0; padding: 0;">{bom}</ul>
<p class="mono" style="font-size: 12px; color: var(--ink-mute); margin: 14px 0 0;">6 componentes · todos del catálogo MakerLab · garantía de 30 días</p>
</div>
</div>
</section>
<section class="section section--alt">
<div class="container">
<div class="eyebrow">// Próximo paso</div>
<h2 style="margin-top: 14px;">Seguí subiendo de nivel.</h2>
<div class="kits-grid" style="margin-top: 28px;">{otros}</div>
</div>
</section>
</main>'''


def shell(home: str, titulo: str, contenido: str) -> str:
    """Arma una página nueva con el head+header y footer de la Home."""
    i_main = home.find("<main")
    i_fin_main = home.find("</main>") + len("</main>")
    assert i_main != -1 and i_fin_main > i_main, "no encontré <main> en la Home"
    pagina = home[:i_main] + contenido + home[i_fin_main:]
    pagina = re.sub(r"<title>[^<]*</title>", f"<title>{titulo}</title>", pagina)
    return pagina


def agregar_nav_cursos(h: str) -> str:
    if 'href="Cursos.html" class="nav__link"' in h:
        return h
    return h.replace(
        '<a href="Catalogo.html" class="nav__link">Catálogo',
        '<a href="Cursos.html" class="nav__link">Cursos</a><a href="Catalogo.html" class="nav__link">Catálogo',
        1)


def desescapar(p: Path) -> str:
    raw = p.read_text()
    if raw.lstrip().startswith('"'):
        return json.loads(raw)
    if "\\n" in raw[:200] or '\\"' in raw[:200]:
        try:
            return json.loads(raw)
        except Exception:
            return raw.encode().decode("unicode_escape")
    return raw


def main() -> None:
    # 1. design-original: Tutorial + Kit-Detalle aplanados + css
    ORIG.mkdir(parents=True, exist_ok=True)
    for nombre in ("Tutorial.html", "Kit-Detalle.html"):
        (ORIG / nombre).write_text(desescapar(CAPTURA / nombre))
    for css in ("styles.css", "styles-components.css"):
        shutil.copy(WEB / css, ORIG / css)

    # 2. prototipo: web-actual + nav Cursos + las dos páginas nuevas
    PROTO.mkdir(parents=True, exist_ok=True)
    for f in WEB.iterdir():
        shutil.copy(f, PROTO / f.name)
    for nombre in ("Home.html", "Catalogo.html", "Carrito.html"):
        p = PROTO / nombre
        p.write_text(agregar_nav_cursos(p.read_text()))

    home = (PROTO / "Home.html").read_text()
    (PROTO / "Cursos.html").write_text(
        shell(home, "Cursos · MakerLab Academy", main_cursos()))
    (PROTO / "Curso-Semaforo.html").write_text(
        shell(home, "Semáforo inteligente · Curso · MakerLab Academy", main_semaforo()))

    # 3. verificación
    for nombre in ("Cursos.html", "Curso-Semaforo.html"):
        h = (PROTO / nombre).read_text()
        assert "<script" not in h.lower(), f"{nombre}: script"
    sem = (PROTO / "Curso-Semaforo.html").read_text()
    for sku, _ in CURSOS[0]["kit"]:
        assert sku in sem, f"falta {sku} en la BOM"
    assert "$89.900" in sem and "$149.900" in sem and "$189.900" in sem
    cur = (PROTO / "Cursos.html").read_text()
    assert cur.count("kit-card__name") == 3
    print("PROTOTIPO OK →", PROTO)


if __name__ == "__main__":
    main()
