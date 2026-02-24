# Урок 11.Форматирование строк
name = 'John'
age = 30

# print('My name is ' + name + '. I\'am is ' + str(age))

print('My name is %(n)s . I\'am is %(a)d' % {'n': name, 'a': age})

print('My name is %s . I\'am is %d' % (name, age))

# когда используем float
print('Title: %s, Price: %f' % ('Sony', 40))  # Title: Sony, Price: 40.000000
print('Title: %s, Price: %.2f' % ('Sony', 40))  # Title: Sony, Price: 40.00  -- .2 количество знаков после запятой

# 2 способ - метод format
print('My name is {} . I\'am is {}'.format(name, age))
print('My {1} name is {0} . I\'am is {1}'.format(name, age))  # можем подставлять в любое место
print('My name is {name} . I\'am is {age}'.format(name=name, age=age))  # именные маркеры для format

# ctrl + alt + l переформатирование кода - выравнивание по стандарту

# f-strings  самый новый метод форматирования строк
print(f'My name is {name}, I\'am {age}')
print(f'5+2={5 + 2}')  # можем сразу проводить вычисления
