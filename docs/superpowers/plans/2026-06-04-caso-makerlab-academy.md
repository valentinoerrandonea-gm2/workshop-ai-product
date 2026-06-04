# Caso MakerLab Academy — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Construir el paquete completo del caso MakerLab Academy (corpus del cliente, web actual estática, outcome esperado con prototipo de referencia, y guión de demo) según el spec `docs/superpowers/specs/2026-06-04-caso-makerlab-academy-design.md`.

**Architecture:** Todo el contenido deriva de un canon único (datos duros: cursos, SKUs, precios, fechas, personas) para garantizar consistencia entre los 11 archivos del corpus. Los formatos binarios se generan con herramientas locales (textutil, cupsfilter, openpyxl, python-pptx, screenshot vía Playwright MCP). La web actual se aplana del bundle React de Claude Design a HTML estático capturando el DOM renderizado.

**Tech Stack:** HTML/CSS estático (sin React), Python (openpyxl + python-pptx solo para GENERAR material, no para las skills), textutil/cupsfilter (macOS built-in), Playwright MCP (render + screenshots), las skills Rufino existentes.

---

## Canon del caso (fuente única de verdad — usar EXACTAMENTE estos datos en todos los archivos)

### Personas del cliente

| Persona | Rol | Voz |
|---|---|---|
| Marcos Etcheverry | Dueño/fundador | Entusiasta, dispara ideas sin filtrar (el mail de los 5 cursos) |
| Carla Domínguez | Gerenta comercial | Pushea el pivot, armó las slides de la visión |
| Tomás Brizuela | Catálogo/operaciones | Pragmático, conoce el desorden del catálogo, frena ideas caras |
| Romina Páez | Instructora | Diseñó los temarios de los 3 cursos |

### Cronología (las fechas resuelven la contradicción: lo más nuevo manda)

| Fecha | Documento | Qué dice |
|---|---|---|
| 2026-02-18 | mail-queja-cliente.md | RUIDO — cliente se queja de demora de envío |
| 2026-03-05 | minuta-logistica.docx | RUIDO — reunión sobre cambio de operador logístico |
| 2026-03-10 | mail-dueno-ideas-cursos.md | **CONTRADICCIÓN** — Marcos propone **5 cursos** |
| 2026-03-28 | pizarra-brainstorm.png | RUIDO — foto de pizarra del brainstorm (garabatos del pivot, sin datos duros) |
| 2026-04-02 | vision-makerlab-academy.pptx | CLAVE — Carla: visión del pivot "de tienda a academia" |
| 2026-04-10 | mail-proveedor.md | RUIDO — proveedor avisa aumento de precios de Arduino |
| 2026-04-15 | slack-canal-pivot.md | CLAVE — el equipo **baja de 5 a 3 cursos** y define precios |
| 2026-05-08 | temarios-cursos.pdf | CLAVE — Romina: temario, nivel y duración de los 3 cursos |
| 2026-05-20 | minuta-kickoff-gm2.docx | CLAVE — pedido formal a GM2: prototipo sección Cursos, 3 cursos |
| (2025-11) | politica-devoluciones.pdf | RUIDO — política de devoluciones vigente |
| (s/f) | catalogo-productos.xlsx | CLAVE — hoja "productos" (desordenada) + hoja "cursos" (mapping) |

### Los 5 cursos del mail de Marcos (2026-03-10)

1. Semáforo inteligente ✅ (queda)
2. Estación meteorológica IoT ✅ (queda)
3. Robot evita-obstáculos ✅ (queda)
4. Domótica con Raspberry Pi ❌ (descartado en Slack: kit demasiado caro, sin stock de RPi)
5. Brazo robótico con servos ❌ (descartado en Slack: requiere impresión 3D, fuera de alcance)

### Los 3 cursos definitivos (Slack 2026-04-15 + temarios 2026-05-08 + minuta 2026-05-20)

| Curso | Nivel | Duración | Precio (curso + kit incluido) | Kit (SKUs) |
|---|---|---|---|---|
| Semáforo inteligente | Inicial | 4 clases / 6 h | **$89.900** | ARD-UNO-R3, PRT-830, LED-5MM-X10, RES-220-X25, BTN-12MM, JMP-MM-40 |
| Estación meteorológica IoT | Intermedio | 6 clases / 10 h | **$149.900** | ESP-NODEMCU, SEN-DHT22, LCD-1602-I2C, PRT-830, JMP-MH-40, PSU-5V-2A |
| Robot evita-obstáculos | Avanzado | 8 clases / 14 h | **$189.900** | ARD-UNO-R3, CHS-2WD, MOT-TT-DC (x2), DRV-L298N, SEN-HCSR04, BAT-4AA, JMP-MH-40 |

Mecánica comercial (definida en Slack, confirmada en minuta): **no se vende el curso sin kit** — un solo precio, un solo CTA ("Inscribirme — kit incluido"). Modalidad: online en vivo + material grabado; el kit se envía al inscribirse.

### Catálogo — hoja "productos" del xlsx (24 filas, CON el desorden marcado)

Columnas: `SKU | Producto | Categoria | Precio | Stock`

| SKU | Producto | Categoria | Precio | Stock |
|---|---|---|---|---|
| ARD-UNO-R3 | Arduino UNO R3 | Placas Arduino | 28500 | 42 |
| ARD-NANO | Arduino Nano | placas arduino | $24.900 | 18 |
| ARD-MEGA | Arduino Mega 2560 | Placas | 52300 | 7 |
| ESP-NODEMCU | NodeMCU ESP8266 | Placas Arduino | 19800 | 25 |
| RPI-4B-4GB | Raspberry Pi 4B 4GB | Placas Raspberry Pi | 145000 | 3 |
| RPI-ZERO-W | Raspberry Pi Zero W | RASPBERRY | $38.000 | 0 |
| SEN-DHT22 | Sensor temperatura y humedad DHT22 | Sensores | 8900 | 31 |
| SEN-HCSR04 | Sensor ultrasónico HC-SR04 | sensores | 4200 | 55 |
| SEN-PIR | Sensor de movimiento PIR HC-SR501 | SENSORES Y MODULOS | 5100 | 12 |
| SEN-LDR | Fotorresistencia LDR 5mm | Sensores | 800 | *(vacío)* |
| LCD-1602-I2C | Display LCD 16x2 con I2C | Modulos | 9700 | 22 |
| DRV-L298N | Driver de motores L298N | Modulos y comunicacion | 6800 | 19 |
| MOT-TT-DC | Motor DC TT con reductora | Actuadores | 3500 | 40 |
| MOT-SG90 | Servo SG90 9g | Actuadores y motores | 4900 | 28 |
| CHS-2WD | Chasis robot 2WD con ruedas | Actuadores | 16500 | 9 |
| PRT-830 | Protoboard 830 puntos | Accesorios | 6200 | 60 |
| JMP-MM-40 | Jumpers macho-macho x40 | Accesorios | 3800 | 75 |
| JMP-MH-40 | Jumpers macho-hembra x40 | accesorios | 3800 | 68 |
| LED-5MM-X10 | Pack 10 LEDs 5mm surtidos | Accesorios | 2100 | 90 |
| RES-220-X25 | Pack 25 resistencias 220 ohm | Accesorios | 1500 | *(vacío)* |
| BTN-12MM | Pulsador táctil 12mm | Accesorios | 600 | 120 |
| BAT-4AA | Portapilas 4xAA con cable | Accesorios | 2900 | 35 |
| PSU-5V-2A | Fuente 5V 2A micro USB | Accesorios | 7400 | 14 |
| ARD-UNO-R3 | ARDUINO UNO R3 ORIGINAL | Placas Arduino | $31.200 | 6 |

Desorden a propósito (que el discovery debe notar): **SKU `ARD-UNO-R3` duplicado** con nombre y precio distintos (filas 1 y 24), categorías inconsistentes en mayúsculas/minúsculas/sinónimos (8 variantes para 6 categorías reales), precios a veces con `$` y puntos a veces números crudos, 2 celdas de stock vacías.

### Hoja "cursos" del xlsx

Columnas: `Curso | Nivel | SKUs del kit | Precio final`
Tres filas, EXACTAMENTE los datos de la tabla de cursos definitivos (SKUs separados por coma; en Robot, `MOT-TT-DC` aparece como `MOT-TT-DC x2`).

---

## Estructura de archivos final

```
caso-makerlab/
├── BRIEF.md
├── material-cliente/            # los 11 archivos del corpus
├── web-actual/                  # Home.html, Catalogo.html, Carrito.html, styles.css, styles-components.css
├── outcome-esperado/
│   ├── OUTCOME.md
│   ├── canon.md                 # este canon, copiado (la "verdad" para validar)
│   └── referencia/
│       ├── design-original/     # Tutorial.html y Kit-Detalle.html del bundle (tal cual)
│       └── prototipo/           # Cursos.html + Curso-Semaforo.html + web-actual integrada (backup de Val)
├── GUION-DEMO.md
_fuentes-caso/                   # (root del repo) textos fuente .txt/.md + scripts de generación — NO se entrega
caso-makerlab.zip                # BRIEF + material-cliente + web-actual (lo que reciben los asistentes)
```

---

### Task 1: Canon + textos fuente del corpus

**Files:**
- Create: `caso-makerlab/outcome-esperado/canon.md`
- Create: `_fuentes-caso/textos/*.txt|.md` (los 11 contenidos en texto plano)

- [ ] **Step 1:** Crear `caso-makerlab/outcome-esperado/canon.md` copiando la sección "Canon del caso" completa de este plan (personas, cronología, cursos, catálogo).
- [ ] **Step 2:** Escribir los textos fuente en `_fuentes-caso/textos/`. Reglas: español rioplatense, voces según el canon, fechas del canon visibles dentro del texto (encabezado o firma), datos duros EXACTOS del canon. Archivos y contenido mínimo:
  - `mail-dueno-ideas-cursos.md` — de Marcos a Carla/Tomás, 2026-03-10. Propone los **5 cursos** con nombres exactos del canon, entusiasta, sin precios. ~15 líneas.
  - `vision-makerlab-academy.txt` — guion de 8 slides para el pptx de Carla, 2026-04-02: (1) título "MakerLab Academy — de tienda a escuela", (2) problema: margen bajo + competencia de importados, (3) la oportunidad: la gente no compra componentes, quiere PROYECTOS, (4) el modelo: cursos pagos con kit incluido, (5) "no vendemos cursos, vendemos el resultado armado", (6) primera camada de cursos (sin numerarlos — dice "estamos definiendo la grilla"), (7) la web hoy no puede mostrar esto, (8) próximos pasos: contratar consultora dev.
  - `slack-canal-pivot.md` — export del canal `#pivot-academy`, 2026-04-15, ~30 mensajes entre Marcos, Carla, Tomás y Romina. Momentos clave: Tomás objeta Domótica RPi ("no hay stock de Raspberry, el kit se va arriba de $300 lucas") y Brazo robótico ("necesita impresora 3D, no tenemos"); acuerdan **3 cursos**; Carla propone los precios finales del canon; Romina se compromete a los temarios; Tomás menciona "el excel del catálogo es un quilombo, hay SKUs duplicados" (pista del desorden).
  - `temarios-cursos.txt` — para el pdf de Romina, 2026-05-08: por cada curso (los 3 del canon): objetivo, nivel, duración exacta del canon, temario de 4-8 clases (títulos de clase), y "Materiales: incluidos en el kit".
  - `minuta-kickoff-gm2.txt` — para el docx, 2026-05-20, reunión MakerLab × GM2 (asisten los 4 del cliente + "equipo GM2"). El pedido formal: prototipo HTML de la sección Cursos sobre la web actual; 3 cursos definitivos listados con precio; mecánica curso+kit con CTA única; mencionar que el catálogo se pasa "como está" en excel; deadline del prototipo: 2 semanas.
  - `mail-queja-cliente.md` — 2026-02-18, cliente enojado por demora de un pedido de jumpers. RUIDO puro.
  - `minuta-logistica.txt` — para docx, 2026-03-05, evaluación Andreani vs OCA. RUIDO.
  - `mail-proveedor.md` — 2026-04-10, importador avisa +12% en placas Arduino desde mayo. RUIDO (pero coherente: explica el duplicado de precio del UNO en el xlsx).
  - `politica-devoluciones.txt` — para pdf, noviembre 2025, política estándar de devoluciones. RUIDO.
  - `pizarra-brainstorm.html` — HTML para screenshotear: fondo blanco pizarra, fuente manuscrita (Caveat de Google Fonts), garabatos del brainstorm del pivot: "TIENDA → ESCUELA???", "cursos = kit + clases", "¿cuántos? 3? 5?", flechas, un círculo alrededor de "EL KIT VA INCLUIDO". Sin datos duros (es ruido, pero temático).
- [ ] **Step 3:** Verificar consistencia: `grep -l "89.900\|89900" _fuentes-caso/textos/` debe matchear slack y minuta (y solo ellos entre los textos); los nombres de los 5 cursos del mail aparecen idénticos en el Slack al descartarse.
- [ ] **Step 4:** Commit: `git add caso-makerlab/outcome-esperado/canon.md _fuentes-caso/ && git commit -m "feat: canon del caso + textos fuente del corpus"`

### Task 2: Generar los binarios del corpus

**Files:**
- Create: `caso-makerlab/material-cliente/*` (los 11 archivos finales)
- Create: `_fuentes-caso/scripts/gen_xlsx.py`, `_fuentes-caso/scripts/gen_pptx.py`

- [ ] **Step 1:** Dependencias de generación (solo máquina de Val): `python3 -c "import openpyxl, pptx" 2>/dev/null || pip3 install --user openpyxl python-pptx`
- [ ] **Step 2:** `gen_xlsx.py`: crear `catalogo-productos.xlsx` con hoja `productos` (las 24 filas EXACTAS del canon, con los valores sucios tal cual — strings `"$31.200"` donde corresponde, celdas vacías de stock) y hoja `cursos` (3 filas del canon). Sin estilos.
- [ ] **Step 3:** `gen_pptx.py`: crear `vision-makerlab-academy.pptx` con las 8 slides del guion (layout título+bullets, sin imágenes).
- [ ] **Step 4:** Word y PDF con built-ins:
  ```bash
  cd _fuentes-caso/textos
  textutil -convert docx minuta-kickoff-gm2.txt -output ../../caso-makerlab/material-cliente/minuta-kickoff-gm2.docx
  textutil -convert docx minuta-logistica.txt -output ../../caso-makerlab/material-cliente/minuta-logistica.docx
  cupsfilter temarios-cursos.txt > ../../caso-makerlab/material-cliente/temarios-cursos.pdf
  cupsfilter politica-devoluciones.txt > ../../caso-makerlab/material-cliente/politica-devoluciones.pdf
  ```
- [ ] **Step 5:** Pizarra: servir `pizarra-brainstorm.html`, capturar con Playwright MCP (`browser_take_screenshot`, viewport 1200×800) → `caso-makerlab/material-cliente/pizarra-brainstorm.png`.
- [ ] **Step 6:** Copiar los `.md` (mails + slack) tal cual a `material-cliente/`.
- [ ] **Step 7:** Verificar la matriz de extracción de las skills contra los binarios generados:
  ```bash
  textutil -convert txt -stdout caso-makerlab/material-cliente/minuta-kickoff-gm2.docx | head -5         # → texto de la minuta
  unzip -p caso-makerlab/material-cliente/vision-makerlab-academy.pptx ppt/slides/slide1.xml | grep -o '<a:t>[^<]*'  # → título
  unzip -p caso-makerlab/material-cliente/catalogo-productos.xlsx xl/sharedStrings.xml | grep -c 'ARD-UNO-R3'        # → 2 (¡el duplicado!)
  ```
  y Read sobre el pdf y el png (multimodal).
- [ ] **Step 8:** Commit: `git commit -am "feat: corpus del cliente generado (11 archivos, 6 formatos)"`

### Task 3: Soporte xlsx en la skill + zip

**Files:**
- Modify: `.claude/skills/process-rufino/references/extraccion.md`
- Regenerate: `rufino-skills.zip`

- [ ] **Step 1:** Agregar a `extraccion.md` la fila `.xlsx` en la tabla y una sección "Excel (.xlsx)":
  ```bash
  # strings compartidos (textos de celdas)
  unzip -p archivo.xlsx xl/sharedStrings.xml | grep -o '<t[^>]*>[^<]*' | sed 's/<t[^>]*>//'
  # estructura por hoja (sheet1, sheet2...) — los valores numéricos viven acá; t="s" indexa sharedStrings
  unzip -p archivo.xlsx xl/worksheets/sheet1.xml | grep -o '<v>[^<]*' | sed 's/<v>//'
  # ver qué hojas hay
  unzip -p archivo.xlsx xl/workbook.xml | grep -o 'name="[^"]*"'
  ```
  con la advertencia: para tablas chicas conviene reconstruir la tabla leyendo ambos XML; si la estructura es compleja, pedir export a CSV.
- [ ] **Step 2:** Probar los tres comandos contra `catalogo-productos.xlsx` (debe verse el nombre de las 2 hojas y los SKUs).
- [ ] **Step 3:** Regenerar el zip: `cd .claude/skills && rm -f ../../rufino-skills.zip && zip -r ../../rufino-skills.zip ask-rufino process-rufino rufino-ingest -x "*.DS_Store"`
- [ ] **Step 4:** Commit: `git commit -am "feat: extracción xlsx en process-rufino + zip regenerado"`

### Task 4: Web actual (aplanado a HTML estático)

**Files:**
- Create: `caso-makerlab/web-actual/{Home,Catalogo,Carrito}.html`, `styles.css`, `styles-components.css`
- Source: `/tmp/rufino-test/design-bundle/arduino-raspberry-pi-web/project/` (si no existe, re-descargar el bundle: `curl -sL "https://api.anthropic.com/v1/design/h/XA8WwFs72N6x3rzVFOfb3w" -o /tmp/design.gz && gunzip … && tar -xf …`)

- [ ] **Step 1:** Servir el bundle: `cd <bundle>/project && python3 -m http.server 8765` (background).
- [ ] **Step 2:** Con Playwright MCP, para cada página (Home, Catalogo, Carrito): navegar a `http://localhost:8765/<P>.html`, esperar el render de React, extraer `document.documentElement.outerHTML` con `browser_evaluate`.
- [ ] **Step 3:** Limpiar cada HTML capturado: quitar TODOS los `<script>` (React/Babel/tweaks/jsx), quitar el tweaks-panel del DOM, dejar los `<link>` de fuentes y CSS. Guardar en `caso-makerlab/web-actual/`. Copiar `styles.css` y `styles-components.css`.
- [ ] **Step 4:** Editar `Home.html`: eliminar las secciones de tutoriales, kits curados y comunidad (la empresa HOY no las tiene); el nav queda: Catálogo · Nosotros · Carrito. Marca: MAKERLAB → "MakerLab Electrónica" donde aparezca el nombre completo.
- [ ] **Step 5:** Editar `Catalogo.html`: reflejar el desorden del canon — repetir la card del Arduino UNO con los dos precios, categorías de filtro inconsistentes ("Sensores" y "SENSORES Y MODULOS" como filtros distintos). Sin JS: los filtros quedan como UI estática (es un prototipo de partida, no funcional).
- [ ] **Step 6:** Verificar con Playwright: las 3 páginas abren sin consola roja, sin referencias 404, los links internos entre ellas funcionan, y `grep -ci react caso-makerlab/web-actual/*.html` → 0.
- [ ] **Step 7:** Commit: `git commit -am "feat: web actual de MakerLab (HTML estático, sin cursos)"`

### Task 5: Prototipo de referencia (backup de la demo)

**Files:**
- Create: `caso-makerlab/outcome-esperado/referencia/prototipo/{Cursos,Curso-Semaforo}.html` + copia integrada de web-actual
- Copy: `Tutorial.html`, `Kit-Detalle.html` del bundle → `caso-makerlab/outcome-esperado/referencia/design-original/`

- [ ] **Step 1:** Copiar el design original (Tutorial.html + Kit-Detalle.html del bundle, tal cual, como referencia "a dónde apuntaba").
- [ ] **Step 2:** Copiar `web-actual/` completa a `referencia/prototipo/` y construir sobre ella:
  - `Cursos.html` — hero del pivot ("Aprendé robótica. El kit va incluido.") + 3 cards de curso (nombre, nivel con badge de color, duración, precio del canon, CTA "Ver curso"). Reusar clases de `styles-components.css` (cards de kits del design).
  - `Curso-Semaforo.html` — detalle completo: hero, qué vas a construir, temario (4 clases del canon), nivel/duración, "Tu kit incluido" con la BOM (6 componentes del canon con SKU en monospace), precio único $89.900, CTA "Inscribirme — kit incluido". Los otros 2 cursos: cards al final ("Próximo paso").
  - Nav de todas las páginas del prototipo: agregar "Cursos".
- [ ] **Step 3:** Verificar con Playwright: navegación Home → Cursos → Curso-Semaforo → (CTA) Carrito; cero JS; datos idénticos al canon (grep de `89.900`, `SEN-DHT22` etc.).
- [ ] **Step 4:** Commit: `git commit -am "feat: prototipo de referencia de la sección Cursos + design original"`

### Task 6: BRIEF.md + OUTCOME.md

**Files:**
- Create: `caso-makerlab/BRIEF.md`
- Create: `caso-makerlab/outcome-esperado/OUTCOME.md`

- [ ] **Step 1:** `BRIEF.md` (la consigna del asistente): historia corta del cliente (3 párrafos: quién es MakerLab, el pivot que quiere gerencia, qué nos contrataron para hacer — SIN revelar los 3 cursos ni la contradicción); qué recibís (`material-cliente/`, `web-actual/`); qué se espera de vos (procesar el material con las skills, descubrir el pedido, escribir el spec, construir el prototipo HTML estático, subirlo a Gizmo); reglas (HTML estático puro, sin frameworks; el prototipo integra el design de la web actual).
- [ ] **Step 2:** `OUTCOME.md`: checklist de discovery (8 ítems: pivot identificado; 3 cursos y NO 5, citando qué documento lo resuelve; tabla curso→kit→precio completa y exacta vs canon; mecánica CTA única; desorden del catálogo detectado — SKU duplicado; el pedido es la sección Cursos; deadline 2 semanas; personas clave identificadas) + checklist del prototipo (6 ítems: estático sin React; design system integrado; listado + ≥1 detalle completo con temario/BOM/precio/CTA; navegable desde Home; datos del canon exactos; publicado en Gizmo).
- [ ] **Step 3:** Commit: `git commit -am "feat: brief del caso + outcome esperado"`

### Task 7: GUION-DEMO.md

**Files:**
- Create: `caso-makerlab/GUION-DEMO.md`

- [ ] **Step 1:** Escribir el runbook con las 6 fases del spec. Por fase: objetivo, qué hace Val en pantalla (comandos exactos), qué replican los asistentes, checkpoint verificable, rescate (qué copiar de dónde si te atrasaste), tiempo estimado. Total objetivo: ~2h30. Incluir: fase 0 setup (instalar `rufino-skills.zip`, descomprimir `caso-makerlab.zip`, chequear `/ask-rufino` vacío — 15'); fase 1 `/process-rufino caso-makerlab/material-cliente/` (~25'); fase 2 discovery con 4 preguntas guiadas a `/ask-rufino` (incluye "¿cuántos cursos quiere lanzar el cliente?" → momento contradicción — 20'); fase 3 spec con plan mode (25'); fase 4 prototipo (45'); fase 5 validación contra OUTCOME.md + subida a Gizmo (20'). Nota final: `outcome-esperado/` no se comparte hasta la fase 5.
- [ ] **Step 2:** Commit: `git commit -am "docs: guión de la demo paso a paso"`

### Task 8: Empaquetado + verificación E2E

**Files:**
- Create: `caso-makerlab.zip`

- [ ] **Step 1:** `zip -r caso-makerlab.zip caso-makerlab/BRIEF.md caso-makerlab/material-cliente caso-makerlab/web-actual -x "*.DS_Store"` y verificar con `unzip -l` que NO incluye `outcome-esperado/` ni `GUION-DEMO.md`.
- [ ] **Step 2:** Verificación E2E del discovery: subagente fresco con este prompt: "Sos un asistente del workshop. Leé caso-makerlab/BRIEF.md y procesá caso-makerlab/material-cliente/ siguiendo .claude/skills/process-rufino/SKILL.md; después respondé usando solo la base: (1) ¿qué pide el cliente?, (2) ¿cuántos cursos y cuáles?, (3) ¿qué componentes y precio tiene cada curso?, (4) ¿encontraste contradicciones en el material?". ⚠️ Antes de correrlo, vaciar o respaldar `~/Documents/projects/` para que el corpus del caso no se mezcle con la base demo previa.
- [ ] **Step 3:** Cotejar la respuesta contra `OUTCOME.md`: debe llegar a 3 cursos citando Slack/minuta, detectar la contradicción del mail de Marcos y el SKU duplicado. Si algo no se descubre, ajustar el corpus (más señal, no menos ruido) y repetir.
- [ ] **Step 4:** Commit final: `git commit -am "feat: caso-makerlab.zip + verificación E2E del discovery"`

---

## Self-review (hecho)

- **Cobertura del spec:** narrativa→canon (T1); corpus 11 archivos→T1/T2; xlsx en skill→T3; web actual→T4; outcome+referencia+prototipo backup→T5/T6; guión→T7; zip asistentes + verificación E2E→T8. Sin gaps.
- **Placeholders:** los textos del corpus se especifican con datos duros del canon + estructura por archivo (el wording exacto es trabajo creativo del executor, acotado por el canon — no es placeholder, es el contrato).
- **Consistencia:** SKUs, precios y fechas viven SOLO en el canon; toda task referencia el canon, nunca redefine valores.
