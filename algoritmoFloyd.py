"""
Integrantes:
    * Juan Pejinakis
    * Pablo Lamela
    * Milagros Soler
"""


import numpy as np 
import random
import math

def generador_grafo(tamaño):
    matriz = []
    for f in range (0,tamaño):
        fila = []
        for c in range (0,tamaño):
            if(f==c):
                fila.append(0)
            else:
                numero_random= random.randint(1,9)
                fila.append(numero_random) 
        matriz.append(fila)
    return matriz

def mostrar_grafo(grafo):
    for fila in grafo:
        print(fila)
    print("\n")

def buscar_matriz_paso_costo_minimo(grafo_ORIGINAL):
    grafo = grafo_ORIGINAL

    for i in range(0,len(grafo)):
        for f in range(0,len(grafo)):
            for c in range(0,len(grafo)):
                if ((grafo[f][i] + grafo[i][c]) < grafo[f][c]):
                    grafo[f][c]=grafo[f][i] + grafo[i][c]
    
    return grafo
                
def recuperar_paso(matriz,nodoS,nodoLL):
    return matriz[nodoS][nodoLL]

def buscar_excentricidad(matriz):
    matriz_Aux = matriz
    aux = 0
    excentricidad = {"Nodo":"Excentricidad"}
    for f in range(0,len(matriz_Aux)):
        for c in range(0,len(matriz_Aux)):
            if matriz_Aux[f][c] > aux:
                excentricidad[f] = matriz_Aux[f][c]
        aux = 0
    
    return excentricidad

def buscar_centro(excentricidad):
    centro = {}
    contador=0
    for clave,valor in excentricidad.items():
        if contador == 0:
            contador+=1
        
        elif not centro:
            centro["Nodo"]=clave
            centro["Excentricidad"] = valor
        
        elif (valor < centro["Excentricidad"]):
            centro["Nodo"]=clave
            centro["Excentricidad"] = valor
    return centro 

    
#grafo=[[0,4,8,20,20],[4,0,1,2,20],[8,20,0,4,2],[20,2,4,0,7],[20,20,2,7,0]]
grafo=generador_grafo(5)
print("La matriz de adyacencia es:")
mostrar_grafo(grafo)

matriz_costo_minimo=buscar_matriz_paso_costo_minimo(grafo)
print("La matriz de costos minimos es:")
mostrar_grafo(matriz_costo_minimo)

nodoSalida = 3
nodoLLegada = 0
paso_minimo = recuperar_paso(matriz_costo_minimo,nodoSalida,nodoLLegada)
print("El paso minimo entre {} y {} es {}".format(nodoSalida,nodoLLegada,paso_minimo))

excentricidad = buscar_excentricidad(matriz_costo_minimo)
for clave, valor in excentricidad.items():
    print(f"{clave}: {valor}")
print("\n")

centro = buscar_centro(excentricidad)
print(centro)

#video del que me apoye https://www.youtube.com/watch?v=yWiNJt2WH44 y con el que verifique los datos  https://www.youtube.com/watch?v=h-nmexY9gtA