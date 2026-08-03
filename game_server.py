#!/usr/bin/env python3
"""
Servidor local para "La Cripta de Nekkman" — igual que `python -m http.server`
(sirve esta misma carpeta tal cual), pero además expone POST /save-config:
recibe el JSON completo del mapa/config y lo escribe DIRECTO en disco, en
cripta_nekkman_config.json, al lado de este script.

Por qué existe: antes, la única forma de que una edición sobreviviera más
allá de esa pestaña del navegador era descargar el JSON a mano y moverlo, o
vincular un archivo (solo Chrome/Edge, y el permiso se puede perder). Con
este endpoint, cada vez que el juego llama a saveMapEditorState()/
saveEditorSettings() (o sea, en CADA edición, no solo al tocar un botón),
también escribe acá — sin pedir permiso, sin depender del navegador.

Uso: python game_server.py [puerto]  (default 8080)
     http://localhost:8080/cripta_nekkman_game.html
"""
import http.server
import json
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(SCRIPT_DIR, "cripta_nekkman_config.json")


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path != "/save-config":
            self.send_response(404)
            self.end_headers()
            return
        try:
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length)
            data = json.loads(body)  # valida que sea JSON válido antes de tocar el archivo
            if not isinstance(data, dict):
                raise ValueError("el body no es un objeto JSON")

            # Escritura atómica: a un .tmp y después rename, para que un corte a
            # mitad de escritura (cierre del navegador, corte de luz) nunca deje
            # el archivo real corrupto a medio escribir.
            tmp_path = CONFIG_PATH + ".tmp"
            with open(tmp_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            os.replace(tmp_path, CONFIG_PATH)

            self._send_json(200, {"ok": True})
        except Exception as e:
            self._send_json(500, {"ok": False, "error": str(e)})

    def do_OPTIONS(self):
        self.send_response(204)
        self._cors_headers()
        self.end_headers()

    def _send_json(self, status, payload):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self._cors_headers()
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _cors_headers(self):
        # Mismo origen siempre (el juego se sirve de acá mismo), pero el fetch
        # del juego igual manda un preflight por el header Content-Type — sin
        # esto el POST fallaría.
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")

    def log_message(self, fmt, *args):
        # Menos ruido: solo loguea el guardado real, no cada GET de assets.
        if self.path == "/save-config":
            super().log_message(fmt, *args)


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    os.chdir(SCRIPT_DIR)
    print(f"Sirviendo {SCRIPT_DIR} en el puerto {port}")
    print(f"Guardado automático -> {CONFIG_PATH}")
    http.server.ThreadingHTTPServer(("", port), Handler).serve_forever()
