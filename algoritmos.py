import statistics
import random


def calculate_median(subarray):
    return statistics.median(subarray)

# Dividir el arreglo en sub arreglos
def split_array(arr):
    subarrays = [sorted(arr[i:i+5]) for i in range(0, len(arr), 5)]
    return subarrays

# Función para calcular la mediana de las medianas de forma recursiva
def recursive_median_of_medians(medians):
    if len(medians) <= 5:
        return calculate_median(medians)
    else:
        # Dividir las medianas en grupos de 5 y calcular las medianas de cada grupo
        submedians = [recursive_median_of_medians(medians[i:i+5]) for i in range(0, len(medians), 5)]
        # Calcular la mediana de las medianas 
        return recursive_median_of_medians(submedians)

# Arreglo
num = 10001
input_array = []
for i in range(1, num+1):
    input_array.append(i)
random.shuffle(input_array)

subarrays = split_array(input_array)

# Calcular las medianas de los subarreglos
medians_of_subarrays = [calculate_median(subarray) for subarray in subarrays]

# Ordenar las medianas de los subarreglos
medians_of_subarrays.sort()

# Calcular la mediana de las medianas de forma recursiva
final_median = recursive_median_of_medians(medians_of_subarrays)

# Imprimir los resultados
print("Arreglo:", input_array)
print("\nSubarreglos ordenados de 5 elementos:")
for i, subarray in enumerate(subarrays):
    print(f"Subarreglo {i + 1}: {subarray}")
print("\nMedianas de los subarreglos:", medians_of_subarrays)
print("\nMediana de las medianas:", final_median)
