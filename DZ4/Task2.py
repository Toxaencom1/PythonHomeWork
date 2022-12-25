# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл,
# содержащий сумму многочленов.
from random import randint


def convert_polynom_koef_to_dict(polynom):  # Функция конвертирования коэффициентов в словарь
    polynom = polynom.strip(" ")
    polynom_list = polynom.split(' ')
    for i in range(len(polynom_list)):  # Преобразую в INT коэффициенты многочлена
        polynom_list[i] = int(polynom_list[i])
    polynom_dict = {}
    for n in range(len(polynom_list)):
        polynom_dict[n] = polynom_list[n]
    return polynom_dict


def generate_polynom(degree_input, kf, file_name):  # Функция генерации многочлена
    polynom = ''
    degree = []
    for i in range(degree_input, -1, -1):  # генерация списка степеней до 0
        degree.append(i)

    kf[-1] = -1  # Последний коэфф. запасной, чтобы проверять следующий элемент без ошибки и в конце не ставить '+'

    for i in range(len(degree)):  # Блок логики генерации
        if degree[i] == 0:  # Если степень = 0
            if kf[i] != 0:
                polynom += str(kf[i])
        elif degree[i] == 1: # Если степень = 1
            if kf[i] == 0:
                pass
            elif kf[i] == 1:
                polynom += 'x'
            elif kf[i] == -1:
                polynom += '-x'
            else:
                polynom += str(kf[i]) + '*' + 'x'
        else:                # Если степень > 0, отрицательной нет
            if kf[i] == 0:
                pass
            elif kf[i] == 1:
                polynom += 'x**' + str(degree[i])
            elif kf[i] == -1:
                polynom += '-x**' + str(degree[i])
            else:
                polynom += str(kf[i]) + '*' + 'x**' + str(degree[i])
        if kf[i + 1] > 0:   # блок установки знака между степенями многочлена
            polynom += '+'
        elif kf[i + 1] == 0:
            pass

    polynom = polynom.replace('+', ' + ').replace('-', ' - ')  # блок форматирования сгенерированного многочлена
    if polynom.startswith(' - '):
        polynom = polynom.lstrip(" - ")
        polynom = '-' + polynom
    if polynom.startswith(' + '):
        polynom = polynom.lstrip(" + ")
    polynom += ' = 0'

    print(f'{polynom} - Вывод многочлена')
    kf.pop()  # Убираю запасной коэффициент

    k_str = ''
    for i in range(len(kf)):  # Формирую коэффициенты в строку для записи
        k_str += str(kf[i]) + ' '
    print(f'{k_str} - Коэффициенты многочлена')
    with open(file_name, 'w', encoding='UTF-8') as data:    # Запись в файл
        data.write(polynom)
        data.write(f'\n{k_str}')

# =====================================================================================================================
# Начало программы

print("Здравствуй пользователь, эта программа считывает 2 файла с многочленами\
 и формирует файл, содержащий сумму многочленов.")
print("Файлы находятся в корне этой папки")
while True:
    try:
        degree_input = int(input("Введите степень k: "))
        if degree_input < 0:
            degree_input *= (-1)
        break
    except ValueError:
        print("Нужно ввести целое положительное число")

kf_1 = []   # Генерация списка случайных коэффициентов
for i in range(degree_input + 2):
    kf_1.append(randint(-10, 10))
kf_2 = []
for i in range(degree_input + 2):
    kf_2.append(randint(-10, 10))

generate_polynom(degree_input, kf_1, 'polynom1.txt')
generate_polynom(degree_input, kf_2, 'polynom2.txt')

polynom_1 = ''
polynom_2 = ''

path = 'polynom1.txt'  # Читаем файлы и записываем коэффициенты в переменную
data = open(path, 'r', encoding='UTF-8')
data.readline()
polynom_1 = data.readline()
data.close()

path = 'polynom2.txt'
data = open(path, 'r', encoding='UTF-8')
data.readline()
polynom_2 = data.readline()
data.close()


polynom_dict1 = convert_polynom_koef_to_dict(polynom_1) # Конвертация в словарь
polynom_dict2 = convert_polynom_koef_to_dict(polynom_2) # /
# print(f'{convert_polynom_koef_to_dict(polynom_1)} - Словарь 1')
# print(f'{convert_polynom_koef_to_dict(polynom_2)} - Словарь 2')

dict_of_sum = {}        # Суммирую элементы словарей
for i in polynom_dict1:
    dict_of_sum[i] = polynom_dict1[i] + polynom_dict2[i]


result_list = []
for i in range(len(dict_of_sum)): # Преобразую в список для формирования результата
    result_list.append(dict_of_sum[i])
print('\nРезультат в корне в файле "result.txt"')
result_list.append(-1)
generate_polynom(degree_input, result_list, 'result.txt') # Результирующий вызов функции с записью в файл result.txt
