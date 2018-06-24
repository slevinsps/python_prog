# Спасенов Иван ИУ7-13
# Работа с файлами
while True:
    name = None # имя файла
    # Начальное меню
    print('Для хранения базы данных игр вам нужен текстовый файл')
    print('''
1 - Создать новый файл
2 - У меня уже есть файл

0 - Выход
    ''')
    
    q = int(input('Ввведите пункт меню: '))
    if q == 0:
        break
    elif q == 1:
        name = input('Введите имя будущего файла с расширением: ')
        file = open(name, 'w+')
        file.write('{:<15}{:^15}{:>15}\n'.format('Название игры', 'год издания', 'стоимость'))
        print('Файл', name, 'создан!')
        file.close()
    elif q == 2:
        name = input('Введите имя вашего файла с расширением: ')
        # Проверяем файл на существование
        try:
            file = open(name)
        except IOError as e:
                print('Не удалось найти ваш файл')
                break
        print('Прогамма запомнила ваш выыбор!')

    # Основное меню
    while True:
        print('''

    1 - Отобразить содержимое файла
    2 - Добавтить запись в файл
    3 - Поиск по фильтрам

    0 - Выход
        ''')
        a = int(input('Введите пункт меню: '))
        if a == 0:
            break
        elif a == 1:
            file = open(name, 'r')
            for line in file:
                print(line,end='')
            file.close()
        elif a == 2:
            file = open(name, 'a')
            s1 = input('Введите название игры: ')
            s2 = input('Введите год издания: ')
            s3 = input('Введите стоимость: ')
            file.write('{:<15}{:^15}{:>15}\n'.format(s1,s2,s3))
            file.close()
        elif a == 3:

            # Реализация поиска по категориям
            while True:
                print('''
    1 - Поиск по названию игры
    2 - Поиск по году издания
    3 - Поиск по стоимости

    0 - Выход в предыдущее меню
                ''')
                b = int(input('Ввведите пункт меню: '))
                if b == 0:
                    break
                elif b == 1:
                    s = input('Введите название игры: ')
                    
                    name1 = input('Введите имя файла с расширением, в который хотите сохранить результаты: ')
                    file = open(name1, 'w+')
                    
                    file = open(name, 'r')
                    st = None # строчка исходного файла
                    while True:
                        st = file.readline()
                        st1 = st.split() # массив из категорий
                        if st == '':
                            break
                        if  st1[0] == s:
                            # создаем файл, в который запишутся результаты
                            file2 = open(name1, 'a+')
                            file2.write('{:<15}{:^15}{:>15}\n'.format(st1[0],st1[1],st1[2]))
                            file2.close()
                    print('Рзультаты сохранены в файле',name1)
                    file.close()
                elif b == 2:
                    s = input('Введите год издания: ')
                    name1 = input('Введите имя файла с расширением, в который хотите сохранить результаты: ')
                    file = open(name1, 'w+')
                    file = open(name, 'r')
                    st = None
                    while True:
                        st = file.readline()
                        st1 = st.split()
                        if st == '':
                            break
                        if st1[1] == s:
                            # создаем файл, в который запишутся результаты
                            file2 = open(name1, 'a+')
                            file2.write('{:<15}{:^15}{:>15}\n'.format(st1[0], st1[1], st1[2]))
                            file2.close()
                    print('Рзультаты сохранены в файле',name1)
                    file.close()
                elif b == 3:
                    s = input('Введите стоимость: ')
                    name1 = input('Введите имя файла с расширением, в который хотите сохранить результаты: ')
                    file = open(name1, 'w+')
                    file = open(name, 'r')
                    st = None
                    while True:
                        st = file.readline()
                        st1 = st.split()
                        if st == '':
                            break
                        if st1[2] == s:
                            # создаем файл, в который запишутся результаты
                            file2 = open(name1, 'a+')
                            file2.write('{:<15}{:^15}{:>15}\n'.format(st1[0], st1[1], st1[2]))
                            file2.close()
                    print('Рзультаты сохранены в файле',name1)
                    file.close()





