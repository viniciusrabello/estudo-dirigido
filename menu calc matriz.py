memoria = []
backup = []

def VerMatriz(ind):
    print()
    for s in memoria[ind]:
        print(s)
    print()

def CriarM(a,b):
    matriz = []
    c = 0
    for i in range (a):
        print()
        linha = [int(i) for i in input("Escreva sua Linha Separando-a por Espaço: ").split()]
        matriz.append(linha)
        while len(linha) < b:
            linha.append(1)
        while len(linha) > b:
            del linha[-1] 
    memoria.append(matriz)
    VerMatriz(len(memoria) - 1)
    return matriz

def VerMemoria(ini, fim):
    i = 0
    if ini < 0: 
        ini = 0
    if fim >= len(memoria): 
        fim = len(memoria) - 1
    while i <= fim and ini <= i:
        VerMatriz(i)
        i += 1

def VerMemoriaToda():
    print('\nEssas são suas Matrizes:\n')
    if len(memoria) != 0:
        for i in range(len(memoria)):
            VerMatriz(i)
            i += 1
    else:
        print("Sua memória está vazia")

def ApagarMatriz(ind,fin):
    print("Essas serão as matrizes que você vai apagar, tem certeza disso?(S para sim e N para não) ")
    VerMemoria(ind,fin)
    confirma = (input("----> ")).lower()
    print("")
    if confirma == 's':
        del memoria[ind:fin+1]
    elif confirma == 'n':
        pass
    else:
        ApagarMatriz(ind,fin)

def ApagarMemoria():
    memoria.clear()

def SomarMatrizes(a,b):
    Mat = []    
    for i in range(len(a)):
        linha = []
        for j in range(int(len(a[i]))):
            linha.append(int(a[i][j]) + int(b[i][j]))
        Mat.append(linha)
    memoria.append(Mat)
    return Mat

def SubtrairMatrizes(a,b):
    Mat = []    
    for i in range(len(a)):
        linha = []
        for j in range(int(len(a[i]))):
            linha.append(int(a[i][j]) - int(b[i][j]))
        Mat.append(linha)
    memoria.append(Mat)
    return Mat

def Escalar(a,b):
    Mat = []    
    for i in range(len(a)):
        linha = []
        for j in range(int(len(a[i]))):
            linha.append(int(a[i][j]) * b)
        Mat.append(linha)
    memoria.append(Mat)
    return Mat

def EscalarLC1(a,b):
    LC = input("Você quer multiplicar uma linha ou uma coluna? ")
    if LC == 'linha':
        Lin = int(input("Qual linha você quer multiplicar por escalar? (contagem começa no 1)")) -1
        for j in range(int(len(a[Lin]))):
            a[Lin][j] = (int(a[Lin][j])*b)
        return a
    if LC == 'coluna':
        Col = int(input("Qual é a coluna que você quer multiplicar por escalar? (contagem começa no 1)")) - 1
        for i in range(len(a)):
            a[i][Col] = (int(a[i][Col])*b)
    memoria.append(a)
    return a

def EscalarLC(a,b,LC):
    if LC == 1:
        print()
        Lin = int(input("Escolha a Linha a ser Multiplicada: "))
        for j in range(int(len(a[Lin]))):
            a[Lin][j] = (int(a[Lin][j])*b)
        return a
    if LC == 2:
        print()
        Col = int(input("Escolha a Coluna a ser Multiplicada: "))
        for i in range(len(a)):
            a[i][Col] = (int(a[i][Col])*b)
    memoria.append(a)
    return a

def MultMat(A, B):
    LinhasA = len(A)
    ColunasA = len(A[0])
    LinhasB = len(B)
    ColunasB = len(B[0])
    if ColunasA != LinhasB:
        print("Você nao pode multiplicar essas matrizes")
        return
    C = [[0 for lin in range(ColunasB)] for col in range(LinhasA)]
    for i in range(LinhasA):
        for j in range(ColunasB):
            for k in range(ColunasA):
                C[i][j] += A[i][k] * B[k][j]
    memoria.append(C)
    return C

def Tranposicao(a):
    Mat = []
    linhas = len(a)
    colunas = len(a[0])
    for i in range(colunas):
        linha = []
        for j in range(linhas):
            linha.append(a[j][i])
        Mat.append(linha)
    memoria.append(Mat)
    return Mat

def Permutadora2x2(a,PLC):
    Mat = []
    if PLC == 1:
        A =[[0,1],[1,0]]
        Mat = MultMat(A,a)
    if PLC == 2:
        A =[[0,1],[1,0]]
        Mat = MultMat(a,A)
    memoria.append(Mat)
    return Mat

def Inversora2x2(a):
    A =[[0,1],[1,0]]
    Mat = MultMat(a,A)
    Mat = MultMat(A,Mat)
    memoria.append(Mat)
    return Mat

# Das funcoes normais so falta somar uma coluna ou uma linha por outra
# depois tenho que fazer tratamento de erros (vale bastante ponto)
# depois o menu e a forma la de printar
# se sobrar tempo tentar fazer as outras funcoes
# Terminar Backup e ler de arquivo a matriz



def Backup():
    for i in range(len(memoria)):
        backup.append(memoria[i])
    print("O seu Backup foi criado/atualizado ")
    return backup

def LerBackup():
    if len(backup) != 0:
        for i in range(len(backup)):
            print(backup[i])
    else:
        print("Seu Backup está vazio")

def AttMemoria():
    print("Você selecionou atualizar sua memoria com o Backup, isso vai destruir sua memoria atual.")
    dec = (input("Você tem certeza disso? (s para sim e n para não) ")).lower()
    if dec == 's':
        memoria = backup
        VerMemoriaToda()
        LerBackup()
    elif dec == 'n':
        pass
    else:
        print("Você digitou algo diferente de n ou s, tente novamente")
        AttMemoria()
    return memoria
    
while True:

    print('\n+==================== Calculadora Matricial ====================+')
    print('|                                                               |')
    print('|0.Criar Matriz                                                 |')
    print('|1.Soma ou Subtração Matricial (C = A + B ou C = A - B)         |')
    print('|2.Multiplicação por Escalar (C = aA onde a é um número inteiro)|')
    print('|3.Multiplicação Matricial (C = A x B)                          |')
    print('|4.Transposição                                                 |')
    print('|5.Permutar Duas Linhas ou Duas Colunas de posição              |')
    print('|6.Somar à uma Linha outra Linha ou à uma Coluna outra Coluna   |')
    print('|7.Multiplicar uma única Linha ou Coluna, por uma Escalar       |')
    print('|8.Inversão de Matrizes Quadradas 2x2                           |')
    print('|9.Outros                                                       |')
    print('|                                                               |')
    print('+===============================================================+\n')

    X = int(input('Escolha a opção desejada: '))

    if X == 0:
        
        a = int(input('\nEscolha o Número de Linhas: ')) #DÁ ERRO QUANDO NÃO COLOCAM NÚMERO
        b = int(input('\nEscolha o Número de Colunas: ')) #DÁ ERRO QUANDO NÃO COLOCAM NÚMERO
        CriarM(a,b)

    if X == 1:

        print('\n+===============================================================+')
        print('|                                                               |')
        print('|1.Soma Matricial (C = A + B)                                   |')
        print('|2.Subtração Matricial (C = A - B)                              |')
        print('|                                                               |')
        print('+===============================================================+\n')

        S = int(input('Escolha a opção desejada: '))

        if S == 1:
            VerMemoriaToda()
            print()
            a = int(input('Escolha A: '))
            b = int(input('Escolha B: '))
            print()
            SomarMatrizes(memoria[a],memoria[b])
            VerMatriz(len(memoria) - 1)

        if S == 2:
            VerMemoriaToda()
            print()
            a = int(input('Escolha A: '))
            b = int(input('Escolha B: '))
            print()
            SubtrairMatrizes(memoria[a],memoria[b])
            VerMatriz(len(memoria) - 1)

    if X == 2:
        VerMemoriaToda()
        print()
        A = int(input('Escolha A: '))
        print()
        a = int(input('Escolha a: '))
        print()
        Escalar(memoria[A],a)
        VerMatriz(len(memoria) - 1)

    if X == 3:
        VerMemoriaToda()
        print()
        a = int(input('Escolha A: '))
        print()
        b = int(input('Escolha B: '))
        print()
        MultMat(memoria[a],memoria[b])
        VerMatriz(len(memoria) - 1)
        
    if X == 4:
        VerMemoriaToda()
        print()
        a = int(input('Escolha sua Matriz: '))
        print()
        Tranposicao(memoria[a])
        VerMatriz(len(memoria) - 1)

    if X == 5:
        VerMemoriaToda()
        print()
        a = int(input('Escolha sua Matriz: '))
        print('\n+===============================================================+')
        print('|1.Linhas                                                       |')
        print('|2.Colunas                                                      |')
        print('+===============================================================+\n')

        PLC = int(input('Escolha a opção desejada: '))
        Permutadora2x2(memoria[a],PLC)
        VerMatriz(len(memoria) - 1)

    #if X == 6:
    if X == 7:
        VerMemoriaToda()
        print()
        a = int(input('Escolha sua Matriz: '))
        print('\n+===============================================================+')
        print('|1.Linhas                                                       |')
        print('|2.Colunas                                                      |')
        print('+===============================================================+\n')

        LC = int(input('Escolha a opção desejada: '))
        b = int(input('\nEscolha a Escalar: '))

        EscalarLC(memoria[a],b,LC)
        VerMatriz(len(memoria) - 1)

    if X == 8:
        VerMemoriaToda()
        print()
        a = int(input('Escolha sua Matriz: '))
        Inversora2x2(memoria[a])

    if X == 9:
        print('\n+==================== Calculadora Matricial ====================+')
        print('|                                                               |')
        print('|0.Ver Lista de Matrizes                                        |')
        print('|1.Importar Matriz                                              |')
        print('|2.Inserir uma Matriz Identidade                                |')
        print('|3.Alterar ou Remover Matrizes                                  |')
        print('|4.Exportar Lista de Matrizes                                   |')
        print('|5.Importar Lista de Matrizes                                   |')
        print('|6.Zerar Lista de Matrizes                                      |')
        print('|7.Outros                                                       |')
        print('|                                                               |')
        print('+===============================================================+\n')

        S = int(input('Escolha a opção desejada: '))

        if S == 0:
            print('\nEscolha o Intervalo da Memória à ser Visto')
            ini = int(input('\nInício do Intervalo: '))
            fim = int(input('\nFim do Intervalo: '))
            VerMemoria(ini,fim)

        if S == 3:
            print('\n+===============================================================+')
            print('|1.Alterar                                                       |')
            print('|2.Remover                                                      |')
            print('+===============================================================+\n')

            C = int(input('Escolha a opção desejada: '))

            VerMemoriaToda()
            print()
            a = int(input('Escolha sua Matriz: '))

            if C == 2:
                del memoria[a]
            
        if S == 6:
            ApagarMemoria()


        if S == 7:
            pass
