#В12. Дано двузначное число. Найти сумму и произведение его цифр.
number = int(input("Введите двузначное число: "))
if 10 <= number <= 99:  #Проверка, двузначное ли число
    x = number // 10
    y = number % 10
    sum = x + y
    proiz = x * y
    print(f"Сумма цифр: {sum}")
    print(f"Произведение цифр: {proiz}")
else:
    print("Ошибка: переписывай")