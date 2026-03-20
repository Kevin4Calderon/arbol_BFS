from flask import Flask, request, jsonify, send_from_directory
from BFS_ciudades import buscar_ruta_BFS

app = Flask(__name__)

# Grafo basado en tu imagen
grafo = {
    "Hidalgo": ["Jilo-York", "SLP", "Monterrey"],
    "Jilo-York": ["Hidalgo", "CDMX"],
    "QRO": ["SLP"],
    "SLP": ["QRO", "Hidalgo", "CDMX", "Zacatecas", "Tamaulipas"],
    "Zacatecas": ["SLP", "GDL"],
    "GDL": ["Zacatecas"],
    "CDMX": ["Jilo-York", "Morelos", "Tamaulipas", "SLP", "Monterrey"],
    "Morelos": ["CDMX", "Tamaulipas"],
    "Tamaulipas": ["Morelos", "CDMX", "SLP"],
    "Monterrey": ["Hidalgo", "CDMX"]
}

# Servir HTML
@app.route("/")
def index():
    return send_from_directory(".", "index.html")

# Endpoint BFS
@app.route("/resolver")
def resolver():
    inicio = request.args.get("inicio")
    objetivo = request.args.get("objetivo")

    if not inicio or not objetivo:
        return jsonify({"error": "Faltan parámetros"}), 400

    ruta = buscar_ruta_BFS(grafo, inicio, objetivo)

    return jsonify(ruta)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)