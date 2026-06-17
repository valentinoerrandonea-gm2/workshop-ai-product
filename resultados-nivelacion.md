# Resultados del cuestionario de nivelación

> Análisis de las respuestas al Form para calibrar el workshop. Fuente: `AI Workshop Proposal & Basic AI Knowledge Assessment.csv` (4 respuestas, 2026-06-11).
> **Caveat**: N=4. Son señales, no estadística. Sirven para orientar dónde poner el foco, no para conclusiones duras.

## Titular

**El grupo es avanzado.** Los 4 usan Claude **todos los días** como parte de su flujo, y los 4 caen en nivel **Operador** (promedio situacional 2.4–3.0 sobre 3). Esto cambia el tono del workshop: **no es una intro**. Hay que ir en profundidad y saltear el hand-holding en lo que ya dominan.

## Nivel por persona (situacionales P4–P10)

| Respondente | Promedio | Nivel |
|---|---|---|
| R1 | 3.0 | Operador |
| R2 | 3.0 | Operador |
| R3 | 2.43 | Operador |
| R4 | 2.57 | Operador |

## Dónde poner el foco (promedio por pregunta)

| Pregunta | Tema | Prom. | Acción en el workshop |
|---|---|---|---|
| **P4** | **Elección de modelo** (capacidad vs costo vs velocidad) | **1.75** | 🔴 **Prioridad #1.** R3 no sabía que se podía elegir; R4 usa siempre el más potente "total es lo mismo". Enseñar cuándo Haiku/rápido vs Opus/razonador, y fast mode. |
| **P7** | **Orquestación / subagentes en paralelo** | **2.5** | 🟡 **Prioridad #2.** R3 y R4 todavía abren 3 chats y copian contexto a mano en vez de lanzar subagentes. Mostrar el patrón de paralelización. |
| P5 | Effort / extended thinking | 3.0 | ✅ Ya lo tienen. Profundizar, no introducir. |
| P6 | Plan mode | 3.0 | ✅ Ídem. |
| P8 | Skills / automatización | 3.0 | ✅ Ídem — acá engancha la demo de Rufino igual, pero como "nivel siguiente", no como novedad básica. |
| P9 | Memoria / CLAUDE.md | 3.0 | ✅ Ídem. |
| P10 | Verificación de outputs | 3.0 | ✅ Ídem. |

## Nuance importante: saben MÁS de lo que aplican

Hay un gap entre lo que dicen haber usado y cómo deciden:
- **Modelos**: 3 de 4 marcaron "elegir modelo/nivel de razonamiento" como algo que usaron (P2), pero en el escenario real (P4) solo 2 eligen bien. La **conciencia** de que se puede elegir está más extendida que el **criterio** para elegir. → El módulo de modelos tiene que ser sobre *cuándo* usar cuál, no sobre *que existe la opción*.
- **Subagentes**: solo 1 de 4 marcó haberlos usado (P2), consistente con el P7 flojo. Es lo más nuevo para ellos junto con modelos.

## Inventario de herramientas (P2 — qué usaron)

| Herramienta | Cuántos (de 4) |
|---|---|
| Plan mode | 4 ✅ |
| MCP connectors | 4 ✅ |
| Elegir modelo / razonamiento | 3 |
| CLAUDE.md / memoria | 2 |
| Skills / slash commands | 2 |
| Subagentes | 1 🔴 |

## Tipo de trabajo (P3)

Escribir docs (4) y analizar info (4) son universales. Prototipar (3). **Automatizar algo repetitivo: solo 1.** → Confirma que el flujo de Rufino (ingest → process → ask) y la automatización son **lo más vendible / novedoso** para este grupo: lo usan para producir y analizar, casi nadie para automatizar su semana.

## Validación de los 4 casos de uso propuestos

Todos validados (Strongly Agree / Agree en los 4):
- Note-taker con repo compartido — 4× Strongly Agree (el más fuerte).
- Requirements → spec — 4× Strongly Agree.
- Publishing protos/artifacts con Gizmos — 3 SA + 1 Agree.
- Automatic capture routines — 2 SA + 2 Agree (el relativamente más tibio, pero positivo).

## Feedback abierto (accionable)

De R2, dos puntos concretos:
1. **¿Entra todo en una hora?** Recordatorio de que el workshop puede durar **2 horas**. → El `GUION-DEMO.md` ya está estimado en ~2h30; confirmar el slot real y, si es 1h, usar el "plan B" del apéndice del guión.
2. **War room previo al workshop**: una sesión corta antes para verificar que todos tengan Claude Code instalado y funcionando (las skills, los MCP), para no quemar tiempo del workshop en setup. → Dado que los 4 ya usan Claude a diario, el setup debería ser liviano, pero el war room cubre el riesgo de los zips/skills.

## Recomendación de calibración (resumen)

1. **Recortar la intro.** El grupo no la necesita: arrancar asumiendo uso diario.
2. **Gastar el tiempo ganado en P4 (modelos) y P7 (orquestación)** — los dos huecos reales.
3. **Rufino y skills**: presentarlos como "el nivel que todavía no operan" (automatización), no como básico.
4. **Hacer el war room previo** para descargar setup fuera del workshop.
5. **Confirmar duración** (1h vs 2h) y elegir guión completo vs plan B en consecuencia.
