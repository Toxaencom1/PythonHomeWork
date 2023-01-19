# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]
from random import randint as RI
print("Здравствуй пользователь, эта программа считает операцию над парами чисел списка")

while True:
    try:
        length = int(input("Введите целое число (длину списка): "))
        if length < 0:
            length *= (-1)
        break
    except ValueError:
        print("Нужно ввести целое положительное число")

list_ = [RI(1, 9) for i in range(length)]
print(list_)
while True:
    operand = input('Введите оператор чтобы сложить = "+", вычесть = "-", умножить = "*", разделить = "/" ')
    if operand in '+-*/':
        break
    else:
        print("Введите операнд, вы неправильно ввели!")

# Lambda
operator = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y
}
# List comprehension, lambda, ternary operator
result = [operator[operand](list_[i], list_[-i - 1]) for i in
          range(len(list_) // 2 if len(list_) % 2 == 0 else len(list_) // 2 + 1)]
print(result)


# # Старый код
# my_list = []
#
# for i in range(length):
#     my_list.append(RI(-10, 10))
# print(my_list)
#
# my_newlist = []
# for i in range(length // 2 if length % 2 == 0 else length // 2 + 1):
#     my_newlist.append(my_list[i] * my_list[- i-1])
#
# print(my_newlist)
