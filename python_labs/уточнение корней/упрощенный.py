from math import *
import numpy as np


def f(x):
    g = sin(x)
    return g


def f1(x):
    g = cos(x)
    return g



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
        if abs(f(nach))<1e-7:
            k += 1
            it = 0
            err = 0
            print("|{:3d}|{:7.2f}|{:7.2f}|{:9.4f}\t|{:7.3e}\t|{:3d}\t |{:3d}\t|".format(k, nach, kon, nach, f(nach), it, err))
            print("-----------------------------------------------------------------")
            
                
        elif abs(f(kon)) > 1e-7:

            if f(nach) * f(kon) < 0:

                # Вызываем метод уточнения корней: Ньютона

                r, it = Kasat(f, nach, kon, maxi, eps)
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
                "|{:3d}|{:7.2f}|{:7.2f}|{:9.4f}\t|{:7.3e}\t|{:3d}\t |{:3d}\t|".format(k, nach, kon, nach, f(nach), it,err))
                print("-----------------------------------------------------------------")

            break


# Метод Ньютона
def Kasat(f, a, b, maxi, eps):
    if f1(a) != 0:
        if not a<a-f(a)/f1(a)<b:
            return None, None
    elif f1(b) != 0:
        if not a<b-f(b)/f1(b)<b:
            return None, None
    elif f1(a) == 0 and f1(b) == 0:
        return None, None
    
    # Вычисляем очередной x
    def get_x(f,a,osn):
        x = a-f(a)/f1(osn)
        return x

    x1 = 0  # начальный x
    if a<a-f(a)/f1(a)<b:
        osn = a
        x2 = get_x(f, a,osn)  # очередной x
        
    elif a<b-f(b)/f1(b)<b:
        osn = b
        x2 = get_x(f,b,osn)  # очередной x
        


    # цикл для определения корня с точностью eps
    k = 1
    while abs(x2 - x1) > eps:
        x1 = x2
        # определяем новые границы интервала
        x2 = get_x(f,x1,osn)
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
'''
#korni = find_roots(f,a,b,h,maxi,eps)
korni = find_roots(f)
print('''
Список ошибок:
0 - нет оштбки
1 - количество итераций превысило максимально допустимое значение
2 - На данном интервале методом Ньютона нельзя посчитать корни,
так как касательные в крайних точках этого интервала пересекают ось x вне этого интервала
''')




