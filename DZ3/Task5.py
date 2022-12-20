# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

print("Здравствуй пользователь, эта программа составляет список чисел Фибоначчи, \
в том числе и для отрицательных элементов ")
while True:
    try:
        k = int(input("Количество элементов фибоначи в '+' и '-' сторону которые хотите увидеть: k = "))
        if k < 0:
            k *= (-1)
        break
    except ValueError:
        print("Нужно ввести целое положительное число")

fib_right = [1, 1]
for i in range(2, k):
    fib_right.append(fib_right[i - 2] + fib_right[i - 1])

fib_left = [1, 1]

for i in range(k + 1):
    fib_left.insert(0, fib_left[1] - fib_left[0])

fib_left.pop(-1)  # Убираю лишнее
fib_left.pop(-1)  # /

for i in range(len(fib_right)):  # Соединение левой и правой стороны
    fib_left.append(fib_right[i])
print(fib_left)
