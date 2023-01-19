# Задайте список из n чисел последовательности (1 + 1/n)^n, выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

print("Здравствуй пользователь, эта программа выводит список из N чисел последовательности", end=" ")
print("и сумму её элементов на экран")
numbers = int(input("Введите положительное число - N: "))
if numbers < 0: numbers *= (-1)


# List comprehension
sequence = [round((1 + (1 / i)) ** i,2) for i in range(1, numbers + 1)]

# sequence = [] # Старый код
# for i in range(1, numbers + 1):
#     fSequence = (1 + (1 / i)) ** i
#     sequence.append(round(fSequence, 2))

print(f"Для N = {numbers} -> {sequence}")
print(f"Сумма элементов последовательности равна: {round(sum(sequence),3)}")
