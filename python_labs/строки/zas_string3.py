# Спасенов Иван ИУ7-13
# Защита

a = ['На прошлой лабораторной работе, которая была 36-12 ноября, группа ИУ7-13 писала',
     'контрольную работу. Они ее написали, возможно,',
     'даже хорошо. Некоторые. Некоторые не написали',
     'номер варианта!']
zn = ['.',',','?','!','?!','...']

minis = len(a[0])
mins = a[0]
for i in range(len(a)):
    if len(a[i])<minis:
        minis = len(a[i])
        mins = a[i]
print(mins)
mins += ' '
maxis = -1
maxs = ''
s = ''
for i in range(len(mins)):
    if mins[i] != ' '  and mins[i] not in zn:
        s += mins[i]
    else:
        if s != '':
            if len(s)>maxis:
                maxis = len(s)
                maxs = s
        s = ''
print('Самое длинное слово в самой короткой строке:')
print(maxs)
    
