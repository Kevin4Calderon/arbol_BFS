def buscar_ruta_BFS(grafo, inicio, objetivo):
    visitados = []
    cola = [[inicio]]  # cada elemento es una ruta

    while cola:
        ruta = cola.pop(0)
        nodo = ruta[-1]

        if nodo == objetivo:
            return ruta

        if nodo not in visitados:
            visitados.append(nodo)

            for vecino in grafo.get(nodo, []):
                nueva_ruta = list(ruta)
                nueva_ruta.append(vecino)
                cola.append(nueva_ruta)

    return []