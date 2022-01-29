# Практическая №13 №1
# В последовательности n чисел найти и вывести: 1. макс. среди положительных 2. мин. среди отрицательных
# 3. произведение элементов.
from random import randint
import math
n = [randint(-9, 9) for i in range(int(input()))]
print(max([i for i in n if i > 0]), '\n' + str(min([i for i in n if i < 0])), '\n' + str(math.prod(n)))
