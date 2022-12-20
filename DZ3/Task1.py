# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint as rand

print("Здравствуй пользователь, эта программа считает сумму элементов нечетных индексов")
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
    my_list.append(rand(-99, 99))
sum = 0
for i in range(1, len(my_list), 2):
    sum += my_list[i]

print(my_list)
print(f'Сумма элементов нечетных индексов равна: {sum}')
