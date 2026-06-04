# Outcome esperado — caso MakerLab Academy

> Checklist de validación. Se comparte con los asistentes recién en la fase final.
> La "verdad" completa del caso está en [canon.md](canon.md); el prototipo de
> referencia en [referencia/prototipo/](referencia/prototipo/).

## A. ¿El discovery llegó a la verdad?

- [ ] **El pivot identificado**: MakerLab quiere pasar de ecommerce puro a
      "escuela que vende sus productos" — cursos pagos con el kit de componentes
      incluido (fuentes: pptx de visión, minuta de kickoff).
- [ ] **3 cursos, NO 5** — y puede citar qué documento lo resuelve: el mail de
      Marcos (10/03) proponía 5, pero el Slack del equipo (15/04) descartó
      "Domótica con Raspberry Pi" (sin stock de RPi, kit carísimo) y "Brazo
      robótico con servos" (requiere impresión 3D). La minuta de kickoff (20/05),
      el documento más reciente, confirma 3. **Si alguien responde "5 cursos",
      cayó en la trampa.**
- [ ] **La tabla curso → kit → precio completa y exacta**:
      | Curso | Nivel | Duración | Precio |
      |---|---|---|---|
      | Semáforo inteligente | Inicial | 4 clases / 6 h | $89.900 |
      | Estación meteorológica IoT | Intermedio | 6 clases / 10 h | $149.900 |
      | Robot evita-obstáculos | Avanzado | 8 clases / 14 h | $189.900 |
      con los SKUs de cada kit según la hoja "cursos" del excel.
- [ ] **La mecánica comercial entendida**: no se vende el curso sin kit. Un solo
      precio, una sola CTA ("Inscribirme — kit incluido"). La discusión está en
      el Slack: Marcos propuso vender "curso solo" y Carla lo bajó.
- [ ] **El desorden del catálogo detectado**: SKU `ARD-UNO-R3` duplicado con dos
      precios ($28500 y $31.200 — el mail del proveedor del 10/04 explica el
      aumento), categorías inconsistentes, stocks vacíos. Tomás lo advierte en el
      Slack y en la minuta.
- [ ] **El pedido concreto**: prototipo HTML de la sección Cursos sobre la web
      actual (listado + detalle), deadline 2 semanas desde el kickoff.
- [ ] **Las personas mapeadas**: Marcos (dueño, el de las ideas), Carla (gerenta
      comercial, dueña del pivot), Tomás (catálogo/operaciones), Romina
      (instructora, autora de los temarios).
- [ ] **El ruido ignorado**: la queja del pedido #4821, la minuta de logística,
      la política de devoluciones y el DNI... digo, la pizarra, no aportan al
      pedido y no contaminaron las respuestas.

## B. ¿El prototipo cumple?

- [ ] **HTML estático puro** — cero `<script>`, cero frameworks. `grep -ri
      "<script" *.html` devuelve nada.
- [ ] **Integra el design system de la web actual** — mismas fuentes, paleta,
      componentes (cards, badges, botones); no parece un sitio aparte.
- [ ] **Listado de cursos** con los 3 de la primera camada, nivel, duración y
      precio de cada uno.
- [ ] **Al menos un detalle de curso completo** con: qué vas a construir, temario
      por clases, nivel y duración, el kit incluido con sus componentes (SKUs del
      excel), precio único y **una sola CTA** de inscripción con kit incluido.
- [ ] **Navegable desde la Home** — la sección Cursos está en el nav de la web,
      no es un archivo suelto.
- [ ] **Datos exactos del canon** — precios, duraciones y SKUs coinciden con el
      material del cliente (nada inventado).
- [ ] **Publicado en Gizmo** y el link abre.

## Cómo usar esto en la demo

En la fase final, abran este archivo y recorran las dos checklists en voz alta
contra lo que cada uno construyó. El valor del ejercicio no es "acerté/no acerté"
sino VER de dónde salió cada dato: qué documento lo decía, cómo lo encontró la
base, y qué hubiera pasado si procesábamos solo el mail de Marcos.
