
from collections import deque

fila = deque([])
filaSize = 10

for i in range(filaSize):
    try:
        fila.append(int(input('Entre com o {} numero: '.format(i+1))))
    except ValueError:
        print("ERRO! Somente numeros sao aceitos. Tente novamente.")
        break
else:
    for i in range(filaSize):
        print(fila.popleft())


    
