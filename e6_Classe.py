
class Tarefa:
    def __init__(self, descricao, prioridade):
        self.descricao = descricao
        self.prioridade = prioridade
    
    def setDescricao(self, descricao):
        self.descricao = descricao

    def setPrioridade(self, prioridade):
        self.prioridade = prioridade
    
    def getDescricao(self):
        return self.descricao

    def getPrioridade(self):
        return self.prioridade

tarefas = []
nTarefas = 10

for i in range(nTarefas):
    try:
        desc = input('Entre com a descricao da tarefa {}: '.format(i+1))
        prior = int(input('Entre com a prioridade da tarefa {}: '.format(i+1)))

        if(prior < 0 or prior > 5):
            print('Erro! Voce nao digitou um numero valido! Tente Novamente')
            exit()
        else:
            tarefa = Tarefa(desc, prior)
            if len(tarefas) == 0:
                tarefas.append(tarefa)
            else:
                insert = False
                for i in range( len(tarefas) ):
                    if tarefa.getPrioridade() >= tarefas[i].getPrioridade():
                        tarefas.insert(i, tarefa)
                        insert = True
                        break
                if insert == False:
                    tarefas.append(tarefa)
    except ValueError:
        print("Ocorreu um erro, tente novamente.")
        exit()
else:
    for i in range(nTarefas):
        print(tarefas[i].getDescricao(), tarefas[i].getPrioridade())


    

   



    