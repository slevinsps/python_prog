# Спасенов Иван ИУ7-13
# Защита


def zamena(zam, zam1, a, e):
    for i in range(len(a)):
        a[i] = ' ' + a[i] + ' '
        s1 = a[i]
        k2 = 0
        t = a[i]
        while zam in t:

            s = ''
            for j in range(k2, len(s1) - len(zam)):
                o = False
                k = 0
                s = ''
                for h in range(len(zam)):
                    s += s1[k + j]
                    k += 1
                if s == zam:
                    if ((s1[j - 1] in zn) or s1[j - 1] == ' ') and ((s1[j + k] in zn) or s1[j + k] == ' '):
                        o = True
                        s11 = s1
                        s1 = ''
                        if e:
                            if s11[j - 1] == ' ':
                                j -= 1
                                for q in range(j):
                                    s1 += s11[q]
                                j += 1
                        else:
                            for q in range(j):
                                s1 += s11[q]
                        s1 += zam1
                        for q in range(j + k, len(s11)):
                            s1 += s11[q]
                        a[i] = s1
                        t = ''
                        for q in range(j+k, len(s11)):
                            t += s11[q]
                        k2 = j + len(zam1)
                        break
                    else:
                        o = False
                if o:
                    break
        f = a[i]
        a[i] = ''
        for q in range(1, len(f) - 1):
            a[i] += f[q]
    for i in range(len(a)):
        print(a[i])


a = ['я роботы я в мир я.',
     '9-6 вкуснейших, пряников я купил себе вчера',
     'артем любит капусту по 5+30?',
     'apple самая богатая - компания в мире я']

zn = ['.',',','?','!','?!','...']

zam = input('Введите слово, которое хотите заменить: ')

print('Измененный текст:')

zamena(zam,'', a, True)
