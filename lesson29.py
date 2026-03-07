# ДЗ 1 - дан список со словом odd, надо функцией выяснить есть ли в этом списке число - индекс слова odd
dol = ['dd', 2, 'odd']  # True
dol2 = ['dd', 5, 'odd']  # False


def ger(lok, word):
    # ind = lok.index(word)
    # if ind in lok:
    #     return True
    # else:
    #     return False
    return lok.index(word) in lok


print(ger(dol, 'odd'))  # True
print(ger(dol2, 'odd'))  # False


# ДЗ 2 - описать функцию которая приничает число - конечное в последовательности включительно
# и вернет суму всех чисел последовательности которые кратны 3 или 5 (в одну стрроку)
def her(ch):
    # return sum([i for i in range(ch+1) if not (i%3) or not (i%5)])
    return sum([i for i in range(ch + 1) if i % 3 == 0 or i % 5 == 0])


print(her(5))  # 8
print(her(15))  # 60

# ДЗ 3 - дан список имен, в новый список отобрать только те которые состоят из 4 букв.
names = ['Mark', 'Den', 'Sora', 'Kentavr']


def myname(lol):
    return [i for i in lol if len(i) == 4]


print(myname(names))  # ['Mark', 'Sora']
