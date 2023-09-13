# Излишняя автоматизация 2.0
# 
# А что будет, если вновь, как в первой главе,
# объединить два принципа — повторение и автоматизацию?
# 
# Формат ввода
# В первой строке записана весьма полезная информация.
# Во второй натуральное число N — количество раз,
# которое её нужно повторить, чтобы она закрепилась.
# 
# Формат вывода
# N раз повторенная весьма полезная информация.

txt = input()
n = int(input())

print(f'{txt}\n' * n)

# Есть ещё 2 решение, оно больше подходит в контексте главы про циклы,
# но лично я предпочитаю 1 вариант

txt = input()

for i in range(int(input())):
    print(txt)