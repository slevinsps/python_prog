def f(): # Функция
    def newf(x):
        f = sin(x)
        return f
    return newf
    
def Steffens(a,b,h,eps,max_i,func): # Метод Стеффенса

    f = func
    
    roots = []

    while (a < b):
        x = a
        i = 0
        while abs(f(x)) > eps:
            i += 1
            x = x - ((f(x)**2)/(f(x+f(x))-f(x)))
            if i > max_i:
                break
                
        if (abs(f(x)) <= eps) and (a <= x < a+h):
            roots.append(x)
            
            
        a += h
        
    return roots
print(roots)
