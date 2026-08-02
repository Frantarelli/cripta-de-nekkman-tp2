# 🎮 La Cripta de Nekkman — Documentación Técnica del Juego

> **Para retomar en otro chat**: pegá este archivo (o decile a Claude que lo lea) y va a tener todo el contexto necesario para seguir trabajando sobre `cripta_nekkman_game.html` sin tener que re-explicar nada.

**Archivo del juego**: `E:\Curso\cripta_nekkman_game.html` (single-file: HTML + CSS + JS, todo en un solo archivo).
**Motor**: Phaser 3.55.2 vía CDN, Arcade Physics, `Scale.FIT` (mundo interno fijo 1024x768, el canvas se escala a pantalla completa sin tocar coordenadas).
**Cómo correrlo**: servidor local en el puerto 8080 (`.claude/launch.json` ya tiene la config "Game Server": `python -m http.server 8080`). Abrir `http://localhost:8080/cripta_nekkman_game.html`.
**Basado en**: un mockup de Figma + un GDD (`.docx`) hecho para la materia de diseño de videojuegos.

---

## 📐 Arquitectura general

Todo vive en un único `<script>` dentro del HTML. Estructura de la escena de Phaser:

```js
scene: {
    init: init,       // recibe { level } al hacer scene.scene.restart({level: N})
    preload: preload,  // carga las 5 texturas del esqueleto normal
    create: create,    // arma todo el nivel: player, trampas, enemigos, puerta, HUD refs
    update: update      // bucle principal (combate, hechizos, HUD, regen, etc.)
}
```

No hay clases: todo son funciones sueltas + variables `let`/`const` a nivel de módulo (compartidas por closures). `scene` es una variable global que apunta a la instancia de la escena viva (se asigna en `create()` con `scene = this`).

### Config data-driven clave

- **`ENEMY_TYPES`** (`normal` / `tanque` / `mago`): un solo objeto de config por categoría controla a TODOS los enemigos de ese tipo. Values: `health`, `speed`, `attackType` (`melee`/`ranged`), `chargeTime`, `attackDamage`, `armor`, etc. `normal` es el único con `sprite: {...}` (ver sección Sprite).
- **`ENEMY_SPAWNS`**: array de `{ type, x, y }` — dónde y de qué tipo spawnea cada instancia. Agregar un enemigo más de una categoría existente es sumar una línea acá.
- **`SPELLS`** (`damage` = Bola de Fuego, `immobilize` = Inmovilizar): daño/duración + cooldown en ms.
- **`trapPositions`** (pozos grises, bloquean el pathfinding por completo) y **`blueTrapPositions`** (trampas eléctricas, dañan pero el pathfinding solo las evita "cuando puede", no las bloquea).
- Todo lo de arriba (salvo `ENEMY_SPAWNS`/posiciones de trampas) es editable en caliente desde el panel **⚙️ Editor** (esquina superior derecha) vía `bindSlider(inputId, valueId, onChange)`.

### Sistemas principales

1. **Movimiento + combate del jugador**: WASD, ESPACIO ataca (rectángulo verde = "Yamel"), cooldown en frames (`PLAYER_ATTACK_COOLDOWN`, editable).
2. **Enemigos con A\* pathfinding**: grilla de 32px (`CELL_SIZE`), recalculan camino cada 80ms. `blockedCells` = pozos grises (bloqueo duro), `blueTrapCells` = trampas azules (costo alto, no bloqueo duro). Un solo `updateEnemyInstance(inst)` maneja las 3 categorías, ramificando por `type.attackType`.
3. **Hechizos** (barra inferior, slots 1-4, solo 1 y 2 usados): click para armar, click sobre el mundo para castear. Si le pegás a un enemigo → daño/inmovilizar + efecto de explosión. Si erras (le pegás al suelo) → efecto de impacto en el piso + igual consume cooldown.
4. **Mecanismo antiguo (cubo negro, centro del mapa, `interactObject`)**: al acercarse y presionar E, aparece un modal con 3 opciones, una es la correcta (random cada partida). Si acertás: `interactActivated = true`, el cubo se pone dorado, y **se destraba la puerta** (ver abajo).
5. **Puerta + transición de nivel** (agregado en esta sesión, ver más abajo).
6. **Editor de Parámetros** (panel lateral, botón "⚙️ Editor"): sliders que tocan las mismas variables/config de arriba en caliente, incluso con la partida en curso. Pausa el juego mientras está abierto.
7. **Optimización de HUD**: `dom` (referencias cacheadas por `cacheDom()`) + `hudLast` (dirty-checking) para no hacer `getElementById` ni reescribir el DOM todos los frames si el valor no cambió.

---

## 🦴 Sprite del Esqueleto Normal (agregado esta sesión)

Antes todos los enemigos eran rectángulos de color (`Phaser.Shape`). Ahora **solo el Esqueleto Normal** usa un sprite de caminata dibujado a mano (5 PNGs sueltos, no un spritesheet), copiados a `E:\Curso\assets\skeleton_walk\{1..5}.png` desde `D:\Diseño de videojuegos\TP2\walk2\walk2\`. Tanque y Mago siguen siendo rectángulos (decisión explícita del usuario).

**Puntos técnicos importantes (si hay que tocar esto de nuevo):**

- `ENEMY_TYPES.normal.sprite` define `animKey`, `displayWidth`/`displayHeight` (tamaño visual, MÁS GRANDE que el hitbox de colisión) y `facing` (`'left'`: el dibujo original mira hacia la izquierda de forma nativa — **no asumir 'right'**, ya causó un bug de flip invertido).
- `createEnemyInstance()` ramifica: si `type.sprite` existe crea un `add.sprite(...)`, si no un `add.rectangle(...)`. Ambos caminos comparten el resto de la lógica (`applyEnemyTint`/`clearEnemyTint` son los helpers polimórficos que abstraen `setTint()` (Sprite) vs `setFillStyle()` (Shape) — mezclarlos fue un bug clásico ya resuelto).
- **Bug de tamaño resuelto**: los 5 PNGs tienen resoluciones nativas distintas (309x484, 307x498, 312x518, 243x606, 366x531). `setDisplaySize()` fija un scale que, si no se corrige, hace que el sprite "pulse" de tamaño al cambiar de frame. Se corrige reaplicando `setDisplaySize` en cada evento `'animationupdate'`.
- **Bug de hitbox resuelto**: `body.setSize()` recibe medidas en espacio LOCAL (pre-escala) y Phaser recalcula `body.width/height` a partir de `scaleX/scaleY` en su propio ciclo interno (`Body.updateBounds`), lo que desincronizaba el hitbox un frame por el cambio de escala entre dibujos. Solución: en `updateEnemyInstance()`, dentro del bloque `if (inst.isSprite)`, se fuerza `body.width/height/halfWidth/halfHeight` al valor de `type.width/height` en TODOS los ticks, sin depender del cálculo automático de Phaser.
- **Sombra**: cada instancia con sprite tiene un `inst.shadow` (elipse negra, `fillAlpha: 0.1`, depth 9, un punto por debajo del sprite en depth 10) que sigue la posición del sprite cada tick.
- **Velocidad de animación editable**: slider "Velocidad de animación (caminata)" en el Editor (sección Esqueleto Normal), 1-24 fps. Como Phaser 3.55 no tiene un `updateFrameRate()` público en `Animation`, la función `setSkeletonWalkFps(fps)` recalcula a mano `frameRate`/`msPerFrame`/`duration` en el objeto `Animation` compartido Y en el `AnimationState` de cada sprite que ya está reproduciendo la animación (si no, un enemigo ya caminando no toma el cambio hasta la próxima vez que arranca a moverse).

---

## 🚪 Puerta + Nivel 2 (agregado esta sesión)

**Ubicación**: lado izquierdo del mapa, `door` en `(60, 384)`, tamaño 30x140. `doorTrigger` (zona invisible) en `(20, 384)`, 40x140, cubre la franja entre la puerta y el borde del mundo.

**Flujo:**

1. Arranca trabada (rojo `0x8b1a1a`, con collider `player`↔`door`).
2. Al acertar el mecanismo antiguo (`showInteractResult(wasCorrect=true)`) se llama `unlockDoor()`: la puerta se pone verde (`0x2ecc71`) y se remueve el collider (`scene.physics.world.removeCollider(doorCollider)`).
3. Al pisar `doorTrigger` se dispara `onDoorTrigger()` → si `interactActivated` es true (guard de seguridad, aunque sin la puerta destrabada es físicamente inalcanzable) y no hay ya una transición en curso (`levelTransitioning`), llama a `playLevelTransitionCinematic()`.
4. **Cinemática**: pausa el juego (`isPaused = true`, congela enemigos), fade a negro (rectángulo `depth:200`, tween de alpha 500ms) → texto "NIVEL N" (`depth:201`, fade in 400ms, se mantiene 900ms, fade out 300ms) → `scene.scene.restart({ level: nextLevel })`.
5. `init(data)` lee `data.level` y actualiza `currentLevel` (variable de módulo). `create()` reconstruye el nivel entero (puerta trabada de nuevo, mecanismo reseteado, enemigos nuevos) — a partir de nivel 2 se suman 2 enemigos extra (`normal` + `tanque`) como progresión de dificultad.
6. El HUD (`this.statusText`) ahora arranca con `Nivel X | ...` antes de vida/enemigos/cooldown.

**Si se quiere expandir a más niveles reales** (mapas distintos, no solo "más enemigos"): lo más simple es, en `create()`, ramificar `trapPositions`/`blueTrapPositions`/`ENEMY_SPAWNS` según `currentLevel` (hoy son `const` a nivel de módulo — habría que convertirlos en funciones o arrays indexados por nivel).

---

## ⚠️ Limitación del entorno de testing (importante para el próximo chat)

El navegador de pruebas (Browser pane) en este entorno tiene un bug/comportamiento donde, si el panel no está visualmente desplegado del lado del usuario, el `requestAnimationFrame` de Phaser queda completamente congelado (`scene.time.now` no avanza, tweens/`delayedCall` no progresan, ni siquiera `scene.scene.restart()` se procesa). Screenshots fallan con "the Browser pane is not displayed, so the page is not compositing frames".

**Workaround usado y que funciona:** avanzar el motor a mano desde `javascript_tool` con `game.step(time, delta)` (NO `game.loop.step(time)` — ese método sí tiene un bug de cómputo de delta si se le pasan timestamps que no coinciden con el timeline interno del loop, y deja los timers/tweens sin avanzar aunque `scene.time.now` sí crezca). Patrón que funciona:

```js
let t = performance.now();
for (let i = 0; i < N; i++) { t += 16.6667; game.step(t, 16.6667); }
```

Con esto se puede simular cualquier cantidad de tiempo de juego (cooldowns, animaciones, cinemáticas, regeneración) y verificar el estado real inspeccionando variables (`enemies`, `door.fillColor`, `scene.statusText.text`, etc.) sin depender de que el rAF real corra ni de screenshots.

---

## ✅ Estado actual (todo verificado y funcionando)

- Efectos de impacto de hechizos (acierto vs error, con su propio cooldown-por-error) + optimización de HUD (DOM cacheado + dirty-checking) y de bucles calientes (`updateGame`).
- Esqueleto Normal con sprite de caminata animado (5 frames, tamaño visual y hitbox estables en todos los frames), flip de dirección correcto, sombra circular, velocidad de animación editable desde el Editor.
- Puerta del lado izquierdo que se destraba con el mecanismo del cubo negro y, al cruzarla, dispara una mini cinemática (fade a negro + "NIVEL N") y pasa al nivel siguiente (más enemigos, todo reseteado).

## 💡 Ideas pendientes / no pedidas todavía

- Niveles con mapas realmente distintos (no solo "mismo mapa + más enemigos").
- Aplicar sprite de caminata a Tanque y Mago (por ahora explícitamente rectángulos, decisión del usuario).
- Sonido / música (no se tocó en ninguna sesión hasta ahora).
