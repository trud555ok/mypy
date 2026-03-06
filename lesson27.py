# дом задание
def register(s):
    if ' ' in s:
        s = s.upper()
    else:
        s = s.lower()
    return s

print(register('sdsd klklk'))

def get_sum(a,b,c=0,d=1):
    return a+b+c+d
print(get_sum(1,2,5,7)) #15
print(get_sum(1,2)) #4
print(get_sum(1,2, d=6)) #9     c - пропустили и все работает, по умолчанию =0

# именованые аргументы всегда передаются после позиционных!!!!
# если написать значения по умолчанию - они становятся именоваными, и могут передаваться не по позиции

def tyret(*args, **kwargs):
    #*args - преобразовывается в кортеж, позиционные аргументы
    #**kwargs - преобразовуется в словарь - именованые аргументы
    print(args)             #(1, 2, 2) - преобразовалось в кортеж
    return sum(args)

print(tyret(1,2,2)) #5

def ff(**kwargs):
    print(kwargs)   #{'a': 1, 'b': 2, 'c': 3} -- преобразовалось в словарь

ff(a=1,b=2,c=3)

def dd(a,x,*args, b=1, c=3, **kwargs):
    print(a)    #1
    print(x)    #2
    print(args)     #(3,4)
    print(b)    #6
    print(c)    #3 - по умолчанию
    print(kwargs)   #{'r': 12, 'rr': 16}

dd(1,2,3,4,b=6,r=12,rr=16)























