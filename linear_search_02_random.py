# DZ_0_Линейный поиск и сложности алгоритмов
# Создайте список из 100 случайных чисел и выполните линейный
# поиск для нескольких различных значений. Запишите результаты

import random

def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

random_numbers = [random.randint(1, 1000) for _ in range(100)]

print("Список случайных чисел:", random_numbers)

search_values = [5, 25, 45, 55, 75]

results = {}
for value in search_values:
    index = linear_search(random_numbers, value)
    if index != -1:
        results[value] = f"Найдено на индексе {index}"
    else:
        results[value] = "Не найдено"

print("\nРезультаты поиска:")
for key, value in results.items():
    print(f"Значение {key}: {value}")