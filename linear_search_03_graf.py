# DZ_03_Линейный поиск и сложности алгоритмов
# Сравните время выполнения линейного поиска для разных
# размеров списков (например, 10, 100, 1000 элементов).

import timeit
import random

def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

def measure_time(arr_size, key):
    arr = [random.randint(1, arr_size * 10) for _ in range(arr_size)]
    time_taken = timeit.timeit(lambda: linear_search(arr, key), number=1000)
    return time_taken

sizes = [10, 100, 1000]
key = 42

for size in sizes:
    time_taken = measure_time(size, key)
    print(f"Размер списка: {size}, Время выполнения: {time_taken:.6f} секунд")