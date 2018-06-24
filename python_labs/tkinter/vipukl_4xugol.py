# Спасенов Иван ИУ7-13
# Выписать точки,  области которых находятся остальные точки
from tkinter import *
from math import sqrt


def udalenie(a):
    b = True
    while b:
        for i in a:
            if a.count(i)!=1:
                a.remove(i)
                break
        b = False
    
# Функция, которая считает угол между векторами
def ugol(a1, a2, a3):
    k1 = [a3[0] - a2[0], a3[1] - a2[1]]
    k2 = [a1[0] - a2[0], a1[1] - a2[1]]
    u = (k1[0] * k2[0] + k1[1] * k2[1]) / (sqrt(k1[0] ** 2 + k1[1] ** 2) * (sqrt(k2[0] ** 2 + k2[1] ** 2)))
    return u

def opred_vip(a):
    min_ld = a[0]  
    # Самая нижняя левая точка
    for i in range(len(a)):
        if a[i][1] < min_ld[1]:
            min_ld = a[i]
        elif a[i][1] == min_ld[1]:
            if a[i][0] < min_ld[0]:
                min_ld = a[i]
    
    # Три точки по которым считаем угол между векторами
    x3 = []
    x2 = min_ld
    x1 = [min_ld[0] - 10, min_ld[1]]
    
    
    q = []  
    q.append(min_ld)
    
    # Массив углов между векторами
    ug = [0] * (len(a))
    u1 = None
    # Находим нужные точки
    while True:
        for i in range(len(a)):
            if a[i] != x2 and a[i] != x1:
                ug[i] = ugol(a[i], x2, x1)
                if not u1:
                    u1 = round(ug[i],11)
                else:
                    if u1 != round(ug[i],11):
                        u1 = round(ug[i],11)
                    else:
                        return(5,5)
            elif a[i] == x2 or a[i] == x1:
                ug[i] = 2
        x3 = a[ug.index(min(ug))]
        if x3 == min_ld:
            break
        x1 = x2
        x2 = x3
        q.append(x3)
        ug = [0] * (len(a))
    

    return(len(q),q)

# Функция, поиска точек и вывода на экран многоугольнинков
def tr(a):
    global k15
    for i in range(len(a)-3):
        for j in range(i+1,len(a)-2):
            for k in range(j+1,len(a)-1):
                for r in range(k+1,len(a)):
                    a1 = [a[i],a[j],a[k],a[r]]
                
                    q,t = opred_vip(a1)
                    if q == 4:
                        w.create_line(t[0][0],t[0][1],t[1][0],t[1][1],width=3,fill="black")
                        w.create_line(t[1][0],t[1][1],t[2][0],t[2][1],width=3,fill="black")
                        w.create_line(t[2][0],t[2][1],t[3][0],t[3][1],width=3,fill="black")
                        w.create_line(t[3][0],t[3][1],t[0][0],t[0][1],width=3,fill="black")
                        k15+=1                   
    for i in range(len(a)):
        x1, y1 = (a[i][0] - 3), (a[i][1]  - 3)
        x2, y2 = (a[i][0] + 3), (a[i][1] + 3)
        w.create_oval(x1, y1, x2, y2, fill = "#FF0000")


# Массив точек
"""
a = [[0, 0],
     [0, 500],
     [500, 500],
     [250, 250],
     [500, 0],
     [250,0]]
"""
a = [[50,50],
     [300,50],
     [50,300],
     [300,300],
     [150,300]]



udalenie(a) # удаляем повторяющиеся координаты

# Определяем размер окна рисования
maxx = a[0][0]
maxy = a[0][1]
for i in a:
    i[0]+=3
    i[1]+=3
    if i[0]>maxx:
        maxx = i[0]
    if i[1]>maxy:
        maxy = i[1]
        
canvas_width = maxx+3
canvas_height = maxy+3


k15 = 0

# Процесс подготовки к рисованию 
master = Tk()
master.title('Convex quadrangles')
w = Canvas(master,
           width = canvas_width,
           height = canvas_height)
w.pack(expand = YES, fill = BOTH)
w.bind('<B1-Motion>', tr(a))
message = Label(master, text = "Количество выпуклых четырехугольников = " + str(k15))
message.pack(side=BOTTOM)
mainloop()





