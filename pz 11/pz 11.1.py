#1. Средствами языка Python сформировать текстовый файл (.txt), содержащий
#последовательность из целых положительных и отрицательных чисел. Сформировать
#новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
#обработку элементов:
#Исходные данные:
#Количество элементов:
#Максимальный элемент:
#Среднее арифметическое элементов первой трети:

import random

l = [' '.join(str(random.randint(-100, 100)) for _ in range(8))]

# Записываем данные в файл data_3.txt
f3 = open('data_3.txt', 'w', encoding='utf-8')
f3.writelines(l)
f3.close()

# Создаем файл data_4.txt
f4 = open('data_4.txt', 'w', encoding='utf-8')
f4.write('Исходные данные: ')
f4.write('\n')
f4.writelines(l)
f4.close()

# Читаем данные из data_3.txt
f3 = open('data_3.txt', encoding='utf-8')
k = f3.read()
k = k.split()
k = [int(num) for num in k]
f3.close()

max_num = max(k)
# Вычисляем среднее первой трети
third = len(k) // 3
first = k[:third] if third > 0 else k
first_third = sum(first) / len(first) if first else 0

# Дописываем результаты в data_4.txt
with open('data_4.txt', 'a', encoding='utf-8') as f4:
    f4.write('\n')
    f4.write(f'Количество элементов: {len(k)}\n')
    f4.write(f'Максимальный элемент: {max_num}\n')
    f4.write(f'Среднее арифметическое первой трети: {first_third:.2f}\n')
