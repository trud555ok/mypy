# списки - масивы

# создание списков
l = [1,2,3,'hello', ['test', 10], 'world', True]
print(type(l))  #<class 'list'>

l2 = list('hello') #из иттерируемой последовательности
print(l2)   #['h', 'e', 'l', 'l', 'o']
# l3 = list(1,2,3)   -- ошибка - нужна иттерируемая последовательность
l3 = list((1,2,3))  # с кортежа
print(l3) #[1, 2, 3]

# Генераторы списков
l4 = [i for i in 'privet']
print(l4)   #['p', 'r', 'i', 'v', 'e', 't']

st1 = 'Privet Vasia'
l5 = [i for i in st1 if i != ' ']
print(l5) #['P', 'r', 'i', 'v', 'e', 't', 'V', 'a', 's', 'i', 'a']
l6 = [i for i in st1 if i not in [' ', 'a', 'o', 'i', 'e']]
print(l6)#['P', 'r', 'v', 't', 'V', 's']

# range()
l7 = list(range(3))   # от 0 до 3 не включая 3
print(l7)  #[0, 1, 2]
l8 = list(range(1,5))
print(l8)   #[1, 2, 3, 4]
l9 = list(range(1, 10, 3))
print(l9)  #[1, 4, 7]

# range - не отдает ничего, он он генерирует элемент на каждой иттерации

for i in range(1, 3):
    print(f'Вывод 1 = {i}')
    for j in range(1,3):
        print(f'\tВывод 2 = {j}')

