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

#Ler o vértice
try:
    v = int(input("Digite o vértice: "))
except ValueError as e:
    print("Erro: {}".format(e))
    exit()

#Verificar se o vértice existe
exist = False
for i in range( len(vertices)):
    if v == vertices[i]:
        exist = True
        break
if exist == False:
    print("Não existe este vértice no grafo")
    exit()

#Retornar os adjacentes
adjacentes = []
for i in range(len (matriz[v]) ):
    if matriz[v][i] != 0:
        adjacentes.append(i)
print(adjacentes)
