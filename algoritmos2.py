import random
import time

# Función para calcular la media
def mean(arr):
    return sum(arr) / len(arr)

# Función para calcular la desviación estándar
def standard_deviation(arr, mean):
    squared_diff_sum = sum((x - mean) ** 2 for x in arr)
    return (squared_diff_sum / len(arr)) ** 0.5

# Tamaño del arreglo
array_size = 1000

# Crear un arreglo y mezclarlo
input_array = list(range(1, array_size + 1))
random.shuffle(input_array)

# Medir el tiempo de ejecución
start_time = time.time()

# Ordenar el arreglo
sorted_data = sorted(input_array)

# Calcular el valor del punto medio
mid_index = len(sorted_data) // 2
mid_value = sorted_data[mid_index]

# Calcular la media y la desviación estándar
arr_mean = mean(sorted_data)
std_deviation = standard_deviation(sorted_data, arr_mean)

end_time = time.time()
execution_time = end_time - start_time

# Imprimir resultados
print("\nArreglo:", input_array)
print("\nArreglo ordenado:")
print(sorted_data)
print("\nValor del punto medio:", mid_value)
print("\nDesviación estándar:", std_deviation)
print("\nTiempo de ejecución:", execution_time)
