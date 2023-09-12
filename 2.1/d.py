# Сдача
# 
# Чаще всего автоматизация идёт на пользу.
# Одна из задач, 
# в которой лучше исключить человеческий фактор, — подсчёт сдачи.
# Определите, какую сдачу нужно выдать тому,
# кто купил 2,5кг черешни по цене 38 руб/кг.
# 
# Формат ввода
# Одно натуральное число - номинал купюры пользователя (≥ 100).
# 
# Формат вывода
# Одно натуральное число — размер сдачи.

money = int(input())
weight = 2.5
price = 38

change = money - (weight * price)

print(int(change))