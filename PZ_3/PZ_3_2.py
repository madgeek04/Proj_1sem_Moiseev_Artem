# Практическая №3 №2
# Если вводимые координаты в нач.(.), вывести 0. Если лежит на x, вывести 1. Если лежит на y вывести 2. Иначе вывести 3
x, y = int(input()), int(input()) # Ввод координат
if x == 0 and y == 0: # Если координаты в нач.(.), то
    print(0) # Выводим 0
elif y == 0: # Если лежит на оси x, то
    print(1) # Выводим 1
elif x == 0: # Если лежит на оси y, то
    print(2) # Выводим 2
else: # Если координаты не в нач.(.) и не лежат на плоскостях, то
    print(3) # Выводим 3