# DOCUMENTO DE PREPRODUCCIÓN — LA CRIPTA DE NEKKMAN
## Basado en Preproduction Blueprints de Alex Galuzin
### TP Módulo 2 — Niveles Platformer/Puzzle

**Autor:** Franco Tarelli
**Nombre del Juego:** La cripta de Nekkman
**Género Puro (Clase 1):** aventura
**Subgénero/Mecánica:** Sin especificar
**Cantidad de Niveles:** 3 (máx. 20 minutos totales)
**Duración Estimada:** 3 + 4 + 4 minutos
**Engine/Plataforma:** html5
**Fecha de Creación:** 18/07/2026
**Estado:** Pre-Producción (Documentación para TP Módulo 2)

**OK: REQUISITOS DEL TP CUMPLIDOS:**
- OK: **Curva de dificultad y balance** (Sección 6: Teoría de Balanceo)
- OK: **Estructura y layouts** (Sección 4: Diagramas Top-Down)
- OK: **Beat Chart de niveles** (Sección 3: Beat Charts Detallados)
- OK: **Referencias visuales** (Sección 1, PASO 5 + Instrucción Miro)
- OK: **Referencia teórica** (Sección 1: Los 11 Pasos Preproduction Blueprints)

---

## TABLA DE CONTENIDOS

1. **INFORMACIÓN GENERAL DEL PROYECTO**
2. **BLUEPRINT GALUZIN — 11 PASOS**
   - Paso 1-3: Idea, Contexto, Propósito
   - Paso 4-6: Features, Referencias, Historia
   - Paso 7-11: Objetivos, Focales, Layout, Visual, Assets
3. **BEAT CHARTS DETALLADOS (Momentos Clave de Cada Nivel)**
4. **DIAGRAMAS TOP-DOWN — LAYOUTS**
5. **DETALLES DESCRIPTIVOS POR NIVEL (Preguntas Clave)**
6. **TEORÍA DE BALANCEO (Clase 9)**
7. **PLAYTESTING FRAMEWORK**

---

# SECCIÓN 0: INFORMACIÓN GENERAL DEL PROYECTO

## 0.1 — Datos Básicos

| Aspecto | Valor |
|---------|-------|
| **Nombre del Juego** | La cripta de Nekkman |
| **Idea Central** | Un paladin que tiene que acabar con un nigromante que esta queriendo convertirse en un liche, sorteando enemigos, puzzles y trampas. |
| **Género Puro (Clase 1)** | aventura |
| **Subgénero** | Sin especificar |
| **Cantidad de Niveles** | 3 |
| **Duración Estimada** | 3 + 4 + 4 minutos |
| **Engine/Plataforma** | html5 |

## 0.2 — Alcance y Factibilidad (Clase 5)

**Tiempo Disponible:** ? horas

**Habilidades del Equipo:**
- Programación: Sin especificar
- Arte/Sprites: Sin especificar

**Assets Estimados:**
- Sprites: 30
- Tiles/Texturas: 20
- Tracks de Música: ?
- SFX (Efectos de Sonido): ?

---

# SECCIÓN 1: BLUEPRINT GALUZIN — 11 PASOS

## PASO 1: LA IDEA (Definiendo el Core)

**Idea Central (1-2 frases):**
> Un paladin que tiene que acabar con un nigromante que esta queriendo convertirse en un liche, sorteando enemigos, puzzles y trampas.

**Inspiración Principal:**
Legend of zelda, D&D

**¿Qué hace esta idea DIFERENTE? (vs juegos similares)**
arte dibujado a mano, mecanicas de D&D en tiempo real

---

## PASO 2: AMBIENTE, UBICACIÓN Y TEMA

### Elementos Espaciales (Galuzin: 3 dimensiones)

**Environment Setting (Categoría Amplia):**
caves

**Ubicación Específica (Narrowed Down):**
Cripta antigua

**Período Histórico:**
Sin especificar

### Tema/Atmósfera (3-5 adjetivos)

oscuro, sombrio, tenebroso, tetrico

---

## PASO 3: PROPÓSITO DEL PROYECTO

### Propósito Interno (Aprendizaje/Desarrollo)
Busco practicar y crear arte por primera vez en 2D, ademas, aprender a diseñar correctamente niveles

### Propósito Externo (Portfolio/Presentación)
Mostrar mi primer videojuego

### Timeline
**Deadline:** 14 de agosto 2026

---

## PASO 4: CARACTERÍSTICAS CLAVE (Features)

Galuzin propone que features deben caer en 5 categorías: Visual, Technical, Gameplay, Story/Emotional, World. Elige 3-5 máximo.

**Feature 1: **


**Feature 2: **


**Feature 3: Sin nombre**
Sin descripción

---

## PASO 5: REFERENCIAS VISUALES E INVESTIGACIÓN

Galuzin propone 5 categorías de referencia. Coleccionarlas ayuda a crear ambientes creíbles.

**1. Referencias de Arquitectura (Estilos, proporciones, detalles)**
fantasia medieval, estilo top down 2D estilizado

**2. Referencias de Ambiente General (Paisajes amplios, escenarios generales)**
cuevas, mazmorra

**3. Referencias de Iluminación (Cómo la luz crea mood y atmosphere)**
Luz azul, tenue, oscuridad

**4. Referencias de Props/Objetos (Elementos individuales, placement)**
2 D estilizado dibujado a mano

**5. Referencias de Estilo/Art Direction (Concepto art, pinturas, visual theme)**
Sin especificar

---

## PASO 6: LA HISTORIA (What/How/Why Framework)

Galuzin enfatiza que el storytelling IMPLÍCITO (mostrado, no dicho) es más poderoso que el explícito.

### WHAT — ¿Cuál es la historia del ambiente ANTES del jugador?
Un Nigromante llamado Nekkman hizo un trato con el Dios Talos. Este le iba a entregar poderes a cambio de entregarle a él su cuerpo y convertirlo en un Liche. 

### HOW — ¿Cómo llegó el jugador aquí? ¿Qué eventos lo trajeron?
El jugador es un Paladin, lo enviaron de la capital porque se rumoreaba que el poderoso Nigromante Nekkman estaba yendo por el mal camino, sacrificando gente en un poblado en los alrededores del templo abandonado.

### WHY — ¿Por qué está el jugador aquí? ¿Cuál es su objetivo?
La mision del personaje, Yamel, es detener a Nekkman, evitar que este logre concentrar el poder de las almas que sacrificio y convertirse en el Liche

### Tipo de Storytelling
Mixto (ambos elementos combinados)

---

## PASO 7: OBJETIVOS, OBSTÁCULOS Y DIFICULTAD

Clase 9 enfatiza que la dificultad debe fluctuar en patrón Sawtooth (introducir mecánica → jugador aprende → introduce variación).

### NIVEL 1: La entrada a la mazmorra

| Aspecto | Valor |
|---------|-------|
| **Duración Esperada** | 3 minutos |
| **Dificultad Objetivo** | 2/10 |
| **Objetivo Principal** | Introducir al jugador a las mecanicas basicas, movimiento, ataque. Que entienda como se va a dar el resto del juego. El jugador se va a encontrar con una gran puerta, que tiene 3 luces. de la puerta y de las luces, salen "tubos" del mismo color a diferentes otras puertas. 

Ademas el jugador vera que uno de estos tubos conduce al centro de la sala donde está una fuente que, al resolver un acertijo, esta apagara su luz y desbloqueara otra puerta. |
| **Enemigos/Obstáculos** | esqueletos basicos, trampas de pinches, y trampas de accion. Tambien va a tener que resolver un puzzle |

**Análisis (Clase 9):** Nivel introducción. Curva de dificultad MUY lenta (jugador está aprendiendo controles). Introduce 1 mecánica a la vez.

---

### NIVEL 2: La puerta izquierda.

| Aspecto | Valor |
|---------|-------|
| **Duración Esperada** | 4 minutos |
| **Dificultad Objetivo** | 4/10 |
| **Objetivo Principal** | el jugador debera abrirse paso hasta la segunda fuente, enfrentando nuevos y mas enemigos, y nuevas y diferentes trampas. |
| **Enemigos/Obstáculos** | Esqueletos simples, esqueletos que tiran hechizos y esqueletos tanques. Trampas nuevas electricas, como rayos y un nuevo puzzle |

**Análisis (Clase 9):** Nivel escalada. Curva escalonada (cada desafío +1-2 en dificultad). Variación constante (combate → exploración → puzzle).

---

### NIVEL 3: La puerta de la derecha

| Aspecto | Valor |
|---------|-------|
| **Duración Esperada** | 4 minutos |
| **Dificultad Objetivo** | 7/10 |
| **Objetivo Principal** | el jugador debera abrirse paso hasta la segunda tercera, enfrentando nuevos y mas enemigos, y nuevas y diferentes trampas. |
| **Enemigos/Obstáculos** | Esqueletos simples, esqueletos que tiran hechizos, esqueletos tanques y esqueletos caballeros. Trampas nuevas electricas, como rayos y un nuevo puzzle |

**Análisis (Clase 9):** Nivel climax. Pico de dificultad máximo (Boss), luego caída emocional (escape cinemático como recuperación). Integra TODO lo aprendido.

---

## PASO 8: PUNTOS FOCALES (Weenies — Scott Rogers)

Elementos visuales DOMINANTES que atraen la atención del jugador y lo guían sin UI explícita.

**Punto Focal Principal (Macro Weenie — visible desde lejos):**
la puerta central con las diferentes luces

**Puntos Focales Secundarios (Marcan progresión dentro de cada nivel):**
fuentes y tubos que llevan la luz de la fuente

**Técnica Visual (Iluminación + Color + Tamaño):**
Sin especificar

---

## PASO 9: TOP-DOWN LAYOUT (Estructura de cada nivel)

Galuzin enfatiza que el layout es el pensamiento detrás de lo que vas a crear. Es tu blueprint antes de blocar en el engine.

**Layout NIVEL 1:**
Entrada, esquivar trampas, combate con algunos esqueletos, esquivar trampas y esqueletos y puzzle de fuente

**Layout NIVEL 2:**
Entrada, combate con esqueletos, trampas, combate con esqueletos magos, trampas, combate con esqueleto tanque, puzzle 

**Layout NIVEL 3:**
Entrada, combate con esqueletos tanque y normales, trampas, esqueletos magos, tanques y el caballero. trampas mientras tanto y puzzle

**Tipo de Estructura:**
Linear (un camino principal, progresión secuencial)

---

## PASO 10: VISUAL DEVELOPMENT (Art Direction)

### Estilo Visual
Estilizado dibujado a mano, sino pixel art

### Paleta de Colores
azules, dorados, grises, negros y marrones

### Iluminación
**Warm/Cool:** Cool (fría, noche, magia azul)

**Contraste:** Low-Key (oscuro, alto contraste, atmosphere dramática)

---

## PASO 11: LISTAS DE RECURSOS (Galuzin Step 11)

### Assets a Crear/Coleccionar

**Sprites de Personajes:**
- Estimado: 30 sprites

**Tiles/Texturas Base:**
- Estimado: 20 variantes

**Audio:**
- Música: ? tracks
- SFX: ? efectos

### Production Pipeline Sugerida

**Engine:** html5

**Fases (Galuzin Step 11: Lists):**
1. Layout block-in (geometría simple)
2. Gameplay integration (mecánicas base, sin visuals)
3. Extensive playtesting (iteración con feedback)
4. Texturing (materiales, texturas)
5. Detailing (models, props, polish)
6. Lighting
7. Atmosphere & post-process
8. Final playtesting & tweaks
9. Release

---

# SECCIÓN 2: DETALLES POR NIVEL — PREGUNTAS CLAVE

## BEAT CHARTS DETALLADOS

### NIVEL 1: La entrada a la mazmorra (Introducción/Onboarding)
**Duración Total:** 3 minutos | **Dificultad Objetivo:** 2/10

| Tiempo (min) | Beat Name | Descripción | Dificultad |
|--------------|-----------|-------------|-----------|
| 0:00-1:00 | OPENING | Entrada visual, establece atmósfera inicial | 1/10 |
| 1:00-2:00 | TUTORIAL | Enseña controles básicos | 1-2/10 |
| 2:00-3:30 | FIRST OBSTACLE | Primer desafío simple para aplicar lo aprendido | 2-3/10 |
| 3:30-4:30 | ESCALATION | Aumenta dificultad ligeramente, introduce variación | 3-4/10 |
| 4:30-5:00 | RESOLUTION | Cierre del nivel, sensación de logro | 1-2/10 |

**Total:** ~3 minutos

---

### NIVEL 2: La puerta izquierda. (Escalada/Desafío)
**Duración Total:** 4 minutos | **Dificultad Objetivo:** 4/10

| Tiempo (min) | Beat Name | Descripción | Dificultad |
|--------------|-----------|-------------|-----------|
| 0:00-1:00 | OPENING | Nueva zona, nuevo ambiente, contexto nuevo | 2/10 |
| 1:00-3:00 | NEW MECHANIC | Introduce mecánica nueva o variación | 4-5/10 |
| 3:00-5:00 | ESCALATION | Múltiples obstáculos combinados, presión | 5-6/10 |
| 5:00-6:30 | PEAK | Pico de dificultad del nivel, máximo desafío | 6-7/10 |
| 6:30-7:30 | RESOLUTION | Cierre y transición a siguiente nivel | 2-3/10 |

**Total:** ~4 minutos

---

### NIVEL 3: La puerta de la derecha (Climax/Boss)
**Duración Total:** 4 minutos | **Dificultad Objetivo:** 7/10

| Tiempo (min) | Beat Name | Descripción | Dificultad |
|--------------|-----------|-------------|-----------|
| 0:00-1:00 | OPENING | Entrada épica, establece el tono del climax | 3/10 |
| 1:00-3:00 | BUILD UP | Tensión creciente, se acerca el confrontamiento | 6-7/10 |
| 3:00-6:00 | CLIMAX | Boss o prueba final, integra TODO lo aprendido | 8-9/10 |
| 6:00-7:00 | RESOLUTION | Victoria, cierre cinematográfico, satisfacción | 1-2/10 |

**Total:** ~4 minutos

**TIEMPO TOTAL DEL JUEGO:** 3 + 4 + 4 = 11 minutos (≤ 20 máx) OK:


# SECCIÓN 3: DIAGRAMAS TOP-DOWN — LAYOUTS

## DIAGRAMAS DE FLUJO — TOP-DOWN LAYOUTS

### LAYOUT NIVEL 1: La entrada a la mazmorra

**Tipo de Estructura:** Linear (progresión secuencial clara)

```
[INICIO]
   ↓
[Zona Segura 1] ──→ [Tutorial] ──→ [Checkpoint 1]
   ↓                                    ↓
[Primer Obstáculo]  ←──────────────────┘
   ↓
[Zona Segura 2] ──→ [Escalada Suave] ──→ [META]
```

**Descripción del Flujo:**
Entrada, esquivar trampas, combate con algunos esqueletos, esquivar trampas y esqueletos y puzzle de fuente

**Propósito Pedagógico:** Introducción suave, enseña un concepto a la vez, seguridad psicológica.

---

### LAYOUT NIVEL 2: La puerta izquierda.

**Tipo de Estructura:** Non-Linear (múltiples caminos posibles)

```
[INICIO]
   ↓
┌──[Bifurcación]──┐
│                  │
[Camino A]    [Camino B]
│                  │
└──[Zona Central]──┘
   ↓
[Obstáculo Complejo]
   ↓
[Pico de Dificultad]
   ↓
[META]
```

**Descripción del Flujo:**
Entrada, combate con esqueletos, trampas, combate con esqueletos magos, trampas, combate con esqueleto tanque, puzzle 

**Propósito Pedagógico:** Más libertad, replay value, descubrimiento, variedad.

---

### LAYOUT NIVEL 3: La puerta de la derecha

**Tipo de Estructura:** Boss Arena (foco en confrontación)

```
[ENTRADA ÉPICA]
   ↓
[Pre-Boss Challenges] ──→ [Checkpoint Final]
   ↓
[════════════════════════════]
[  ARENA DEL BOSS / CLIMAX   ]
[════════════════════════════]
   ↓
[VICTORIA] ──→ [Cierre Cinematográfico] ──→ [CRÉDITOS]
```

**Descripción del Flujo:**
Entrada, combate con esqueletos tanque y normales, trampas, esqueletos magos, tanques y el caballero. trampas mientras tanto y puzzle

**Propósito Pedagógico:** Culminación, demostración de maestría, catarsis emocional.

---


# SECCIÓN 4: DESCRIPCIÓN DETALLADA POR NIVEL

## NIVEL 1: La entrada a la mazmorra

### Identidad del Nivel
- **Duración:** 3 minutos
- **Dificultad:** 2/10
- **Tema:** Introducción + Aprendizaje

### Descripción
**Objetivo:** Introducir al jugador a las mecanicas basicas, movimiento, ataque. Que entienda como se va a dar el resto del juego. El jugador se va a encontrar con una gran puerta, que tiene 3 luces. de la puerta y de las luces, salen "tubos" del mismo color a diferentes otras puertas. 

Ademas el jugador vera que uno de estos tubos conduce al centro de la sala donde está una fuente que, al resolver un acertijo, esta apagara su luz y desbloqueara otra puerta.

**Enemigos/Obstáculos:** esqueletos basicos, trampas de pinches, y trampas de accion. Tambien va a tener que resolver un puzzle

---

## NIVEL 2: La puerta izquierda.

### Identidad del Nivel
- **Duración:** 4 minutos
- **Dificultad:** 4/10
- **Tema:** Escalada + Desafío

### Descripción
**Objetivo:** el jugador debera abrirse paso hasta la segunda fuente, enfrentando nuevos y mas enemigos, y nuevas y diferentes trampas.

**Enemigos/Obstáculos:** Esqueletos simples, esqueletos que tiran hechizos y esqueletos tanques. Trampas nuevas electricas, como rayos y un nuevo puzzle

---

## NIVEL 3: La puerta de la derecha

### Identidad del Nivel
- **Duración:** 4 minutos
- **Dificultad:** 7/10
- **Tema:** Climax + Conclusión

### Descripción
**Objetivo:** el jugador debera abrirse paso hasta la segunda tercera, enfrentando nuevos y mas enemigos, y nuevas y diferentes trampas.

**Enemigos/Obstáculos:** Esqueletos simples, esqueletos que tiran hechizos, esqueletos tanques y esqueletos caballeros. Trampas nuevas electricas, como rayos y un nuevo puzzle

---

# SECCIÓN 3: TEORÍA DE BALANCEO (Clase 9 — Eduardo Ortega)

## Curva de Dificultad (Sawtooth Pattern)

Basado en Clase 9, la dificultad debe fluctuar, no ser lineal:

```
NIVEL 1 (Introducción):  ▁ ▂ ▃ ▂ ▃ ▂  (muy bajo)
NIVEL 2 (Escalada):      ▂ ▃ ▄ ▃ ▄ ▅  (bajo-medio)
NIVEL 3 (Climax):        ▅ ▆ ▇ █ ▆ ▂  (alto, luego caída)
```

---

# SECCIÓN 4: PLAYTESTING FRAMEWORK (Clase 9)

## Cohortes de Jugadores (Segmentación por Skill)

**COHORTE 1: Principiante**
- Expectativa Nivel 1: 2/10
- Expectativa Nivel 2: 4/10
- Expectativa Nivel 3: 7/10

**COHORTE 2: Intermedio**
- Expectativa Nivel 1: 1/10
- Expectativa Nivel 2: 3/10
- Expectativa Nivel 3: 6/10

**COHORTE 3: Avanzado**
- Expectativa Nivel 1: 1/10
- Expectativa Nivel 2: 2/10
- Expectativa Nivel 3: 5/10

## Playtesting Dual-Métrica

### Métrica Objetivo
- Contar MUERTES por nivel

### Métrica Subjetiva
- Rating 1-10 (¿Cuán difícil te pareció?)

### Gap Analysis
- Si predicción ≠ realidad → Ajustar valores

---

# SECCIÓN 8: MOODBOARD Y REFERENCIAS VISUALES

## Instrucciones para Crear Moodboard en Miro

1. **Abre:** https://miro.com
2. **Crea un nuevo board**
3. **Agrega referencias visuales** en estas categorías:
   - Arquitectura/Environment
   - Paleta de Colores
   - Iluminación
   - Inspiración de juegos similares
   - Sketches de niveles
4. **Organiza por sección**
5. **Comparte el link** (copiar enlace público)
6. **Pega el link aquí en el documento** (reemplaza [PEGAR_LINK_MIRO])

**Link al Miro Board:** [PEGAR_LINK_MIRO]

---

# OK: CHECKLIST FINAL — REQUISITOS DEL TP

- [x] Curva de dificultad y balance documentada (Sección 6)
- [x] Estructura y layouts con diagramas (Sección 4)
- [x] Beat Chart detallado momento a momento (Sección 3)
- [x] Referencias visuales e instrucción Miro (Sección 8)
- [x] Referencia teórica: Preproduction Blueprints (Sección 1: 11 pasos)
- [x] Idea central clara y diferenciada
- [x] 3 Niveles descritos (nombre, duración, dificultad, objetivos)
- [x] Narrativa (What/How/Why) definida
- [x] Features clave (3-5) documentadas
- [x] Focal Points (weenies) identificados
- [x] Visual Development definido (estilo, colores, iluminación)
- [x] Assets estimados (sprites, tiles, audio)
- [x] Playtesting framework planificado

---

**Documentación Completada:** 18/07/2026 16:12:45

**Status:** OK: LISTO PARA ENTREGA (PRE-ENTREGA: 28 JULIO | FINAL: 14 AGOSTO 2026)

**Próximos Pasos:**
1. OK: Documento de Preproducción (ENTREGABLE 1)
2. ⏳ Crear Moodboard en Miro (referencias visuales)
3. ⏳ Construir 3 Niveles Ejecutables (ENTREGABLE 2)
4. ⏳ Preparar sesión de Playtesting (3+ jugadores)
5. ⏳ Recolectar métricas (muertes + rating por cohorte)
6. ⏳ Iterar basado en datos reales
7. ⏳ Presentar ante Ignacio Rud + Eduardo Ortega

---

**Documentación generada automáticamente desde FORMULARIO_GDD_COMPLETO.html**

**Estructura integrada:**
- OK: Blueprint Galuzin (11 pasos) — Metodología profesional de preproducción
- OK: Clase 9 (Balanceo de dificultad) — Teoría de curvas sawtooth, cohorts
- OK: Clase 1 (Géneros, MDA, Flow) — Fundamentos de diseño
- OK: Clase 5 (Factibilidad) — Alcance, skills, assets

**Para profesores:** Este documento demuestra aplicación práctica de conceptos de Módulos 1 y 2, con justificación teórica de cada decisión de diseño.

---

*Generado automáticamente desde FORMULARIO_GDD_COMPLETO.html*
*Estructura: Blueprint Galuzin (11 pasos) + Clase 9 (Balanceo) + Clase 1 (Géneros) + Clase 5 (Factibilidad)*
