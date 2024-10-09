import json
from collections import deque

class AccessToNonExistingNode(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.msg = msg

class Grafo:
    def __init__(self, P, E):
        self.P = P
        self.E = E

    def search_algorithm(self, s, t):
        OPEN = deque([(s, None)])
        CLOSED = []

        if s not in self.P or t not in self.P:
            raise AccessToNonExistingNode(f"{s} or {t} are not in P")

        while OPEN:
            (z, y) = OPEN.popleft() [(1,3), (4,2), (5, 7)] [1,4,5]
            CLOSED.append((z, y))
        
            if t in self.R(z):
                CLOSED.append((t,z)) 
                print(f"Se ha alcanzado el nodo objetivo {t}") 
                camino = self.get_path(CLOSED, t)
                return camino
            
            for w in self.R(z):
                if w not in [n for n,_ in OPEN] and w not in [n for n,_  in CLOSED]:
                    OPEN.append((w,z))

        print(f'NO se encontro el nodo objetivo {t}')
        return CLOSED    

    def R(self, z):
        return self.E.get(z)
    
    def get_path(self,CLOSED, t):
        camino = []
        nodo_actual = t
        
        # Iteramos hasta que lleguemos al nodo de inicio s
        while nodo_actual is not None:
            # Encontramos el nodo actual en la lista CLOSED
            for nodo, padre in reversed(CLOSED):
                if nodo == nodo_actual:
                    camino.append((padre, nodo))
                    nodo_actual = padre
                    break
        
        # Como hemos construido el camino en orden inverso, lo revertimos
        camino.reverse()
        
        # Eliminamos el primer elemento del camino que contiene (None, s)
        if camino and camino[0][0] is None:
            camino = camino[1:]
        
        return camino


def read_json_file(file):
    with open(file, "r") as file:
        data = json.load(file)
    return data

def main():
    file_path = "./archivosPaso-b/20k-b.json"
    data = read_json_file(file_path)
    P = data.get('P')
    E = data.get('E')
    grafo = Grafo(P, E)
    #print(grafo.search_algorithm('12','19000'))
    print(grafo.search_algorithm('12','19229'))

if __name__ == "__main__":
    main()
