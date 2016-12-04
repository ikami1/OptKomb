# Reprezentacja grafu

from random import randint
from math import sqrt


def funkcja():
    nodes = int(input('Podaj liczbe wierzcholkow: '))
    odwiedzony = {}                                 # odwiedzony = {wierzcholek : True/False, ...} gdzie True - odwiedzony
    graph = {}                                      # graf = {wierzcholek : [(wierz_konc1, waga) , (wierz_konc2, waga)], wierzcholek_nast...}
                                                    # gdzie wierzcholek = (wsp_x, wsp_y)
    edge = {}                                       # edge = {(node1, node2) : waga, ...}
    for i in range(1, nodes+1):
        wsp_x = int(input())
        wsp_y = int(input())
        add_node(graph, (wsp_x, wsp_y))

    for node1 in graph:                             #dodawanie krawedzi
        for node2 in graph:
            add_edge(graph, node1, node2, edge)

    for node in graph:                              # ustawiamy wszystkie wierzcholki na nieodwiedzone
        odwiedzony[node] = False

    greedy(graph, nodes, odwiedzony, edge)
    #print(greedy(graph, nodes, odwiedzony, edge))


def add_node(graph, node):                          # Wstawia wierzchołek do grafu
    if node not in graph:
        graph[node] = []


def add_edge(graph, node1, node2, edge):                  #node = (x,y)
    if node1 == node2:
        return
    x1, y1 = node1
    x2, y2 = node2

    weight = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))

    if (node2, weight) not in graph[node1]:
        edge[(node1, node2)] = weight
        graph[node1].append((node2, weight))
    if (node1, weight) not in graph[node2]:
        edge[(node2, node1)] = weight
        graph[node2].append((node1, weight))


def greedy(graph, nodes, odwiedzony, edge):

    first = los_start_node(graph, nodes)
    odwiedzony[first] = True

    current = first                                 # z tego wierzcholka chodzimy do nastepnego
    whole_weight = 0                                # koszt przejscia grafu
    TSP_path = [first]                              # kolejne odwiedzone wierzcholki

    print(odwiedzony[first], first, "abc")          # dlaczego tylko 3 printy?
    for node in odwiedzony:
        if odwiedzony[node] == False:
            min_weight, next = first_next_node(graph, current, odwiedzony, edge)    # pierwszy nieodwiedzony jako najblizszy
            odwiedzony[next] = True
            print(odwiedzony[next], next)
            #for node in graph:

    """
    min_waga = 100
    min_node = list_nodes[start_node]

    while False in odwiedzony:
        for (node, waga) in graph[list_nodes[start_node]]:
            if waga <= waga:
                min_waga = waga
                min_node = node

        start_node = min_node
        kolejni_odwiedzeni.append(start_node)
        waga_przejscia = waga_przejscia + min_waga
        odwiedzony[node] = True

    #na koncu wrocic do first

    return waga_przejscia, kolejni_odwiedzeni
    """

def los_start_node(graph, nodes):
    L = []
    for node in graph:
        L.append(node)
    return L[randint(0, nodes - 1)]


def first_next_node(graph, current, odwiedzony, edge):
    '''for node in graph:                                  # pierwszy nieodwiedzony jako najblizszy
        if odwiedzony[node] == False:
            for (node2, weight) in graph[current]:
                if node2 == node:
                    return (weight, node)'''
    for (node1, node2) in edge:
        if node1 == current and odwiedzony[node2] == False:
            return (edge[(current, node2)], node2)          #return (weight, node2)

"""
Do ew. wyswietlenie grafu

def listnodes(graph):
    #Zwraca listę wierzchołków grafu.
    return graph.keys()


def listedges(graph):
    #Zwraca listę krawędzi (krotek) grafu.
    L = []
    for source in graph:
        for (target, weight) in graph[source]:
            L.append((source, target, weight))
    return L
"""

funkcja()