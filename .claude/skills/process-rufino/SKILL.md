---
name: process-rufino
description: Procesa notas crudas en cualquier formato (md, txt, pdf, docx, pptx, imágenes) y las convierte en notas .md augmentadas dentro de la base de conocimiento Rufino en ~/Documents/projects — con tags de 4 ejes, wikilinks, triples tipados y una carpeta por proyecto. Usala SIEMPRE que el usuario quiera procesar, guardar, archivar o "meter en sus notas" un documento, minuta, apunte, pdf o presentación, aunque no mencione la palabra "rufino" — frases como "procesá esta nota", "guardá este pdf en mis notas", "archivá la minuta de hoy".
argument-hint: <path-a-archivo(s)-o-carpeta>
---

# /process-rufino

Convertís notas crudas en notas procesadas de la base de conocimiento Rufino. Una nota procesada es un `.md` que contiene el contenido original intacto + una augmentation que lo resume, lo desafía y lo conecta con el resto de la base.

**Antes de procesar nada**, leé el spec canónico: [references/formato.md](references/formato.md). Define la estructura de la base, el formato de nota, los 4 ejes de tags, la augmentation, los triples y las reglas duras. Este SKILL.md solo describe el pipeline; el formato manda allá.

## Input

El argumento es uno o más paths a archivos, o una carpeta:

- **Archivo(s)**: procesar cada uno.
- **Carpeta**: procesar todos los archivos con formato soportado que no tengan ya `status: processed`.
- **Sin argumento**: revisar si hay crudos en `~/Documents/projects/_inbox/`; si los hay, procesarlos. Si no, preguntar al usuario qué quiere procesar.

## Pipeline

### 1. Bootstrap (solo la primera vez)

Si `~/Documents/projects/` no existe, crearla junto con `_index.md` y `_people.md` usando los templates de `formato.md` (tablas vacías, stats en 0). No crear `_people/`, `_conceptos/` ni `_inbox/` hasta que haga falta.

### 2. Leer el estado de la base

Leer `~/Documents/projects/_index.md` completo. De acá salen:

- Los **proyectos existentes** (para reusar antes de crear).
- El **vocabulario de tags vivo** (temas, conceptos, aristas ya usados).
- Las **candidatas a Connections** (por tags y resúmenes).

Si la nota menciona personas, leer también `_people.md`.

### 3. Extraer el contenido

Según el formato del archivo, seguir [references/extraccion.md](references/extraccion.md). El resultado es el contenido original que se embebe tal cual en la nota procesada.

### 4. Determinar proyecto, arista y carpeta destino

- **Proyecto** = la carpeta en `~/Documents/projects/<proyecto>/`. Inferirlo del contenido; reusar un proyecto existente del índice si encaja. Si la nota no pertenece a ningún proyecto puntual, va a `general/`.
- **Arista** = sub-área dentro del proyecto (va en el tag `proyecto/<nombre>/<arista>`, no en la estructura de carpetas).
- **Subcarpeta** = qué tipo de nota es → `decisiones/`, `aprendizajes/`, `docs/`, `notas/`, o una subcarpeta nueva si no encaja (ver "Ruteo" en `formato.md`). La nota final vive en `<proyecto>/<subcarpeta>/<filename>`.

Si el proyecto es genuinamente ambiguo entre dos existentes, preguntale al usuario con AskUserQuestion en vez de adivinar.

Si el proyecto es **nuevo** (la carpeta no existe), creá su `overview.md` esqueleto al final (paso 8) con lo que sepas de esta primera nota.

### 5. Generar la nota procesada

Siguiendo `formato.md` al pie de la letra:

1. Tags de 4 ejes (reuso > creación).
2. Augmentation: Resumen estructurado / Analisis (tiene que desafiar la nota) / Implicaciones + Context.
3. Connections: solo wikilinks a notas que existen; si no hay, "Sin conexiones relevantes aún".
4. Triples tipados en el frontmatter: uno por cada wikilink de Connections (default `references`), más los de personas cuando aplique (`decided-by`, etc. — ver la sección Triples de `formato.md`).

### 6. Personas

Por cada persona mencionada, crear o actualizar `_people/<nombre>.md` y el índice `_people.md` (sección Personas de `formato.md`).

### 7. Promoción de conceptos

Contar menciones de cada `concepto/<x>` en la base; con ≥2 menciones y sin página, crear `_conceptos/<x>.md` (sección Promoción de `formato.md`).

### 8. Escribir, overview y actualizar índices

1. Escribir la nota en `~/Documents/projects/<proyecto>/<subcarpeta>/<filename>` (la subcarpeta del paso 4; `decisiones/` lleva filename fechado).
   - Caso especial: si el input era un crudo de `_inbox/`, el crudo SE CONVIERTE en la nota procesada — `mv` del archivo de `_inbox/` a su subcarpeta destino y reescribirlo con la versión procesada (mismo contenido, relocado y augmentado). Nunca deben quedar dos copias: ni en el inbox ni como `-raw`.
   - Cualquier otro archivo fuente (el pdf en el Desktop, el docx en Downloads) queda donde está, intacto.
2. **`overview.md` del proyecto** (sección "`overview.md` por proyecto" de `formato.md`):
   - Proyecto nuevo → crear el esqueleto en `<proyecto>/overview.md`.
   - Proyecto existente → actualizar SOLO las secciones que esta nota cambia (Decisiones clave si fue una decisión, Estado actual si movió el estado, etc.) + `updated`. Incremental, no regenerar.
3. Actualizar `_index.md`: fila nueva en "Notas procesadas", tabla de Proyectos (con link al overview) y Stats.
4. **Cross-references**: revisar las notas existentes que esta nota referencia o que deberían referenciarla — agregarles el wikilink en su sección Connections y el triple correspondiente en su frontmatter.
   - **Batch grande** (procesás muchas notas juntas, ej. la primera ingesta): no intentes cerrar los cross-references nota por nota mientras escribís. Escribí primero todas las notas, y al final hacé UNA pasada de cierre: por cada par relacionado, asegurate de que el link y su triple inverso existan en ambas (`caused-by`↔`led-to`, `contradicts` simétrico). Es fácil dejar inversos a medias si lo hacés sobre la marcha.

## Reporte final

Al terminar, contale al usuario en 3-5 líneas: qué se procesó, a qué proyecto y subcarpeta fue cada nota (con path clickeable), qué tags y triples se generaron, si se creó o actualizó el `overview.md`, y si hubo personas registradas o conceptos promovidos. Sin transcribir la nota entera — el archivo habla.
