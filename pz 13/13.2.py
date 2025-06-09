#В двумерном списке найти отрицательные элементы, сформировать из них новый
#массив. Вывести размер полученного массива.

import random

rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

matrix = [list(map(lambda _: random.randint(-10, 10), range(cols))) for _ in range(rows)]

print("\nСгенерированная матрица:")
list(map(print, matrix))
negative_elements = [x for row in matrix for x in row if x < 0]

print("\nОтрицательные элементы:", negative_elements)
print("Количество отрицательных элементов:", len(negative_elements))