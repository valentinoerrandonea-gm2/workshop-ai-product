# Consigna — Caso MakerLab

> Este documento explica **todo lo que tenés que hacer** en el ejercicio, de
> principio a fin. La historia del cliente está en [BRIEF.md](BRIEF.md); acá está
> tu tarea concreta, paso a paso.

## El objetivo en una frase

Partiendo de un montón de material desordenado que mandó el cliente, descubrir
qué nos están pidiendo y entregar un **prototipo navegable de la sección de
cursos** integrado a la web que MakerLab ya tiene — usando Claude Code de punta a
punta (procesar → entender → planificar → construir → publicar).

No vas a escribir código a mano ni necesitás saber programar. Vas a **dirigir** a
Claude en cada paso.

## Lo que recibís

- **`material-cliente/`** — todo lo que mandó el cliente: minutas, mails, una
  conversación de Slack, una presentación, una foto y un Excel. Crudo,
  desordenado, y no todo dice lo mismo.
- **`web-actual/index.html`** — la web que MakerLab tiene hoy: un único archivo
  HTML autocontenido (estilos y navegación adentro, sin dependencias). Es tu punto
  de partida; abrilo en el navegador y recorrelo (Inicio · Catálogo · Carrito).
- Las **skills de Rufino** ya instaladas en Claude Code (`/process-rufino`,
  `/ask-rufino`, `/rufino-ingest`).

## Antes de empezar (setup)

1. Tené las skills instaladas: descomprimí `rufino-skills.zip` en `~/.claude/skills/`
   y reiniciá Claude Code.
2. Descomprimí el material del caso (`caso-makerlab.zip`) en un lugar cómodo (ej.
   tu Escritorio).
3. Verificá que tu base de Rufino arranca vacía: corré `/ask-rufino tengo algo en mi base?`
   — tiene que decir que no hay nada todavía.

## El paso a paso

### Paso 1 — Procesar el material del cliente

Convertí el material crudo en una base de conocimiento ordenada:

```
/process-rufino <ruta-a>/caso-makerlab/material-cliente/
```

Claude va a leer cada archivo (sí, también el PDF, el Excel, la presentación y la
foto), entender de qué trata, y guardarlo como notas ordenadas en
`~/Documents/projects/`, agrupadas por proyecto y por tipo (decisiones,
documentos, notas...), con un `overview.md` que resume el proyecto. **Mirá cómo
queda esa carpeta**: pasaste de un cajón de archivos sueltos a una base navegable.

### Paso 2 — Descubrir qué nos están pidiendo

Acá está el corazón del ejercicio. Interrogá tu base con `/ask-rufino` hasta tener
clarísimo el pedido. Preguntas que conviene hacer:

```
/ask-rufino ¿qué nos está pidiendo el cliente exactamente?
/ask-rufino ¿cuántos cursos quiere lanzar y cuáles son?
/ask-rufino ¿qué componentes y qué precio tiene cada curso?
/ask-rufino ¿hay contradicciones en lo que mandó el cliente?
```

**Ojo**: el material tiene ruido y no todos los documentos están de acuerdo entre
sí. Parte del trabajo es darte cuenta de eso y resolver con qué versión quedarte
(pista: cuando dos documentos se contradicen, el más reciente suele ganar — y
Claude te puede mostrar las fechas y las fuentes). No avances al paso 3 hasta
poder responder, con seguridad y citando de dónde sale cada dato: qué hay que
construir, cuántos cursos, qué lleva cada uno y a qué precio.

### Paso 3 — Escribir el spec del prototipo

Con el pedido claro, pedile a Claude que escriba el **spec** de lo que vas a
construir, apoyándose en tu base. Conviene usar el **plan mode** (que proponga un
plan y lo apruebes antes de que toque nada):

```
Basándote en mi base de Rufino, escribí el spec del prototipo de la sección de
cursos que pide MakerLab, integrada a la web de caso-makerlab/web-actual/.
Haceme las preguntas que necesites antes de escribirlo.
```

El spec tiene que decir qué páginas hay, qué lleva cada una, y de dónde sale cada
dato (todo del material del cliente, nada inventado).

### Paso 4 — Construir el prototipo

Pedile a Claude que ejecute el spec agregando la sección de cursos **dentro de
`web-actual/index.html`** (mismo archivo, reutilizando los estilos embebidos y el
menú que ya tiene). El entregable mínimo:

- **Una vista de listado** con los cursos (nombre, nivel, duración, precio).
- **Al menos una vista de detalle de curso** completa: qué vas a construir, el
  temario, nivel y duración, el **kit de componentes incluido** con su lista, el
  **precio único**, y **un solo botón** de inscripción ("Inscribirme — kit incluido").
- Un link **"Cursos"** en el menú, y que se navegue sin salir del archivo.

Todo queda en un único `index.html` autocontenido — ideal para subirlo a Gizmo.
- **Navegable desde la home** de la web actual (un link "Cursos" en el menú).

### Paso 5 — Validar

Cuando tengas el prototipo, cotejalo contra el `outcome-esperado/` (tu instructor
lo comparte en esta etapa): ¿llegaste al pedido correcto? ¿el prototipo cumple
con todo lo de arriba? ¿los datos coinciden con el material del cliente?

### Paso 6 — Publicar

Subí tu prototipo a **Gizmo** (la plataforma interna) y compartí el link.

## Las reglas

- **HTML estático puro**: sin React, sin frameworks, sin pasos de build. Lo que el
  navegador abre, es.
- **Se tiene que sentir parte de la web actual**: mismo diseño, misma navegación.
  Reutilizá los estilos que ya están embebidos en `web-actual/index.html`, no
  inventes un estilo nuevo.
- **El contenido sale del material del cliente, no de tu imaginación**: cada
  curso, precio, componente y texto tiene una fuente en lo que mandó MakerLab.
- **No hace falta checkout real ni backend**: es un prototipo para validar el
  concepto, no la tienda final.

## Cómo sabés que lo lograste

- Podés explicar el pedido (qué, cuántos cursos, qué incluye cada uno, a qué
  precio) **citando de qué documento sale cada cosa**, y resolviste las
  contradicciones del material.
- Tenés un spec escrito antes de haber construido.
- El prototipo abre en el navegador, se navega desde la home, se siente parte de
  la web actual, y sus datos coinciden con el material del cliente.
- Está publicado en Gizmo y el link funciona.
