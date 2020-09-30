
nlinhas = 10
ncolunas = 10

matriz = []

for i in range(nlinhas):
    linha = []
    for j in range(ncolunas):
        try:
            linha.append(int(input('Entre com o {} numero da {} linha: '.format(j+1, i+1))))
        except ValueError:
            print("ERRO! Somente numeros sao aceitos. Tente novamente.")
            exit()
    matriz += [linha]
else:
    for i in range(nlinhas):
        print(matriz[i])
        

    
