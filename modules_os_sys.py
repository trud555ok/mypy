# модуль os
import os
print(os.name) # nt - название семейства ос компа (сюда входит винда 10) ?
print(os.environ) # словарь с переменными окружениями и их значения

print(os.getcwd())  # Получение текущей директории  --  C:\Users\trud5\PycharmProjects\mypy
#os.chdir("path")  --  Смена директории   ????

print(os.listdir(path="."))  #Список файлов в деректории -- в нашем случае - в тек дерект

# os.mkdir("test") - создать папку
# os.makedirs("a/b/c") - создать папки вложеные

# os.remove("file.txt")   # файл
# os.rmdir("dir")         # пустая папка
# os.removedirs("a/b/c")  # рекурсивно
#
# os.path.exists("file.txt")   -- Проверка существования файла

#3. Работа с путями (os.path)
# os.path.join("folder", "file.txt")   --- Соединение путей (ОБЯЗАТЕЛЬНО использовать)
#os.path.split(path) ---  Разделение пути --('/home/user', 'file.txt')
# os.path.basename(path)   --- Имя файла
# os.path.dirname(path)  --- Папка файла
#os.path.splitext("file.txt")  --- Расширение файла
# os.path.abspath("file.txt")  ---  Абсолютный путь

# проверка типа
# os.path.isfile(path)
# os.path.isdir(path)
# os.path.islink(path)

# os.path.getsize("file.txt")  -- размер файла

# 4. Переменные окружения   Очень важно для backend / devops.
# os.getenv("HOME")    os.environ["HOME"]     --- Получить переменную 2 способв
# os.environ["DEBUG"] = "1"  --- Установить переменную
# os.environ   --- Все переменные (как словарь)

# 5. Работа с процессами
# os.getpid()  --- ID процесса
# os.getppid()  --- Родительский процесс

# Запуск команды ОС
# os.system("ls")   --- старый способ ⚠️ Лучше использовать subprocess.
# os.kill(pid, signal)   --- Завершить процесс

# 6. Пользователь и права (Linux/Mac)    ?????
# os.getuid()
# os.getgid()
# os.getlogin()

# 7. Информация об ОС
# os.name   -- Тип ОС
# Возвращает:
# nt → Windows
# posix → Linux/Mac

# os.sep   -- Разделитель путей   Windows: \  Linux: /

# os.pathsep  Переменная PATH separator

# 8. Время файлов
# os.path.getmtime(path)  # изменение
# os.path.getctime(path)  # создание
# os.path.getatime(path)  # доступ

# 9. Обход директорий (очень важно)
# os.walk()                 --- примеры работы
# for root, dirs, files in os.walk("project"):
#     print(root, files)
# Возвращает:
# текущую папку
# подпапки
# файлы

# 10. Работа с файловыми дескрипторами (низкий уровень)    --- ????
# fd = os.open("file.txt", os.O_RDONLY)
# os.close(fd)

# 11. Права доступа
# os.chmod("file.txt", 0o777)     ???????

# 12. Полезные константы
# os.curdir   # "."
# os.pardir   # ".."
# os.linesep  # \n или \r\n

# Создание файла
# 1 способ
# with open("nant.py", "w") as f:
#     pass
# если файла нет → он создаётся
# если есть → очищается

# Сразу записать код в файл
# with open("nant.py", "w") as f:
#     f.write('print("Hello from nant")\n')

# Создать файл через os      --- Но ⚠️ это почти никогда не используют — слишком низкоуровнево.
# fd = os.open("nant.py", os.O_CREAT)           os.O_CREAT - говорит ОС создай файл если он не существует
# Второй аргумент — это набор флагов, которые управляют тем, как открывается файл.
# os.close(fd)

# 3. Правильный современный способ — pathlib ⭐ (рекомендуется)
# from pathlib import Path
# Path("nant.py").touch()
# ✔ создаёт файл
# ✔ не удаляет содержимое если уже существует

# Создать и записать код
# from pathlib import Path
# Path("nant.py").write_text('print("hello")\n')

# 4. Через терминал (самый частый способ у разработчиков)
# Linux / Ubuntu / WSL
# touch nant.py   nano nant.py      2 способа в терминале линукса
# Windows (cmd)
# type nul > nant.py
# PowerShell
# New-Item nant.py

# Практический пример (автогенерация python файла)
# from pathlib import Path
#
# name = "nant"
# file = Path(f"{name}.py")
#
# file.write_text(
# '''def main():
#     print("Program started")
#
# if __name__ == "__main__":
#     main()
# '''
# )