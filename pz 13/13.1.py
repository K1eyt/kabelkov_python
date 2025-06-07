#1. В двумерном списке найти сумму и произведение элементов столбца N (N задать с
#клавиатуры).

import random

# Ввод размеров матрицы
rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

matrix = []
for i in range(rows):
    row = [random.randint(1, 10) for _ in range(cols)]
    matrix.append(row)

print("\nСгенерированная матрица:")
for row in matrix:
    print(row)

N = int(input("\nВведите номер столбца N (начиная с 0): "))

if N < 0 or N >= cols:
    print("Ошибка: номер столбца выходит за пределы диапазона")
else:
    # Вычисление суммы и произведения элементов столбца N
    column_sum = 0
    column_product = 1
    for row in matrix:
        column_sum += row[N]
        column_product *= row[N]

    print(f"\nСумма элементов столбца {N}: {column_sum}")
    print(f"Произведение элементов столбца {N}: {column_product}")