#В-12. Дан список A размера N (N — нечетное число). Вывести его элементы с нечетными номерами в порядке убывания номеров: AN, AN-2, AN-4, ..., A1. Условный оператор не использовать.
import random

# Ввод размера списка N (должно быть нечётное число)
while True:
    try:
        N = int(input("Введите нечётное число N: "))
        if N % 2 == 1:  # Проверяем, что число нечётное
            break
        else:
            print("Ошибка! Введите нечётное число.")
    except ValueError:
        print("Ошибка! Введите целое число.")

# Создаём список A размера N со случайными числами
A = [random.randint(1, 100) for _ in range(N)]


result = A[-1::-2]

# Вывод результата
print("Список A:", A)
print("Результат:", result)

