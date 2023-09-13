# Властелин Чисел: Возвращение Цезаря
# 
# До победы над злом остался один шаг — разрушить логово Зерона.
# Для этого нужно создать трёхзначное магическое число,
# которое будет сильнее двух двухзначных защитных чисел Зерона.
# Самый простой способ создать сильное число:
# первой взять максимальную цифру из всех защитных чисел;
# последней — минимальную;
# в середину поставить сумму оставшихся без учёта переноса разряда.
# Помогите одолеть зло.
# 
# Формат ввода
# В двух строках записаны защитные числа Зерона.
# 
# Формат вывода
# Одно трёхзначное число, которое приведёт к победе.

a = input()
b = input()

combined = a + b
sorted_digits = sorted(combined)

first_digit = sorted_digits[-1]
middle_digit = (int(sorted_digits[1]) + int(sorted_digits[2])) % 10
last_digit = sorted_digits[0]

print(f'{first_digit}{middle_digit}{last_digit}')