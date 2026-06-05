# Cuestionario de nivelación — Workshop Claude Code / Cowork

> Audiencia: equipo de producto (no-devs). 10 preguntas: 3 de inventario + 7
> situacionales. Cada opción de las situacionales tiene su nivel entre
> corchetes `[N0-N3]` — **eso es para vos, sacalo antes de pasarlo al Form**.
> Al final está la guía de lectura para calibrar los módulos del workshop.

---

## Parte 1 — Inventario (sin nivel, para mapear terreno)

**1. ¿Con qué frecuencia usás Claude Code o Claude Cowork hoy?**
- Nunca lo usé / no lo tengo instalado
- Lo probé un par de veces
- Algunas veces por semana
- Todos los días, es parte de mi flujo de trabajo

**2. ¿Cuáles de estas cosas usaste alguna vez? (marcá todas las que apliquen)**
- Plan mode (que Claude planifique antes de ejecutar)
- Skills o slash commands (comandos tipo `/algo`)
- Subagentes (que Claude lance otros Claudes en paralelo)
- Conectores MCP (Claude conectado a Drive, Slack, Jira, Notion...)
- CLAUDE.md o memoria (que Claude recuerde contexto entre sesiones)
- Elegir el modelo o el nivel de razonamiento para una tarea
- Ninguna de las anteriores / no sé qué son

**3. ¿Para qué tipo de trabajo usaste Claude hasta ahora? (marcá todas)**
- Escribir o mejorar documentos (PRDs, specs, mails, presentaciones)
- Analizar información (feedback, datos, research, competencia)
- Automatizar algo repetitivo de mi semana
- Prototipar algo (una pantalla, una landing, un flujo)
- Todavía no lo uso para trabajo real

---

## Parte 2 — Situacionales (4 opciones, cada una delata un nivel)

**4. Tenés que clasificar 300 comentarios de usuarios en 5 categorías. Es una tarea simple pero larga. ¿Qué hacés con el modelo?**
- Uso el que viene por defecto, no sabía que se podía elegir `[N0]`
- Uso siempre el más potente para todo, total es lo mismo `[N1]`
- Elijo uno rápido/barato: para clasificar en masa no hace falta el más inteligente `[N3]`
- Le pregunto a alguien del equipo cuál conviene `[N1]`

**5. Le pediste a Claude un análisis estratégico complejo y la respuesta te quedó corta, superficial. ¿Cuál es tu próximo movimiento?**
- Le digo "dame más detalle" y espero que mejore `[N1]`
- Subo el nivel de razonamiento/effort (o extended thinking) y reformulo qué quiero que evalúe `[N3]`
- Lo doy por perdido y lo termino a mano `[N0]`
- Abro un chat nuevo y pruebo la misma pregunta de nuevo `[N1]`

**6. Tenés que armar un PRD grande partiendo de 20 documentos sueltos (minutas, mails, research). ¿Cómo arrancás con Claude?**
- Le pego los documentos de a uno y le pido que vaya resumiendo `[N1]`
- Le pido directamente "escribime el PRD" con todo adjunto y veo qué sale `[N1]`
- Arranco en plan mode: que primero proponga un plan de cómo procesar todo y lo apruebo antes de que toque nada `[N3]`
- No usaría Claude para algo tan grande, se pierde `[N0]`

**7. Necesitás tres análisis que no dependen entre sí: competencia, pricing y feedback de usuarios. ¿Cómo lo organizás?**
- Se los pido a Claude uno atrás del otro en el mismo chat `[N1]`
- Abro tres chats y voy copiando contexto entre ventanas `[N2]`
- Le pido que lance subagentes en paralelo, uno por análisis, y me consolide los resultados `[N3]`
- Hago uno con Claude y los otros dos a mano mientras tanto `[N0]`

**8. Todas las semanas hacés el mismo resumen de feedback con el mismo formato. ¿Cómo lo manejás con Claude?**
- Cada semana le explico de nuevo qué formato quiero `[N0]`
- Tengo el prompt guardado en un doc y lo pego cada vez `[N1]`
- Lo convertí en una skill / comando propio: escribo `/resumen-feedback` y sale `[N3]`
- Lo agendé para que corra solo y me llegue listo `[N3]`

**9. Cada vez que abrís Claude, no sabe nada de tu producto: el contexto, las decisiones, el roadmap. ¿Cómo lo resolvés?**
- Se lo re-explico cada vez, ya tengo práctica `[N0]`
- Tengo un doc de contexto que le pego al arrancar cada sesión `[N1]`
- Armé un CLAUDE.md / memoria del proyecto: cada sesión arranca ya sabiendo todo `[N3]`
- Trato de hacer todo en un solo chat eterno para no perder el contexto `[N1]`

**10. Claude te entrega un análisis con números y conclusiones que te suenan raras. ¿Qué hacés antes de llevarlo a una reunión?**
- Lo presento igual, Claude no suele equivocarse `[N0]`
- Lo reviso por arriba y corrijo lo que me hace ruido `[N1]`
- Le pido que muestre las fuentes y el trabajo: de dónde salió cada número, y verifico los críticos `[N3]`
- Descarto el análisis: si suena raro, no sirve `[N1]`

---

## Guía de lectura (para calibrar el workshop)

**Score por persona**: promedio de las 7 situacionales (P4-P10).

| Promedio | Nivel | Qué significa |
|---|---|---|
| 0 – 0.9 | Explorador | Usa Claude como un chat. Hay que arrancar de cero. |
| 1 – 1.9 | Usuario | Lo usa de verdad pero con fuerza bruta: re-explica, copia/pega, un solo chat. |
| 2 – 3 | Operador | Ya orquesta: modelos, skills, agentes, memoria. Quiere profundidad, no introducción. |

**Calibración por pregunta** (qué módulo enfatizar si el promedio de ESA pregunta da bajo):

| Pregunta baja | Módulo a enfatizar |
|---|---|
| P4 | Elección de modelos: capacidad vs costo vs velocidad (Opus/Sonnet/Haiku, fast mode) |
| P5 | Effort y extended thinking: cuándo y cómo pedir más razonamiento |
| P6 | Plan mode y specs antes de ejecutar |
| P7 | Orquestación: subagentes y trabajo en paralelo |
| P8 | Skills y automatización (acá enchufás la demo de Rufino) |
| P9 | Memoria y contexto persistente (CLAUDE.md) |
| P10 | Supervisión y verificación de outputs — crítico para producto |

**Señales rápidas del inventario**:
- P1 mayoría "nunca/lo probé" → sumá 20 min de setup y primeros pasos a la Fase 0 de la demo.
- P2 con "Ninguna de las anteriores" dominante → el cuestionario situacional va a dar bajo: validá que el guión arranque sin asumir vocabulario.
- P3 sin "automatizar" marcado → el pitch de Rufino (ingest → process → ask) es la novedad más vendible del workshop.
