memoria = []

def VerMatriz(ind):
    print()
    for s in memoria[ind]:
        print(*s)
    print()
    
def CriarMatriz(m,n):
    mat = []
    print()
    for i in range (m):
        l = []
        l = input('linha: ').split()
        c = len(l)
        while c < n:
            l.append(1)
            c += 1
        if c > n:
            del l[n:c]
        mat.append(l)
    memoria.append(mat)
    VerMatriz(len(memoria) - 1)

def VerMemoria(ini, fim):
    i = 0
    if ini < 0: ini = 0
    if fim >= len(memoria): fim = len(memoria) - 1
    while i <= fim and ini <= i:
        VerMatriz(i)
        i += 1

def ApagarMatriz(ind):
    del memoria[ind:ind+1]
