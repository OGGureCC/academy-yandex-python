# Просто здравствуй, просто как дела
# 
# Умение вести диалог — важный навык для воспитанного человека.
# Напишите диалоговую программу, 
# которая сначала познакомится с пользователем, 
# а затем поинтересуется его настроением.
# 
# Формат ввода
# В первой строке записано имя пользователя.
# Во второй — ответ на вопрос: «хорошо» или «плохо».
# 
# Формат вывода
# В первой строке должен быть вопрос «Как Вас зовут?»
# Во второй строке — «Здравствуйте, %username%!»
# В третьей строке — вопрос «Как дела?»
# В четвёртой строке реакция на ответ пользователя:
# если пользователь ответил «хорошо», 
# следует вывести сообщение «Я за вас рада!»;
# если пользователь ответил «плохо», 
# следует вывести сообщение «Всё наладится!».

print(f'Как Вас зовут?')
name = input()
print(f'Здравствуйте, {name}a!')
print(f'Как дела?')
mood = input()
response = 'Я за вас рада!' if mood == 'хорошо' else 'Всё наладится!'
print(response)