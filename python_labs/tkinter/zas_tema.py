#Защита Доктора Артёма
#Графика

from tkinter import *
from random import *

def create_array(n):
    array = []
    for i in range (n):
        array.append(randint(40, 400));
    return array

def is_in(xA, yA, xB, yB, xT, yT):
    if (xB - xA) * (yT - yA) < (yB - yA) * (xT - xA):
        rc = 1
    elif (xB - xA) * (yT - yA) > (yB - yA) * (xT - xA):
        rc = -1
    else: rc = 0
    return rc
   
def build_all(w, len1, len2, x, y, xr, yr):
    n1 = len(x)
    n2 = len(xr)
    for i in range (n2):
        xr1, yr1 = (xr[i] - len2), (yr[i] - len2)
        xr2, yr2 = (xr[i] + len2), (yr[i] + len2)
        w.create_oval(xr1, yr1, xr2, yr2)
    for i in range (n1):
        x1, y1 = (x[i] - len1), (y[i] - len1)
        x2, y2 = (x[i] + len1), (y[i] + len1)
        w.create_oval(x1, y1, x2, y2, fill = "#FF0000")
    maxkolvo = -1
    iA = 0
    iB = 1
    for i in range (n1):
        for j in range (n1):
            kolvo = 0
            for k in range (n2):
                bool = 0
                for p in range(-(length-2), (length-2)):
                    for f in range(-(length-2), (length-2)):
                        if (is_in(x[i], y[i], x[j],
                                    y[j], xr[k] + p, yr[k] + f) == 0):
                            bool=1
                            kolvo+=1
                            break
                    if bool:
                        break
            if kolvo > maxkolvo and i != j:
                maxkolvo = kolvo
                iA = i
                iB = j
    #print(y[iA],y[iB],x[iA],x[iB],iA,iB, maxkolvo)
    if ((x[iA]-x[iB])==0):
        k = 0
    else:
        k = (y[iA]-y[iB])/(x[iA]-x[iB])
    aa = y[iB] - k*x[iB]
    if k == 0:
        w.create_line(x[iA], 0, x[iB], 1000, width = 2)
    else:
        w.create_line(-1000 * x[iB], aa - k * 1000 * x[iB],
                  1000 * x[iA], aa + k * 1000 * x[iA], width = 2)
    print( 'Количество пересечений:', maxkolvo)
    

canvas_width = 500
canvas_height = 500

#x=[0,10,57,76,31]
#y=[68,10,17,176,256]
#xr=[15,80,77,26,311]
#yr=[289,140,175,16,56]
x=[]
y=[]
xr=[]
yr=[]

kolvo= int(input("Введите количество точек: "))
for i in range (kolvo):
    x1 = int(input('Координата x (точка '+str(i+1)+"): "))
    x.append(x1)
    y1 = int(input('Координата y (точка '+str(i+1)+"): "))
    y.append(y1)

kolvo1= int(input("Введите количество окружностей: "))
for i in range (kolvo1):
    xr1 = int(input('Координата x (центр окружности '+str(i+1)+"): "))
    xr.append(xr1)
    yr1 = int(input('Координата y (центр окружности '+str(i+1)+"): "))
    yr.append(yr1)

length = int(input("Введите радиус: "))

n1 = len(x)
n2 = len(xr)

print( 'Здесь ' + str(n1) + ' точек и '+ str(n2) +' окружностей')

master = Tk()
master.title('Points, circles and one line')
w = Canvas(master, width = canvas_width, height = canvas_height)
w.pack(expand = YES, fill = BOTH)
w.bind('<B1-Motion>', build_all(w, 2, length, x, y, xr, yr))

mainloop()
#tema_lox
