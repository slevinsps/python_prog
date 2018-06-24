from tkinter import *
from random import *
from math import *

canvas_width = 500
canvas_height = 500


def pol_otr(xA, yA, xB, yB, xT, yT):

    if (xA-xB) == 0:
        if xT > xA:
            rc = 1
        elif xT < xA:
            rc = -1
        else: rc = 0
        return rc
    else:
        k = (yA-yB)/(xA-xB)
        a = yB-k*xB
        if yT > k*xT+a:
            rc = 1
        elif yT < k*xT+a:
            rc = -1
        else: rc = 0
        return rc
    """
    if (xB-xA)*(yT-yA)<(yB-yA)*(xT-xA):
        rc = 1
    elif (xB-xA)*(yT-yA)>(yB-yA)*(xT-xA):
        rc = -1
    else: rc = 0
    return rc
    """


def points(w, x, y):
    n = len(x)
    minPoint = x[0]**2 + y[0]**2 
    minI = 0
    maxPoint = x[0]**2 + y[0]**2 
    maxI = 0
    python_green = "#FF0000"
    for i in range (n):
        x1, y1 = (x[i] - 3), (y[i] - 3)
        x2, y2 = (x[i] + 3), (y[i] + 3)
        w.create_oval(x1, y1, x2, y2, fill = python_green)
    fl = 0
    for i in range (n):
        for j in range (n):
            pol = 0
            otr = 0
            for k in range (n):
                if pol_otr(x[i],y[i],x[j],y[j],x[k],y[k])>0:
                    pol+=1;
                elif pol_otr(x[i],y[i],x[j],y[j],x[k],y[k])<0:
                    otr+=1;
            if (((n%2==0) and (pol==otr)) or ((n%2==1) and (abs(pol-otr)<2))) and (pol!=0):
                fl = 1;
                minI = i
                maxI = j
                break
        if fl==1:
            break
        
    k = (y[minI]-y[maxI])/(x[minI]-x[maxI])
    aa = y[maxI] - k*x[maxI]
    w.create_line(-1000*x[maxI], aa-k*1000*x[maxI],1000*x[minI],aa+k*1000*x[minI],width=2)



x1 = []
y1 = []
r1 = int(input("Введите количество точек: "))
for i in range(r1):
    x11,y11 = map(int,input().split())
    x1.append(x11)
    y1.append(y11)
    

master = Tk()
master.title('Точки и прямая')
w = Canvas(master,
           width = canvas_width,
           height = canvas_height)
w.pack(expand = YES, fill = BOTH)
w.bind('<B1-Motion>', points(w, x1, y1))

mainloop()




























































