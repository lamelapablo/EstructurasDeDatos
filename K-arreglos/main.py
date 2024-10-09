# d0: edificio (4 edificios)
# d1: piso (5 pisos por edificio) 
# d2: ala (norte o sur) 
# d3: aula (25 aulas por ala) 
# d4: bloque horario (85 - 17 bloques horarios por 5 días) (17 bloques horarios en un dia)

import matplotlib.pyplot as plt
from K_arreglo_uni import K_arreglo_uni
from K_arreglo_multi import K_arreglo_multi

d0 = 4
d1 = 5
d2 = 2
d3 = 25
d4 = 85

def prueba_varias_dimensiones():
    dimensiones = range(3, 15)
    tiempos_uni = []
    tiempos_multi = []
    for dimension in dimensiones:
        k_arreglo_uni = K_arreglo_uni([dimension]*5)
        tiempo_uni = k_arreglo_uni.run()
        tiempos_uni.append(tiempo_uni)

        k_arreglo_multi = K_arreglo_multi([dimension]*5)
        tiempo_multi = k_arreglo_uni.run()
        tiempos_multi.append(tiempo_multi)
    
    # Grafico los resultados
    plt.plot(dimensiones, tiempos_uni, label='Uni', marker='o')
    plt.plot(dimensiones, tiempos_multi, label='Multi', marker='x')
    plt.xlabel('Dimensiones')
    plt.ylabel('Tiempo')
    plt.title('Comparación de Tiempos: Uni vs Multi')
    plt.legend()
    plt.grid(True)
    plt.show()
    #plt.savefig('comparacion_tiempos.png')
    #print("Grafico guardado como 'comparacion_tiempos.png'")
        

def main():
    print("*************** Inicia ejecucion con arreglos unidimensionales ***************")
    k_arreglo_uni = K_arreglo_uni([d0,d1,d2,d3,d4])
    k_arreglo_uni.run()
    print("*************** Finaliza ejecucion con arreglos unidimensionales ***************")

    print()

    print("*************** Inicia Ejecucion con arreglos multidimensionales ***************")
    k_arreglo_multi = K_arreglo_multi([d0,d1,d2,d3,d4])
    k_arreglo_uni.run()
    print("*************** Finaliza ejecucion con arreglos multidimensionales ***************")

if __name__ == "__main__":
    prueba_varias_dimensiones()
