from tkinter import *
from math import *

def line(b):
    if b[0]-b[2] == 0:
        return 'e','e'
    k = (b[1]-b[3])/(b[0]-b[2])
    a = b[3]-k*b[2]
    return k,a

"""
def peres(b,c):
    k,b = line(b)
    a = 1 + k**2                                                                                    
    b = -2*c[0] + 2*k*b -2*k*c[1]                                                         
    c = -c[2]**2 + b**2+c[0]**2-2*b*c[1] + c[1]**2                                                
    D = b**2 - 4*a*c
    print(D)
    if D < 0:                                                                                       
        return False
    else:
        return True 
"""
def peres(b,c):
    k,a = line(b)
    if k == 'e':
        if abs(abs(b[0]-c[0]) - c[2])<=1e-2:
            return True
        return False
    #print(k,' ',a)
    #a = a - (c[1]-c[0]*k)
    #print(a)
    #D = k*k +1
    #if a*a>c[2]*c[2]*D:
    #    return False
    #else:
    #    return True
    for i in range(c[0]-c[2],c[0]+c[2]+1):
        if sqrt(((k*i+a)-c[1])**2+(i-c[0])**2)-c[2]<=1e-2:
            return True
    return False
print(peres([0,100,700,500],[601,600,50]))

"""    
    #print(D)
    if D < 0:                                                                                       
        return False
    else:
        return True

    b1 =2*a*k-2*c[0]*k-2*c[1]
    a1 = k*k+1
    c1 = a*a-2*a*c[0]+c[0]*c[0]-c[2]*c[2]+c[1]*c[1]
    d1 = b1*b1-4*a1*c1
    if d1 >= 0:
        return True
    else:
        return False
"""

e = [[150,50,50],
     [350,100,50],
     [250,200,50],
     [100,50,50],
     [300,100,50],
     [400,200,50],
     [500,300,50],
     [550,340,50],
     [600,400,50],
     [700,500,50]]



a = [[200,0],
     [0,0],
     [50,230],
     [300,300],
     [130,700],
     [700,500]]


def tr(e,a):
    i = 0
    j = 0
    maxi = 0
    maxii = []
    for q in range(len(a)-1):
        for j in range(q+1,len(a)):
            k = 0
            b = []
            b.append(a[q][0])
            b.append(a[q][1])
            b.append(a[j][0])
            b.append(a[j][1])
            for i in e:
                res = peres(b,i)

                if res:

                    #w.create_line(b[0]*(-1000),b[1]*(-1000),b[2]*1000,b[3]*1000,width=3,fill="blue")
                    k+=1
                    
            if k > maxi:
                #w.create_line(b[0]*(-1000),b[1]*(-1000),b[2]*1000,b[3]*1000,width=3,fill="yellow")
                maxi = k
                maxii = b
                print(maxii)
    #if maxii:
    print(maxii)
    w.create_line(maxii[0],maxii[1],maxii[2],maxii[3],width=3,fill="black")        
        
                    




canvas_width = 700
canvas_height = 700

"""
n = int(input("Введите количетво точек: "))
print("Введите точки")
a = []
rt = 0
while True:
    if rt == n:
        break
    a1 = list(map(int,input().split()))
    a.append(a1)
    rt+=1

n1 = int(input("Введите количетво окружностей: "))
print("Введите окружности")

e = []
rt = 0
while True:
    if rt == n1:
        break
    e1 = list(map(int,input().split()))
    e.append(e1)
    rt +=1
 """

master = Tk()
master.title('Convex quadrangles')
w = Canvas(master,
           width = canvas_width,
           height = canvas_height)
w.pack(expand = YES, fill = BOTH)
for i in e:
    w.create_oval([i[0]-i[2],i[1]-i[2]],[i[0]+i[2],i[1]+i[2]],fill=None)
for i in a:
    w.create_oval([i[0]-2,i[1]-2],[i[0]+2,i[1]+2],fill='black')
#w.create_line(0,0,700,500,width=3,fill="black")
w.bind('<B1-Motion>', tr(e,a))
mainloop()

