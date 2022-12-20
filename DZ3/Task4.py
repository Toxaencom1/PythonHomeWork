# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

print("Здравствуй пользователь, эта программа преобразует десятичное число в двоичное")
while True:
    try:
        denary = int(input("Введите число для перевода в двоичную систему: "))
        if denary < 0:
            denary *= (-1)
        break
    except ValueError:
        print("Нужно ввести целое положительное число")
denary_first = denary  # <-Для отображения результата (изначальное число)
binary = []
while True:
    binary.append(denary % 2)
    denary = denary // 2
    if denary == 0:
        break
binary.reverse()
print(f'Результат перевода десятичного числа "{denary_first}" в двоичное будет равен :  ', end='')
for i in binary:
    print(f'{i}', end='')
