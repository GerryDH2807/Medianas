import random
import time
import matplotlib.pyplot as plt

def calcular_mediana(subarray):
    subarray.sort()
    n = len(subarray)
    if n % 2 == 0:
        mid1 = subarray[n // 2]
        mid2 = subarray[n // 2 - 1]
        mediana = (mid1 + mid2) / 2
    else:
        mediana = subarray[n // 2]
    return mediana

def division(arr):
    subarrays = [sorted(arr[i:i+5]) for i in range(0, len(arr), 5)]
    return subarrays

def media_de_medianas(medians):
    if len(medians) <= 5:
        return calcular_mediana(medians)
    else:
        submedians = [media_de_medianas(medians[i:i+5]) for i in range(0, len(medians), 5)]
        return media_de_medianas(submedians)

def tiempo_ejecucion(input_array):
    tiempo_inicial = time.time()
    subarrays = division(input_array)
    medianas_de_subarrays = [calcular_mediana(subarray) for subarray in subarrays]
    medianas_de_subarrays.sort()
    media_de_las_medianas = media_de_medianas(medianas_de_subarrays)
    tiempo_final = time.time()
    execution_time = tiempo_final - tiempo_inicial
    
    return execution_time, subarrays, medianas_de_subarrays

# Lista inicializada
input_sizes = list(range(1, 10001, 1000))
tiempo_promedio_de_ejecucion = []
desviacion_times = []

for num in input_sizes:
    input_array = list(range(1, num + 1))
    random.shuffle(input_array)

    execution_times = []
    subarrays_list = []  
    median_lists = []    

    num_measurements = 10 
    for _ in range(num_measurements):
        execution_time, subarrays, medians = tiempo_ejecucion(input_array)
        execution_times.append(execution_time)
        subarrays_list.append(subarrays)
        median_lists.append(medians)

    # Calculo y almacenamiento del tiempo promedio de ejecución y la desviación estándar
    tiempo_promedio_de_ejecucion_actual = sum(execution_times) / num_measurements
    desviacion = (sum((t - tiempo_promedio_de_ejecucion_actual) ** 2 for t in execution_times) / (num_measurements - 1)) ** 0.5

    tiempo_promedio_de_ejecucion.append(tiempo_promedio_de_ejecucion_actual)
    desviacion_times.append(desviacion)

    # Imprimir subarreglos y sus medianas
    if num == input_sizes[-1]:
        print("Last Measurement:")
        for i, subarray in enumerate(subarrays_list[-1]):
            print(f"Subarreglo {i + 1}: {subarray}")
        print("Medianas de los subarreglos:", median_lists[-1])
        print("Mediana de las medianas:", calcular_mediana(median_lists[-1]))
        print()

# Imprimir reporte
for i, size in enumerate(input_sizes):
    print(f"Input Size: {size}, Tiempo en segundos: {tiempo_promedio_de_ejecucion[i]:.6f} , Desviacion estandar: {desviacion_times[i]:.6f} seconds")

# Gráficas
plt.figure(figsize=(10, 12))

# Subplot 1: Gráfica de línea con barras de error

plt.errorbar(input_sizes, tiempo_promedio_de_ejecucion, yerr=desviacion_times, fmt='-o', label='Execution Time')
plt.xlabel('Input Size')
plt.ylabel('Tiempo en segundos')
plt.title('Crecimiento en tiempo de ejecucion')
plt.legend()
plt.grid(True)

plt.show()  # Muestra la figura con los dos subplots en una misma ventana