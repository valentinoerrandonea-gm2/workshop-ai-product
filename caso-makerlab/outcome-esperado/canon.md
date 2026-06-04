# Canon del caso MakerLab Academy

> Fuente única de verdad. Todos los archivos del corpus derivan de acá. Si un documento del corpus contradice este canon, es a propósito (ver "la contradicción").

## Personas del cliente

| Persona | Rol | Voz |
|---|---|---|
| Marcos Etcheverry | Dueño/fundador | Entusiasta, dispara ideas sin filtrar (el mail de los 5 cursos) |
| Carla Domínguez | Gerenta comercial | Pushea el pivot, armó las slides de la visión |
| Tomás Brizuela | Catálogo/operaciones | Pragmático, conoce el desorden del catálogo, frena ideas caras |
| Romina Páez | Instructora | Diseñó los temarios de los 3 cursos |

## Cronología (lo más nuevo manda — así se resuelve la contradicción)

| Fecha | Documento | Qué dice |
|---|---|---|
| 2025-11 | politica-devoluciones.pdf | RUIDO — política de devoluciones vigente |
| 2026-02-18 | mail-queja-cliente.md | RUIDO — queja por demora de envío |
| 2026-03-05 | minuta-logistica.docx | RUIDO — Andreani vs OCA |
| 2026-03-10 | mail-dueno-ideas-cursos.md | **CONTRADICCIÓN** — Marcos propone **5 cursos** |
| 2026-03-28 | pizarra-brainstorm.png | RUIDO — foto de pizarra del brainstorm del pivot |
| 2026-04-02 | vision-makerlab-academy.pptx | CLAVE — Carla: visión "de tienda a escuela" |
| 2026-04-10 | mail-proveedor.md | RUIDO — aumento de precios de placas Arduino (explica el precio duplicado del UNO) |
| 2026-04-15 | slack-canal-pivot.md | CLAVE — el equipo **baja de 5 a 3 cursos** y define precios |
| 2026-05-08 | temarios-cursos.pdf | CLAVE — Romina: temario, nivel y duración |
| 2026-05-20 | minuta-kickoff-gm2.docx | CLAVE — pedido formal a GM2 |
| s/f | catalogo-productos.xlsx | CLAVE — hoja "productos" (desorden) + hoja "cursos" (mapping) |

## La contradicción sembrada

Mail de Marcos (2026-03-10): **5 cursos** — los 3 definitivos + "Domótica con Raspberry Pi" (descartado en Slack: sin stock de RPi, kit arriba de $300.000) + "Brazo robótico con servos" (descartado: requiere impresión 3D). La resolución está en el Slack (2026-04-15) y se confirma en la minuta de kickoff (2026-05-20). **Respuesta correcta: 3 cursos.**

## Los 3 cursos definitivos

| Curso | Nivel | Duración | Precio (curso + kit incluido) | Kit (SKUs) |
|---|---|---|---|---|
| Semáforo inteligente | Inicial | 4 clases / 6 h | **$89.900** | ARD-UNO-R3, PRT-830, LED-5MM-X10, RES-220-X25, BTN-12MM, JMP-MM-40 |
| Estación meteorológica IoT | Intermedio | 6 clases / 10 h | **$149.900** | ESP-NODEMCU, SEN-DHT22, LCD-1602-I2C, PRT-830, JMP-MH-40, PSU-5V-2A |
| Robot evita-obstáculos | Avanzado | 8 clases / 14 h | **$189.900** | ARD-UNO-R3, CHS-2WD, MOT-TT-DC x2, DRV-L298N, SEN-HCSR04, BAT-4AA, JMP-MH-40 |

**Mecánica comercial** (Slack, confirmada en minuta): no se vende el curso sin kit. Un solo precio, un solo CTA: "Inscribirme — kit incluido". Modalidad online en vivo + material grabado; el kit se envía al inscribirse.

## Catálogo — hoja "productos" (24 filas, CON el desorden)

Columnas: `SKU | Producto | Categoria | Precio | Stock`

| SKU | Producto | Categoria | Precio | Stock |
|---|---|---|---|---|
| ARD-UNO-R3 | Arduino UNO R3 | Placas Arduino | 28500 | 42 |
| ARD-NANO | Arduino Nano | placas arduino | $24.900 | 18 |
| ARD-MEGA | Arduino Mega 2560 | Placas | 52300 | 7 |
| ESP-NODEMCU | NodeMCU ESP8266 | Placas Arduino | 19800 | 25 |
| RPI-4B-4GB | Raspberry Pi 4B 4GB | Placas Raspberry Pi | 145000 | 3 |
| RPI-ZERO-W | Raspberry Pi Zero W | RASPBERRY | $38.000 | 0 |
| SEN-DHT22 | Sensor temperatura y humedad DHT22 | Sensores | 8900 | 31 |
| SEN-HCSR04 | Sensor ultrasónico HC-SR04 | sensores | 4200 | 55 |
| SEN-PIR | Sensor de movimiento PIR HC-SR501 | SENSORES Y MODULOS | 5100 | 12 |
| SEN-LDR | Fotorresistencia LDR 5mm | Sensores | 800 | *(vacío)* |
| LCD-1602-I2C | Display LCD 16x2 con I2C | Modulos | 9700 | 22 |
| DRV-L298N | Driver de motores L298N | Modulos y comunicacion | 6800 | 19 |
| MOT-TT-DC | Motor DC TT con reductora | Actuadores | 3500 | 40 |
| MOT-SG90 | Servo SG90 9g | Actuadores y motores | 4900 | 28 |
| CHS-2WD | Chasis robot 2WD con ruedas | Actuadores | 16500 | 9 |
| PRT-830 | Protoboard 830 puntos | Accesorios | 6200 | 60 |
| JMP-MM-40 | Jumpers macho-macho x40 | Accesorios | 3800 | 75 |
| JMP-MH-40 | Jumpers macho-hembra x40 | accesorios | 3800 | 68 |
| LED-5MM-X10 | Pack 10 LEDs 5mm surtidos | Accesorios | 2100 | 90 |
| RES-220-X25 | Pack 25 resistencias 220 ohm | Accesorios | 1500 | *(vacío)* |
| BTN-12MM | Pulsador táctil 12mm | Accesorios | 600 | 120 |
| BAT-4AA | Portapilas 4xAA con cable | Accesorios | 2900 | 35 |
| PSU-5V-2A | Fuente 5V 2A micro USB | Accesorios | 7400 | 14 |
| ARD-UNO-R3 | ARDUINO UNO R3 ORIGINAL | Placas Arduino | $31.200 | 6 |

**El desorden a propósito** (que el discovery debería notar): SKU `ARD-UNO-R3` duplicado con nombre y precio distintos (filas 1 y 24 — el mail del proveedor del 2026-04-10 explica el aumento), categorías inconsistentes (8 variantes escritas para 6 categorías reales), precios a veces con `$` y puntos a veces números crudos, 2 celdas de stock vacías.

## Hoja "cursos" del xlsx

Columnas: `Curso | Nivel | SKUs del kit | Precio final` — tres filas, exactamente los datos de la tabla de cursos definitivos.

## El pedido formal (minuta kickoff 2026-05-20)

Prototipo HTML de la **sección Cursos** integrada a la web actual: listado de cursos + página de detalle (temario, nivel, duración, kit incluido con su lista de componentes, precio único curso+kit, CTA única "Inscribirme — kit incluido"). El catálogo se entrega "como está" en excel. Deadline del prototipo: 2 semanas.
