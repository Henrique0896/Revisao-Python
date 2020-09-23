
pilha = []
pilhaSize = 10


for i in range(pilhaSize):
    try:
        pilha.append(int(input('Entre com o {} numero: '.format(i+1))))
    except ValueError:
        print("ERRO! Somente numeros sao aceitos. Tente novamente.")
        break
else:
    for i in range(pilhaSize):
        print(pilha.pop())


    
