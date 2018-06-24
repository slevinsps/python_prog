from random import *
from math import *

def pov(g):
    f = []
    for i in g:
        f.append(i[:])
    n = len(f)
    f.reverse()
    for i in range(n - 1):  # Меняем местами элементы матрицы
        for j in range(i + 1, n):
            f[i][j], f[j][i] = f[j][i], f[i][j]
    return f

def setka(k):
    a = []
    x = []
    k1 = k // 2
    for i in range(k1 * k1):
        x.append(i + 1)
        if len(x) == k1:
            a.append(x)
            x = []

    a1 = pov(a)
    for i in range(len(a)):
        for j in a1[i]:
            a[i].append(j)

    a2 = pov(a1)
    a3 = pov(a2)
    for i in range(len(a3)):
        for j in a2[i]:
            a3[i].append(j)

    a.extend(a3)

    q = k1 * k1
    d1 = ()
    d2 = ()
    w1 = []
    while q != 0:
        h = randint(0, k - 1)
        h1 = randint(0, k - 1)
        for i in range(h1):
            h3 = randint(0, k - 1)
            if a[h][h3] not in w1 and a[h][h3] != 0:
                w1.append(a[h][h3])
                a[h][h3] = 0
                q -= 1
                if q == 0:
                    break
            else:
                break

    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == 0:
                a[i][j] = 1
            else:
                a[i][j] = 0
            print(a[i][j], end=' ')
        print()
    print()
    return a

def kodirovka(s):
    k = int(sqrt(len(s)))
    a = setka(k)
    f = []
    for i in a:
        f.append(i[:])
    t = 0
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == 1:
                if t<=len(s):
                    f[i][j] = s[t]
                    t += 1


    for i in range(3):
        
        f = pov(f)

        for y in range(len(a)):
            for j in range(len(a[i])):
                if a[y][j] == 1:
                    f[y][j] = s[t]
                    t += 1
    f = pov(f)

    
    return f

while True:
    print('''
Выберите, что вы хотите сделать:'
1 - закодиовать
2 - раскодировать


0 - выйти''')
    e = int(input())
    if e == 0:
        break
    elif e == 1:
        print('Введите без пробелов предложение длиной 64:')
        s = input()
        if len(s)<=64:
            while len(s) != 64:
                s += chr(randint(1072,1103))
            f = kodirovka(s)
            print(s)
            print('Зашифрованная матрица:')
            for i in range(len(f)):
                for j in range(len(f[i])):
                    print(f[i][j],end=' ')
                print()
        else:
            print('Длина предложения > 64')
    elif e == 2:
        s = ''
        
        n = int(input('Введите размер матрицы: '))
        print('Введите зашифрованную матрицу:')
        w = [[j for j in input().split()] for i in range(n)]
        print('Введите ключ:')
        w1 = [[int(j) for j in input().split()] for i in range(n)]
        for y in range(len(w1)):
            for j in range(len(w1[y])):
                if w1[y][j] == 1:
                    s += w[y][j]
        for i in range(3):

            w = pov(w)

            for y in range(len(w1)):
                for j in range(len(w1[y])):
                    if w1[y][j] == 1:
                        s += w[y][j]

        print('Зашифрованное послание:')
        print(s)
