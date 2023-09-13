# Корень зла
# 
# Не все любят математику, а кто-то даже считает её настоящим злом во плоти,
# хотя от неё никуда не деться. 
# К примеру, Python изначально разрабатывался только для решения математических задач,
# поэтому давайте используем его, чтобы найти корни уравнения.
# 
# Формат ввода
# Вводится 3 вещественных числа a, b, c — коэффициенты уравнения вида:
# ax^2+bx+c=0.
# 
# Формат вывода
# Если у уравнения нет решений — следует вывести «No solution».
# Если корней конечное число — их нужно вывести через пробел в порядке возрастания с точностью до сотых.
# Если корней неограниченное число — следует вывести «Infinite solutions».
# 
# Примечание
# Обратите внимание, что ограничения на значения коэффициентов отсутствуют.

a = float(input())
b = float(input())
c = float(input())

if a == 0:
    if b == 0:
        if c == 0:
            print('Infinite solutions')
        else:
            print('No solution')
    else:
        x1 = -c / b
        print(f'{x1:.2f}')
else:
    d = b ** 2 - 4 * a * c
    if d < 0:
        print('No solution')
    elif d == 0:
        x1 = -b / (2 * a)
        print(f'{x1:.2f}')
    else:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        if x1 > x2:
            print(f'{x2:.2f} {x1:.2f}')
        else:
            print(f'{x1:.2f} {x2:.2f}')