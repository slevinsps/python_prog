from math import *
import numpy as np
import matplotlib.pyplot as plt
import time


# Задаваемая функция
def f(x):
    g = x*x*sin(x)
    return g


def f1(x):
    g = cos(x)
    return g


def f2(x):
    g = -sin(x)
    return g


# Осуществляем поиск корней
def find_roots(f, a=-10, b=10, h=0.1, maxi=100, eps=1e-7):
    t3 = 0
    print("-----------------------------------------------------------------")
    print("| № |  X(n) | X(n+1)|     X     |    f(X)       | число  |код   |")
    print("|   |       |       |           |               |итераций|ошибки|")
    print("-----------------------------------------------------------------")
    k = 0
    nach = a
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

        else:

            if f(nach) * f(kon) < 0:

                # Вызываем метод уточнения корней
                r, it = PolovDel(f, nach, kon, maxi, eps)
                k += 1
                if r == None:
                    err = 1
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

            print("Время выполнения = ", t3)
            break



# Метод половинного деления
def PolovDel(f, a, b, maxi, eps):

    # Вычисляем очередной x
    def get_x(f, a, b):
        x = (a + b) / 2
        return x

    x1 = 0  # начальный x
    x2 = get_x(f, a, b)  # очередной x

    # цикл для определения корня с точностью eps
    k = 1
    while abs(x2 - x1) > eps:
        x1 = x2
        # определяем новые границы интервала
        if f(a) * f(x2) < 0:
            b = x2
        elif f(x2) * f(b) < 0:
            a = x2
        x2 = get_x(f, a, b)
        k += 1
        if k > maxi:
            return None, k
    return x2, k


a = float(input("Введите левую границу интервала: "))
b = float(input("Введите правую границу интервала: "))
h = float(input("Введите шаг: "))
eps = float(input("Введите точность eps: "))
maxi = float(input("Введите максимальное число итераций: "))
print("Метод половинного деления")

korni = find_roots(f,a,b,h,maxi,eps)


print('''
Список ошибок:
0 - нет оштбки
1 - количество итераций превысило максимально допустимое значение
''')




