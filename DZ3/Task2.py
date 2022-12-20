# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

from random import randint as rand

print("Здравствуй пользователь, эта программа считает произведение пар чисел списка")
while True:
    try:
        length = int(input("Введите целое число (длину списка): "))
        if length < 0:
            length *= (-1)
        break
    except ValueError:
        print("Нужно ввести целое положительное число")

my_list = []

for i in range(length):
    my_list.append(rand(-10, 10))
print(my_list)

my_newlist = []
for i in range(length // 2 if length % 2 == 0 else length // 2 + 1):
    my_newlist.append(my_list[i] * my_list[- i-1])

print(my_newlist)
