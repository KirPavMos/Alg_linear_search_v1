# DZ_01_Линейный поиск и сложности
1. Временная сложность (Time Complexity)
Временная сложность линейного поиска зависит от размера входных данных (длины массива) и положения искомого элемента.

2. Лучший случай (Best Case):
Искомый элемент находится на первом месте в массиве.
В этом случае алгоритм завершает работу после одной итерации.
Временная сложность: O(1).

3. Средний случай (Average Case):
Искомый элемент находится где-то в середине массива.
В среднем, алгоритму потребуется проверить половину элементов массива.
Временная сложность: O(n/2), что упрощается до O(n).

4. Худший случай (Worst Case):
Искомого элемента нет в массиве, или он находится на последнем месте.
В этом случае алгоритм проверяет все элементы массива.
Временная сложность: O(n).

5. Итог по временной сложности:
В худшем и среднем случае временная сложность линейного поиска составляет O(n), где n — количество элементов в массиве.
В лучшем случае — O(1).

6. Пространственная сложность (Space Complexity)
Пространственная сложность алгоритма линейного поиска зависит от объема дополнительной памяти, которую он использует.
Алгоритм линейного поиска не использует дополнительную память, которая зависит от размера входных данных. Он работает только с входным массивом и несколькими переменными (например, индексом и искомым значением).
Таким образом, пространственная сложность составляет O(1) (константная сложность).
Итог по пространственной сложности:
Пространственная сложность линейного поиска: O(1).

7. Объяснение выводов
Временная сложность O(n):
Алгоритм линейного поиска проходит по каждому элементу массива один раз в худшем случае. Это означает, что время выполнения растет линейно с увеличением размера массива.
Например, если массив содержит 1000 элементов, в худшем случае алгоритм выполнит 1000 сравнений.
Пространственная сложность O(1):
Алгоритм не создает новых структур данных, которые зависят от размера входного массива. Он использует только фиксированное количество переменных (например, для хранения индекса и искомого значения), поэтому объем используемой памяти не зависит от размера массива.
