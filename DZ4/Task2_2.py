# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл,
# содержащий сумму многочленов.


def sum_of_dicts(my_dict1: dict, my_dict2: dict): # Функция суммирующая словари
    dict_sum = my_dict1.copy()
    for k, v in my_dict2.items():
        dict_sum[k] = dict_sum.get(k, 0) + v
    dict_sum = sorted(dict_sum.items(), reverse=True)
    dict_sum = dict(dict_sum)
    return dict_sum


def format_str_to_last(pm: str):  # Преобразование строки для изъятия последнего элемента многочлена
    new_pm = pm.replace(' ', '').replace('=0', '').replace('+', ' ').replace('-', ' -')
    new_pm = new_pm.strip()
    new_pm = new_pm.split(' ')
    last = int(new_pm.pop())
    return last


def format_str_to_dict(pm: str):  # Преобразование строки для конвертации в словарь
    polynom = pm.replace(' ', '').replace('=0', '')
    polynom = polynom.replace('+x', '+1*x').replace('-x', '-1*x')
    polynom = polynom.replace('x+', 'x**1+').replace('x-', 'x**1-')
    polynom = polynom.replace('+', ' ').replace('-', ' -')
    polynom = polynom.strip()
    polynom = polynom.split(' ')
    _ = int(polynom.pop())
    tmp_dict = {}
    for i in range(len(polynom)):
        polynom[i] = polynom[i].split("*x")
        polynom[i][-1] = polynom[i][-1].replace('**', '')
        tmp_dict[polynom[i][-1]] = int(polynom[i][0])
    return tmp_dict


# =====================================================================================================================
# Начало программы

print("Здравствуй пользователь, эта программа считывает 2 файла с многочленами\
 и формирует файл, содержащий сумму многочленов.")
print("Файлы находяться в папке 'files_Task2_2'")

path = 'files_Task2_2/pm.txt'   # Читаем файлы
data = open(path, 'r', encoding='UTF-8')
pm = data.readline()
data.close()

path = 'files_Task2_2/pm2.txt'  # /
data = open(path, 'r', encoding='UTF-8')
pm2 = data.readline()
data.close()

last = format_str_to_last(pm) + format_str_to_last(pm2)

my_dict1 = format_str_to_dict(pm)
my_dict2 = format_str_to_dict(pm2)

dict_sum = sum_of_dicts(my_dict1, my_dict2)

result = ''
for i in (dict_sum):   # Блок вывода из словаря в строку
    if i == '0':
        pass
    elif i == '1':
        result += str(dict_sum[i]) + '*x'
    else:
        if dict_sum[i] == 1:
            result += 'x**' + i
        elif dict_sum[i] == -1:
            result += '-x**' + i
        else:
            result += str(dict_sum[i]) + '*x**' + i
        result += '+'
if last == 0:  # Блок вывода последнего элемента
    pass
elif last > 0:
    result += '+' + str(last) + ' = 0'
else:
    result += str(last) + ' = 0'
result = result.replace('+-', '-')  # Финальное форматирование строки
result = result.replace('+', ' + ').replace('-', ' - ')
result = result.lstrip('+')

print(f'\nСумма многочленов: {result}\nРезультат в папке с файлами "result.txt"')
with open('files_Task2_2/result.txt', 'w', encoding='UTF-8') as data:                # Запись в файл
    data.write(result)
