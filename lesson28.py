# Пользовательские функции. Часть 3
# коментирование функций
def get_sum(a, b):
    """
    Возвращает сумму аргументов.

    :param a: первый параметр
    :type a: int
    :param b: второй параметр
    :type b: int
    :return: сумму аргументов
    """
    return a + b


print(get_sum(2, 3))  # 5 но при ctrl + наведение у принт есть описание а get_sum нету описания
# ctrl + q выводит документацию по функции

# Области видимости
# локальная, глобальная, +(нонлокал) - разбираем только 2 первых, 3 посмотреть!
# вне функции - глобальная переменная -- доступна везде, в функции только на чтение
# внутри функции - локальная переменная     -- доступна только в функции

a = 5
b = 6


def forant():
    # a += 1 #-- ошибка, глобальную функции нельзя менять
    print(a)  # 5 - глобальная переменная доступна для чтения
    b = 12
    b += 1
    print(b)


print(b)  # 6
forant()  # 13  12+1 вывелась локальная переменная b
print(b)  # 6 - глобальная переменная не изменилась, изменилась локальная b в функции

# Если надо изменить глобальную переменную в функции

f = 4


def retro():
    global f  # позволяет изменять глобальную переменную в функции
    f += 1


print(f)  # 4
retro()
print(f)  # 5 - функция изменила глабальную переменную

# Функция в функции
l = [1, '2', 3]


def mult(l):
    return [i * 2 for i in l]


print(mult(l))  # [2, '22', 6]


def mult2(l):
    def umka(el):
        return el * 2

    return [umka(i) for i in l]  # используем функцию которую описали в этой функции


print(mult2(l))  # [2, '22', 6]


def mult3(l):
    def umka(el):
        if isinstance(el, int):
            return el * 2

    # return [umka(i) for i in l]     # [2, None, 6] - результат вызова функции
    return [umka(i) for i in l if umka(i)]  # [2, 6] - условие исключает None


print(mult3(l))  # [2, None, 6]


# вариант с map
def mult4(l):
    def umka(el):
        return el * 2

    return list(map(umka, l))  # [2, '22', 6] - umka не вызываем а передаем название функции которая вызвится к каждому елем


print(mult4(l))  # [2, '22', 6]

# ДЗ 1 - дан список со словом odd, надо функцией выяснить есть ли в этом списке число - индекс слова odd
dol = ['dd', 2, 'odd']  # True
dol2 = ['dd', 5, 'odd']  # False

def ger(lok, word):
    ind = lok.index(word)
    if ind in lok:
        return True
    else:
        return False
print(ger(dol, 'odd'))  #True
print(ger(dol2, 'odd')) #False

# ДЗ 2 - описать функцию которая приничает число - конечное в последовательности включительно
# и вернет суму всех чисел последовательности которые кратны 3 или 5 (в одну стрроку)
def her(ch):
    return sum([i for i in range(ch+1) if not (i%3) or not (i%5)])
print(her(5)) #8
print(her(15)) #60

# ДЗ 3 - дан список имен, в новый список отобрать только те которые состоят из 4 букв.
names = ['Mark', 'Den', 'Sora', 'Kentavr']
def myname(lol):
    return [i for i in lol if len(i) == 4]
print(myname(names))    #['Mark', 'Sora']