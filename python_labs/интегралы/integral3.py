# Спасенов Иван ИУ7-13
# Вычисление интегралов методом правых прямоугольников и 3/8

from math import *
def f(x):
    g = x*x
    return g

def int_3(a,b,n):
    h=(b-a)/n
    s1 = 0
    s2 = 0
    for i in range(1,n):
        x = a+i*h
        if i%3 == 0:
            s2 += 2*f(x)
        else:
            s1 += 3*f(x)
    t = (3*h/8)*(s1+s2+f(a)+f(b))
    return t

def int_right(a,b,n):
    h=(b-a)/n
    s = 0
    for i in range(1,n+1):
        x = a+i*h
        s += f(x)*h
    return s

def int_left(a,b,n):
    h=(b-a)/n
    s = 0
    x = a
    for i in range(1,n):
        s += f(x)*h
        x += i*h
    return s

def int_mid(a,b,n):
    h=(b-a)/n
    s = 0
    for i in range(1,n+1):
        x = a+i*h-h/2
        s += f(x)*h
    return s

def int_trap(a,b,n):
    h=(b-a)/n
    s = 0
    for i in range(1,n):
        x = a+i*h
        s += f(x)
    s = h*(s+(f(a)+f(b))/2)
    return s


def int_par(a,b,n):
    h=(b-a)/n
    s = f(a)
    for i in range(1,n+1):
        x = a+i*h
        t = f(x)
        if i == 1:
            t = -t
        if i % 2 == 0:
            t = t*2
        else:
            t= 4*t
        s += t
    s = (h/3)*s
    return s


def int_bool(a,b):
    h=(b-a)/4
    s = (2/45)*h*(7*f(a)+32*f(h+a)+12*f(2*h+a)+32*f(3*h+a)+7*f(b))
    return s

a = float(input('Введите начальное значение a: '))
b = float(input('Введите начальное значение b: '))
n1 = int(input('Введите n1 разбиений: '))
n2 = int(input('Введите n2 разбиений: '))
print()
print('\tМетод\t\t\t n1=',n1,'\t n2=',n2)
s1 = int_right(a,b,n1)
s2 = int_right(a,b,n2)
print('Метод правых прямоугольников\t','{:7.5f}'.format(s1),'\t','{:7.5f}'.format(s2))
s3 = int_3(a,b,n1)
s4 = int_3(a,b,n2)
print('Метод 3/8\t\t\t','{:7.5f}'.format(s3),'\t','{:7.5f}'.format(s4))
print('Метод левых\t\t\t','{:7.5f}'.format(int_right(a,b,n1)),'\t','{:7.5f}'.format(int_right(a,b,n2)))
print('Метод средних\t\t\t','{:7.5f}'.format(int_mid(a,b,n1)),'\t','{:7.5f}'.format(int_mid(a,b,n2)))
print('Метод трапеций\t\t\t','{:7.5f}'.format(int_trap(a,b,n1)),'\t','{:7.5f}'.format(int_trap(a,b,n2)))
print('Метод парабол\t\t\t','{:7.5f}'.format(int_par(a,b,n1)),'\t','{:7.5f}'.format(int_par(a,b,n2)))
print('Метод Буля\t\t\t','{:7.5f}'.format(int_bool(a,b)),'\t','{:7.5f}'.format(int_bool(a,b)))


