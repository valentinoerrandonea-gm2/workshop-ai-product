---
name: rufino-ingest
description: Trae contenido externo a la base de conocimiento Rufino usando el MCP que el usuario indique (Google Drive, Slack, Gmail, Notion, Jira, etc.) — lo recopila, lo guarda como crudo en ~/Documents/projects/_inbox y lo procesa al formato Rufino. Usala SIEMPRE que el usuario quiera importar, traer o ingestar documentos, mails, mensajes, tickets o archivos desde un servicio externo hacia sus notas — frases como "traé mis docs del Drive", "importá los mensajes de #canal", "meté estos mails en rufino".
argument-hint: <qué traer y desde qué servicio>
---

# /rufino-ingest

Conectás una fuente externa (vía MCP) con la base de conocimiento Rufino: recopilás el contenido que el usuario pida, lo guardás como crudo con proveniencia, y lo procesás al formato canónico.

## Flujo

### 1. Clarificar el pedido

Necesitás tres cosas antes de tocar nada. Si alguna falta o es ambigua, preguntá con AskUserQuestion:

- **Fuente**: qué MCP usar (Google Drive, Slack, Gmail, Notion, etc.).
- **Alcance**: qué traer exactamente — una búsqueda, una carpeta, un canal, un rango de fechas, ítems puntuales.
- **Volumen**: cuántos ítems espera. Ingerir 200 mails cuando quería 5 es peor que preguntar.

### 2. Cargar las tools del MCP

Las tools de MCP suelen estar deferred: cargalas con ToolSearch (ej: `"+gdrive search"` o `"select:mcp__..."`) antes de llamarlas. Si el MCP que pidió no está conectado, decile que lo conecte con `/mcp` y frenás ahí — no improvises con otra fuente.

### 3. Recopilar

1. Primero **listar/buscar** (metadata: títulos, fechas, ids) — todavía sin traer contenido completo.
2. Si la lista es ambigua o tiene más de ~10 ítems, mostrásela al usuario y confirmá qué entra antes de seguir.
3. Traer el **contenido completo** de cada ítem confirmado. Documentos de Drive: exportar/leer como texto. Threads de Slack o Gmail: el thread completo, con autores y fechas.

### 4. Guardar los crudos en `_inbox/`

Un `.md` por ítem en `~/Documents/projects/_inbox/`, con naming `<fuente>-import-<slug>-<YYYY-MM-DD>.md` (ej: `gdrive-import-spec-onboarding-2026-06-03.md`) y frontmatter de proveniencia:

```markdown
---
source: <mcp> (gdrive | slack | gmail | ...)
origin_id: <id o URL del ítem en el servicio de origen>
origin_date: <fecha del contenido original, si se conoce>
imported: YYYY-MM-DD
---

<contenido extraído, sin modificar>
```

¿Por qué pasar por `_inbox/` en vez de procesar directo? Si el procesamiento falla a mitad de camino, los crudos ya están a salvo localmente y el retry no vuelve a pegarle a la API externa.

### 5. Procesar

Correr el pipeline de `/process-rufino` sobre los crudos del inbox: leé [../process-rufino/SKILL.md](../process-rufino/SKILL.md) y su `references/formato.md`, y seguilos. Cada crudo termina como nota procesada en `~/Documents/projects/<proyecto>/` y sale del inbox.

### 6. Reporte final

Tabla corta: qué se trajo → de dónde → en qué nota/proyecto terminó. Si algún ítem falló (sin permisos, contenido no extraíble), listalo aparte con el motivo — no lo escondas.

## Reglas

- Solo LECTURA sobre el servicio externo: nunca modificar, mover ni borrar nada en la fuente.
- Respetar el alcance confirmado: no traer "ya que estamos" ítems que el usuario no pidió.
- Contenido no extraíble (imagen sin OCR, archivo binario raro): igual crear el crudo con la metadata y anotar "sin contenido extraíble" — la proveniencia vale aunque el contenido no esté.
