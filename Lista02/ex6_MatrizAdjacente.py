#A lista que vai receber as arestas
arestas = []
#A lista que vai receber todos os vértices
vertices = []
#Matriz de adjacencia
matriz = []

#Classe para salvar as informações de cada aresta do grafo
class Aresta:
    def __init__(self, v1, v2, a):
        self.v1 = v1
        self.v2 = v2
        self.a = a

#Preencher a lista de arestas conforme informações do arquivo
try:
    grafo = open('grafo.txt', 'r')
    for i in grafo:
        linha = i.split()
        arestas.append(Aresta(int(linha[0]), int(linha[1]), int(linha[2])))
except ValueError:
      print('Erro ao tentar manipular arquivo {}'.format(ValueError))
finally:
    grafo.close()

#Função para verificar se o vértice já está na lista 'vertices'
def inserido(v):
    inserted = False
    for i in range( len(vertices) ):
        if (v == vertices[i]):
            inserted = True
            break
    return inserted

#Iterar para preencher a lista 'vertices'
for i in range( len(arestas) ):
    if(not inserido(arestas[i].v1)):
        vertices.append(arestas[i].v1)
    if(not inserido(arestas[i].v2)):
        vertices.append(arestas[i].v2)
vertices = sorted(vertices)

#Preencher matriz com zeros
for i in range( len(vertices) ):
    linha = []
    for j in range( len(vertices) ):
        linha.append(0)
    matriz.append(linha)

#Criando matriz adjacente
for i in range( len(arestas) ):
    matriz[arestas[i].v1][arestas[i].v2] = arestas[i].a
    matriz[arestas[i].v2][arestas[i].v1] = arestas[i].a

#Imprimir Matriz
print()
print("A Matriz de Adjacencia é: ")
for i in range( len(matriz) ):
    print(matriz[i])
print()

#Calculando e imprimindo o grau de cada vértice:
print("O grau de cada vértice é: ")
for i in range( len(matriz) ):
    grau = 0
    for j in range( len(matriz[i]) ):
        if(matriz[i][j] != 0):
            grau += 1
    print('Grau de {}: {}'.format(i,grau) )
