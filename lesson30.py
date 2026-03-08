import  os, random      #os - для работы с операционной системой  random - для генерации случайных чисел
##import readline as rl   # для нашего названия импортируемых модулей можно использовать псевдонимы
from random import randint, shuffle   #когда не нужно импортировать весь модуль а только определенные его функции
from  random import * # импортировать все модули с random

import os
import os as my



# 3доступны оба имени
print(os.getcwd())
print(my.getcwd())



print(os.getcwd())  #C:\Users\trud5\PycharmProjects\mypy  --- путь к текущей папке
print(randint(1, 100))   #генерация случайного целого числа от 1 до 100
l = [1,2,3,4,5]
shuffle(l)  #[4, 1, 3, 5, 2]
print(l)

import libs         #импортируем весь наш модуль

from libs  import get_count, get_len
print(get_count('helllo', 'l'))    #3
print(get_len('hello'))    #5
print(__name__)         # __main__ - если запущен этот файл, имя файла(lesson30) если будет импортирован

# Переменной присваиваем функцию, без скобок
f = libs.get_count  # после этого можем вызывать f как функцию



# если запустить прогу то увидим то что напечаталось через libs.py

# ДЗ - игра угадай число со случайными числами и после игры програма предлагает сыграть еще