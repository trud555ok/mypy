# Урок 33.Работа с файлами

# f = open("file.txt", 'r', encoding="utf-8")      #encoding="utf-8"  -- правильно отображаются файлы
# print(f.encoding)       #cp1251 - системная кодировка
# f_read = f.read()           #проблемы с отображением кирилицы!!!!
# f_read2 = f.read(20)           #прочитается 20 символов
# print(f_read)
# print(f_read2)          #второе чтение начнется там где закончилось первое
# f.close()

# Запись - дозапись в файл
# f = open("file.txt", 'a', encoding="utf-8")
# f.write("Новая строка\n")
# f.close()

# Если надо записать список строк
# lines = ['строчка 1', 'строчка 2', 'строчка 3']
# ff = open('file.txt', 'a', encoding='utf-8')
# метод цыкла
# for i in lines:
#     ff.write(i + '\n')
#метод writelines
# ff.writelines(lines)
#метод writelines с циклом внутри
# ff.writelines(f"{i+'\n'}" for i in lines)
# ff.close()

# Методы чтения
f = open("file.txt", 'r', encoding="utf-8")
for line in f:
    #print(line)     #лишние переносы
    #print(line, end='')     #нету лишних переносов
    print(line.replace('\n', ''))     #нету лишних переносов

f.close()

# file.readline() -> str    считывает одну строку и возвращает ее
# file.readlines() -> list  считывает все строки и возвращает список этих строк
# file.writelines(lines) -> None  записывает список строк - разделители надо самому добавлять




