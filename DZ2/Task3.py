# Реализуйте алгоритм перемешивания списка.
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE,
# максимум использование библиотеки Random для и получения случайного int

from random import randint


def shuffle_my_list(f_list):
    for el in range(0, len(f_list)):
        r = randint(0, len(f_list) - 1)
        temp = my_list[el]
        my_list[el] = my_list[r]
        my_list[r] = temp


print("Здравствуй пользователь, эта программа для обучения, чтобы научиться перемешивать элементы списка")
my_list_length = int(input("Введите число длинны списка: "))
if my_list_length < 0:
    my_list_length *= (-1)

my_list = []
for i in range(0, my_list_length):
    my_list.append(randint(0, 99))
print(my_list)

shuffle_my_list(my_list)
print(my_list)
