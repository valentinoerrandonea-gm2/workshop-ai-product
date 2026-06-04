# Caso: MakerLab Electrónica

> Tu consigna para el workshop. Leé esto primero.

## El cliente

**MakerLab Electrónica** es una tienda online argentina de Arduino, Raspberry Pi y
componentes electrónicos, con casi cinco años de operación. Les va razonablemente
bien, pero el margen se achica, compiten por precio contra importados directos, y
su catálogo —en la web y en el excel interno— creció sin orden durante años.

Hace unos meses, desde la gerencia empezaron a empujar un cambio grande: dejar de
ser solamente una tienda y convertirse en una **plataforma de educación sobre
hardware y robótica que vende sus propios productos**. La idea, en sus palabras,
es que la gente no compre componentes sueltos sino proyectos completos: cursos
pagos donde el kit de componentes va incluido en la inscripción.

Ellos ya tienen el negocio pensado — saben qué cursos quieren dar, quién los va a
dictar y qué componentes lleva cada uno. Lo que **no** tienen es la capacidad de
desarrollo para mostrarlo en su web, ni del todo claro cómo debería verse. Por eso
nos contrataron a nosotros (GM2).

## Qué recibís

- **`material-cliente/`** — todo lo que el cliente nos mandó: minutas, mails,
  conversaciones internas, presentaciones, fotos y su famoso excel del catálogo.
  Está tal cual nos lo dieron: desordenado, con ruido, y no todo dice lo mismo.
- **`web-actual/`** — la web que MakerLab tiene HOY (HTML estático). Abrila en el
  browser y recorrela: es tu punto de partida.

## Qué se espera de vos

1. **Procesá el material** del cliente con las skills de Rufino
   (`/process-rufino`) para construir tu base de conocimiento del caso.
2. **Descubrí qué nos están pidiendo** interrogando tu base con `/ask-rufino`:
   ¿qué quieren construir? ¿cuántos cursos? ¿qué incluye cada uno? ¿a qué precio?
   Ojo: no todos los documentos están de acuerdo entre sí — parte del trabajo es
   darse cuenta de eso y resolver con qué versión quedarse.
3. **Escribí el spec** del entregable usando el planning de Claude Code.
4. **Construí el prototipo**: la sección de cursos integrada a la web actual.
5. **Validá y publicá**: cotejá contra el outcome esperado (se comparte al final)
   y subí tu prototipo a Gizmo.

## Reglas del juego

- El prototipo es **HTML estático puro**: sin React, sin frameworks, sin build
  steps. Lo que el browser abre, es.
- Tiene que **sentirse parte de la web actual** — mismo diseño, misma navegación.
  Reusá el CSS que ya existe en `web-actual/`.
- El contenido del prototipo sale del material del cliente, no de tu imaginación:
  cursos, precios, componentes y textos tienen una fuente.
- No hace falta checkout real ni backend: es un prototipo navegable para validar
  el concepto.
