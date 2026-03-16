import os

# os.mkdir('dir_os')
# os.makedirs('dz_os/papka1/papka2')
# os.chdir('./dz_os')
# fd = os.open("nant.py", os.O_CREAT)
# os.close(fd)
# os.chdir('./papka1')
# fd = os.open("nant1111.py", os.O_CREAT)
# os.close(fd)
# fd = os.open("nant2222.py", os.O_CREAT)
# os.close(fd)
# os.chdir('./papka2')
# fd = os.open("1111.py", os.O_CREAT)
# os.close(fd)
# fd = os.open("2222.py", os.O_CREAT)
# os.close(fd)
# os.chdir('./../../../')
# print(os.getcwd())
#
# for root, dirs, files in os.walk("dz_os"):
#     # print(root, dirs, files)
#     print(root)
#     print('\t', dirs)
#     print('\t', files)

# вариант учителя
# tree = os.walk('dz_os')
# print(tree)     #<generator object walk at 0x000002294BA35740> - генератор
# генератор не содержит данных он их генерирует по запросу

# если прогнать этот генератор через цыкл for
# каждая иттерация - это уровень вложенности
# на каждой иттерации получаем -
# 1 - путь к уровню вложенности
# 2 - список папок/деректорий
# 3 - список файлов
# for f in tree:
#     print(f)

def read_dir(folder):
    for root, dirs, files in os.walk(folder):
        # вложеность - считаем сколько слэшей в пути - такая и вложеность
        level = root.count(os.sep)  #os.sep - разделитель в ОС
        intend = ' '*4*level
        sub_intend = ' '*4 + intend
        print(f'{intend}[{os.path.basename(root)}]')    #вывод папки
        for file in files:
            print(f'{sub_intend}{file}')

read_dir('dz_os')
# dz_os ['nant.py'] 0
# dz_os\papka1 ['nant1111.py', 'nant2222.py'] 1
# dz_os\papka1\papka2 ['1111.py', '2222.py'] 2
