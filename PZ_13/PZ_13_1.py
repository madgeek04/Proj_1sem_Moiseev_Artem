from random import randint
import math
n = [randint(-9, 9) for i in range(int(input()))]
print(max([i for i in n if i > 0]))
print(min([i for i in n if i < 0]))
print(math.prod(n))
