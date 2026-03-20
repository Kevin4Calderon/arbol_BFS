from flask import Flask, request, send_file
from BFS import buscar_solucion_BFS

app = Flask(__name__)

# 👉 Servir el HTML
@app.route("/")
def home():
    return send_file("index.html")

# 👉 Endpoint BFS
@app.route("/resolver")
def resolver():
    inicial = request.args.get("inicial", "4,2,3,1")
    objetivo = request.args.get("objetivo", "1,2,3,4")

    # Convertir a listas
    estado_inicial = list(map(int, inicial.split(",")))
    solucion = list(map(int, objetivo.split(",")))

    # Ejecutar BFS
    nodo_solucion = buscar_solucion_BFS(estado_inicial, solucion)

    resultado = []
    nodo = nodo_solucion

    while nodo.get_padre() != None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()

    resultado.append(estado_inicial)
    resultado.reverse()

    return str(resultado)

if __name__ == "__main__":
    app.run()