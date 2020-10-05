from copy import deepcopy

nlinhas = 3
ncolunas = 3

matriz = []
#INDEX DO ESPAÇO EM BRANCO
iEB = [None]

#Lendo o estado do jogo
for i in range(nlinhas):
    linha = []
    for j in range(ncolunas):
        try:
            elemento = (input('Entre com o {} elemento da {} linha  *n para espaco branco*: '.format(j+1, i+1)))
            if elemento == 'n':
                if iEB[0] is None:
                    elemento = ''
                    iEB = [i, j]
                else:
                    print("Apenas um espaco em branco, comece de novo")
                    exit()
            else:
                elemento = int(elemento)
            linha.append(elemento)
        except ValueError:
            print("ERRO! Somente 'n' ou numeros sao aceitos. Tente novamente.")
            exit()
    matriz.append(linha)
else:
    if iEB[0] is None:
        print("O quebra cabeça deve possuir um espaço em branco, tente novamente")
        exit()

#Imprimir Estado inicial
print()
print("ESTADO INICIAL:")
for i in range(nlinhas):
    print(matriz[i])

#Troca espaço em branco por peça acima
if iEB[0] != 0:
    m = deepcopy(matriz)
    m[ iEB[0] ][ iEB[1] ] = m[ iEB[0]-1 ][ iEB[1] ]
    m[ iEB[0]-1 ][ iEB[1] ] = ''
    print()
    print("Espaço em branco para cima:")
    for i in range(nlinhas):
        print(m[i])

#Troca espaço em branco por peça da direita
if iEB[1] != 2:
    m = deepcopy(matriz)
    m[ iEB[0] ][ iEB[1] ] = m[ iEB[0] ][ iEB[1]+1 ]
    m[ iEB[0] ][ iEB[1]+1 ] = ''
    print()
    print("Espaço em branco para a direita:")
    for i in range(nlinhas):
        print(m[i])

#Troca espaço em branco por peça da esquerda
if iEB[1] != 0:
    m = deepcopy(matriz)
    m[ iEB[0] ][ iEB[1] ] = m[ iEB[0] ][ iEB[1]-1 ]
    m[ iEB[0] ][ iEB[1]-1 ] = ''
    print()
    print("Espaço em branco para a esquerda:")
    for i in range(nlinhas):
        print(m[i])

#Troca espaço em branco por peça de baixo
if iEB[0] != 2:
    m = deepcopy(matriz)
    m[ iEB[0] ][ iEB[1] ] = m[ iEB[0]+1 ][ iEB[1] ]
    m[ iEB[0]+1 ][ iEB[1] ] = ''
    print()
    print("Espaço em branco para baixo:")
    for i in range(nlinhas):
        print(m[i])
