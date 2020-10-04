import heapq

class Tarefa:
    def __init__(self,desc,ordem):
        self.desc = desc
        self.ordem = ordem

nTarefas = 3
tarefas = []

#Função para verificar se a ordem já foi inserida
def inserido(o):
    inserted = False
    for i in range( len(tarefas) ):
        if (o == tarefas[i][0]):
            inserted = True
            break
    return inserted

#inserir
for i in range(nTarefas):
    try:
        desc = input('Entre com a descricao da tarefa {}: '.format(i+1))
        ordem = int(input('Entre com a ordem da tarefa {}: '.format(i+1)))

        while inserido(ordem):
            print("Essa ordem já foi inserida! Tente Novamente")
            print()
            ordem = int(input('Entre com a ordem da tarefa {}: '.format(i+1)))

        tarefa = Tarefa(desc, ordem)
        heapq.heappush(tarefas, (tarefa.ordem, tarefa.desc))
            
    except ValueError:
        print("Ocorreu um erro, tente novamente.")
        exit()

#Imprir Lista
for i in range(nTarefas):
        print(tarefas[i][1])
