vetor = []
tamanho = 5
for i in range(tamanho):
    try:
        x = int(input('Digite um numero: '))
        vetor.append(x)
 
    except ValueError:
        print("Entrada invalida")
        exit()

def Soma(vetor):
    if len(vetor) == 1:
        return vetor[0]
    else:
        return vetor[0] + Soma(vetor[1:])
print (Soma(vetor))
