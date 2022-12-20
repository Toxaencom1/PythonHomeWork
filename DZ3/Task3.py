# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from copy import copy
from random import random, randrange


def partitive_diff_max_min(my_list):  # Метод поиска разницы Max Min дробной части вещественного числа
    my_new_list = copy(my_list)
    for i in range(len(my_new_list)):
        my_new_list[i] = round(my_new_list[i] % 1, 2)  # Оставляем только дробную часть вещ.числа

    while True:
        if min(my_new_list) == 0:
            my_new_list.pop(my_new_list.index(min(my_new_list)))  # находим целые числа и изымаем из поиска Min
        else:
            break

    print(f'Дробное Max = {max(my_new_list)}')  # для наглядности
    print(f'Дробное Min = {min(my_new_list)}')  # /
    return max(my_new_list) - min(my_new_list)


print("Здравствуй пользователь, эта программа которая найдёт разницу между максимальным \
и минимальным значением дробной части элементов")
while True:
    try:
        length = int(input("Введите целое число (длину списка): "))
        if length < 0:
            length *= (-1)
        break
    except ValueError:
        print("Нужно ввести целое положительное число")

list1 = []
for i in range(length):
    list1.append(round(randrange(0, 10) + random(), 2))

print(list1)
print(f'Разницу между максимальными минимальным значением дробной части элементов: {partitive_diff_max_min(list1)}')
