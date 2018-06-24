# Спасенов ИУ7-13
# Повернуть матрицу

f = [[],[]]
n = int(input('Введите n: '))
print('Введите матрицу',n,'x',n)
f = [[int(j) for j in input().split()] for i in range(n)]
ch = input('Введите r, чобы повенруть матрицу вправо, l, \
чтобы повернуть влево: ')

while True:
    f.reverse()
    for i in range(n-1):  # Меняем местами элементы матрицы
        for j in range(i+1,n):
            f[i][j],f[j][i] = f[j][i],f[i][j]
            
    if ch =='l':
        f.reverse()
        for i in range(n):
            f[i].reverse()
            
    print('Полученная матрица: ')        
    for i in range(n):
        for j in range(n):
            if (j+1) % n ==0:
                print(f[i][j],end='\n')
            else:
                print(f[i][j],end=' ')
                
    print('Чтобы выйти, нажмите Enter')
    ch = ''
    ch = input('Введите r, чобы повенруть матрицу вправо, l, \
чтобы повернуть влево: ')
    if ch == '':
        break

        
