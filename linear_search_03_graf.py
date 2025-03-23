# Сравнение времени выполнения линейного поиска для разных
# размеров списков

import timeit
import random

# Функция линейного поиска
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

# Функция для измерения времени выполнения
def measure_time(arr_size, key):
    arr = [random.randint(1, arr_size * 10) for _ in range(arr_size)]
    time_taken = timeit.timeit(lambda: linear_search(arr, key), number=1000)
    return time_taken

# Размеры списков для тестирования
sizes = [10, 100, 1000]
key = 42

# Измеряем время выполнения для каждого размера списка
for size in sizes:
    time_taken = measure_time(size, key)
    print(f"Размер списка: {size}, Время выполнения: {time_taken:.6f} секунд")