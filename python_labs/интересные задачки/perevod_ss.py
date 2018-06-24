a,a1 = map(float,input('Введите первое и второе число: ').split())
b = int(input('Введите систему счисления: '))
e = ('A', 'B', 'C', 'D', 'E', 'F')
e1 = (10, 11, 12, 13, 14, 15)
a = a/a1
s = '0.'
while a - int(a) != 0 and len(s)<=50:
    k = int(a*b)
    a *= b
    a = a - k
    if 16> k > 9:
        k = e[e1.index(k)]
    s += str(k)
f1 = ''
f = None
for i in range(2,len(s)):
    if f == '':
        break
    else:
        f = ''
        for j in range(i,i+(len(s)-i)//2):
            f+=s[j]
            if s[i:len(s)].count(f)*len(f) == len(s[i:len(s)]):
                f1 = f
                f = ''
                break
if f1:
    s = s.replace(f1,'')
    s+='('+f1+')'
print('Число в',b,'ичной системе счисления:')
print(s)

