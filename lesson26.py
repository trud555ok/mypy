# Пользовательские функции. Часть 1
def privet():
    print('Hello')
privet()    # вызов функции

def yuo_say(name, ys):
    print(f'{name} say {ys}')
yuo_say('Вадим', 'Привет')  #Вадим say Привет
yuo_say('Толик', 'Здрасте')  #Толик say Здрасте

# def sum():      #в таком случае мы переопределяем функцию sum() которая уже есть
#     pass

def sumka(a, b):
    print(a+b)
sumka(2,3)  #5
a1 = 10
a2 = 20
sumka(a1, a2)   #30

print(len('Hello')) #5 - возвращает результат а не печатает

def get_sum(a, b):
    return a+b
print(get_sum(8, 9))    #17

# если нету return - то вернет None

# дом задание - использовать функцию для вывода таблицы умножения
def tablik(mnoz1, mnoz2):
    for x in range(1, mnoz1+1):
        for y in range(1, mnoz2+1):
            print(f'{x} * {y} = {x*y}', end='\t')
        print('')
tablik(9, 9)
