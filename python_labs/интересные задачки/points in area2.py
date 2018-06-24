# Спасенов Иван ИУ7-13
# Выписать точки,  области которых находятся остальные точки
from tkinter import *
from math import sqrt

# Функция, которая считает угол между векторами
def ugol(a1, a2, a3):
    k1 = [a3[0] - a2[0], a3[1] - a2[1]]
    k2 = [a1[0] - a2[0], a1[1] - a2[1]]
    u = (k1[0] * k2[0] + k1[1] * k2[1]) / (sqrt(k1[0] ** 2 + k1[1] ** 2) * (sqrt(k2[0] ** 2 + k2[1] ** 2)))
    return u

# Массив точек
a = [[0, 0],
     [10, -10],
     [20, -10],
     [10, -20],
     [10, -30],
     [-10, -10],
     [-10, 10],
     [10,20],
     [30,-10],
     [0,-20],
     [-5,-25]]

def opred_vip(a)
min_ld = a[0]  
# Самая нижняя левая точка
for i in range(len(a)):
    if a[i][1] < min_ld[1]:
        min_ld = a[i]
    elif a[i][1] == min_ld[1]:
        if a[i][0] < min_ld[0]:
            min_ld = a[i]

# Три точки по которым считаем угол между векторами
x3 = []
x2 = min_ld
x1 = [min_ld[0] - 10, min_ld[1]]


q = []  
q.append(min_ld)

# Массив углов между векторами
ug = [0] * (len(a))

# Находим нужные точки
while True:
    for i in range(len(a)):
        if a[i] != x2 and a[i] != x1:
            ug[i] = ugol(a[i], x2, x1)
        elif a[i] == x2 or a[i] == x1:
            ug[i] = 2
    x3 = a[ug.index(min(ug))]
    if x3 == min_ld:
        break
    x1 = x2
    x2 = x3
    q.append(x3)
    ug = [0] * (len(a))


print('Точки:')    
for i in q:
    for j in i:
        print(j,end = ' ')
    print()
