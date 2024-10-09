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

    def destructive_Tsort(self):
        ST = []
        while self.P:
            ST.append(self.MIN())
            self.P = list(set(self.P)-set(self.MIN()))
            self.E = {node:self.E.get(node) for node in self.P}

        return ST


    def non_destructive_Tsort(self):
        visitedP = []
        nonVisitedP = self.P[:]
        EOfNonVisitedP = self.E.copy()
        ST = []

        #while calculate_difference_between_lists(self.P, visitedP) and Grafo(nonVisitedP, EOfNonVisitedP)

    def MIN(self):
        nodes = set(self.P)
        nodesWithLeftNeigh = set()
        for vecinos in self.E.values():
            nodesWithLeftNeigh.update(vecinos)

        nodesWithoutLeftNeigh = nodes - nodesWithLeftNeigh

        return list(nodesWithoutLeftNeigh)


def calculate_difference_between_lists(ls1, ls2):
        result = [item for item in ls1 if item not in ls2]
        return result

def read_json_file(file):
    with open(file, "r") as file:
        data = json.load(file)
    return data

def main():
    file_path = "./archivosPaso-b/20k-b.json"`
    file_path = "./test.json"
    data = read_json_file(file_path)
    P = data.get('P')
    E = data.get('E')
    grafo = Grafo(P, E)
    #print(grafo.search_algorithm('12','19000'))
    #print(grafo.search_algorithm('12','19229'))

    print(grafo.destructive_Tsort())

if __name__ == "__main__":
    main()
