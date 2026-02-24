test = None # переменная не определена, значение отсутствует

x, y =  (1, 5) #множественное присваивание, распаковка кортежа
print(x, y) #1 5

my_true = True
my_false = False
print(type(my_true)) #<class 'bool'>
print(type(my_false)) #<class 'bool'>

# str()  int()  float()  bool()
x = 5.2
print(x, type(x))  #5.2 <class 'float'>
x = int(x)
print(x, type(x))  #5 <class 'int'>
x = str(x)
print(x, type(x))  #5 <class 'str'>

# bool() - 0, пустая строка, None - приводятся к False, стальное к True