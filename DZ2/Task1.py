# Продолжаем решать задачи типа "Здравствуй пользователь, эта программа..."

# Задача №1:
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

print("Здравствуй пользователь, эта программа считает сумму цифр вещественного числа")
sumOfSigns = 0
realNumber = input('Введите вещественное число: ')
try:                                                      # Валидация ввода вещественного числа
    realNumber = int(realNumber.replace('.', ''))
except ValueError:
    try:
        realNumber = int(realNumber.replace(',', ''))
    except ValueError:
        print(f'Вы ввели "{realNumber}", а не вещественное число')
        exit()

while not (realNumber >= 0 and realNumber < 10):
    remainder = realNumber % 10
    realNumber //= 10
    sumOfSigns += remainder
    remainder = 0
sumOfSigns += realNumber    # Добавляем последний знак
print(f"Сумма знаков равна: {sumOfSigns}")
