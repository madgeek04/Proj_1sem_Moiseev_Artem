# Практическая №4 №1
# Вещ. число A, целое N. В 1 цикл найти сумму 1 + A + A**2 + ... + A**N
a, n = float(input()), int(input()) # Ввод вещ. числа A и целого N
s = 1 # Объявляем переменную для подсчёта(=1, потому что 1 + A)
for i in range(1, n + 1): # В один цикл от 1 до N
    s += a ** i # Считаем сумму
print(s) # Выводим результат