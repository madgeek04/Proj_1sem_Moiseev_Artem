# Практическая работа №2
# Дано трёхзначное число, вывести последнюю и вторую цифру
n = int(input()) # Ввод натурального, трёхзначного числа
a = n % 10 # Находим последнее число, через расчёт остатка
b = (n // 10) % 10 # Находим второе число, через расчёт остатка
print(a, b, sep='') # Выводим последнее  и второе число, без пробелов