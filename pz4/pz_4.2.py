#Дано целое число N (> 1). Вывести наибольшее из целых чисел K, для которых сумма
#1 + 2 + ... + K будет меньше или равна N, и саму эту сумму.
while True:
    try:
        N = int(input("Введите целое число N (> 1): "))
        if N > 1:
            break
        else:
            print("Число должно быть больше 1.")
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите целое число.")

k = 1
sum = 0

while sum < N:
    sum += k
    k += 1

print(f"Наименьшее K: {k - 1}")
print(f"Сумма 1 + 2 + ... + K: {sum}")

