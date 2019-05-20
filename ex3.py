arq = open('mat.txt')
q = arq.read()
mat = q.split('\n')
print(q)
mat2 = []
matriz = ''
state = 'lendo'

for i in range (len(mat)):
    line = []
    j = 0
    while j < len(mat[i]) - 1:
        if state == 'lendo':
            if mat[i][j] == '1':
                line.append(1)
                j += 1
            if mat[i][j] == '0':
                line.append(0)
                state = 'prenchendo'
                j += 1
        if state == 'prenchendo':
            if mat[i][j] == '1':
                line.append(0)
                j += 1
            if mat[i][j] == '0':
                line.append(0)
                state = 'lendo'
                j += 1
    mat2.append(line)
    
