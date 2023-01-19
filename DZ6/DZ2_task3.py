# Реализуйте алгоритм перемешивания списка.
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE,
# максимум использование библиотеки Random для и получения случайного int

from random import randint as RI

# Enumerate
def shuffle_my_list(f_list):
    for i, el in enumerate(f_list):
        r = RI(0, len(f_list) - 1)
        print(f'i={i} el= {el} c i={r} el={f_list[r]} ', end="")
        temp = f_list[i]
        f_list[i] = f_list[r]
        f_list[r] = temp
        print(f_list)
# # Старый код
# def shuffle_my_list(f_list):
#     for el in range(0, len(f_list)):
#         r = randint(0, len(f_list) - 1)
#         temp = my_list[el]
#         my_list[el] = my_list[r]
#         my_list[r] = temp

print("Здравствуй пользователь, эта программа для обучения, чтобы научиться перемешивать элементы списка")
my_list_length = int(input("Введите число длинны списка: "))
if my_list_length < 0:
    my_list_length *= (-1)

# List comprehension
my_list = [RI(0, 99) for i in range(my_list_length)]
# # Старый код
# for i in range(0, my_list_length):
#     my_list.append(randint(0, 99))
print(my_list)

shuffle_my_list(my_list)
print(my_list)
