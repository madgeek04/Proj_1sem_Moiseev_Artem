# Практическая №8 №1
# Сгенерировать словарь, где значение - это 3 степень ключа
# Удалить из него первый и последний элементы
# Использовать for range
r = {}  # Создаём пустой словарь
for i in range(0, int(input()) + 1):  # Создаём цикл с 0 до вводимого числа(вводиое число - последний ключ)
    r[i] = int(i) ** 3  # Записываем в словарь значения, используя расчёт по ключу
print(r)  # Выводим начальный словарь
del r[list(r.keys())[0]], r[list(r.keys())[-1]]  # Удаляем первый и последний элемент
print(r)  # Возврат значения
