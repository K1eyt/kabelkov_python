#Вариант 12.Дано целое число N (>0). Найти значение выражения 1.1 - 1.2 + 1.3 - ... (N слагаемых,
#знаки чередуются).
while True:
    try:
        number = int(input("Введите целое число N (>0): "))
        if number > 0:
            result = sum(((-1) ** (i + 1)) * (1 + i / 10) for i in range(1, number + 1))
            print(f"Результат: {result:.2f}")
            break
        else:
            print("Число должно быть больше 0.")
    except ValueError:
        print("Неправильный ввод. Введите целое число.")


