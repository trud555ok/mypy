# Урок 15.Д/з. Вывод таблицы умножения
for i in range(1, 10):
    for k in range(2, 10):
        print(f'{i} * {k} = {i*k}', end = '\t')
    print('')
