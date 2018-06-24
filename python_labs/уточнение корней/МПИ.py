from math import *
import numpy as np
import matplotlib.pyplot as plt
import time


# Задаваемая функция
# f(x)
def f(x):
    return sin(x)

#f'(x)
def f1(x):
    return cos(x)

#f''(x)
def f11(x):
    return -sin(x)

# fi(x)
def fi(lyambda, x):
    return x + lyambda * f(x)

# fi'(x)
def fid(lyambda, x):
    return 1 + lyambda * fd(x)


# Осуществляем поиск корней
def find_roots(f, a=-10, b=10, h=0.01, maxi=1000, eps=1e-7):
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
                it = 1
                r = comb(f, nach, kon, maxi, eps)
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


# Метод МПИ
def comb(f, a, b, maxi, eps):
    #if not a<=a-f(a)/f1(a)<=b or not a<=b-f(b)/f1(b)<=b:
    #    return None, None
    


    # lyambda: на [Xn, Xn1] |fi'(x)| < 1+
    def fi_lyambda(x0):  # x*
        ly0 = -1; h = abs(2*ly0)/10  # Шаг h на [ly0, -ly0]
        p = 2; eps = 1e-5                                        
        ly = ly0
        # |fi'(x)| <= 1    
        while abs(fid(ly, x0)- eps) >= 1 and abs(fid(ly, x0)+ eps) >= 1:  
            if ly >= abs(ly0):  # >= -ly0
                ly0*= p;
                h = abs(2*ly0)/10
                ly = ly0
            if abs(ly) > eps:
                ly+= 2*h
            else:
                ly+= h
        return ly
    
    def msi(x0, ly):
        x1 = fi(fi_lyambda(x0), x0) 
        while abs(x1 - x0) > eps:
            x0 = x1
            x1 = fi(fi_lyambda(x0), x0)       
        return x1    

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


def fixedp(f,x0,tol=10e-5,maxiter=100):
 """ Fixed point algorithm """
 e = 1
 itr = 0
 xp = []
 while(e > tol and itr < maxiter):
  x = f(x0)      # fixed point equation
  e = abs(x0-x) # error at the current step
  x0 = x
  xp.append(x0)  # save the solution of the current step
  itr = itr + 1
 return x,xp




