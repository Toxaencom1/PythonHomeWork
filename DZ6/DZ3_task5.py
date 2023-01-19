# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи
def fibonacci(n):
    if n <= 0:
        if n == 1:
            return 1
        if n == 0:
            return 0
        return fibonacci(n + 2) - fibonacci(n + 1)
    else:
        if n in (1, 2):
            return 1
        return fibonacci(n - 1) + fibonacci(n - 2)


print("Здравствуй пользователь, эта программа составляет список чисел Фибоначчи, \
в том числе и для отрицательных элементов ")
while True:
    try:
        k = int(input("Количество элементов Фибоначчи в '+' и '-' сторону которые хотите увидеть: k = "))
        if k < 0:
            k *= (-1)
        break
    except ValueError:
        print("Нужно ввести целое положительное число")

# Через List comprehensions, далее нужно выбирать способ решения, комментируя этот и открывая следующий
list_ = [fibonacci(i) for i in range(-k, k+1)]
print(list_)

# # Через Map
# res = list(map(fibonacci, [i for i in range(-k, k+1)]))
# print(res)

# # При проверке, в комментариях к заданию, вы говорили сократить тут код, вот он -
# fib = [1, 0, 1]
# for i in range(k - 1):
#     fib.append(fib[-1] + fib[-1 - 1])
#     fib.insert(0,fib[0 + 1] - fib[0])
# print(fib)

# # Старый код
# fib_right = [1, 1]
# for i in range(2, k):
#     fib_right.append(fib_right[i - 2] + fib_right[i - 1])
#
# fib_left = [1, 1]
#
# for i in range(k + 1):
#     fib_left.insert(0, fib_left[1] - fib_left[0])
#
# fib_left.pop(-1)  # Убираю лишнее
# fib_left.pop(-1)  # /
#
# for i in range(len(fib_right)):  # Соединение левой и правой стороны
#     fib_left.append(fib_right[i])
# print(fib_left)
