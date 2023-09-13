# Музыкальный инструмент
# 
# Есть много музыкальных инструментов, но Вася обожает треугольник.
# У него завалялось немного алюминиевых трубочек разной длины,
# и он задаётся вопросом, а можно ли из них сделать любимый музыкальный инструмент.
# 
# Формат ввода
# Три числа — длины трубочек, каждое с новой строки.
# 
# Формат вывода
# YES — если Васе удастся создать музыкальный треугольник, иначе — NO
# 
# Примечание
# Обратите внимание, что в треугольнике любая сторона меньше суммы двух других.

a = int(input())
b = int(input())
c = int(input())

if a + b > c and a + c > b and b + c > a:
    print("YES")
else:
    print("NO")