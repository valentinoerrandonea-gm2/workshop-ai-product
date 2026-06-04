---
name: ask-rufino
description: Responde preguntas del usuario usando su base de conocimiento Rufino (~/Documents/projects), citando las notas fuente con wikilinks. Usala SIEMPRE que el usuario pregunte sobre sus notas, sus proyectos, reuniones pasadas, decisiones tomadas o cualquier cosa que pueda estar guardada en su base — frases como "qué dijimos de X", "qué notas tengo sobre Y", "según mis notas...", "buscá en rufino".
argument-hint: <pregunta>
---

# /ask-rufino

Respondés la pregunta del usuario basándote EXCLUSIVAMENTE en las notas de `~/Documents/projects/`. El valor de esta skill es que las respuestas están ancladas en lo que el usuario realmente escribió — no en conocimiento general.

El formato de la base (tags de 4 ejes, triples, índices) está en [../process-rufino/references/formato.md](../process-rufino/references/formato.md) — leelo si necesitás entender la estructura para navegar mejor.

## Flujo

### 1. ¿Existe la base?

Si `~/Documents/projects/` o su `_index.md` no existen, la base está vacía: decilo y sugerí `/process-rufino` para cargar las primeras notas. No inventes una respuesta.

### 2. Identificar candidatas por el índice

Leer `~/Documents/projects/_index.md`. La tabla "Notas procesadas" tiene tags y resumen de una línea por nota — con eso identificás qué notas pueden contener la respuesta sin leer toda la base.

### 3. Buscar más allá del índice si hace falta

Si el índice no alcanza (la pregunta usa palabras que no aparecen en tags ni resúmenes), Grep sobre `~/Documents/projects/` con los términos clave de la pregunta **y sus sinónimos** (case-insensitive). Las notas crudas usan el vocabulario del usuario, no el tuyo.

Cuidado con los falsos positivos por subcadena: buscar "pod" matchea "podría". Usar word boundaries (`-w`) o verificar el contexto de cada match antes de tratarlo como evidencia.

### 4. Leer y expandir una vuelta

Read de las notas candidatas completas (original + augmentation). Desde ahí, seguir **un salto** de contexto — la expansión completa de cada candidata (sus wikilinks, sus triples, las páginas de persona o concepto que toque), pero no los links de los links:

- Los wikilinks de sus secciones Connections.
- Los `triples:` del frontmatter — la relación tipada te dice si vale la pena seguirlo (`contradicts` y `replaces` son críticos: puede haber una nota más nueva que invalide lo que estás por citar).
- Si la pregunta es sobre una persona, leer `_people/<nombre>.md` y sus menciones.
- Si es sobre un concepto, arrancar por `_conceptos/<slug>.md` si existe.

### 5. Responder

En español, con esta estructura:

1. **La respuesta directa primero** — lo que el usuario preguntó, sintetizado desde las notas.
2. **Fuentes** — lista de las notas usadas: `[[slug]]` + path clickeable (`~/Documents/projects/<proyecto>/<slug>.md`) + una línea de por qué es relevante.

Citar SOLO notas que efectivamente leíste. Si dos notas se contradicen, mostrá ambas versiones con sus fechas — no elijas en silencio.

### 6. Honestidad ante todo

Si la base no tiene la respuesta: decilo claramente, mencioná qué notas cercanas al tema existen (si las hay), y en Fuentes poné "ninguna nota citada". Si el usuario esperaba tener ese material, sugerí `/process-rufino` para incorporarlo. Si agregás conocimiento general tuyo para completar, marcalo explícitamente ("esto no está en tus notas, pero..."). Nunca presentes conocimiento general como si saliera de la base.
