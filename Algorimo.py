grafo = {'Aresta1':{'Aresta2':1,'Aresta3':222},
         'Aresta2':{'Aresta3':44},        
         'Aresta3':{'Aresta1':2,'Aresta4':104},
         'Aresta4':{'Aresta3':76}}
#Caminho 1: Aresta1 - Aresta2 = 1
        #   Aresta2 - Aresta3 = 45
        #   Aresta3 - Aresta4 = 104 
        #                     = 149
def dijkstra(grafo,inicio,fim):
    menor_caminho = {}
    antecessor = {}
    n_visitados = grafo
    infinito = 10000
    caminho = []
    for node in n_visitados:
        menor_caminho[node] = infinito
    menor_caminho[inicio]=0

    while n_visitados:
        minNode = None
        for no in n_visitados:
            if minNode is None:
                minNode = no
            elif menor_caminho[no] < menor_caminho[minNode]:
                minNode = no
        for childNode, weight in grafo[minNode].items():
            if weight + menor_caminho[minNode] < menor_caminho[childNode]:
                menor_caminho[childNode] = weight + menor_caminho[minNode]
                antecessor[childNode] = minNode
        n_visitados.pop(minNode)

    no_atual = fim
    while no_atual != inicio:
        try:
            caminho.insert(0,no_atual)
            no_atual = antecessor[no_atual]
        except KeyError:
            print('erro no caminho')
            break
    caminho.insert(0,inicio)
    if menor_caminho[fim] != infinito:
        print('distancia do menor caminho é '+str(menor_caminho[fim]))
        print('o caminho é '+ str(caminho))


dijkstra(grafo,'Aresta1','Aresta4')