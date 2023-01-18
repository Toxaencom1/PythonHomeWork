# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +, -, /, *.приоритет операций стандартный.
#
# *Пример: *
#
# 2 + 2 = > 4;
#
# 1 + 2 * 3 = > 7;
#
# 1 - 2 * 3 = > -5;


def multiply(list_: list):
    for i in range(len(list_)):
        if list_[i] == '*':
            extra_symbol_pos = i
            if list_[i - 2] == '-':
                list_[i - 1] = -list_[i - 1] * list_[i + 1]
                list_[i - 2] = '+'
                break
            else:
                list_[i - 1] = list_[i - 1] * list_[i + 1]
                break
    list_.pop(extra_symbol_pos + 1)
    list_.pop(extra_symbol_pos)
    return list_


def div(list_: list):
    for i in range(len(list_)):
        if list_[i] == '/':
            extra_symbol_pos = i
            if list_[i - 2] == '-':
                list_[i - 1] = -list_[i - 1] / list_[i + 1]
                list_[i - 2] = '+'
                break
            else:
                list_[i - 1] = list_[i - 1] / list_[i + 1]
                break
    list_.pop(extra_symbol_pos + 1)
    list_.pop(extra_symbol_pos)
    return list_


def sum_phrases(list_: list):
    extra_symbol_pos = -1
    for i in range(len(list_)):
        if list_[i] == '+':
            extra_symbol_pos = i
            if list_[i - 2] == '-':
                list_[i - 1] = -list_[i - 1] + list_[i + 1]
                list_[i - 2] = '+'
            else:
                list_[i - 1] = list_[i - 1] + list_[i + 1]
            break
    if extra_symbol_pos != -1:
        list_.pop(extra_symbol_pos + 1)
        list_.pop(extra_symbol_pos)
    return list_


def pop_extra_symbol(list_: list, symbol, letter):
    flag = True
    extra_symbol_pos = 0
    while flag:
        for i in range(len(list_)):
            if list_[i] == symbol and list_[i + 1] == letter:
                flag = True
                break
        else:
            flag = False
            break
        if list_[i] == symbol and list_[i + 1] == letter:
            extra_symbol_pos = i
        if extra_symbol_pos != 0:
            list_.pop(extra_symbol_pos + 1)
    return list_


def phrase_calc(string_: str):
    string_ = string_.replace(' ', '').replace('-', ' - ').replace('+', ' + ').replace('*', ' * ').replace('/',
                                                                                                           ' / ').replace(
        '  ', ' ')
    string_ = string_.split()
    # Парсинг и сплит строки
    for i in range(len(string_)):
        if string_[i].isdigit():
            string_[i] = int(string_[i])
        if string_[i - 1] == '-':
            string_[i] = -string_[i]
            string_[i - 1] = '+'

    if string_[0] == '-':
        string_[1] = -string_[1]
        string_.pop(0)
    elif string_[0] == '+':
        string_.pop(0)
    # Превращение строковых чисел в Int учитывая знак, и обработка знака начала строки

    string_ = pop_extra_symbol(string_, '*', '+')
    string_ = pop_extra_symbol(string_, '/', '+')
    # string_ = pop_extra_symbol(string_, '+', '+')
    # string_ = pop_extra_symbol(string_, '-', '-')
    # Убираю лишние знаки образованные логикой выше

    while True:
        if '*' in string_ or '/' in string_:
            i = 1
            while i < len(string_):
                if string_[i] == '*':
                    string_ = multiply(string_)
                if string_[i] == '/':
                    string_ = div(string_)
                    continue
                i += 1
        else:
            break
    while True:
        if '+' in string_:
            i = 1
            while i < len(string_):
                if string_[i] == '+':
                    string_ = sum_phrases(string_)
                    continue
                i += 1
        else:
            break
    # Результат выполненного выражения
    return string_


string_ = '-2 + 2 * -3 / +2-3+5  + 18 / 3 * 2 - 6/3'
print(f'{string_} - Изначальная строка\n')
result = round(*phrase_calc(string_), 2)
print(f'Результат вычисления выражения = {result} !!!')
