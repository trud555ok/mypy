
# решение домашнего задания
# import  random
# my_ch = random.randint(1, 11)
# col_popyt = 0
#
# while True:
#     otvet = int(input('Угадай число от 1 до 10:'))
#     col_popyt +=1
#
#     if isinstance(otvet, int) and 0< otvet < 11:
#         if otvet == my_ch:
#             print(f'Победа с {col_popyt} попытки')
#             if input('Сыграем еще y/n') == 'y':
#                 my_ch = random.randint(1, 11)
#                 col_popyt = 0
#                 continue
#             else:
#                 break
#         if otvet < my_ch:
#             print('Твой ответ меньше')
#         else:
#             print('Твой ответ больше')
#     else:
#         print('неадекватные данные')
#         break
# Модуль datetime - в нем классы для работы с датой и временем
from datetime import date, datetime, timedelta
import locale

# date
today = date.today()
print(today)    #2026-03-09  -- текущая дата с учетом локали
print(today.day)    #9
print(today.month)  #3
print(today.year)   #2026
print(today.weekday())   #0 - понедельник, в Англии 0 будет в воскресенье

#datetime
now = datetime.today()
now2 = datetime.now()
print(now, now2, sep='\n') #2026-03-09 22:00:38.989535 - одинаковые значения, разницы нету today() == now()
print(now.day)
print(now.month)
print(now.year)
print(now.weekday())
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)

print(now.strftime('%a'))   #Mon
print(now.strftime('%A'))   #Monday

# как получить на русском - поменять локаль
locale.setlocale(locale.LC_ALL, "ru_ru")

print(now.strftime('%a'))   #Пн
print(now.strftime('%A'))   #понедельник

print(f'Сейчас такая дата:{now.strftime("день - %d, месяц - %m, год - %Y,  час - %H : %M ")}')

# timedelta
now3 = datetime.today()
print(now.strftime('%c')) # %c - вывод в норм формате
# если хотим прибавить какой то промежуток времени
d1 = now + timedelta(days=2, hours=5, minutes=15)     #можно ли сравнивать даты?
print(d1.strftime('%c'))

# os - изучить модуль, какие там есть классы,
# создать папку, в ней файлы и подпапки, в подпапках файлы --- вывести в консоли схему папок и документов с отступами
# метод walk ????
