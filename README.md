# Rufino — Skills de Claude Code para el Workshop de AI

Rufino es un set de 3 skills que convierte notas sueltas y sin formato en una **base de conocimiento personal**: notas `.md` organizadas por proyecto, relacionadas entre sí con wikilinks, tags y triples tipados, y consultables en lenguaje natural.

```
        fuentes externas                archivos locales
     (Drive, Slack, Gmail...)        (md, pdf, docx, pptx)
              │                              │
              ▼                              ▼
       /rufino-ingest ──crudos──▶    /process-rufino
                                             │
                                             ▼
                                  ~/Documents/projects/
                                  (notas .md augmentadas,
                                   por proyecto, con tags,
                                   wikilinks y triples)
                                             │
                                             ▼
                                        /ask-rufino
                                  (preguntas con respuestas
                                   citando tus notas)
```

## Instalación

1. Descomprimí `rufino-skills.zip` dentro de `~/.claude/skills/` de tu máquina:

   ```bash
   unzip rufino-skills.zip -d ~/.claude/skills/
   ```

2. Verificá que quedaron las tres carpetas:

   ```
   ~/.claude/skills/
   ├── ask-rufino/
   ├── process-rufino/
   └── rufino-ingest/
   ```

3. Abrí (o reiniciá) Claude Code. Los comandos `/process-rufino`, `/ask-rufino` y `/rufino-ingest` ya están disponibles en cualquier sesión.

> Requisitos: macOS + Claude Code. Cero dependencias — la extracción de pdf/docx/pptx usa las capacidades multimodales de Claude y herramientas built-in del sistema. Para `/rufino-ingest` necesitás tener conectado el MCP de la fuente que quieras usar (`/mcp`).

## Los 3 comandos

### `/process-rufino <archivo-o-carpeta>`

Procesa notas crudas en cualquier formato (`md`, `txt`, `pdf`, `docx`, `pptx`, imágenes) y las convierte en notas de la base:

- Extrae el contenido (sin modificarlo — el original queda embebido tal cual).
- Le agrega una **augmentation**: resumen estructurado, un análisis que desafía la nota (contradicciones, riesgos, preguntas no obvias) e implicaciones.
- La taggea en **4 ejes**: `proyecto/<nombre>/<arista>`, `tema/<amplio>`, `persona/<nombre>`, `concepto/<específico>`.
- La conecta con notas existentes vía **wikilinks** y **triples tipados** (`references`, `depends-on`, `contradicts`, `refines`...).
- La guarda en `~/Documents/projects/<proyecto>/<tipo>/`, ruteándola por tipo (decisión, aprendizaje, doc formal, nota), y crea/actualiza el `overview.md` del proyecto.

```
/process-rufino ~/Desktop/minuta-reunion.pdf
```

### `/ask-rufino <pregunta>`

Responde preguntas usando exclusivamente el contenido de tus notas, citando las fuentes:

```
/ask-rufino qué decidimos sobre el piloto del asistente de soporte?
```

Si la base no tiene la respuesta, lo dice — no inventa.

### `/rufino-ingest <qué traer y de dónde>`

Trae contenido desde un servicio externo usando el MCP que indiques (Google Drive, Slack, Gmail, Notion...), lo guarda con proveniencia y lo procesa al formato Rufino:

```
/rufino-ingest traete los docs de la carpeta "specs" de mi Drive
/rufino-ingest importá los últimos 20 mensajes de #proyecto-retail en Slack
```

## La base de conocimiento

Todo vive en `~/Documents/projects/`:

```
~/Documents/projects/
├── _index.md                 # índice global de notas (lo mantiene Rufino)
├── _people.md                # índice de personas mencionadas
├── _people/<nombre>.md       # una página por persona, con sus menciones
├── _conceptos/<slug>.md      # páginas de concepto (auto-creadas con ≥2 menciones)
├── _inbox/                   # crudos de /rufino-ingest esperando proceso
└── <proyecto>/               # una carpeta por proyecto, estructurada por dentro:
    ├── overview.md           #   síntesis viva del proyecto (lo mantiene Rufino)
    ├── decisiones/           #   decisiones y acuerdos (fechados)
    ├── aprendizajes/         #   learnings, gotchas, insights
    ├── docs/                 #   documentos formales: specs, briefs, políticas
    └── notas/                #   ideas, apuntes, notas de trabajo
```

Cada proyecto no es una bolsa plana: tiene su `overview.md` y las notas repartidas por tipo (más subcarpetas propias si hacen falta, ej. `reuniones/`). Es markdown plano: podés abrirlo con Obsidian (los wikilinks y tags funcionan nativos), con cualquier editor, o dejar que `/ask-rufino` lo navegue por vos.

## Demo sugerida (con `notas-ejemplo/`)

1. `/process-rufino notas-ejemplo/minuta-kickoff-asistente-soporte.md` — mirá cómo crea la base, detecta el proyecto, registra a las personas y augmenta la nota.
2. `/process-rufino notas-ejemplo/idea-busqueda-semantica-docs.md` — esta nota comparte conceptos con la anterior: aparecen las **Connections**, los **triples** y la **promoción de conceptos** (`concepto/rag` llega a 2 menciones → nace `_conceptos/rag.md`).
3. `/process-rufino notas-ejemplo/apunte-costos-api.md` — una nota de 3 líneas: augmentation proporcional, sin inflar.
4. `/ask-rufino qué dudas planteó diego en el kickoff?` — respuesta citando `[[minuta-kickoff-asistente-soporte]]`.
5. `/ask-rufino qué notas tengo sobre RAG?` — navegación por concepto.

## Cómo está armado (para los curiosos)

- Cada skill es una carpeta con un `SKILL.md` (frontmatter `name` + `description` + instrucciones). La `description` es lo único que Claude ve siempre — decide cuándo disparar la skill.
- El spec del formato (tags, triples, augmentation) vive una sola vez en `process-rufino/references/formato.md` y las otras skills lo referencian por path relativo: *progressive disclosure* — el detalle se carga solo cuando hace falta.
- Para regenerar el zip después de editar las skills:

  ```bash
  cd .claude/skills && zip -r ../../rufino-skills.zip ask-rufino process-rufino rufino-ingest
  ```
