#1. В двумерном списке найти сумму и произведение элементов столбца N (N задать с
#клавиатуры).

import random

rows, cols = map(int, (input("Введите количество строк: "), input("Введите количество столбцов: ")))
matrix = [list(map(lambda _: random.randint(1, 10), range(cols))) for _ in range(rows)]

print("\nСгенерированная матрица:")
list(map(print, matrix))

N = int(input("\nВведите номер столбца N (начиная с 0): "))

if N < 0 or N >= cols:
    print("Ошибка: номер столбца выходит за пределы диапазона")
else:
    column = list(map(lambda row: row[N], matrix))
    sum_result = sum(column)
    product_result = 1
    for num in column:
        product_result *= num

    print(f"\nСумма элементов столбца {N}: {sum_result}")
    print(f"Произведение элементов столбца {N}: {product_result}")