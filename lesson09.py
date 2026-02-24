name = r'C:\d\name.txt' # сырая строка - не обрабатывает управл последовательности \n
print(name)

# конкатенация
z = 'Pyth' 'on'
print(z)    #Python - склеит строки

s1 = "Hello, "
s2 = "world!"
s3 = s1 + s2
print(s3)   #Hello, world!

n = 'Nikol'
age = 56
print('My name is ' + n + ". I'm " + str(age) ) #My name is Nikol. I'm 56

# Дублирование строк
print('Hi ' * 5)

# индексация строк - строка не изменяется, создается новая строка
st = "Hello world!"
print(st[0]) #H
print(st[-1]) #!
# st[0] = 'D' -- ошибка, попытка изменить строку

# СРЕЗЫ
# [x:y:z] - все индексы необязательные
# x - начало среза -- от какого символа включительно
# y - конец среза -- до какого символа НЕ включительно
# z - шаг среза
print(st[0:5]) #Hello
print(st[:5]) #Hello
print(st[6:]) #world!
print(st[::2]) #Hlowrd
print(st[::-1]) #строка наоборот
print(st[:5] + st[6:]) #Helloworld!











