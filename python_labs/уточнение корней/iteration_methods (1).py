# Sviridov Ilya IU7-23
# Iteration Algorithmes
import math as m
eps = 1e-3

# f(x)
def f(x):
    return m.sin(x)

#f'(x)
def f1(x):
    return m.cos(x)

#f''(x)
def f11(x):
    return -m.sin(x)

# fi(x)
def fi(lyambda, x):
    return x + lyambda * f(x)

# fi'(x)
def fid(lyambda, x):
    return 1 + lyambda * fd(x)

# Метод половинного деления+
def harf_shaping_method(a, b):
    x0 = a  # None
    while abs(b - a) > eps:
        x0 = a + (b - a)/2
        if a * x0 < 0:
            b = x0
        else:
            a = x0
    return x0

# Метод хорд+
def chords_method(a, b):
    k = 0
    while abs(b - a) > eps:
        a = b - (b - a) * f(b)/(f(b) - f(a))
        b = a + (a - b) * f(a)/(f(a) - f(b))
    # a - i-1, b - i-тый члены
    return b

# Метод Ньютона+
def newtons_method(a, b):
    x0 = None
    if f(a)*f11(a) > 0 :
        x0 = a
    else:
        x0 = b
    while abs(x1 - x0) < eps:
        x1 = x0 - (f(x0) / f1(x0))
        x0 = x1
    return x1        

# Упрощенный метод Ньютона+
def newtons_simple_method(a, b):
    x00 = None
    if f(a)*f11(a) > 0 :
        x00 = a
    else:
        x00 = b
    x0 = x00; x1 = x0 - f(x0)/f1(x00)
    while abs(x1 - x0):
        x0 = x1
        x1 = x0 - f(x0)/f1(x00)   
    return x1
        
# Метод секущих(модификация метода Ньютона)+
def secant_method(a, b):
    x0 = (b - a)/2
    x1 = x0 - eps
    x2 = x1 - (x1 - x0)*f(x1) / (f(x1) - f(x0))
    while abs(x1 - x0) > eps:
        tmp2 = x2
        x0 = x1
        x1 = tmp2
        x2 = x1 - (x1 - x0)*f(x1) / (f(x1) - f(x0))
    return x2    

# Комбинированный метод (x0 = (b-a)/2+
def combine_method(a, b):
    x0 = (b - a)/2
    x1 = x0 - eps
    x2 = x1 - (x1 - x0)*f(x1) / (f(x1) - f(x0))
    while abs(x2 - x1) > eps:
        tmp2 = x2
        x0 = x1
        x1 = tmp2
        x2 = x1 - (x1 - x0)*f(x1) / (f(x1) - f(x0))
    return x2

# Метод Стеффенсона
def Steffenson_method(a, b):
    x0 = ????
    while abs(x1 - x0) > eps:
        x0 = x1
        x1 = x0 - m.pow(f(x0), 2) / (f(x0 + f(x0)) - f(x0))
        return x1
   

# МПИ+
def msi(x0, ly):
    x1 = fi(fi_lyambda(x0), x0) 
    while abs(x1 - x0) > eps:
        x0 = x1
        x1 = fi(fi_lyambda(x0), x0)       
    return x1

# lyambda: на [Xn, Xn1] |fi'(x)| < 1+
def fi_lyambda(x0):  # x*
    ly0 = -1; h = abs(2*ly0)/10  # Шаг h на [ly0, -ly0]
    p = 2; eps = 1e-5                                        
    ly = ly0
    # |fi'(x)| <= 1    
    while abs(fid(ly, x0)- eps) >= 1 and abs(
        fid(ly, x0)+ eps) >= 1:  
        if ly >= abs(ly0):  # >= -ly0
            ly0*= p;
            h = abs(2*ly0)/10
            ly = ly0
        if abs(ly) > eps:
            ly+= 2*h
        else:
            ly+= h
    return ly 





    
