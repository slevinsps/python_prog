def quicksort(a,l,r):
    i = l
    j = r
    x = a[(l+r)//2]
    while True:
        while a[i]<x:
            i+=1
        while a[j]>x:
            j-=1
        if i<=j:
            a[i],a[j] = a[j],a[i]
            i+=1
            j-=1
        if i>=j:
            break
    if l<j:
        quicksort(a,l,j)
    if r>i:
        quicksort(a,i,r)


def sheiker(a):
    l = 1
    r = len(a)-1
    while l<=r:
        for i in range(l,r+1):
            if a[i-1]>a[i]:
                a[i-1],a[i] = a[i],a[i-1]
        r-=1
        for i in range(r,l-1,-1):
            if a[i-1]>a[i]:
                a[i-1],a[i] = a[i],a[i-1]
        l+=1
        
def shell(a):
    s = len(a)//2
    while s > 0:
        for i in range(s,len(a)):
            x = a[i]
            j = i-s
            
            while x<a[j]:
                a[j+s] = a[j]
                j-=s

                if j<0:
                    break
            a[j+s] = x
        s//=2

     
    

def binary(a):
    for i in range(1,len(a)):
        l = 0
        r = i-1
        x = a[i]
        while l<=r:
            m = (l+r)//2
            if a[m]>x:
                r = m-1
            else:
                l = m+1
        x = a[i]
        for j in range(i-1,l-1,-1):
            a[j+1] = a[j]
        a[l] = x

def prost_vibor(a):
    for i in range(0,len(a)-1):
        mini = i
        for j in range(i+1,len(a)):
            if a[j]<a[mini]:
                mini = j
        a[mini],a[i] = a[i],a[mini]


def bubble_sort(a):
    for i in range(1,len(a)):
        for j in range(len(a)-1,i-1,-1):
            if a[j-1]<a[j]:
                a[j-1],a[j] = a[j],a[j-1]

def bubble_sort_best(a):
    for i in range(1,len(a)):
        p = True
        for j in range(len(a)-1,i-1,-1):
            if a[j-1]>a[j]:
                a[j-1],a[j] = a[j],a[j-1]
                p = False
        if p:
            break

def prost_vstavk(a):
    for i in range(1,len(a)):
        x = a[i]
        j = i-1
        while j>-1 and x < a[j]:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = x

print('Введите массив:')
#a = list(map(int,input().split()))
a = [3,2,1]
b = [9,6,-1,0,4,7,12,2,-1]

#prost_vstavk(b)
#bubble_sort(a)
#bubble_sort_best(b)
#prost_vibor(a)
#binary(a)
#shell(a)
#sheiker(a)
#quicksort(a,0,len(a)-1)
print(b)
