from math import *
import numpy as np
import matplotlib.pyplot as plt
import time


# Задаваемая функция
def f(x):
    g = x * x - 5
    return g


def f1(x):
    g = 2 * x
    return g


def f2(x):
    g = 2
    return g


# Осуществляем поиск корней
def find_roots(f, a=0, b=10, h=3, maxi=100, eps=1e-7):
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
        if f(nach) == 0:
            k += 1
            it = 0
            err = 0
            print(
            "|{:3d}|{:7.2f}|{:7.2f}|{:9.4f}\t|{:7.3e}\t|{:3d}\t |{:3d}\t|".format(k, nach, kon, nach, f(nach), it, err))
            print("-----------------------------------------------------------------")
            korni.append(nach)

        if f(nach) * f(kon) < 0:

            # Вызываем метод уточнения корней: ridder
            t = time.clock()
            r, it = ridders_method(f, nach, kon, maxi, eps)
            t2 = time.clock() - t
            t3 += t2
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
                korni.append(r)
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
def ridders_method(f, a, b, maxi, eps):
    # Функция которая определяет знак в выражении функциии get_x
    def sign(q1, q2):
        if q1 - q2 < 0:
            return -1
        elif q1 - q2 > 0:
            return 1
        else:
            return 0

    # Вычисляем очередной x
    def get_x(f, a, b):
        c = (a + b) / 2
        x = c + (c - a) * (sign(f(a), f(b)) * f(c)) / sqrt(f(c) * f(c) - f(a) * f(b))
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


# a = float(input("Введите левую границу интервала: "))
# b = float(input("Введите правую границу интервала: "))
# h = float(input("Введите шаг: "))
# eps = float(input("Введите точность eps: "))
# maxi = float(input("Введите максимальное число итераций: "))
print("Метод Риддера")

# korni = find_roots(f,a,b,h,maxi,eps)
korni = find_roots(f)
korni1 = find_roots(f1)
korni2 = find_roots(f2)

print('''
Список ошибок:
0 - нет оштбки
1 - количество итераций превысило максимально допустимое значение
''')

x = np.linspace(0, 10, 100)
y = [f(i) for i in x]
zn_k = [f(i) for i in korni]
zn_k1 = [f(i) for i in korni1 if f2(i) != 0]
zn_k2 = [f(i) for i in korni2]
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
# plt.legend(loc = 'best')
plt.grid()

plt.subplot(221)
plt.plot(x, y, 'g-')
plt.title('sin(x)')

plt.subplot(222)
plt.plot(x, y, 'g-')
plt.plot(korni, zn_k, 'b.')
plt.title('Корни sin(x)')

plt.subplot(223)
plt.plot(x, y, 'g-')
plt.plot(korni1, zn_k1, 'm.')
plt.title('Экстремум sin(x)')

plt.subplot(224)
plt.plot(x, y, 'g-')
plt.plot(korni2, zn_k2, 'k.')
plt.title('Точки перегиба sin(x)')

plt.show()



