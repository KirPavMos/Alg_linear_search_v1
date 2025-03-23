import random

# Функция линейного поиска
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i  # Возвращаем индекс найденного элемента
    return -1  # Если элемент не найден

# Создаем список из 100 случайных чисел в диапазоне от 1 до 1000
random_numbers = [random.randint(1, 1000) for _ in range(100)]

# Выводим список для наглядности (опционально)
print("Список случайных чисел:", random_numbers)

# Значения, которые будем искать
search_values = [5, 25, 45, 55, 75]

# Выполняем линейный поиск для каждого значения
results = {}
for value in search_values:
    index = linear_search(random_numbers, value)
    if index != -1:
        results[value] = f"Найдено на индексе {index}"
    else:
        results[value] = "Не найдено"

# Выводим результаты
print("\nРезультаты поиска:")
for key, value in results.items():
    print(f"Значение {key}: {value}")