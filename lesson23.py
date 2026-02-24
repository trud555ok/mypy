# Словари
# создание словаря
d = {}
product1 = {'title': 'Sony', 'price': 100}
product2 = dict(title = 'IPhone', price = 120)

print(d, product1, product2, sep='\n')
'''{}
{'title': 'Sony', 'price': 100}
{'title': 'IPhone', 'price': 120}'''

# преобразование со списка
users = [
    ['bob@mail.com', 'Bob'],
    ['katy@mail.com', 'Katy'],
    ['ray@mail.com', 'Ray'],
]
d_users = dict(users)
print(d_users)  #{'bob@mail.com': 'Bob', 'katy@mail.com': 'Katy', 'ray@mail.com': 'Ray'}
# с кортежами аналогично, меняется только скобочка

product3 = dict.fromkeys(['price1', 'price2', 'price3'], 20)
print(product3) #{'price1': 20, 'price2': 20, 'price3': 20} - одинаковые значения

# создание через генераторы
ff = { i: i+1 for i in range(1, 10)}
print(ff)   #{1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 10}

print(product1['title'])    #Sony
#print(ff['1']) # ошибка, все ключи int
print(ff[1])    #2

# при обращении к несуществующему ключу
# print(product1['title2']) - ошибка
print(product1.get('title2'))   #None (значение по умолчаниию)
print(product1.get('title2', ' '))   #пустая строка - 2 парам

# достать ключи и их значение
for key in product1:
    print(f'{key} : {product1[key]}')
# title : Sony
# price : 100

print(product1.items()) #dict_items([('title', 'Sony'), ('price', 100)])
for key, value in product1.items():
    print(f'{key} - {value}')
# title - Sony
# price - 100

products = [
    {'title': 'Sony', 'price': 100},
    {'title': 'Wert', 'price': 150},
    {'title': 'Fam', 'price': 200},
]
for product in products:
    print(product['title'])     #обращаемся к каждому названию