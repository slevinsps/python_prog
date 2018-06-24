x=[]
for i in range(3):
    x.append([])
    for j in range(4):
        x[i].append(list(map(int,input().split())))
for i in range(3):
    for j in range(4):
        print(x[i][j],end=' ')
    print()
