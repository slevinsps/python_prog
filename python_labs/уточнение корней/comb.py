from math import *
import numpy as np
import matplotlib.pyplot as plt
import time


# Задаваемая функция
def f(x):
    g = sin(x)
    return g


def f1(x):
    g = cos(x)
    return g


def f2(x):
    g = -sin(x)
    return g


# Осуществляем поиск корней
def find_roots(f, a=-10, b=10, h=2, maxi=1000, eps=1e-7):
    t3 = 0
    print("-----------------------------------------------------------------")
    print("| № |  X(n) | X(n+1)|     X     |    f(X)       | число  |код   |")
    print("|   |       |       |           |               |итераций|ошибки|")
    print("-----------------------------------------------------------------")
    k = 0
    nach = a
    korni = []
    while True:
        if nach + h < b:
            kon = nach + h
        else:
            kon = b
        if abs(f(nach))<1e-5:
            k += 1
            it = 0
            err = 0
            print("|{:3d}|{:7.2f}|{:7.2f}|{:9.4f}\t|{:7.3e}\t|{:3d}\t |{:3d}\t|".format(k, nach, kon, nach, f(nach), it, err))
            print("-----------------------------------------------------------------")
            korni.append(nach)
        else:

            if f(nach) * f(kon) < 0:

                # Вызываем метод уточнения корней: ridder
                t = time.clock()
                r, it = comb(f, nach, kon, maxi, eps)
                t2 = time.clock() - t
                t3 += t2
                k += 1
                if r == None:
                    err = 1
                    if it == None:
                        it = 0
                    err = 2
                    print('|{:3d}|{:7.2f}|{:7.2f}|  ---   \t|   ---   \t|{:3d}\t |{:3d}\t|'.format(k, nach, kon, it, err))
                    print("-----------------------------------------------------------------")
                else:
                    err = 0
                    print(
                    "|{:3d}|{:7.2f}|{:7.2f}|{:9.4f}\t|{:7.3e}\t|{:3d}\t |{:3d}\t|".format(k, nach, kon, r, f(r), it, err))
                    print("-----------------------------------------------------------------")
                    
        nach = kon
        if nach == b:
            if f(nach) == 0:
                k += 1
                it = 0
                err = 0
                print(
                "|{:3d}|{:7.2f}|{:7.2f}|{:9.4f}\t|{:7.3e}\t|{:3d}\t |{:3d}\t|".format(k, nach, kon, nach, f(nach), it,
                                                                                      err))
                print("-----------------------------------------------------------------")
                korni.append(kon)
            print("Время выполнения = ", t3)
            break
    return korni


# Метод Риддера
def comb(f, a, b, maxi, eps):

    if f1(a) != 0:
        if not a<a-f(a)/f1(a)<b:
            return None, None
    elif f1(b) != 0:
        if not a<b-f(b)/f1(b)<b:
            return None, None
    elif f1(a) == 0 and f1(b) == 0:
        return None, None

    # Вычисляем очередной x
    def get_x(f,a,b):
        x = a-f(a)*(a-b)/(f(a)-f(b))
        return x
    def get_x1(f,a):
        x = a-f(a)/f1(a)
        return x



    # цикл для определения корня с точностью eps
    k = 1
    while abs(a - b) > eps:

        # определяем новые границы интервала
        if f(a) * f2(a) < 0:
            a = get_x(f,a,b)
        elif f(a) * f2(a) > 0:
            a = get_x1(f,a)
        if f(b) * f2(b) < 0:
            b = get_x(f,b,a)
        elif f(b) * f2(b) > 0:
            b = get_x1(f,b)
        
        k += 1
        if k > maxi:
            return None, k
    return (a+b)/2, k

'''
a = float(input("Введите левую границу интервала: "))
b = float(input("Введите правую границу интервала: "))
h = float(input("Введите шаг: "))
eps = float(input("Введите точность eps: "))
maxi = float(input("Введите максимальное число итераций: "))
print("Метод половинного деления")

korni = find_roots(f,a,b,h,maxi,eps)
'''
korni = find_roots(f)
print('''
Список ошибок:
0 - нет оштбки
1 - количество итераций превысило максимально допустимое значение
''')




