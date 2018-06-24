a = ['На прошлой лабораторной работе, которая была 36-12 ноября, группа ИУ7-13 писала',
     'контрольную работу. Они ее написали, возможно, яч яч яч яч яч яч яч яч яч яч,',
     'даже хорошо. Некоторые. Некоторые не написали',
     'номер варианта!']
zn = ['.',',','?','!','?!','...']
kon = ['.','?','!']
gl = ['а','е','ё','и','о','ю','y','я','э','ы']

a2 = ['']*(len(a)+1)
sl = []

k = 0
for i in range(len(a)):
    a[i] += ' '
    for j in range(len(a[i])):
        if a[i][j] not in kon:
            a2[k] += a[i][j]
        else:
            a2[k] += a[i][j]
            k += 1
            
for j in range(len(a2)):
    ks = 0
    mins = a2[j]

    s = ''
    for i in range(len(mins)):
        if mins[i] != ' '  and mins[i] not in zn:
            s += mins[i].lower()
        else:
            if s != '':
                
                if s[0] in gl:
                    b = True

                elif 'а'<=s[0]<='я' and s[0] not in gl:
                    b = False
                if b:
                    rt = 0
                    for h in range(len(s)):
                        if (h+1) % 2 == 0:
                            if 'а'<=s[h]<='я' and s[h] not in gl:
                                rt += 1
                        else:
                            if s[h] in gl:
                                rt += 1

                    if rt == len(s):
                        ks+=1
                else:
                    rt = 0
                    for h in range(len(s)):
                        if (h+1) % 2 == 0:
                            if s[h] in gl:
                                rt += 1
                        else:
                            if 'а'<=s[h]<='я' and s[h] not in gl:
                                rt += 1

                    if rt == len(s):
                        ks+=1
            s = ''                
    sl.append(ks)

print('Предложение с максимальным количеством слов, в которых буквы чередуются: ')
print(a2[sl.index(max(sl))])

