# Rufino — Extracción de contenido por formato

Cero dependencias externas: todo se resuelve con las capacidades multimodales de Claude Code y herramientas que ya vienen en macOS. No instalar nada.

| Formato | Cómo extraer |
|---------|--------------|
| `.md`, `.txt` | Read directo |
| `.pdf` | Read directo (es multimodal: lee texto, tablas e imágenes escaneadas). Si tiene más de 10 páginas, usar el parámetro `pages` en tandas |
| `.png`, `.jpg`, `.heic`, capturas | Read directo (multimodal) |
| `.docx`, `.doc`, `.rtf`, `.odt` | `textutil` (built-in de macOS, ver abajo) |
| `.pptx` | Es un zip de XML — `unzip -p` + limpiar tags (ver abajo) |
| `.xlsx` | También es un zip de XML — dos variantes según quién lo guardó (ver abajo) |
| `.ppt`, `.xls` (binarios legacy) | Sin soporte nativo. Pedir al usuario que lo exporte al formato moderno o PDF |

## Word (.docx, .doc, .rtf, .odt)

```bash
textutil -convert txt -stdout "/path/al/archivo.docx"
```

Si `textutil` falla con un `.docx` (raro, pero pasa con archivos generados por herramientas no-Microsoft), el `.docx` también es un zip de XML:

```bash
unzip -p "/path/al/archivo.docx" word/document.xml | grep -o '<w:t[^>]*>[^<]*' | sed 's/<w:t[^>]*>//'
```

## PowerPoint (.pptx)

Un `.pptx` es un zip. El texto de cada slide vive en `ppt/slides/slideN.xml` dentro de tags `<a:t>`.

```bash
# 1. Ver cuántas slides hay (y si hay speaker notes)
unzip -l "/path/al/deck.pptx" | grep -E 'ppt/(slides|notesSlides)/[^_]'

# 2. Extraer el texto de cada slide, EN ORDEN NUMÉRICO
unzip -p "/path/al/deck.pptx" ppt/slides/slide1.xml | grep -o '<a:t>[^<]*' | sed 's/<a:t>//'
unzip -p "/path/al/deck.pptx" ppt/slides/slide2.xml | grep -o '<a:t>[^<]*' | sed 's/<a:t>//'
# ... etc
```

Cuidados:

- **Orden numérico, no lexicográfico**: `slide10.xml` ordena antes que `slide2.xml` si se usa un glob. Iterar slide por slide (`slide1`, `slide2`, ..., `slide10`) para preservar el orden de la presentación.
- **Speaker notes**: si existen `ppt/notesSlides/notesSlideN.xml`, extraerlas igual — suelen tener el contenido más valioso de la presentación.
- Marcar cada slide en el contenido extraído (`## Slide 1`, `## Slide 2`...) para que la estructura sobreviva a la conversión.

## Excel (.xlsx)

Un `.xlsx` es un zip. Primero ver qué hojas tiene:

```bash
unzip -p "/path/al/archivo.xlsx" xl/workbook.xml | grep -o 'name="[^"]*"'
```

Los textos de las celdas viven en uno de dos lugares según qué herramienta guardó el archivo:

```bash
# Variante 1 — Excel real (Microsoft): strings compartidos en sharedStrings.xml
unzip -p "/path/al/archivo.xlsx" xl/sharedStrings.xml | grep -o '<t[^>]*>[^<]*' | sed 's/<t[^>]*>//'

# Variante 2 — generado por librerías (openpyxl, etc.): strings inline en cada hoja
unzip -p "/path/al/archivo.xlsx" xl/worksheets/sheet1.xml | grep -o '<t>[^<]*' | sed 's/<t>//'
```

Probá la 1; si `unzip` dice "filename not matched", es la 2. Los valores numéricos están siempre en la hoja (`xl/worksheets/sheetN.xml`) dentro de `<v>`:

```bash
unzip -p "/path/al/archivo.xlsx" xl/worksheets/sheet1.xml | grep -o '<v>[^<]*' | sed 's/<v>//'
```

Cuidados:

- En la variante sharedStrings, las celdas de texto de la hoja guardan **índices** (`t="s"`, `<v>3</v>` = el cuarto string del sharedStrings) — para tablas chicas conviene reconstruir la tabla leyendo ambos XML lado a lado.
- Cada hoja es un `sheetN.xml` distinto: extraer todas, no solo la primera. El orden de `workbook.xml` es el orden visible de las pestañas.
- Si la planilla es grande o con fórmulas complejas, pedir al usuario un export a CSV en vez de pelear con el XML.

## Después de extraer

El texto extraído es el "contenido original" de la nota: embebido tal cual en el `.md` procesado (ver `formato.md`). Corregir solo artefactos obvios de la extracción (tags XML sueltos, líneas vacías repetidas) — nunca el contenido en sí. Registrar el path del archivo fuente en el frontmatter `source:`.
