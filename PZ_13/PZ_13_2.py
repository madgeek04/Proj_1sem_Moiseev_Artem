# Практическая №13 №2
# Составить генератор (yield), который выводит из строки только буквы.
def finding_letters(n):
    yield from [i for i in n if i.isalpha()]


print(''.join([o for o in finding_letters(input())]))
