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

funkcja()