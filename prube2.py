import random
import time
import matplotlib.pyplot as plt

# Función para calcular el promedio
def promedio(arr):
    return sum(arr) / len(arr)

# Función para calcular la desviación estándar
def desviacion_estandar(arr, promedio):
    suma_diff_cuadrados = sum((x - promedio) ** 2 for x in arr)
    return (suma_diff_cuadrados / len(arr)) ** 0.5

# Tamaños de los arreglos con intervalos de 1000
tamaños_arreglos = list(range(1000, 10001, 1000))
tiempos_ejecucion = []

for tamaño_arreglo in tamaños_arreglos:
    # Crear un arreglo y mezclarlo
    arreglo_entrada = list(range(1, tamaño_arreglo + 1))
    random.shuffle(arreglo_entrada)

    # Medir el tiempo de ejecución
    tiempo_inicio = time.time()

    # Ordenar el arreglo
    arreglo_ordenado = sorted(arreglo_entrada)

    tiempo_fin = time.time()
    tiempo_ejecucion = tiempo_fin - tiempo_inicio
    tiempos_ejecucion.append(tiempo_ejecucion)

    # Calcular el valor del punto medio
    indice_medio = len(arreglo_ordenado) // 2
    valor_medio = arreglo_ordenado[indice_medio]

    # Imprimir resultados
    print("\nArreglo de entrada:", arreglo_entrada)
    print("\nArreglo ordenado:")
    print(arreglo_ordenado)
    print("\nValor del punto medio:", valor_medio)
    print("\nTiempo de Ejecución:", tiempo_ejecucion)

# Aumentar el ancho de las barras 
ancho_barras = 150

# Crear la gráfica de barras 
plt.bar(tamaños_arreglos, tiempos_ejecucion, width=ancho_barras, align='center', alpha=0.7)
plt.xticks(tamaños_arreglos, rotation=80)
plt.xlabel('Tamaño del Arreglo')
plt.ylabel('Tiempo de Ejecución (segundos)')
plt.title('Tiempo de Ejecución vs. Tamaño del Arreglo')
plt.grid(True)

# Mostrar la gráfica
plt.show()
