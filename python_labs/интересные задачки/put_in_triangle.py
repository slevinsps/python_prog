# Спасенов ИУ7-13
# Максимальный путь в треугольнике чисел
from random import *
a = []
n = int(input('Введите n: '))

k = 1

for i in range(n):
    a.append([randint(0,9) for i in range(k)])
    k += 1
for i in range(n):
    for j in range(len(a[i])):
        print(a[i][j],end=' ')
    print()

for i in range(1,n):
    for j in range(len(a[i])):
        if j == 0:
            a[i][j] += a[i-1][j]
        elif j == len(a[i])-1:
            a[i][len(a[i])-1] += a[i-1][len(a[i])-2]
        else:
            if a[i-1][j-1]>a[i-1][j]:
                a[i][j] += a[i-1][j-1]
            else:
                a[i][j] += a[i-1][j]

max1 = max(a[n-1])
print('Максимальная сумма равна: ',max1)
