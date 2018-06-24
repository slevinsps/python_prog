# Спасенов Иван ИУ7-13
# Вариант 2


def per(a):

    ki = -1
    k = -1
    for i in range(1,len(a)-1):
        if a[i-1]<a[i]:
            if a[i-1]<=a[i+1]<a[i]:
                ki = i-1
                k = a[i-1]
            elif a[i+1]<a[i-1]:
                ki = i
                k = a[i]
            break
    if ki == -1 and k == -1:
        if a[0]<a[1]:
            ki = 0
            k = a[0]
        elif a[len(a)-1]>a[len(a)-2]:
            ki = len(a)-1
            k = a[ki]
        else:
            return a


    for i in range(len(a)):
        if a[i]<k:
            hi = i-1
            break

    if ki < hi:
        for i in range(ki, hi):
            c = a[i]
            a[i] = a[i + 1]
            a[i + 1] = c
    elif ki > hi:
        for i in range(ki, hi + 1, -1):
            c = a[i]
            a[i] = a[i - 1]
            a[i - 1] = c
    return a

a = [123,50,25,12,7,600]
print('Исходная последовательность:')
for i in a:
    print(i,end = ' ')
print()
print('Измененная последовательность:')
a = per(a)
for i in a:
    print(i,end = ' ')
