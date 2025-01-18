#Дана непустая строка S и целое число N (> 0). Вывести строку, содержащую символы
#строки S, между которыми вставлено по N символов «*» (звездочка).

import random
S = (input("Введите непустую строку:"))
while True:
    if S == "":
        print("Строка пустая")
        S = (input("Введите непустую строку:"))
    else:
        break

N = random.randint(1 , 10)
stars = '*' * N
result = stars.join(S)
print(result)





