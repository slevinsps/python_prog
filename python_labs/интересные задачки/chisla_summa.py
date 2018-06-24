print('Введите массив: ')
a = list(map(int,input().split()))
ans = []
for i in range(len(a)):
    r = 0
    u = -1
    while (u != len(a) - 1) and (r == 0):
        u += 1
        x = a[:]
        del(x[i])
        x.sort()
        x1 = x[:]
        for j in range(u, len(x)):
            for k in range(len(x)):
                if k != j:
                    x[k] += x1[j]
                if a[i] in x:
                    ans.append(a[i])
                    r = 1
                    break
            if a[i] in x:
                break
print('Числа, которые нельзя получить суммой других чисел: ')

if ans == a:
    print('Увы, таких чисел нет')
for i in a:
    if i not in ans:
        print(i,end=' ')
