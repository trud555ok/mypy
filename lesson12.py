print(2 == "2")  # False - проверяется и по типу

lite = 'red'

if lite == 'red':
    print("Stop")
elif lite == 'yellow':
    print('Wait')
elif lite == 'green':
    print('Go!')
else:
    print('What?')

# для ввода инфы от пользователя
a = int(input('Сколько Вам лет? '))  # int потому что input возращает строку
if a > 18:
    print("Заходи!")
else:
    print("Тебе еще рано!")

a1 = int(input("Сколько лет твоему брату? "))
if a1 > 18:
    print(f'Брат пусть заходит, ему уже {a1} лет')
else:
    print(f'Брату еще рано, ему не хватает {19 - a1} годиков')

t = 11
if t <= 12 or t >= 14:  # or - логическое ИЛИ
    print('Нету перерыва сейчас')
else:
    print("Сейчас перерыв!")

t1 = 12
day = 'st'
if t1 > 7 and day != 'su':
    print("Мы открыты")
else:
    print("Мы закрыты")

x = 1
if not x:
    print("-")
else:
    print('+')

# Тернарного оператора нету -- его подобие
f = 1
m = "ok" if f else "nieOk"
print(m)  # ok
