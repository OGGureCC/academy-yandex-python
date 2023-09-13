# Автоматизация безопасности
# 
# Группа исследователей собирается высадиться на остров невероятно ровной формы,
# но разведка при помощи спутника выяснила, что на острове есть зона зыбучих песков.
# Для повышения безопасности экспедиции было решено разработать систему оповещения,
# которая предупредит исследователей об опасности.
# А для снижения расходов на производство было решено заказать программное обеспечение.
# Напишите программу, которая по координатам исследователя, будет сообщать о безопасности в этой точке.
# 
# Формат ввода
# Два рациональных числа — координаты исследователя.
# 
# Формат вывода
# Одно из сообщений:
# Опасность! Покиньте зону как можно скорее!
# Зона безопасна. Продолжайте работу.
# Вы вышли в море и рискуете быть съеденным акулой!

x = float(input())
y = float(input())
c = (x ** 2 + y ** 2) ** 0.5
y_para = (0.25 * (x ** 2)) + (0.5 * x) + 8.75

if c > 10:
    print("Вы вышли в море и рискуете быть съеденным акулой!")
elif x >= 0 and y >= 0: 
    if c <= 5: 
        print("Опасность! Покиньте зону как можно скорее!")
    else:
        print("Зона безопасна. Продолжайте работу.")
elif x <= 0 and y >= 0:  
    if y <= 5 and y <= ((5 * x) + 35) / 3:
        print("Опасность! Покиньте зону как можно скорее!")
    else:
        print("Зона безопасна. Продолжайте работу.")
else:  
    if y < y_para:
        print("Опасность! Покиньте зону как можно скорее!")
    else:
        print("Зона безопасна. Продолжайте работу.")