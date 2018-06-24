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

                # Вызываем метод уточнения корней:
                t = time.clock()
                r, it = sek(f, nach, kon, maxi, eps)
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


# Метод секущих
def sek(f, a, b, maxi, eps):
    a1 = a
    b1 = b
    def get_x(f,a,b):
        x = b - ((b-a)/(f(b)-f(a)))*f(b)
        return x

    # Вычисляем очередной x
    
    # начальный x
    if f(a)-f(b) != 0:
        if a1 < get_x(f,a,b) < b1:
            x2 = get_x(f, a,b)  # очередной x
        elif a1 < get_x(f,b,a) < b1:
            x2 = get_x(f, b,a)  # очередной x
        else:
            return None, None
    else:
        return None, None
        

    # цикл для определения корня с точностью eps
    k = 1
    while abs(x2 - b) > eps:
        a = b
        b = x2
        if f(a)-f(b) != 0:
            if a1 < get_x(f,a,b) < b1:
                x2 = get_x(f, a,b)  # очередной x
            elif a1 < get_x(f,b,a) < b1:
                x2 = get_x(f, b,a)  # очередной x
            else:
                return None, None
        else:
            return None, None
        k += 1
        if k > maxi:
            return None, k
    return x2, k

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























