# Rufino — Formato canónico de notas

Spec compartido por `/process-rufino`, `/ask-rufino` y `/rufino-ingest`. Si una skill contradice este archivo, gana este archivo.

## La base de conocimiento

Todo vive en `~/Documents/projects/`:

```
~/Documents/projects/
├── _index.md                 # índice global: tabla de notas procesadas
├── _people.md                # índice de personas
├── _people/<nombre>.md       # una página por persona mencionada
├── _conceptos/<slug>.md      # páginas de concepto (promoción automática)
├── _inbox/                   # crudos de /rufino-ingest esperando proceso
└── <proyecto>/<nota>.md      # notas procesadas, una carpeta por proyecto
```

Las carpetas meta llevan `_` al inicio para que nunca colisionen con el nombre de un proyecto.

## Estructura de una nota procesada

Una nota = UN solo archivo `.md`. El contenido original queda embebido arriba del separador, la augmentation abajo. Nunca crear copias `-raw` ni dejar el archivo fuente duplicado dentro de `projects/`.

```markdown
---
tags:
  - proyecto/<nombre>/<arista>
  - tema/<amplio>
  - persona/<nombre>
  - concepto/<específico>
status: processed
source: <path absoluto o URL del archivo original>
created: YYYY-MM-DD
processed: YYYY-MM-DD
triples:
  - { r: references, o: <slug-de-otra-nota> }
---

# <Título descriptivo>

<CONTENIDO ORIGINAL — exactamente como fue escrito, sin modificaciones>

---

## Rufino Augmentation

### Resumen estructurado

### Analisis

### Implicaciones

## Context

## Connections
```

**Filename**: slug kebab-case del título, sin espacios, acentos ni mayúsculas. Ej: `minuta-kickoff-asistente-soporte.md`.

**`created`** = fecha del contenido original si se puede inferir (fecha mencionada en la nota, fecha del archivo); ante una fecha relativa o ambigua ("el martes", "la semana pasada"), usar la fecha de modificación del archivo fuente; último recurso, la de hoy. **`processed`** = hoy.

## Tags de 4 ejes

Entre 4 y 10 tags por nota, distribuidos así:

| Eje | Formato | Mínimo | Qué captura | Ejemplos |
|-----|---------|--------|-------------|----------|
| proyecto | `proyecto/<nombre>/<arista>` | 1 | Proyecto + sub-área | `proyecto/oiko/producto`, `proyecto/umbru/matching` |
| tema | `tema/<amplio>` | 1 | Tópico amplio | `tema/ai`, `tema/arquitectura`, `tema/finanzas` |
| persona | `persona/<nombre>` | 0 | Personas mencionadas (una por persona) | `persona/gabi`, `persona/diego` |
| concepto | `concepto/<específico>` | 1 | Concepto puntual | `concepto/embeddings`, `concepto/rag` |

**Regla del concepto**: un concepto es algo que alguien googlearía si lo viera por primera vez — entidades técnicas, herramientas, técnicas, ideas con nombre propio. Los tópicos amplios van en `tema/`, no acá. Evitar baldes genéricos (`concepto/cosas-de-ai` ❌). Si hay más conceptos candidatos que cupo, priorizar los más centrales: los que usarías para reencontrar esta nota en seis meses.

**Regla de reuso**: antes de crear un proyecto, arista, tema o concepto nuevo, leer `_index.md` y reusar los existentes si encajan. La fragmentación de vocabulario mata la utilidad del grafo — `tema/ai` y `tema/inteligencia-artificial` conviviendo es peor que cualquiera de los dos solo.

**Arista**: sub-área dentro del proyecto (`producto`, `arquitectura`, `ux`, `negocios`, `operaciones`...). La lista es abierta — si ninguna arista existente describe la nota, crear la que corresponda, pero elegir UNA sola: la dominante. Si la nota cruza varias sin que ninguna domine, usar `general`.

## Augmentation

Tres secciones bajo `## Rufino Augmentation`, todas en español (términos técnicos en inglés, sin traducir):

- **Resumen estructurado** — reescritura limpia del contenido con headers, tablas y bullets. Ordena lo que la nota cruda dice desordenado.
- **Analisis** — DEBE plantear al menos una contradicción interna, un riesgo no mencionado, o una pregunta no obvia. Si solo describe o resume, no es análisis — reescribilo hasta que desafíe la nota. Usar tablas para comparaciones e incluir números cuando se pueda.
- **Implicaciones** — contexto amplio: cómo conecta esto con otros proyectos, con el trabajo o con los intereses del usuario.

Después:

- **`## Context`** — explicar los conceptos clave mencionados, con el detalle técnico que agrega valor. No sobre-explicar lo obvio: explicar lo que alguien necesitaría googlear.
- **`## Connections`** — conexiones REALES con otras notas de la base (ver abajo) + preguntas abiertas + follow-ups sugeridos.

## Connections y wikilinks

Buscar notas relacionadas leyendo `_index.md` (y las notas candidatas si hace falta). Cada conexión:

```markdown
- [[slug-de-la-nota]] — una línea explicando POR QUÉ está relacionada
```

Si no hay conexiones reales, escribir exactamente: **"Sin conexiones relevantes aún"**. NUNCA fabricar links a notas que no existen — la honestidad de un no-link vale tanto como un link. Verificar que el archivo destino existe antes de linkear.

## Triples tipados

Los triples capturan las relaciones tipadas de esta nota con otros nodos de la base: **uno por cada wikilink de Connections**, más relaciones a personas registradas cuando la nota lo amerite (ej. `decided-by` hacia quien tomó la decisión que la nota documenta — la persona no necesita aparecer en Connections). Clasificar cada relación con este vocabulario canónico:

| Relación | Cuándo usarla |
|----------|---------------|
| `depends-on` | La idea/decisión de esta nota requiere que la linkeada sea cierta o esté hecha antes |
| `blocks` | Esta nota impide avanzar con la linkeada |
| `caused-by` | La situación de esta nota surgió por la linkeada |
| `led-to` | Esta nota resultó en la linkeada |
| `references` | Mención genérica sin semántica más fuerte — **DEFAULT** |
| `contradicts` | Lo que afirma esta nota es incompatible con la linkeada |
| `refines` | Esta nota clarifica o mejora la linkeada |
| `replaces` | Esta nota reemplaza/deja obsoleta la linkeada |
| `decided-by` | Una persona tomó la decisión que esta nota documenta (objeto = persona) |
| `learned-in` | Este aprendizaje salió del proyecto/reunión linkeado |

En el frontmatter:

```yaml
triples:
  - { r: references, o: otra-nota }
  - { r: decided-by, o: gabi }
```

- El sujeto es implícito (la nota actual). El objeto es el slug del archivo destino (basename sin `.md`); para personas, solo el nombre (`gabi`, no `_people/gabi`).
- Default `references` cuando el contexto es ambiguo: mejor un triple genérico que ningún triple.
- Deduplicar: si `(r, o)` ya existe en la nota, no repetirlo.
- Solo emitir triples a objetos que EXISTEN (nota, persona o concepto con archivo). Un triple a un slug inexistente es un link roto.
- **Inversos** (para el triple de vuelta al hacer cross-references): `caused-by` ↔ `led-to`; `contradicts` es simétrico (mismo en ambas); para el resto del vocabulario no hay inverso definido — usar `references`. No inventar relaciones fuera del vocabulario canónico.

## Personas

Detectar personas por nombre, rol ("mi jefe", "el cliente", "la dev del proyecto") o apodo. Cruzar con `_people.md` para resolver roles y apodos a nombres; si no hay match, registrar con lo que se tenga.

Por cada persona mencionada:

- **Si existe** `_people/<nombre>.md`: actualizar `updated` en el frontmatter y agregar a la sección "## Menciones": `- [[<slug-de-la-nota>]] — YYYY-MM-DD — contexto: <una línea>`
- **Si no existe**: crear `_people/<nombre>.md`:

```markdown
---
tags:
  - tipo/persona
  - persona/<nombre>
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

# <Nombre>

<Contexto inferido de la nota: quién es, relación, en qué proyectos aparece.>

## Menciones

- [[<slug-de-la-nota>]] — YYYY-MM-DD — contexto: <una línea>
```

Después, actualizar el índice `_people.md` (tabla: Nombre | Relación | Proyectos | Menciones | Archivo — en la columna Archivo, linkear como `[[_people/<nombre>]]`).

## Promoción de conceptos

Después de taggear, contar en cuántas **notas distintas** aparece cada `concepto/<x>` como tag. Ojo con el conteo: `_index.md` replica los tags de cada nota en su tabla, así que un grep ingenuo cuenta doble — excluir los archivos meta (`_index.md`, `_people.md`, `_people/`, `_conceptos/`) y contar solo notas dentro de las carpetas de proyecto. Para cada concepto presente en **≥2 notas** y sin página en `_conceptos/<x>.md`, crearla:

```markdown
---
tags:
  - tipo/concepto
  - concepto/<x>
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

# <Concepto>

<Definición de 2-3 oraciones: qué es y por qué importa en el contexto de estas notas. NUNCA inventar hechos sin evidencia.>

## Menciones

- [[<nota-1>]]
- [[<nota-2>]]

## Relacionado

```

## `_index.md`

```markdown
---
tags:
  - tipo/meta
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

# Rufino — Índice de notas

> Mantenido automáticamente por las skills de Rufino. No editar a mano.

## Proyectos

| Proyecto | Notas |
|----------|-------|
| `<proyecto>/` | N |

## Notas procesadas

| Nota | Proyecto/Arista | Tags | Resumen | Fecha |
|------|-----------------|------|---------|-------|
| [[slug]] | proyecto/arista | tema/x, concepto/y, persona/z | Resumen en una línea. | YYYY-MM-DD |

## Stats

- Total notas: N
- Proyectos: N
- Conceptos con página: N
- Personas: N
- Última ejecución: YYYY-MM-DD
```

## Reglas duras

- NUNCA modificar el contenido original de una nota — se embebe tal cual, errores incluidos.
- NUNCA borrar archivos. Solo crear, mover y editar.
- NUNCA tocar archivos fuera de `~/Documents/projects/` (el archivo fuente original queda donde está, intacto).
- Una nota = un solo `.md` (original + augmentation juntos).
- Idioma: español. Términos técnicos en inglés sin traducir. Si la nota original está en inglés, la augmentation va en español igual.
- Nota muy corta (<20 palabras): procesar igual, con augmentation proporcional — no inflar.
- Si una nota ya tiene `status: processed` en el frontmatter, no reprocesarla.
