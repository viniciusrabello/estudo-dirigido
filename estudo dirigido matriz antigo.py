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
        l = input(': ').split()
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
    if ini < 0:
        ini = 0
    if fim >= len(memoria):
        fim = len(memoria) - 1
    while i <= fim and ini <= i:
        VerMatriz(i)
        i += 1
        
def ApagarMatriz(ind,fim):
    del memoria[ind:fim+1]

def SomarMatriz(a,b): #NÃO FUNCIONA
    if len(memoria[a]) == len(memoria[b]) and len(memoria[a][0]) == len(memoria[b][0]):
        mat = []
        l = []
        for i in range(len(memoria[a])):
            for s in range(len(memoria[a][i])):
                c = float(memoria[a][i][s]) + float(memoria[b][i][s])
            l.append(c)
            mat.append(l)
        memoria.append(mat)
        VerMatriz(len(memoria) - 1)
    else:
        print('as matrizes tem que ter mesmo numero de linhas e de colunas')

def SubtrairMatriz(a,b): #NÃO FUNCIONA
    if len(memoria[a]) == len(memoria[b]) and len(memoria[a][0]) == len(memoria[b][0]):
        mat = []
        l = []
        for i in range(len(memoria[a])):
            for s in range(len(memoria[a][i])):
                c = float(memoria[a][i][s]) - float(memoria[b][i][s])
            l.append(c)
            mat.append(l)
        memoria.append(mat)
        VerMatriz(len(memoria) - 1)
    else:
        print('as matrizes tem que ter mesmo numero de linhas e de colunas')

