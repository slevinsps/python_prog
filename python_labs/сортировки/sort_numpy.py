import numpy as nm
from random import *
import time

print('Количество элементов   Время выполнения')
a = []
el = 1000
for i in range(el):
    a.append(randint(-300,300))
t = time.clock()
a = nm.sort(a,kind='heapsort')
t2 = time.clock() - t
print("{:12d}   {:17.2f}".format(el,t2*1000))

a = []
el = 10000
for i in range(el):
    a.append(randint(-300,300))
t = time.clock()
a = nm.sort(a,kind='heapsort')
t2 = time.clock() - t
print("{:12d}   {:17.2f}".format(el,t2*1000))

a = []
el = 100000
for i in range(el):
    a.append(randint(-300,300))
t = time.clock()
a = nm.sort(a,kind='heapsort')
t2 = time.clock() - t
print("{:12d}   {:17.2f}".format(el,t2*1000))

a = []
el = 1000000
for i in range(el):
    a.append(randint(-300,300))
t = time.clock()
a = nm.sort(a,kind='heapsort')
t2 = time.clock() - t
print("{:12d}   {:17.2f}".format(el,t2*1000))
