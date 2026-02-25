# методы словаря
# dict.clear() - очищает словарь
# dict.copy()  - возвращает копию словаря
# dict.get(key[, default])  - вернет значение ключа, если нету такого ключа вернет default(по умолч None)
# dict.items() - вернет пары (ключ, значение) - [('title', 'Sony'), ('price', 100)] список кортежей
# dict.keys() - вернет ключи словаря
# dict.pop(key[, default])  - удаляет ключ, возвращает значение, если нету - дефолт (по умол - ОШИБКА)
# dict.popitem()  - удаляет пару ключ, значение, если словарь пуст - ошибка
# dict.setdefault(key[, default]) - вернет значение ключа, если такого нету - создаст такой ключ со знач дефолт(по умолч - None)
# dict.update([other]) - обновит словарь добавив пары с офер
# СУЩЕСТВУЮЩИЕ КЛЮЧИ перезапишутся, возвращает NONE (не новый словарь!!!)
# dict.values()  - вернет значения в словаре

d = {'title': 'Sony', 'price': 100}
d1 = d.popitem()
print(d1)   #('price', 100) -- любую пару взял
print(d)    #{'title': 'Sony'} - в словаре пара исчезла

dd = {'title': 'Sony2', 'price': 200}
dd3 = dd.setdefault('is_one')
print(dd)   #{'title': 'Sony2', 'price': 200, 'is_one': None}
print(dd3)  #None - значение того ключа которого небыло но он создался
dd2 = dd.setdefault('price')
print(dd2) #200

ddd = {'title': 'Sony3', 'price': 300}
ddd.update({'link': 'aaaaa', 'name': 'Bob'})
print(ddd) #{'title': 'Sony3', 'price': 300, 'link': 'aaaaa', 'name': 'Bob'}
ddd.update({'name': 'Ron'})
print(ddd) #{'title': 'Sony3', 'price': 300, 'link': 'aaaaa', 'name': 'Ron'} name перезаписалось


