
vetor = []

for i in range(0, 10):
    try:
        vetor.append(int(input('Entre com o {} numero: '.format(i+1))))
    except ValueError:
        print("ERRO! Somente numeros sao aceitos. Tente novamente.")
        break
else:
    print(vetor)