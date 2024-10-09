from K_arreglo import K_arreglo
from functools import reduce
import random

class K_arreglo_uni(K_arreglo):
    def __init__(self, dimensiones):
        super().__init__(dimensiones)
        largo_arr_uni = reduce(lambda x, y: x * y, self.dimensiones)
        self.inscriptos:list = [0] * largo_arr_uni
        self.capacidad:list = [0] * largo_arr_uni

    def cargar_estructuras(self):
        limite_inf_capacidad = 20
        limite_sup_capacidad = 50

        for i_edif in range(self.dimensiones[0]):
            for j_piso in range(self.dimensiones[1]):
                for k_ala in range(self.dimensiones[2]):
                    for l_aula in range(self.dimensiones[3]):
                        capacidad_random = random.randint(limite_inf_capacidad, limite_sup_capacidad)
                        for m_bloque in range(self.dimensiones[4]):
                            indice_uni = self.h([i_edif, j_piso, k_ala, l_aula, m_bloque], self.dimensiones)
                            self.capacidad[indice_uni] = capacidad_random
                            inscriptos_random = random.randint(limite_inf_capacidad, capacidad_random)
                            self.inscriptos[indice_uni] = inscriptos_random

    def aula_por_bloq_mayor_ocupacion(self):
        max_porcentaje = -1
        max_coords = (0, 0, 0, 0, 0)  # (edificio, piso, ala, aula, bloque horario)
        ocupacion_max = 0
        capacidad_max = 0

        for i_edif in range(self.dimensiones[0]):
            for j_piso in range(self.dimensiones[1]):
                for k_ala in range(self.dimensiones[2]):
                    for l_aula in range(self.dimensiones[3]):
                        for m_bloque in range(self.dimensiones[4]):
                            indice_uni = self.h([i_edif, j_piso, k_ala, l_aula, m_bloque], self.dimensiones)
                            if self.capacidad[indice_uni] > 0:
                                ocup = self.inscriptos[indice_uni]
                                cap = self.capacidad[indice_uni]
                                porcentaje_ocupacion = (ocup / cap) * 100
                                if porcentaje_ocupacion > max_porcentaje:
                                    max_porcentaje = porcentaje_ocupacion
                                    max_coords = (i_edif, j_piso, k_ala, l_aula, m_bloque)
                                    ocupacion_max = ocup
                                    capacidad_max = cap
    
        print(f"El aula con mayor porcentaje de ocupación ({max_porcentaje}%) es:")
        print(f"| Edificio: {max_coords[0]} | Piso: {max_coords[1]} | Ala: {max_coords[2]} | Aula: {max_coords[3]} | Bloque horario: {max_coords[4]} |")
        print(f"Ocupacion: {ocupacion_max}")
        print(f"Capacidad: {capacidad_max}")

    def promedio_por_piso(self, bloq_horario):
        promedios = []
        for i_edif in range(self.dimensiones[0]):
            cant_alumnos = 0
            for j_piso in range(self.dimensiones[1]):
                for k_ala in range(self.dimensiones[2]):
                    for l_aula in range(self.dimensiones[3]):
                        indice_uni = self.h([i_edif, j_piso, k_ala, l_aula, bloq_horario], self.dimensiones)
                        cant_alumnos += self.inscriptos[indice_uni]
            promedios.append(cant_alumnos / self.dimensiones[0]+1)

        print(f"Promedios por piso: {promedios}")

    def alumnos_cada_ala(self, edif, piso, bloq_horario):
        #mapeo = {0: "norte", 1:"sur"}
        alumnos_por_ala = {}
        for i_ala in range(self.dimensiones[2]):
            for l_aula in range(self.dimensiones[3]):
                    indice_uni = self.h([edif, piso, i_ala, l_aula, bloq_horario], self.dimensiones)
                    ocuapcion = self.inscriptos[indice_uni]
                    alumnos_por_ala[i_ala] = alumnos_por_ala.get(i_ala,0) + ocuapcion

        print(f"Alumnos por ala: {alumnos_por_ala}")