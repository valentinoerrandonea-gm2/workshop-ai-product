# Caso MakerLab Academy — diseño del outcome del workshop

**Fecha:** 2026-06-04
**Estado:** aprobado por Val
**Contexto:** segundo entregable del workshop de AI de GM2 (el primero fueron las skills Rufino, ya shippeadas en `.claude/skills/` + `rufino-skills.zip`). Este caso es el hilo conductor de la demo: Val lo resuelve en vivo y los asistentes lo siguen paso a paso (follow-along con checkpoints).

## El caso (narrativa)

**MakerLab Electrónica**: tienda online argentina de Arduino, Raspberry Pi y componentes, ~4 años operando. Su web actual es un ecommerce puro (home + catálogo + carrito) y su catálogo está desordenado: categorías inconsistentes, SKUs duplicados, precios desactualizados.

**El pivot**: gerencia quiere convertirse en **MakerLab Academy** — una escuela de hardware y robótica que vende sus productos. Cursos pagos donde **comprar el curso incluye el kit de componentes** ("un ecommerce camuflado de educación"). Ya saben qué cursos quieren y qué componentes lleva cada uno; no saben cómo mostrarlo en la web ni tienen equipo de desarrollo → contratan a GM2.

**El pedido (lo que el discovery debe destapar)**: un prototipo de la sección "Cursos" integrada a la web actual — listado de cursos + página de detalle (temario, nivel, duración, kit incluido con su lista de componentes, precio curso+kit, CTA de compra única).

**Los 3 cursos definitivos** (progresión pedagógica; derivan de los kits del design base):

| # | Curso | Nivel | Componentes (núcleo) |
|---|-------|-------|----------------------|
| 1 | Semáforo inteligente | Inicial | Arduino UNO, LEDs, resistencias, protoboard, jumpers, pulsador |
| 2 | Estación meteorológica IoT | Intermedio | Arduino/ESP, sensor DHT22, LCD, módulo WiFi |
| 3 | Robot evita-obstáculos | Avanzado | Chasis, motores DC, driver L298N, sensor ultrasónico HC-SR04 |

**La contradicción sembrada** (momento didáctico del discovery): un mail viejo del dueño propone **5** cursos; el Slack y la minuta de kickoff (posteriores) los bajan a **3**. Las skills la detectan con triples `contradicts`/`replaces` y `/ask-rufino` la resuelve citando las fuentes más recientes.

## El flujo de la demo (lo que hacen los asistentes)

1. Reciben el caso: `BRIEF.md` + `material-cliente/` + `web-actual/`. Todo local, sin dependencias externas.
2. **Procesan el corpus** con `/process-rufino` → base de conocimiento en `~/Documents/projects/`.
3. **Discovery** con `/ask-rufino`: qué pide el cliente, cuántos cursos, qué componentes, qué precios. Validan contra el outcome al final.
4. **Spec** del prototipo con planning de Claude (plan mode / brainstorming).
5. **Implementan** el prototipo de la sección Cursos: **HTML estático puro, sin React** — sobre la base de `web-actual/`.
6. **Validan** contra `outcome-esperado/OUTCOME.md` y suben el prototipo a **Gizmo** (plataforma interna de GM2).

## Estructura a crear en el repo

```
caso-makerlab/
├── BRIEF.md                      # consigna que reciben los asistentes (narrativa + qué hacer)
├── material-cliente/             # el corpus "que mandó el cliente" (~11 archivos)
├── web-actual/                   # la web HOY: HTML estático puro (sin React/Babel)
│   ├── Home.html                 #   sin secciones de tutoriales/kits/comunidad
│   ├── Catalogo.html             #   con el desorden visible (espejo del xlsx)
│   ├── Carrito.html
│   └── styles.css (+ assets compartidos)
├── outcome-esperado/
│   ├── OUTCOME.md                # checklist de validación del discovery + del prototipo
│   └── referencia/               # Tutorial.html y Kit-Detalle.html del design original
│                                 # + prototipo terminado de Val (backup de la demo)
└── GUION-DEMO.md                 # runbook de Val: fases, comandos, checkpoints, tiempos
```

## El corpus (`material-cliente/`, dificultad media)

Info clave repartida en 6 archivos, ruido realista en 5. Los formatos ejercitan toda la matriz de extracción de las skills (pptx, docx, pdf, xlsx, md, imagen):

| Archivo | Formato | Rol |
|---------|---------|-----|
| `vision-makerlab-academy.pptx` | pptx | CLAVE — slides de gerencia con la visión del pivot |
| `minuta-kickoff-gm2.docx` | docx | CLAVE — el pedido concreto a GM2, los 3 cursos definitivos, fecha más reciente |
| `mail-dueno-ideas-cursos.md` | md | CONTRADICCIÓN — mail viejo del dueño con 5 cursos |
| `slack-canal-pivot.md` | md | CLAVE — el equipo baja de 5 a 3 cursos, define precios |
| `catalogo-productos.xlsx` | xlsx | CLAVE — hoja "productos" desordenada (categorías inconsistentes, SKUs duplicados) + hoja "cursos" con el mapping curso→componentes |
| `temarios-cursos.pdf` | pdf | CLAVE — temario y duración de cada curso |
| `mail-queja-cliente.md` | md | ruido |
| `minuta-logistica.docx` | docx | ruido |
| `pizarra-brainstorm.png` | imagen | ruido (extracción multimodal — foto de pizarra con garabatos del pivot) |
| `mail-proveedor.md` | md | ruido |
| `politica-devoluciones.pdf` | pdf | ruido |

Reglas de generación del corpus:
- Español rioplatense, tono interno real (typos leves, informalidad en Slack/mails).
- Fechas coherentes: mail del dueño (viejo) → pptx gerencia → Slack → minuta kickoff (la más reciente, manda).
- Los datos duros (componentes, precios, SKUs) consistentes entre xlsx, Slack y temarios — salvo el desorden a propósito de la hoja "productos".
- El desorden del xlsx es el MISMO que se ve en `web-actual/Catalogo.html` (verosimilitud).

## Cambios a las skills (mínimos)

- `process-rufino/references/extraccion.md`: agregar **xlsx** (es un zip de XML — `xl/sharedStrings.xml` + `xl/worksheets/sheetN.xml`, mismo patrón que pptx/docx). Regenerar `rufino-skills.zip` después.

## Web actual (`web-actual/`)

Derivada del bundle de Claude Design (`arduino-raspberry-pi-web`, ya descargado). Trabajo: **aplanar a HTML+CSS estático puro** (el bundle monta React 18 + Babel standalone vía JSX — restricción de Val: nada de React). Conservar el sistema visual (Space Grotesk/Inter/JetBrains Mono, teal `#0BB07B`, detalles PCB). Quitar de la Home las secciones de tutoriales, kits curados y comunidad (la empresa hoy no las tiene). El catálogo muestra el desorden del caso.

## Outcome esperado (`outcome-esperado/OUTCOME.md`)

Dos checklists:
1. **Discovery correcto**: identificó el pivot; 3 cursos (no 5) con la fuente que lo resuelve; tabla curso→componentes→precio completa; mecánica curso+kit entendida; el pedido = sección Cursos sobre la web actual.
2. **Prototipo correcto**: HTML estático sin React; integra el design system de `web-actual/`; listado de cursos + al menos un detalle completo (temario, nivel, duración, BOM del kit, precio combinado, CTA única "Inscribirme con kit incluido"); navegable desde la Home.

`referencia/` guarda Tutorial.html y Kit-Detalle.html originales (a dónde apuntaba el design) y el prototipo terminado que Val construye como respaldo de la demo en vivo.

## Guión (`GUION-DEMO.md`)

| Fase | Qué pasa | Checkpoint |
|------|----------|------------|
| 0. Setup | Skills instaladas, carpeta del caso descargada | `/ask-rufino` responde "base vacía" |
| 1. Procesar | `/process-rufino caso-makerlab/material-cliente/` | Base creada, N notas, contradicción visible en triples |
| 2. Discovery | `/ask-rufino` ×3-4 preguntas guiadas | Respuesta "3 cursos, no 5" citando el Slack |
| 3. Spec | Plan mode / brainstorming → spec del prototipo | Spec escrito en el repo del asistente |
| 4. Prototipo | Implementación HTML estático de la sección Cursos | Página abre en el browser, navegable |
| 5. Validar + publicar | Cotejo contra OUTCOME.md, subida a Gizmo | URL en Gizmo funcionando |

Cada checkpoint tiene "rescate": el resultado pre-armado vive en el repo para que quien se atrasó copie y siga.

## Fuera de alcance (YAGNI)

- Checkout/carrito funcional del prototipo (es prototipo de UI, no ecommerce real).
- Backend, base de datos, pagos.
- Los 3 detalles de curso completos: con UNO alcanza para la demo (los otros dos pueden quedar como cards del listado).
- Demostrar `/rufino-ingest` en vivo (corpus 100% local por decisión de robustez; la skill se menciona).

## Verificación end-to-end

Antes del workshop: correr el flujo completo como un asistente fresco (subagente que solo ve BRIEF + material) y validar que (a) el discovery llega a los 3 cursos con la contradicción resuelta, (b) el spec sale completo, (c) el prototipo es construible en el tiempo de la demo.
