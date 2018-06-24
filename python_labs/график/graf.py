n, sh, k = map(float,input('Введите начальное значение, шаг последовательности и конечное значение: ').split())
print('\n\t  Y\t  ',' X\t\t ','N')
l = n
e = 1
while True:
    l1 = round(l,5)
    k1 = round(k,5)
    if l1 <= k1:
        w = 2048*l**12-6144*l**10+6912*l**8-3584*l**6+840*l**4-72*l**2+1
        print('\t{:7.3f}\t'.format(w),'{:7.3f}\t'.format(l),'{:2d}'.format(e))
        l += sh
        e += 1
    else:
        break  
print('\n\n')
print('График функции: y = 2048*x^12-6144*x^10+6912*x^8-3584*x^6+840*x^4-72*x^2+1')
print('\n\n')
max = 2048*n**12-6144*n**10+6912*n**8-3584*n**6+840*n**4-72*n**2+1
min = 2048*n**12-6144*n**10+6912*n**8-3584*n**6+840*n**4-72*n**2+1
l = n
dlina = round(l, 4)
maxdl = len(str(dlina))
while l<k+sh:
    if 2048*l**12-6144*l**10+6912*l**8-3584*l**6+840*l**4-72*l**2+1 > max:
        max = 2048*l**12-6144*l**10+6912*l**8-3584*l**6+840*l**4-72*l**2+1
    if 2048*l**12-6144*l**10+6912*l**8-3584*l**6+840*l**4-72*l**2+1 < min:
        min = 2048*l**12-6144*l**10+6912*l**8-3584*l**6+840*l**4-72*l**2+1
    l += sh
    dlina = round(l, 4)
    if len(str(dlina)) > maxdl:
        maxdl = len(str(dlina))

dl = (max-min)/70
zero = False
if min < 0 and max > 0:
    zero = True

print('{:.4f}'.format(min), end='')
min1 = round(min,4)
for i in range(68-len(str(min1))):
    print(' ', end='')
print('{:.4f}'.format(max))

print('+', end='')
for i in range(70):
    print('-', end='')
print('+    X\t    N')

q1 = 0
if zero:
    q1 = round((0-min)/dl)
    min1 = round(min,4)
    for i in range(q1+1):
        print(' ', end='')
    print('0')
    
l = n
e = 1
p = 2
while True:
    l1 = round(l,5)
    k1 = round(k,5)
    if l1 <= k1:
        w = 2048*l**12-6144*l**10+6912*l**8-3584*l**6+840*l**4-72*l**2+1
        q = round((w-min)/dl)
        print(' ',end='')
        x = 0
        while True:
            if x > 70:
                print('', end=' ')
                break
            else:
                if x == q1:
                    print('|', end='')
                if x == q:
                    print('*', end='')
                else:
                    print(' ', end='')
            x += 1
        if p == e:
            if l>=0:
                print(' ',end='')
            print(' {:.3f} '.format(l), end=' ')
            print('{:2d}'.format(p), end='\n')
            p += 2
        else:
            print('',end='\n')
        
        e += 1
        l += sh
    else:
        break
