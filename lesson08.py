w1 = "Hello, my 'test' world"  #Hello, my 'test' world
print(w1)
w2 = 'Hello, my "test" world'  #Hello, my "test" world
print(w2)
w3 = "Hello, 'my' super \"test\" world"  #Hello, 'my' super "test" world   \ - экранирует
print(w3)
w4 = "Hello, my super \test world"  #Hello, my super 	est world   \t - табуляция
print(w4)
w5 = "Hello, my super \\test world"  #Hello, my super \test world   \\t - экранирует спецсимвол
print(w5)

verse = 'Ты помнишь? Начинали мы с любви.\
Она к нам неожиданно пришла.\
Раскрыла нам объятия свои,\
Казалось, осязаемой была.'

# \ - тут экранирует конец физической строки
print(verse) # получим слитную одну строку стиха

verse2 = 'Ты помнишь? Начинали мы с любви.\n\
Она к нам неожиданно пришла.\n\
Раскрыла нам объятия свои,\n\
Казалось, осязаемой была.'
print(verse2) # получим четверостишье

verse3 = ('это строка1\n'
          'это строка2')
print(verse3) #() - обьеденяет строки

verse4 = '''
    строка1
    строка2
    строка3
'''
print(verse4) # получаем на разных строках