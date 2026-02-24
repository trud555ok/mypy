# while										
i = 1										
while i <= 10:										
    print(i, end = ' ')										
    i += 1										
    # i++  такого нету

print('')
print('hello', 'world', sep='!')    #hello!world . а по умолчанию - пустая строка ' '
print('hello', 'world', end=' ')    # след строка в этой же строке, перевода строки не будет

# for - для работы с иттерируемыми обьектами
s = 'Hello world!'										
for l in s:										
    if l == ' ':										
        continue										
    # print(l, end = ' ')										
    print(f'"{l}"', sep = " ", end = " ")										
print(' ')										
for i in 'Hello world!':										
    if i == ' ':										
        break										
    print(i, end = ' ')										
else:										
    print('нет пробелов!')   # сработает когда цикл for сработает полностью и не прервется
