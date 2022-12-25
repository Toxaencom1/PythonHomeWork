# A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ:
# Расширить значение коэффициентов до [-100..100]
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from random import randint

print("Здравствуй пользователь, эта программа формирует случайным образом список коэффициентов\
многочлена и записать в файл многочлен степени k.")
while True:
    try:
        degree_input = int(input("Введите степень k: "))
        if degree_input < 0:
            degree_input *= (-1)
        break
    except ValueError:
        print("Нужно ввести целое положительное число")

polynom = ''
degree = []
for i in range(degree_input, -1, -1):
    degree.append(i)
print(degree)

k = []
for i in range(len(degree)+1):
    k.append(randint(-100, 100))
k[-1]=-1 # запасной, чтобы проверять следующий элемент без ошибки и в конце не ставить '+'
print(f'{k}, - Коэффициенты')
for i in range(len(degree)):
    if degree[i] == 0:
        if k[i] != 0:
            polynom += str(k[i])
    elif degree[i] == 1:
        if k[i] == 0:
            pass
        elif k[i] == 1:
            polynom += 'x'
        elif k[i] == -1:
            polynom += '-x'
        else:
            polynom += str(k[i]) + '*' + 'x'

    else:
        if k[i] == 0:
            pass
        elif k[i] == 1:
            polynom += 'x**' + str(degree[i])
        elif k[i] == -1:
            polynom += '-x**' + str(degree[i])
        else:
            polynom += str(k[i]) + '*' + 'x**' + str(degree[i])
    if k[i+1]>0:
        polynom+='+'
    elif k[i+1] == 0:
        pass

# print(polynom)
# exit()
polynom = polynom.replace('+', ' + ').replace('-', ' - ')
if polynom.startswith(' - '):
    polynom = polynom.lstrip(" - ")
    polynom = '-' + polynom
if polynom.startswith(' + '):
    polynom = polynom.lstrip(" + ")

polynom += ' = 0'
print('\n Результат в файле "file.txt"')
with open('file.txt', 'w', encoding='UTF-8') as data:
    data.write(polynom)
    data.write(f'\nНатуральная степень k = {degree_input}')
    data.write('\nЭто многочлен с сформированным случайным образом списком коэффициентов (значения [-100..100])')
print(polynom)
