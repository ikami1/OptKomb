# Reprezentacja grafu

from random import randint
from math import sqrt

def funkcja():
    nodes = int(input('Podaj liczbe wierzcholkow: '))
    list_nodes = []                                 # lista wierzcholkow (numerowanie)
    odwiedzony = [True]                             # Zeby liczylo od 1 a nie 0
    graph = {}                                      # graf = {wierzcholek : [(wierz_konc1, waga) , (wierz_konc2, waga)], wierzcholek_nast...}
    for i in range(1, nodes+1):
        list_nodes.append(add_node(graph, list_nodes))
        odwiedzony.append(False)

    for i in range(1, int(nodes*(nodes-1)/2)):
        losuj(graph, list_nodes)

    #for node in graph:
    #    print(graph[node], odwiedzony[node])

    print(greedy(graph, nodes, odwiedzony, list_nodes))


def add_node(graph, list_nodes):
    while True:
        node = (randint(1, 1000), randint(1, 1000))
        # Wstawia wierzchołek do grafu
        if node not in graph:
            graph[node] = []
            list_nodes.append(node)
            break


def losuj(graph, list_nodes):

    while True:
        node = randint(1, len(list_nodes))
        node2 = randint(1, len(list_nodes))
        if node != node2 and :
            break

    waga = sqrt(pow(x1-x2,2) + pow(y1-y2,2))

    if node2 not in graph[node1]:
        graph[node1].append((node2, waga))
        graph[node2].append((node1, waga))

def greedy(graph, nodes, odwiedzony, list_nodes):
    start_node = randint(1, nodes)
    min_waga = 100
    min_node = list_nodes[start_node]
    odwiedzony[start_node] = True
    waga_przejscia = 0
    kolejni_odwiedzeni = [start_node]

    while False in odwiedzony:
        for (node, waga) in graph[list_nodes[start_node]]:
            if waga <= waga:
                min_waga = waga
                min_node = node

        start_node = min_node
        kolejni_odwiedzeni.append(start_node)
        waga_przejscia = waga_przejscia + min_waga
        odwiedzony[node] = True

    return waga_przejscia, kolejni_odwiedzeni


funkcja()