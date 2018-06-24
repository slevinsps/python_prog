# Спасенов Иван ИУ7-13
# Массив строк

def kol(s1):
    maxi = -1
    maxs = ''
    k = 0
    s = ''
    for i in range(len(s1)):
        if s1[i] != ' ':
            s += s1[i]
        else:
            if s != '':
                k += 1
                if len(s)>maxi:
                    maxi = len(s)
                    maxs = s
            s = ''
            
    return maxs, k

def count(s1):
    maxi = -1  # частота слова
    maxs = ''  # самое частовстречаемое слово
    s = ''
    ss = ''
    k = 0
    for i in range(len(s1)):
        if s1[i] != ' ':
            s += s1[i]
        else:
            for i in range(len(s1)):
                if s1[i] != ' ':
                    ss += s1[i]
                else:
                    if ss == s:
                        k += 1
                    ss = ''
            if k>maxi:
                maxi = k
                maxs = s
            k = 0
            s = ''
    return maxs

def pechat(c,k):
    s = ''
    for i in range(k):
        s += c
    return(s)

def for_shirina(s1):
    s1 += ' '
    k = 0
    k1 = 0
    s = ''
    for i in range(len(s1)):
        if s1[i] != ' ':
            s += s1[i]
        else:
            k += len(s)
            k1 += 1
            s = ''
    return k,k1


def shirina(a):
    for i in range(len(a)):
        if len(a[i]) != nm:
            nm3,nm2 = for_shirina(a[i])
         
            nm1 = nm - nm3
            nm2 = nm2 - 1
            k = 0
            k1 = 0
            for j in range(nm2-nm1 % nm2):
                s = ''
                for h in range(k,len(a[i])):
                    if a[i][h] != ' ':
                        s += a[i][h]
                    else:
                        print(s, ' ' * (nm1//nm2), sep='', end='')
                        s = ''
                        k = h
                        while a[i][k] == ' ':
                            k+=1
                        break

            for j in range(nm1 % nm2):
                s = ''
                for h in range(k,len(a[i])):
                    if a[i][h] != ' ':
                        s += a[i][h]
                    else:            
                        print(s, ' ' * (nm1//nm2+1), sep='', end='')
                        k = h
                        while a[i][k] == ' ':
                            k+=1
                        break
            for h in range(k,len(a[i])):
                print(a[i][h],sep='', end='')
            print()
        else:
            print(a[i])


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
a = ['На прошлой лабораторной работе, которая была 36-12 ноября, группа ИУ7-13 писала',
     'контрольную работу. Они ее написали, возможно,',
     'даже хорошо. Некоторые. Некоторые не написали',
     'номер варианта!']

zn = ['.',',','?','!','?!','...']
maxdef = len(max(a))

print('Исходный текст:')
print()
for i in range(len(a)):
    print(a[i])

dl = ['']*len(a)  # массив максимальных длин слов
slova = 0  # количество слов
s = ''
# Заполняем массив dl словами максимальной длины
# Одновременно подсчитываем количество слов
dl = ['']*len(a)
for i in range(len(a)):
    t = ''
    for j in range(len(a[i])):
        if a[i][j] == '-':
            if a[i][j-1] != ' ' and a[i][j+1] != ' ':
                t += a[i][j]
        elif a[i][j] not in zn:
                t += a[i][j]
    s += t+' '
    dl[i], slova1 = kol(t+' ')
    slova += slova1

maxi = -1  # частота слова
maxs = ''  # самое частовстречаемое слово
# Находим самое частовстречаемое слово
maxs = count(s)
# Заменяем в тексте все операции '+','-' на результат
for i in range(len(a)):
    w = 0
    qo = True
    while w != len(a[i]):
        if a[i][w] == '+' or a[i][w] == '-':
            k = 1
            s2 = ''
            s3 = ''
            while w+k <= len(a[i])-1 and '0' <= a[i][w+k] <= '9':
                s2 += a[i][w+k]
                k += 1
            if a[i][w+k]!=' ':
                if a[i][w+k] not in zn and w+k  <= len(a[i])-1:
                    qo = False
            k1 = 1
            while w-k1 >= 0 and '0' <= a[i][w-k1] <= '9':
                s3 = a[i][w-k1] + s3
                k1 += 1
            if a[i][w-k1]!=' ':
                if a[i][w-k1] not in zn and w-k1 >= 0:
                    qo = False
            if qo:
                if a[i][w] == '+':
                    q = ''
                    q1 = ''
                    for j in range(w-k1+1):
                        q += a[i][j]
                    for j in range(w+k,len(a[i])):
                        q1 += a[i][j]
                    a[i] = q + str(int(s2)+int(s3)) + q1
                elif a[i][w] == '-' and s2 and s3:
                    q = ''
                    q1 = ''
                    for j in range(w-k1+1):
                        q += a[i][j]
                    for j in range(w+k,len(a[i])):
                        q1 += a[i][j]
                    a[i] = q + str(int(s3)-int(s2)) + q1
            qo = True
        w += 1
print('-'*maxdef)
print('Текст с заменой арифметических операций "+" и "-" на результат:')
print()
for i in range(len(a)):
    print(a[i])
print(pechat('-',maxdef))

for i in range(len(dl)):
    print('Самое длинное слово в строке № ',i+1,': ',dl[i],sep='')
print(pechat('-',maxdef))
print('Количество слов в тексте:',slova)
print(pechat('-',maxdef))
print('Наиболее часто встречается слово: ',maxs)
print(pechat('-',maxdef))

# Выравниваниваем текст по правому краю
print('Текст выравненный по правому краю:')
print()
nm = -1
for i in range(len(a)):
    if len(a)>nm:
        nm = len(a[i])
for i in range(len(a)):
    print(pechat(' ',nm-len(a[i])), a[i], sep='')
print(pechat('-',maxdef))

# Выравниваниваем текст по ширине
print('Текст выравненный по ширине:')
print()
shirina(a)
print(pechat('-',maxdef))

# Производим замену всех исходных слов на новое
zam = input('Введите слово, которое хотите заменить: ')
zam1 = input('Введите замену: ')
print('Измененный текст:')
print()
zamena(zam,zam1,a,False)
print('-'*maxdef)

# Удаляем слово
ud = input('Введите слово, которое хотите удалить: ')
zamena(ud,'',a,True)
print('-'*maxdef)
