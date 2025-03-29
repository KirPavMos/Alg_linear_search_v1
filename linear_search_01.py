# DZ_01_Линейный поиск и сложности алгоритмов
# Реализуйте алгоритм линейного поиска на языке Python. Функция
# должна принимать список и элемент для поиска, и возвращать
# индекс элемента или -1, если элемент не найден

import timeit

def linear_search(arr, n, key):
    for i in range(0, n):
        if arr[i] == key:
            return i
    return -1

def swap_test():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = len(arr)
    key = 7
    return linear_search(arr, n, key)

result = swap_test()
print("Результат поиска:", result)

time_taken = timeit.timeit(stmt=swap_test, number=100)
print("Время выполнения 100 вызовов функции:", time_taken)