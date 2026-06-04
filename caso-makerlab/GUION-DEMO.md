# Guión de la demo — caso MakerLab Academy

> Runbook de Val. Los asistentes siguen cada fase en su máquina (follow-along).
> Duración objetivo: **~2h30** + buffer. Cada fase tiene un checkpoint y un
> rescate: el que se atrasó copia el resultado y sigue — nadie se queda mirando.

## Antes del workshop (checklist de Val)

- [ ] Compartir `rufino-skills.zip` y `caso-makerlab.zip` (link de descarga listo).
- [ ] Verificar que `outcome-esperado/` NO está dentro de `caso-makerlab.zip`.
- [ ] Tener el prototipo de referencia abierto en una pestaña aparte
      (`outcome-esperado/referencia/prototipo/Cursos.html`) — es el plan B si la
      implementación en vivo se complica.
- [ ] Probar el flujo de subida a Gizmo con un HTML cualquiera.
- [ ] Asistentes avisados: traer Claude Code instalado y logueado en macOS.

---

## Fase 0 — Setup (15 min)

**Objetivo:** todos con las skills instaladas y el caso descomprimido.

Qué hacen todos:

```bash
unzip rufino-skills.zip -d ~/.claude/skills/
unzip caso-makerlab.zip -d ~/Desktop/
```

Reiniciar Claude Code (las skills se cargan al inicio de sesión). Después, en
Claude Code:

```
/ask-rufino tengo algo en mi base?
```

**Checkpoint ✓**: responde que la base está vacía y sugiere `/process-rufino`.
Si alguien ya tiene una base en `~/Documents/projects/` de antes, que la renombre:
`mv ~/Documents/projects ~/Documents/projects-backup`.

**Mientras instalan, contás el caso** (2 min, sin spoilers): "MakerLab nos
contrató. Nos mandaron una carpeta con TODO lo que tenían: minutas, mails, su
Slack, un excel. Nuestro trabajo: entender qué quieren y construirles el
prototipo. Como en la vida real: nadie nos va a escribir el requerimiento limpio."

## Fase 1 — Procesar el corpus (25 min)

**Objetivo:** convertir los 11 archivos del cliente en una base de conocimiento.

```
/process-rufino ~/Desktop/caso-makerlab/material-cliente/
```

Mientras procesa, narrás lo que va pasando en pantalla:

- **La extracción multi-formato**: el pptx y el xlsx son zips de XML, el docx lo
  abre `textutil`, el PDF y el PNG los lee Claude directo (multimodal). Cero
  dependencias instaladas.
- **Los 4 ejes de tags** y cómo el índice se va armando.
- **El momento clave**: cuando procesa el mail de Marcos y el Slack, mirá el
  frontmatter — debería aparecer un triple `contradicts`/`replaces` entre ambos.
  Todavía no lo expliques del todo: "guarden esto, vuelve en la fase 2".

**Checkpoint ✓**: `ls ~/Documents/projects/` muestra el proyecto del caso con
~11 notas, `_index.md` poblado, `_people/` con los 4 del cliente.

**Rescate**: el que no terminó sigue mirando tu pantalla en fase 2 y procesa
después — las preguntas de discovery las puede correr contra tu narración.

## Fase 2 — Discovery con /ask-rufino (20 min)

**Objetivo:** descubrir el pedido real interrogando la base. Las 4 preguntas, en
este orden (la 3 es el momento de la demo):

```
/ask-rufino qué nos está pidiendo MakerLab exactamente?
/ask-rufino quiénes son las personas del cliente y qué rol tiene cada una?
/ask-rufino cuántos cursos quiere lanzar el cliente y cuáles son?
/ask-rufino qué componentes y qué precio tiene cada curso?
```

**El momento contradicción (pregunta 3)**: la respuesta correcta es **3 cursos**,
citando el Slack y la minuta — y mencionando que el mail de Marcos decía 5.
Pausa acá y mostrá el porqué: la base no eligió al azar, los triples tipados
(`replaces`, fechas) le dieron la cronología. Preguntale a la audiencia: "¿qué
hubiera pasado si solo procesábamos el mail del dueño?"

Bonus si hay tiempo: `/ask-rufino hay algún problema conocido con el catálogo?`
(→ SKU duplicado, categorías inconsistentes, citando a Tomás).

**Checkpoint ✓**: todos tienen la tabla curso→kit→precio correcta en pantalla.

**Rescate**: la tabla está en `outcome-esperado/canon.md` — pero NO la compartas
todavía; alcanzan con tu pantalla.

## Fase 3 — Spec con planning (25 min)

**Objetivo:** convertir el discovery en un spec del prototipo.

En Claude Code, **plan mode** (shift+tab) o brainstorming:

```
Basándote en mi base de Rufino (~/Documents/projects), escribí el spec del
prototipo que nos pidió MakerLab: sección Cursos en HTML estático integrada a
la web de ~/Desktop/caso-makerlab/web-actual/. Antes de escribirlo, haceme las
preguntas que necesites.
```

Puntos a narrar: cómo Claude consulta la base para el spec, las preguntas que
hace (alcance, qué curso detallar), y el spec resultante (páginas, contenido,
criterios). Insistí: **el spec cita las fuentes** — cada precio y cada SKU
trazan al material del cliente.

**Checkpoint ✓**: spec escrito (en el repo del asistente o donde Claude lo dejó),
con: 2 páginas (listado + detalle del Semáforo), datos del canon, regla "HTML
estático, CSS de web-actual".

## Fase 4 — Prototipo (45 min)

**Objetivo:** implementar la sección Cursos sobre `web-actual/`.

```
Ejecutá el spec: construí Cursos.html y Curso-Semaforo.html dentro de
~/Desktop/caso-makerlab/web-actual/, reusando styles.css y
styles-components.css, y agregá "Cursos" al nav de las páginas existentes.
HTML estático puro, sin JS.
```

Narrar mientras construye: reuso de componentes del design system (kit-cards,
badges de nivel, monospace para SKUs), la CTA única "Inscribirme — kit incluido",
la BOM del kit en el detalle.

**Checkpoint ✓**: `open ~/Desktop/caso-makerlab/web-actual/Cursos.html` —
navegable: Home → Cursos → Semáforo → CTA. Y `grep -ri "<script" *.html` vacío.

**Rescate**: tu prototipo de referencia (`outcome-esperado/referencia/prototipo/`)
— compartilo como zip SOLO a quien se trabó fuerte; que el resto termine el suyo
aunque sea más feo. El feo propio enseña más que el lindo ajeno.

## Fase 5 — Validación + Gizmo (20 min)

**Objetivo:** cotejar contra el outcome y publicar.

1. Ahora SÍ compartís `outcome-esperado/` (OUTCOME.md + canon.md + referencia).
2. Recorren juntos la checklist A (discovery) en voz alta — cada ítem, ¿quién lo
   tiene? ¿de qué documento salió?
3. Checklist B (prototipo) cada uno contra el suyo.
4. Suben el prototipo a **Gizmo** (flujo interno GM2) y pegan los links en el
   canal del workshop.

**Checkpoint final ✓**: links de Gizmo funcionando + las dos checklists
recorridas.

## Cierre (5 min)

El arco de la demo, en una frase: *"de una carpeta con 11 archivos desordenados
a un prototipo navegable y validado, sin escribir requerimientos a mano — el
conocimiento quedó en una base consultable que va a seguir sirviendo después del
prototipo"*. Lo que se llevan: las skills instaladas y el patrón
ingest → process → ask → spec → build.

---

## Apéndice: tiempos y plan B

| Fase | Tiempo | Si te quedás corto de tiempo |
|------|--------|------------------------------|
| 0 Setup | 15' | — (no comprimible) |
| 1 Procesar | 25' | Procesar solo los 6 archivos clave (mail dueño, pptx, slack, temarios, minuta kickoff, xlsx) |
| 2 Discovery | 20' | Preguntas 1 y 3 solamente |
| 3 Spec | 25' | Mostrar el spec tuyo en pantalla en vez de que cada uno genere el suyo |
| 4 Prototipo | 45' | Detalle del curso solo (sin listado), o mostrar la referencia |
| 5 Validación | 20' | Checklist A solamente; Gizmo queda de tarea |

Plan B total (demo muere): el prototipo de referencia + el canon cuentan la
historia completa en 10 minutos.
