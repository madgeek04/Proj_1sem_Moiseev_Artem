# Практическая №7 №2
# Дана строка-предложение на рус., посчитать кол-во знаков препинания в ней
# Используя цикл перебираем список и используя 'если' ищем знаки припенания
# Считаем кол-во таких символов и выводим
print(len([x for x in input() if x in '-:;,.!?']))
