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
            s2 += f(x)
        else:
            s1 += f(x)
    t = (3*h/8)*(3*s1+2*s2+f(a)+f(b))
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

    for i in range(n):
        x = a + i * h
        s += f(x)*h
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
    s = f(a)+f(b)
    for i in range(1,n):
        x = a+i*h
        t = f(x)
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

def int_weddla(a,b,n):
    h = (b-a)/n
    s = f(a)+f(b)
    for i in range(1,n,6):
            s += 5*f(a+i*h) + f(a+(i+1)*h) + 6*f(a+(i+2)*h)+f(a+(i+3)*h) + 5*f(a+(i+4)*h) +2*f(a+(i+5)*h)
    s -= 2*f(b)        
    s = (3*h/10)*s
   
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
print('Метод левых\t\t\t','{:7.5f}'.format(int_left(a,b,n1)),'\t','{:7.5f}'.format(int_left(a,b,n2)))
print('Метод средних\t\t\t','{:7.5f}'.format(int_mid(a,b,n1)),'\t','{:7.5f}'.format(int_mid(a,b,n2)))
print('Метод трапеций\t\t\t','{:7.5f}'.format(int_trap(a,b,n1)),'\t','{:7.5f}'.format(int_trap(a,b,n2)))
print('Метод парабол\t\t\t','{:7.5f}'.format(int_par(a,b,n1)),'\t','{:7.5f}'.format(int_par(a,b,n2)))
print('Метод Буля\t\t\t','{:7.5f}'.format(int_bool(a,b)),'\t','{:7.5f}'.format(int_bool(a,b)))
print('Метод Уэдля\t\t\t','{:7.5f}'.format(int_weddla(a,b,n1)),'\t','{:7.5f}'.format(int_weddla(a,b,n2)))


