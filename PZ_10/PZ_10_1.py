# Практическая №10 №1
# Средствами языка Python сформировать текстовый файл (.txt), содержайщий последовательность из целых положительных и
# отрицательных чисел. Сформировать новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов: Исхдные данные: Количество элементов: Индекс последнего минимального элемента:
# Умножаем все элементы на первый элемент:
print('5, 4, 3, 2, 1, -1, -2, -3, -4, -5', file=open('file7_1.txt', 'w'))
d, u = [int(i) for i in open('file7_1.txt').read().split(', ')], open('file_new7_1.txt', 'w')
print('Исходные данные:', open('file7_1.txt').read(), file=u)
print('Количество элементов:', len(open('file7_1.txt').read().split(', ')), '\n', file=u)
print('Индекс последнего минимального элемента:', d.index(min(d)), '\n', file=u)
print('Список умноженный на первый элемент:', [i * d[0] for i in d], file=u)
