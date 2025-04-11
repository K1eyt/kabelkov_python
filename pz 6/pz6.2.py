#Дан список размера N и целое число K (1 < K < N). Осуществить сдвиг элементов списка вправо на K позиций
# (при этом A₁ перейдет в Aₖ₊₁, A₂ — в Aₖ₊₂, ..., Aₙ₋ₖ — в Aₙ, а исходное значение K последних элементов будет потеряно).
# Первые K элементов полученного списка положить равными 0.
import random
N = int(input("Введите размер списка (N): "))

lst = [random.randint(0, 100) for _ in range(N)]
print("Случайный список:", lst)

max_sum = float('-inf')
result = []
for i in range(len(lst) - 1):
    if lst[i] + lst[i + 1] > max_sum:
        max_sum = lst[i] + lst[i + 1]
        result = [lst[i], lst[i + 1]]

if len(result) == 2:
    print(f"Максимальная сумма у элементов {min(result)} и {max(result)}.")
else:
    print("Не удалось найти пары.")
