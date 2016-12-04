# Reprezentacja grafu

from random import randint
from math import sqrt


def funkcja():
    nodes = int(input('Podaj liczbe wierzcholkow: '))
    rozmiar = int(input('Podaj maksymalny rozmiar wspolrzednej: '))
    losuj(nodes, rozmiar)
    odwiedzony = {}                                 # odwiedzony = {wierzcholek : True/False, ...} gdzie True - odwiedzony
    graph = {}                                      # graf = {wierzcholek : [(wierz_konc1, waga) , (wierz_konc2, waga)], wierzcholek_nast...}
                                                    # gdzie wierzcholek = (wsp_x, wsp_y)
    edge = {}                                       # edge = {(node1, node2) : waga, ...}
    nazwa_pliku = input('Podaj nazwe pliku: ')
    plik = open(nazwa_pliku,'r')
    nodes = int(plik.readline())
    for i in range(1, nodes+1):
        linia = plik.readline()
        dane = linia.split()
        wsp_x = int(dane[0])
        wsp_y = int(dane[1])
        add_node(graph, (wsp_x, wsp_y))

    for node1 in graph:                             # dodawanie krawedzi
        for node2 in graph:
            add_edge(graph, node1, node2, edge)

    for node in graph:                              # ustawiamy wszystkie wierzcholki na nieodwiedzone
        odwiedzony[node] = False

    print(greedy(graph, nodes, odwiedzony, edge))


def add_node(graph, node):                          # Wstawia wierzchołek do grafu
    if node not in graph:
        graph[node] = []


def losuj(nodes,rozmiar):
    ile = 0
    lista_wierzcholkow = []
    f = open('dane.txt', 'w')
    f.write(str(nodes)+'\n')
    while(ile<nodes):
        wsp_x = randint(0,rozmiar)
        wsp_y = randint(0,rozmiar)
        if (wsp_x,wsp_y) not in lista_wierzcholkow:
            lista_wierzcholkow.append((wsp_x,wsp_y))
            ile+=1
            f.write(str(wsp_x)+' '+str(wsp_y)+'\n')




def add_edge(graph, node1, node2, edge):                  # node = (x,y)
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
    current = first                                 # aktualny wierzcholek, od niego szukamy nastepnego

    whole_weight = 0                                # koszt przejscia grafu
    TSP_path = [first]                              # kolejne odwiedzone wierzcholki

    print(odwiedzony[first], first, "abc")
    while True:
        min_weight, next = first_next_node(current, odwiedzony, edge)    # pierwszy nieodwiedzony jako najblizszy
        if min_weight == -1:                        # wszystkie wierzcholki juz odwiedzone
            break

        for node in graph:                          # sprawdzamy czy jest jakis blizszy current niz next
            if (odwiedzony[node] == False) and (min_weight > edge[(node, current)]):
                min_weight = edge[(node, current)]
                next = node

        odwiedzony[next] = True                     # idziemy do nastepnego
        whole_weight += edge[(current, next)]
        TSP_path.append(next)
        current = next
        print(odwiedzony[next], next)

    whole_weight += edge[(current, first)]          # zamykamy cykl
    TSP_path.append(first)

    return whole_weight, TSP_path


def los_start_node(graph, nodes):
    L = []
    for node in graph:
        L.append(node)
    return L[randint(0, nodes - 1)]


def first_next_node(current, odwiedzony, edge):      # pierwszy nieodwiedzony jako najblizszy
    for (node1, node2) in edge:
        if node1 == current and odwiedzony[node2] == False:
            return (edge[(current, node2)], node2)          # return (weight, node2)
    return (-1, (-1, -1))                                   # wszystkie odwiedzone juz

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