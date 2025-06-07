#В двумерном списке найти отрицательные элементы, сформировать из них новый
#массив. Вывести размер полученного массива.

import random

rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

matrix = []
for i in range(rows):
    row = [random.randint(-10, 10) for _ in range(cols)]
    matrix.append(row)

print("\nСгенерированная матрица:")
for row in matrix:
    print(row)

# Поиск отрицательных элементов и формирование нового массива
negative_elements = []
for row in matrix:
    for element in row:
        if element < 0:
            negative_elements.append(element)

print("\nОтрицательные элементы:", negative_elements)
print("Количество отрицательных элементов:", len(negative_elements))