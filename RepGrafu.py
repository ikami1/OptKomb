#Reprezentacja grafu

def funkcja():
    x = int(input('Podaj liczbe wierzcholkow: '))
    odwiedzony = [False]                        #Zeby liczylo od 1 a nie 0
    graph = {}                                  #graf = {wierzcholek : [(wierz_konc1, waga) , (wierz_konc2, waga)], wierzcholek_nast...}
    for i in range(1,x + 1):
        add_node(graph, i)
        odwiedzony.append(False)

    for node in graph:
        print(graph[node], odwiedzony[node])

def add_node(graph, node):
    #Wstawia wierzchołek do grafu
    if node not in graph:
        graph[node] = []
        
def losuj(graph,x):
    do
        node1 = randint(1, x)
        node2 = randint(1, x)
    while(wierzcholek1 == wierzcholek2)
    waga = randint(1,20)
    if node2 not in graph[node1]
        graph[node1].append(node2,waga)
    
    
    

funkcja()
