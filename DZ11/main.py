import numpy as np
import matplotlib.pyplot as plt


# f(x) = -12x^4*sin(cos(x)) - 18x^3 + 5x^2 + 10x - 30
# Определить корни
# Найти интервалы, на которых функция возрастает
# Найти интервалы, на которых функция убывает
# Построить график
# Вычислить вершину
# Определить промежутки, на котором f > 0
# Определить промежутки, на котором f < 0


def func(x_value) -> float:
    function_ = a * np.sin(np.cos(x_value)) * x_value ** 4 + b * x_value ** 3 + c * x_value ** 2 + e * x_value + f
    return function_


def find_exrt(from_: int, till_: int) -> tuple:
    y_from = func(from_)
    y_from_next = func(from_ + 0.0001)
    if y_from_next < y_from:
        for x_value in np.arange(from_, till_, 0.0001):
            function_ = func(x_value)
            if function_ > y_from:
                min_x = round(x_value, 4)
                min_y = round(function_, 4)
                return min_x, min_y
            y_from = function_
    else:
        for x_value in np.arange(from_, till_, 0.0001):
            function_ = func(x_value)
            if function_ < y_from:
                max_x = round(x_value, 4)
                max_y = round(function_, 4)
                return max_x, max_y
            y_from = function_


# Находим корни
a, b, c, e, f = -12, -18, 5, 10, -30
roots = []
for x in np.arange(-11, 0, 0.00001):
    function = round(func(x), 0)
    if function == 0:
        roots.append(round(x, 2))
roots = set(roots)
roots = list(roots)
roots.sort()
pos = 0
for i in range(len(roots) - 1):
    if round(roots[i + 1] - roots[i], 2) == 0.01:
        pos = i + 1
roots.pop(pos)
# print(roots)

#  Рисуем функцию до начала убывания
x = np.arange(-10.5, find_exrt(-11, roots[0])[0], 0.001)
plt.rcParams['lines.linestyle'] = '-.'
plt.plot(x, func(x), 'y-')

# Рисуем функцию убывания при положительных Y
go_down_pos = np.arange(find_exrt(-11, -9)[0], roots[0], 0.001)
plt.rcParams['lines.linestyle'] = '-'
plt.plot(go_down_pos, func(go_down_pos), 'r', label='Убывает > Нуля')

# Рисуем функцию убывания при отрицательных Y
go_down_neg = np.arange(roots[0], find_exrt(roots[0], roots[1])[0], 0.001)
plt.rcParams['lines.linestyle'] = '-.'
plt.plot(go_down_neg, func(go_down_neg), 'r', label='Убывает < Нуля')

# Рисуем функцию возрастания при отрицательных Y
go_up_neg = np.arange(find_exrt(roots[0], roots[1])[0], roots[1], 0.001)
plt.plot(go_up_neg, func(go_up_neg), 'b', label='Возрастает < Нуля')

# Рисуем функцию возрастания при положительных Y
go_up_pos = np.arange(roots[1], find_exrt(roots[1], roots[2])[0], 0.001)
plt.rcParams['lines.linestyle'] = '-'
plt.plot(go_up_pos, func(go_up_pos), 'b', label='Возрастает > Нуля')

# Рисуем функцию убывания при положительных Y
go_down_pos = np.arange(find_exrt(roots[1], roots[2])[0], roots[2], 0.001)
plt.plot(go_down_pos, func(go_down_pos), 'r-')

#  Рисуем функцию до нуля
x = np.arange(roots[2], 0, 0.001)
plt.rcParams['lines.linestyle'] = '-.'
plt.plot(x, func(x), 'y')

# Рисуем корни, экстремумы
plt.title(f'Функция на участке (-10; 0):')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.grid()
plt.plot(roots[0], 0, 'go', label=f'Корни {roots[0]}, {roots[1]}, {roots[2]}')
plt.plot(roots[1], 0, 'go')
plt.plot(roots[2], 0, 'go')
plt.plot(find_exrt(-11, roots[0])[0], find_exrt(-11, roots[0])[1], 'gx', label=f'Экстремумы')
plt.plot(find_exrt(roots[0], roots[1])[0], find_exrt(roots[0], roots[1])[1], 'gx')
plt.plot(find_exrt(roots[1], roots[2])[0], find_exrt(roots[1], roots[2])[1], 'gx')
plt.legend()
plt.show()
