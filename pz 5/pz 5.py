#Вариант 12. Составить функцию, которая выполнит суммирования числового ряда
def sum_of_series(n):
    return n * (n + 1) // 2
n = input("Введите целое число: ")
while True:
    try:
        n = int(n)
        break
    except ValueError:
        print('Неправильно ввели! Попробуйте снова.')
        n = input("Введите целое число: ")

result = sum_of_series(n)
print(result)
