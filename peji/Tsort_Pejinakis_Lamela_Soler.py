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

def calcular_orden_Topologico(grafo):
    orden_topologico =[]
    grados_entrada = {nodo: 0 for nodo in grafo}
    
    for nodo in grafo:
        for vecino in grafo[nodo]:
            if vecino not in grados_entrada:
                grados_entrada[vecino] = 0

    for nodo in grafo:
        for vecino in grafo[nodo]:
            grados_entrada[vecino]+=1
        
    cola= deque([nodo for nodo in grados_entrada if grados_entrada[nodo]==0])

    while cola:
        nodo = cola.popleft()
        orden_topologico.append(nodo)

        for vecino in grafo.get(nodo, []):
            grados_entrada[vecino]-=1
            if(grados_entrada[vecino]==0):
                cola.append(vecino)

    if len(orden_topologico) != len(grafo):
        raise ValueError("El grafo contiene un ciclo")

    return orden_topologico
    
archivo_grafo = 'test.json'
grafo = cargar_grafo(archivo_grafo)

try:
    orden_topologico = calcular_orden_Topologico(grafo)
    if orden_topologico:
        print(f"Orden topológico: {' -> '.join(orden_topologico)}")
except ValueError as e:
    print(e)

