# Reprezentacja grafu

from random import randint

def funkcja():
    nodes = int(input('Podaj liczbe wierzcholkow: '))
    odwiedzony = [False]                            # Zeby liczylo od 1 a nie 0
    graph = {}                                      # graf = {wierzcholek : [(wierz_konc1, waga) , (wierz_konc2, waga)], wierzcholek_nast...}
    for i in range(1, nodes + 1):
        losuj(graph, nodes)
        odwiedzony.append(False)

    for node in graph:
        print(graph[node], odwiedzony[node])


def add_node(graph, node):
    # Wstawia wierzchołek do grafu
    if node not in graph:
        graph[node] = []


def losuj(graph, nodes):
    while True:
        node1 = randint(1, nodes)
        node2 = randint(1, nodes)
        if node1 != node2:
            break

    waga = randint(1, 20)

    add_node(graph, node1)
    add_node(graph, node2)

    if node2 not in graph[node1]:
        graph[node1].append((node2, waga))
        graph[node2].append((node1, waga))

def greedy(graph, nodes):
    start = randint(1, nodes)



funkcja()