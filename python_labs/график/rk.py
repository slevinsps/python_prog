g = list(map(int,input().split()))
n = len(g)
for i in range(n-1):
    for j in range(n-2,i-1,-1):
        if g[j]>g[j+1]:
            g[j],g[j+1] = g[j+1],g[j]
print(g)

for i in range(n-1):
    nmin = i
    for j in range(j+1,n):
        if g[j]<g[nmin]:
            nmin = j
        g[i],g[nmin] = g[nmin],g[i]
print(g)

for i in range(n-1):
    for j in range(i+1,n):
        if g[j]>g[i]:
            g[j],g[j] = g[j],g[j]
print(g)