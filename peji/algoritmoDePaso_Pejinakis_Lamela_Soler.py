"""
Integrantes:
    * Juan Pejinakis
    * Pablo Lamela
    * Milagros Soler
"""

import json
from collections import deque

def cargar_grafo(desde_archivo):
    with open(desde_archivo, 'r') as f:
        grafo = json.load(f)
    return grafo['E']

def buscar_camino(grafo, inicio, fin):
    cola = deque([[inicio]])
    visitados = set()
    
    while cola:
        camino = cola.popleft()
        nodo = camino[-1]

        if nodo == fin:
            return camino
        
        if nodo not in visitados:
            visitados.add(nodo)
            for vecino in grafo.get(nodo, []):
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                cola.append(nuevo_camino)

    return None

archivo_grafo = '../archivosPaso-b/20k-b.json'
grafo = cargar_grafo(archivo_grafo)

nodo_inicial = '12'
nodo_final = '19229'

camino_encontrado = buscar_camino(grafo, nodo_inicial, nodo_final)

if camino_encontrado:
    print(f"Camino encontrado: {' -> '.join(camino_encontrado)}")
else:
    print("No se encontró un camino entre los nodos especificados.")
