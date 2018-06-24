# Спасенов ИУ7-13
# Вывести таблицу значений функции и построить ее график
try:
    n, sh, k = map(float, input('Введите начальное значение, шаг пос\
ледовательности и конечное значение: ').split())

    if sh == 0 or n == k or abs(n - k) <= sh or sh < 0:
        print('Невозможно построить таблицу и график с такими значен\
иями! ')
    else:

        print('\t    w\t\t', '    t\t\t', ' n')
        l = n
        e = 1
        while True:  # Выводим таблицу значений функции
            l1 = round(l, 5)
            k1 = round(k, 5)
            if l1 <= k1:
                w = 2048 * l ** 12 - 6144 * l ** 10 + 6912 * l ** 8 \
                    - 3584 * l ** 6 + 840 * l ** 4 - 72 * l ** 2 + 1
                if abs(w) >= 1000:
                    print('\t{:.3e}'.format(w), end='')
                else:
                    print('\t{:9.3f}'.format(w), end='')
                if abs(l) >= 1000:
                    print('\t{:.3e}\t'.format(l), end='')
                else:
                    print('\t{:9.3f}\t'.format(l), end='')
                print('{:3d}'.format(e))
                l += sh
                e += 1
            else:
                break
        print('\n')

        v = 2048 * n ** 12 - 6144 * n ** 10 + 6912 * n ** 8 - 3584 * n ** 6 + 840 * n ** 4 - 72 * n ** 2 + 1
        max = v
        min = v
        mint = n
        l = n
        while l < k:  # Находим максимальное и минималное значение
            v = 2048 * l ** 12 - 6144 * l ** 10 + 6912 * l ** 8 - 3584 * l ** 6 + 840 * l ** 4 - 72 * l ** 2 + 1
            if v > max:
                max = v
            if v < min:
                min = v
                mint = l
            l += sh

        print('Минимальное значение w = {:.3f} оно достигается при t = {:.3f}'.format(min, mint))
        print('\n')
        print('График функции: w = 2048*t^12-6144*t^10+6912*t^8-3584*t^6+840*t^4-72*t^2+1')
        print('\n\n')

        zero = False  # Определяем, нужно ли печатать нулевую линию
        if min < 0 and max > 0:
            zero = True

        if abs(min) >= 1000:
            print('{:.3e}'.format(min), end='')
        else:
            print('{:.3f}'.format(min), end='')
        min1 = round(min, 4)
        for i in range(60 - 9):
            print(' ', end='')
        if abs(max) >= 1000:
            print('{:.3e}'.format(max))
        else:
            print('{:.3f}'.format(max))

        print('+', end='')
        for i in range(60):
            print('-', end='')
        print('+       t\t   n')

        q1 = -1
        q2 = -1
        if zero:
            c = abs(min) / abs(max - min)
            q1 = 60 * c
            q2 = round(q1)
            for i in range(q2):
                print(' ', end='')
            print('0')

        l = n
        e = 1
        p = 2
        while True:  # Печатаем график
            l1 = round(l, 5)
            k1 = round(k, 5)
            if l1 <= k1:
                w = 2048 * l ** 12 - 6144 * l ** 10 + 6912 * l ** 8 - 3584 * l ** 6 + 840 * l ** 4 - 72 * l ** 2 + 1
                c = abs(w - min) / abs(max - min)
                q1 = 61 * c
                q3 = round(q1)

                # print(' ', end='')
                x = 0
                while True:
                    if x > 61:
                        print('', end=' ')
                        break
                    else:
                        if x == q2:
                            print('|', end='')
                        elif x == q3:
                            print('*', end='')
                        else:
                            print(' ', end='')
                    x += 1
                if p == e:
                    if abs(l) >= 1000:
                        print('{:.3e}'.format(l), end=' ')
                    else:
                        print('{:9.3f}'.format(l), end=' ')
                    print('{:3d}'.format(p), end='\n')
                    p += 2
                else:
                    print('', end='\n')

                e += 1
                l += sh
            else:
                break
        input('\nНажите Enter, чтобы выйти...')
except ValueError:
    print('Введены некорректные данные!')
