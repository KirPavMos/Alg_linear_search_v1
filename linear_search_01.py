# DZ_01_Линейный поиск и сложности
import timeit

def linear_search(arr, n, key):
    for i in range(0, n):
        if arr[i] == key:
            return i
    return -1

# Определение функции swap_test
def swap_test():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = len(arr)
    key = 7
    return linear_search(arr, n, key)  # Возвращаем результат, а не выводим его

# Вызов функции один раз для вывода результата
result = swap_test()
print("Результат поиска:", result)

# Измерение времени выполнения функции swap_test
time_taken = timeit.timeit(stmt=swap_test, number=100)
print("Время выполнения 100 вызовов функции:", time_taken)