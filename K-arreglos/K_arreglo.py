from abc import ABC, abstractmethod
import random
import time

class K_arreglo(ABC):
    def __init__(self, dimensiones):
        if len(dimensiones) != 5:
            raise ValueError("Debe pasarse una lista con 5 dimensiones")
        self.dimensiones = dimensiones

    def h(self, indices, dimensiones):
        if len(indices) != len(dimensiones):
            raise ValueError("Las listas de índices y dimensiones deben tener la misma longitud")
        
        result = 0
        multiplicador = 1
        
        for i in reversed(range(len(indices))):
            result += indices[i] * multiplicador
            multiplicador *= dimensiones[i]
        
        return result

    def run(self):
        inicio = time.time()
        self.cargar_estructuras()
        self.aula_por_bloq_mayor_ocupacion()
        self.promedio_por_piso(random.randint(0, self.dimensiones[4]-1))
        self.alumnos_cada_ala(random.randint(0,self.dimensiones[0]-1),random.randint(0,self.dimensiones[1]-1),random.randint(0,self.dimensiones[4]-1))
        fin = time.time()
        tiempo = fin - inicio
        print(f"Tiempo de ejecución: {tiempo} segundos")
        return tiempo

    @abstractmethod
    def cargar_estructuras(self):
        pass

    @abstractmethod
    def aula_por_bloq_mayor_ocupacion(self):
        pass

    @abstractmethod
    def promedio_por_piso(self, bloq_horario):
        pass

    @abstractmethod
    def alumnos_cada_ala(self, edif, piso, bloq_horario):
        pass
