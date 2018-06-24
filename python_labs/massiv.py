"""# Вводим массив в разных строках
n = int(input('Введите кол-во элементов: '))
x = [0]*n
for i in range(n):
    print('x[',i+1,'] = ',end='')
    x[i] = int(input())
print(x)

# Вводим массив прикольным способом, но неудобным
l = [0]*n
l = [int(input()) for i in range(n)]
print(l)

# Выводим массив столбиком
m = input('Введите символы в строке\n').split()
for a in m:
    print(a)

c = list(map(int, input().split()))
print(c)

#Максимальное значение разными способами
x = list(map(int,input().split()))
xmax = x[0]
for a in x:
    if a > xmax:
        xmax = a
print(xmax)
print()

nmax = 0
for a in range(1,len(x)):
    if x[a] > x[nmax]:
        nmax = a
print(nmax, x[nmax])
print()

xmax = max(x)
nmax = x.index(xmax)
print(nmax, x[nmax])

# Поиск
print('Введите массив')
x = list(map(int,input().split()))
a = int(input('Введите число, которое хотите найти: '))
k = 0
while x[k] != a and k<len(x):
    k += 1
if k == len(x):
    print('Такого элемента не существует')
else:
    print(k+1)
print()


if a in x:
    print(x.index(a))
else:
    print('Такого элемента не существует')
print()

for i in range(len(x)):
    if a == x[i]:
        print(i)
        break
else:
    print('Такого элемента не существует')

print('Введите массив')
x = list(map(int,input().split()))
a = int(input('Введите число, которое хотите найти: '))
l = 0
r = len(x)
while l < r-1:
    t = (r+l)//2
    if a<x[t]:
        r = t
    else:
        l = t
if x[l] == a:
    print(l)
else:
    print('Такого элемента не существует')
    
a=[]
for i in range(int(input('Введите число элементов: '))):
    a.append(int(input()))
print(a)
for i in range(len(a)):
    if (i+1) % 3 == 0:
        print(a[i])
    else:
        print(a[i],end=' ')

# слияние масивов
print('Введите массив 1')
x = list(map(int,input().split()))
print('Введите массив 2')
y = list(map(int,input().split()))
n = len(x)
m = len(y)
k = [0]*(m+n)
i = 0
j = 0
while i<=n-1 and j<=m-1:
    if x[i]<=y[j]:
        k[i+j] = x[i]
        i+=1
    else:
        k[i+j] = y[j]
        j+=1
while i<=n-1:
    k[m+i] = x[i]
    i+=1
while j<=m-1:
    k[n+j] = x[i]
    j+=1
print(k)
  

print('Введите массив 1')
x = list(map(int,input().split()))
print('Введите массив 2')
y = list(map(int,input().split()))
n = len(x)
m = len(y)
k = [0]*(m+n)
i = 0
j = 0
if x[n-1]<y[m-1]:
    x.append(y[m-1]+1)
else:
    y.append(x[n-1]+1)
for q in range(n+m):
    if x[i]<=y[j]:
        k[q] = x[i]
        i+=1
    else:
        k[q] = y[j]
        j+=1
print(k)

"""
# Сдвиги
x = list(map(int,input().split()))
f = input()
if f == 'l':
    g = x[0]
    for i in range(1,len(x)-1,1):
        x[i-1] = x[i]
    x[len(x)-1] = g
if f == 'r':
    g = x[len(x)-1]
    for i in range(len(x)-2,0,-1):
        x[i+1] = x[i]
    x[0] = g
print(x)

w = int(input('VALUE'))
pos = int(input('POS'))
x.append(0)
for i in range(len(x)-1,pos,-1):
    x[i] = x[i-1]
x[pos] = w
print(x)
for i in range(len(x)-2,0,-1):
    print(i)
