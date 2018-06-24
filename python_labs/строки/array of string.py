
# Спасенов Иван ИУ7-13
# Массив строк

def zamena(zam, zam1, a, e):
    for i in range(len(a)):
        a[i] = ' ' + a[i] + ' '
        s1 = a[i]
        k2 = 0
        t = a[i]
        while zam in t:

            s = ''
            for j in range(k2, len(s1) - len(zam)):
                o = False
                k = 0
                s = ''
                for h in range(len(zam)):
                    s += s1[k + j]
                    k += 1
                if s == zam:
                    if ((s1[j - 1] in zn) or s1[j - 1] == ' ') and ((s1[j + k] in zn) or s1[j + k] == ' '):
                        o = True
                        s11 = s1
                        s1 = ''
                        if e:
                            if s11[j - 1] == ' ':
                                j -= 1
                                for q in range(j):
                                    s1 += s11[q]
                                j += 1
                        else:
                            for q in range(j):
                                s1 += s11[q]
                        s1 += zam1
                        for q in range(j + k, len(s11)):
                            s1 += s11[q]
                        a[i] = s1
                        t = ''
                        for q in range(j+k, len(s11)):
                            t += s11[q]
                        k2 = j + len(zam1)
                        break
                    else:
                        o = False
                if o:
                    break
        f = a[i]
        a[i] = ''
        for q in range(1, len(f) - 1):
            a[i] += f[q]
    for i in range(len(a)):
        print(a[i])


# Массив строк
a = ['я роботы захватят в мир я. Когда-нибудь в 2+1 а может и я нет.',
     '9-6 вкуснейших, пряников я купил себе вчера',
     'артем любит капусту по 5+30?',
     'apple самая богатая - компания в мире я']

zn = ['.',',','?','!','?!','...']
maxdef = len(max(a))

print('Исходный текст:')
print()
for i in a:
    print(i)

dl = []  # массив максимальных длин слов
slova = 0  # количество слов
s = ''
# Заполняем массив dl словами максимальной длины
# Одновременно подсчитываем количество слов
for i in range(len(a)):
    t = ''
    for j in range(len(a[i])):
        if a[i][j] == '-':
            if a[i][j-1] != ' ' and a[i][j+1] != ' ':
                t += a[i][j]
        elif a[i][j] not in zn:
                t += a[i][j]
    s += t+' '
    d = t.split()

    slova += len(d)
    d1 = []
    for i in d:
        d1.append(len(i))
    dl.append(d[d1.index(max(d1))])


maxi = -1  # частота слова
maxs = ''  # самое частовстречаемое слово
# Находим самое частовстречаемое слово

s = s.split()
for i in range(len(s)):
    if s.count(s[i]) > maxi:
        maxs = s[i]
        maxi = s.count(s[i])

# Заменяем в тексте все операции '+','-' на результат
for i in range(len(a)):
    w = 0
    while w != len(a[i]):
        if a[i][w] == '+' or a[i][w] == '-':
            k = 1
            s2 = ''
            s3 = ''
            while w+k <= len(a[i])-1 and '0' <= a[i][w+k] <= '9':
                s2 += a[i][w+k]
                k += 1
            k1 = 1
            while w-k1 >= 0 and '0' <= a[i][w-k1] <= '9':
                s3 += a[i][w-k1]
                k1 += 1
            if a[i][w] == '+':
                a[i] = a[i][:w-k1+1] + str(int(s2)+int(s3)) + a[i][w+k:]
            elif a[i][w] == '-' and s2 and s3:
                a[i] = a[i][:w-k1+1] + str(int(s3)-int(s2)) + a[i][w+k:]
        w += 1
print('-'*maxdef)
print('Текст с заменой арифметических операций "+" и "-" на результат:')
print()
for i in a:
    print(i)
print('-'*maxdef)

for i in range(len(dl)):
    print('Самое длинное слово в строке № ',i+1,': ',dl[i],sep='')
print('-'*maxdef)
print('Количество слов в тексте:',slova)
print('-'*maxdef)
print('Наиболее часто встречается слово: ',maxs)
print('-'*maxdef)

# Выравниваниваем текст по правому краю
print('Текст выравненный по правому краю:')
print()
nm = len(max(a))
for i in range(len(a)):
    print(' '*(nm-len(a[i])), a[i], sep='')
print('-'*maxdef)

# Выравниваниваем текст по центру
print('Текст выравненный по центу:')
print()
for i in range(len(a)):
    if len(a[i]) != nm:
        d = a[i].split()
        nm3 = 0
        for j in d:
            nm3 += len(j)
        nm1 = nm-nm3
        nm2 = len(d)-1
        k = 0
        for j in range(nm2-nm1 % nm2):
            print(d[k], ' ' * (nm1//nm2), sep='', end='')
            k += 1
        for j in range(nm1 % nm2):
            print(d[k], ' ' * (nm1 // nm2 + 1), sep='', end='')
            k += 1
        print(d[k])
    else:
        print(a[i])
print('-'*maxdef)

# Производим замену всех исходных слов на новое
zam = input('Введите слово, которое хотите заменить: ')
zam1 = input('Введите замену: ')
print('Измененный текст:')
print()
zamena(zam,zam1, a, False)
print('-'*maxdef)

# Удаляем слово
ud = input('Введите слово, которое хотите удалить: ')
print('Измененный текст:')
print()
zamena(zam,'', a, True)
print('-'*maxdef)
























