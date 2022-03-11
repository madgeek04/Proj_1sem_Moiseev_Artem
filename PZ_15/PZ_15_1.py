from random import randint

m, n, y, z = [int(input(i)) for i in ("Количество строк = ", "Количество столбцов = ", "От = ", "До = ")]
matrix = [[randint(y, z) for _ in range(n)] for j in range(m)]
print('Исходная матрица:')
for i in matrix:
    print(*i)
matrix[1] = [sum([matrix[i][x] for i in range(m)]) for x in range(n)]
print('Полученная матрица:')
for i in matrix:
    print(*i)
