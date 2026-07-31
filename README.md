# La Cripta de Nekkman

TP2 — Diseño de Videojuegos (Módulo Level Design). Juego en Phaser 3, un solo
archivo HTML (`cripta_nekkman_game.html`), sin backend — corre entero en el navegador.

## Links

- **Jugar** (sin botones de edición): la URL del sitio publicado, tal cual.
- **Editar** (mapa + balance de enemigos/jugador/hechizos): la misma URL +
  `?editor=1`. Ahí aparecen los botones "⚙️ Editor" y "🗺️ Editor de Mapa".

Los botones de edición NO son un login real — solo están ocultos con CSS a menos
que la URL tenga `?editor=1`. Alcanza para que un compañero/profesor que entra al
link normal no vea ni un botón de edición, pero no es un sistema de permisos
seguro (cualquiera que sepa el truco de la URL, o abra las devtools, podría
forzarlos).

## Cómo publicar tus cambios

1. Jugá con `?editor=1`, editá el mapa y/o los parámetros (Editor de Parámetros).
   Todo se autoguarda en el navegador (localStorage).
2. Para que esos cambios viajen al sitio publicado (y los vea cualquiera que
   entre desde otra compu), tenés que volcarlos a `cripta_nekkman_config.json`:
   - Abrí el Editor de Parámetros → sección "📁 Archivo de guardado".
   - Tocá "💾 Descargar cripta_nekkman_config.json" y guardalo reemplazando el
     que ya está en esta misma carpeta (al lado del `.html`).
   - (Opcional, solo Chrome/Edge) "Vincular archivo de guardado" para que cada
     "Guardar" lo escriba solo, sin tener que descargar/mover a mano cada vez.
3. `git add -A && git commit -m "..." && git push`
4. GitHub Pages redeploya solo en ~1 minuto. No hace falta tocar nada más.

El juego lee `cripta_nekkman_config.json` al arrancar (`tryLoadBundledConfig`) y
lo aplica si es más nuevo que lo que el navegador de quien juega ya tenía
guardado — así cualquiera que entre ve siempre tu última versión publicada.

## Desarrollo local

```
python -m http.server 8080
```

y abrís `http://localhost:8080/cripta_nekkman_game.html` (agregá `?editor=1`
para ver los botones de edición).
