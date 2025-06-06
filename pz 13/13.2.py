#В двумерном списке найти отрицательные элементы, сформировать из них новый
#массив. Вывести размер полученного массива.

# Ввод двумерного списка (матрицы)
rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))
matrix = []
for i in range(rows):
    row = list(map(int, input(f"Введите {cols} элементов строки {i + 1} через пробел: ").split()))
    matrix.append(row)

# Поиск отрицательных элементов и формирование нового массива
negative_elements = []
for row in matrix:
    for element in row:
        if element < 0:
            negative_elements.append(element)

# Вывод результата
print("Отрицательные элементы:", negative_elements)
print("Размер полученного массива:", len(negative_elements))