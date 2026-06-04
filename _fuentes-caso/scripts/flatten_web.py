#!/usr/bin/env python3
"""Transforma las capturas del design (React aplanado) en la web "actual" de
MakerLab Electrónica: ecommerce puro, sin cursos/tutoriales/kits/comunidad,
con el catálogo reflejando el desorden del xlsx (canon.md)."""
import re
import shutil
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
CAPTURA = BASE / "captura"
OUT = BASE.parent / "caso-makerlab" / "web-actual"
BUNDLE = Path("/tmp/rufino-test/design-bundle/arduino-raspberry-pi-web/project")

# ── catálogo canon (mismas filas que gen_xlsx.py, MISMO desorden) ──────────
PRODUCTOS = [
    ("ARD-UNO-R3", "Arduino UNO R3", "Placas Arduino", "$28500", 42),
    ("ARD-NANO", "Arduino Nano", "placas arduino", "$24.900", 18),
    ("ARD-MEGA", "Arduino Mega 2560", "Placas", "$52300", 7),
    ("ESP-NODEMCU", "NodeMCU ESP8266", "Placas Arduino", "$19800", 25),
    ("RPI-4B-4GB", "Raspberry Pi 4B 4GB", "Placas Raspberry Pi", "$145000", 3),
    ("RPI-ZERO-W", "Raspberry Pi Zero W", "RASPBERRY", "$38.000", 0),
    ("SEN-DHT22", "Sensor temperatura y humedad DHT22", "Sensores", "$8900", 31),
    ("SEN-HCSR04", "Sensor ultrasónico HC-SR04", "sensores", "$4200", 55),
    ("SEN-PIR", "Sensor de movimiento PIR HC-SR501", "SENSORES Y MODULOS", "$5100", 12),
    ("SEN-LDR", "Fotorresistencia LDR 5mm", "Sensores", "$800", None),
    ("LCD-1602-I2C", "Display LCD 16x2 con I2C", "Modulos", "$9700", 22),
    ("DRV-L298N", "Driver de motores L298N", "Modulos y comunicacion", "$6800", 19),
    ("MOT-TT-DC", "Motor DC TT con reductora", "Actuadores", "$3500", 40),
    ("MOT-SG90", "Servo SG90 9g", "Actuadores y motores", "$4900", 28),
    ("CHS-2WD", "Chasis robot 2WD con ruedas", "Actuadores", "$16500", 9),
    ("PRT-830", "Protoboard 830 puntos", "Accesorios", "$6200", 60),
    ("JMP-MM-40", "Jumpers macho-macho x40", "Accesorios", "$3800", 75),
    ("JMP-MH-40", "Jumpers macho-hembra x40", "accesorios", "$3800", 68),
    ("LED-5MM-X10", "Pack 10 LEDs 5mm surtidos", "Accesorios", "$2100", 90),
    ("RES-220-X25", "Pack 25 resistencias 220 ohm", "Accesorios", "$1500", None),
    ("BTN-12MM", "Pulsador táctil 12mm", "Accesorios", "$600", 120),
    ("BAT-4AA", "Portapilas 4xAA con cable", "Accesorios", "$2900", 35),
    ("PSU-5V-2A", "Fuente 5V 2A micro USB", "Accesorios", "$7400", 14),
    ("ARD-UNO-R3", "ARDUINO UNO R3 ORIGINAL", "Placas Arduino", "$31.200", 6),
]

PLUS_SVG = (
    '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" '
    'stroke-width="1.75" stroke-linecap="round"><path d="M12 5v14M5 12h14"></path></svg>'
)


def card(sku: str, nombre: str, precio: str, stock) -> str:
    badge = ""
    if stock == 0:
        badge = '<span class="badge badge--danger">Sin stock</span>'
    elif stock is not None and stock <= 9:
        badge = '<span class="badge badge--warning">Stock bajo</span>'
    return (
        '<article class="product-card card">'
        f'<div class="product-card__media ph">PRODUCTO<div class="product-card__badges">{badge}</div></div>'
        '<div class="product-card__body">'
        f'<div class="product-card__sku">{sku}</div>'
        f'<h3 class="product-card__name">{nombre}</h3>'
        '<div class="product-card__foot">'
        f'<div class="product-card__price">{precio}</div>'
        f'<button class="btn btn--primary btn--sm" aria-label="Sumar {nombre} al pedido">{PLUS_SVG} Sumar</button>'
        "</div></div></article>"
    )


def filtros_categorias() -> str:
    cats: dict[str, int] = {}
    for _, _, cat, _, _ in PRODUCTOS:
        cats[cat] = cats.get(cat, 0) + 1
    filas = []
    for cat, n in cats.items():
        filas.append(
            f'<label><input type="checkbox"> {cat} '
            f'<span class="mono" style="margin-left: auto; color: var(--ink-mute); font-size: 12px;">{n}</span></label>'
        )
    return "".join(filas)


def comunes(h: str) -> str:
    """Transformaciones compartidas por las tres páginas."""
    # nav: fuera Kits / Tutoriales / Comunidad
    h = re.sub(r'<a href="Kit-Detalle\.html" class="nav__link">Kits\s*</a>', "", h)
    h = re.sub(r'<a href="Tutorial\.html" class="nav__link">Tutoriales\s*</a>', "", h)
    h = re.sub(r'<a href="#comunidad" class="nav__link">Comunidad\s*</a>', "", h)
    # footer: fuera la columna "Aprender" completa (div contenedor) y el link a kits
    h = re.sub(r'<div[^>]*>\s*<h4>Aprender</h4>.*?</ul>\s*</div>', "", h, flags=re.S)
    h = re.sub(r'<li><a href="[^"]*">Kits curados</a></li>', "", h)
    # tagline del footer: sin kits/tutoriales/comunidad
    h = h.replace(
        "Componentes con stock real, kits curados, tutoriales probados y una comunidad que te banca.",
        "Componentes con stock real y envíos a todo el país desde 2021.")
    # marca completa
    h = h.replace("MAKERLAB — Arduino, Raspberry Pi y kits para makers",
                  "MakerLab Electrónica — Arduino, Raspberry Pi y componentes")
    h = h.replace("· MAKERLAB</title>", "· MakerLab Electrónica</title>")
    # cualquier link suelto a páginas que la web actual no tiene
    h = h.replace('href="Kit-Detalle.html"', 'href="Catalogo.html"')
    h = h.replace('href="Tutorial.html"', 'href="Catalogo.html"')
    return h


def home(h: str) -> str:
    # 1. fuera las secciones del "futuro": kits curados, tutoriales, comunidad
    secciones = re.findall(r"<section.*?</section>", h, flags=re.S)
    for s in secciones:
        if ("Kits curados por proyecto" in s or "Tutoriales que funcionan</h2>" in s
                or 'id="comunidad"' in s):
            h = h.replace(s, "")
    # 2. hero: una tienda, no una escuela
    h = h.replace(
        "Componentes con stock real, kits curados por proyecto, tutoriales que "
        "funcionan y una comunidad de makers que te banca cuando algo no compila.",
        "Componentes con stock real, precios claros y envíos a todo el país. "
        "Todo lo que necesitás, en un solo lugar.")
    h = re.sub(r'<a class="btn btn--secondary btn--lg" href="[^"]*">Empezar con un kit\s*</a>', "", h)
    # 3. "¿por qué comprarnos?": sin promesas de tutoriales/comunidad
    h = h.replace(
        '<h3 class="why-item__title">Tutoriales que funcionan</h3><p class="why-item__desc">'
        "Cada producto tiene una guía probada. Si no anda, te respondemos.</p>",
        '<h3 class="why-item__title">Garantía sin vueltas</h3><p class="why-item__desc">'
        "Si algo llega fallado, lo cambiamos dentro de los 30 días. Sin formularios eternos.</p>")
    h = h.replace(
        '<h3 class="why-item__title">Comunidad activa</h3><p class="why-item__desc">'
        "Discord, workshops, showcase. No estás solo cuando algo no compila.</p>",
        '<h3 class="why-item__title">Atención posventa real</h3><p class="why-item__desc">'
        "Te responde una persona que sabe de electrónica, no un bot.</p>")
    # 4. newsletter sin tutoriales
    h = h.replace("El kit del mes, tutoriales nuevos y descuentos.",
                  "Ofertas, ingresos nuevos y descuentos.")
    # 5. FAQ: fuera las preguntas de tutoriales y Discord (accs cerrados, sin body)
    h = re.sub(r'<div class="acc ">(?:(?!</button>).)*?tutoriales(?:(?!</button>).)*?</button></div>',
               "", h, flags=re.S | re.I)
    h = re.sub(r'<div class="acc ">(?:(?!</button>).)*?Discord(?:(?!</button>).)*?</button></div>',
               "", h, flags=re.S | re.I)
    return h


def catalogo(h: str) -> str:
    # grid: reemplazo posicional de TODOS los cards por las 24 filas del canon
    cards = "".join(card(s, n, p, st) for s, n, _, p, st in PRODUCTOS)
    primero = h.find('<article class="product-card')
    ultimo = h.rfind("</article>") + len("</article>")
    assert primero != -1 and ultimo > primero, "no encontré el grid de cards"
    h = h[:primero] + cards + h[ultimo:]
    # filtros de categoría: los 6 labels con contador del design → las 14
    # variantes inconsistentes del canon (bloque consecutivo)
    viejos = re.findall(
        r'<label><input type="checkbox"(?: checked="")?> [^<]*<span class="mono"[^>]*>[^<]*</span></label>', h)
    assert viejos, "no encontré los filtros de categoría"
    bloque_viejo = "".join(viejos)
    assert bloque_viejo in h, "los filtros de categoría no son consecutivos"
    h = h.replace(bloque_viejo, filtros_categorias())
    # contador de resultados
    h = re.sub(r"\d+\s*productos", "24 productos", h)
    return h


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for css in ("styles.css", "styles-components.css"):
        shutil.copy(BUNDLE / css, OUT / css)

    paginas = {
        "Home.html": home,
        "Catalogo.html": catalogo,
        "Carrito.html": lambda h: h,
    }
    for nombre, extra in paginas.items():
        h = (CAPTURA / nombre).read_text()
        h = comunes(extra(h)) if nombre == "Home.html" else extra(comunes(h))
        (OUT / nombre).write_text(h)
        print(f"OK → {OUT / nombre} ({len(h)} bytes)")

    # verificación
    for nombre in paginas:
        h = (OUT / nombre).read_text()
        assert "<script" not in h.lower(), f"{nombre}: quedó un <script>"
        assert "Tutorial.html" not in h, f"{nombre}: quedó link a Tutorial"
        assert "Kit-Detalle.html" not in h, f"{nombre}: quedó link a Kit-Detalle"
    cat = (OUT / "Catalogo.html").read_text()
    assert cat.count("ARD-UNO-R3") == 2, "falta el SKU duplicado en el catálogo"
    assert "SENSORES Y MODULOS" in cat, "faltan las categorías inconsistentes"
    home_html = (OUT / "Home.html").read_text()
    assert "Kits curados" not in home_html and 'id="comunidad"' not in home_html
    print("VERIFICACIÓN OK")


if __name__ == "__main__":
    main()
