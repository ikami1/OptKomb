# Reprezentacja grafu

from random import randint
from math import sqrt


def funkcja():
    nodes = int(input('Podaj liczbe wierzcholkow: '))
    rozmiar = int(input('Podaj maksymalny rozmiar wspolrzednej: '))
    losuj(nodes, rozmiar)
    lista_wierzcholkow=[]                                                                           # lista_wierzcholkow = [(x,y),(x,y)......]
    odwiedzony = {}                                                                                 # odwiedzony = {wierzcholek : True/False, ...} gdzie True - odwiedzony
                                                                                                    # gdzie wierzcholek = (wsp_x, wsp_y)
    Matrix = [[0 for x in range(rozmiar)] for y in range(rozmiar)]
    nazwa_pliku = input('Podaj nazwe pliku: ')
    plik = open(nazwa_pliku,'r')
    nodes = int(plik.readline())

    for i in range(0, nodes):
        linia = plik.readline()
        dane = linia.split()
        wsp_x = int(dane[0])
        wsp_y = int(dane[1])
        lista_wierzcholkow.append((wsp_x, wsp_y))
    for i in range(0,nodes):                                                                        # dodawanie krawedzi
        for j in range(0,nodes):
            Matrix[i][j]=sqrt(pow(lista_wierzcholkow[i][0] - lista_wierzcholkow[j][0], 2) + pow(lista_wierzcholkow[i][1] - lista_wierzcholkow[j][1], 2))

    for node in lista_wierzcholkow:                                                                 # ustawiamy wszystkie wierzcholki na nieodwiedzone
        odwiedzony[node] = False
    print(greedy(Matrix, nodes, odwiedzony,lista_wierzcholkow))

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

def greedy(Matrix, nodes, odwiedzony,lista_wierzcholkow):

    first = los_start_node(lista_wierzcholkow, nodes)
    odwiedzony[first] = True
    current = first                                                                                 # aktualny wierzcholek, od niego szukamy nastepnego

    whole_weight = 0                                                                                # koszt przejscia grafu
    TSP_path = [first]                                                                              # kolejne odwiedzone wierzcholki

    print(odwiedzony[first], first, "abc")
    while True:
        min_weight, next = first_next_node(current, odwiedzony, Matrix, nodes, lista_wierzcholkow)  # pierwszy nieodwiedzony jako najblizszy
        if min_weight == -1:                                                                        # wszystkie wierzcholki juz odwiedzone
            break

        for node in lista_wierzcholkow:                                                             # sprawdzamy czy jest jakis blizszy current niz next
            if (odwiedzony[node] == False) and (min_weight > Matrix[lista_wierzcholkow.index(node)][lista_wierzcholkow.index(current)]):
                min_weight = Matrix[lista_wierzcholkow.index(node)][lista_wierzcholkow.index(current)]
                next = node

        odwiedzony[next] = True                                                                     # idziemy do nastepnego
        whole_weight += Matrix[lista_wierzcholkow.index(current)][lista_wierzcholkow.index(next)]
        TSP_path.append(next)
        current = next
        print(odwiedzony[next], next)

    whole_weight += Matrix[lista_wierzcholkow.index(current)][lista_wierzcholkow.index(first)]                                                          # zamykamy cykl
    TSP_path.append(first)

    return whole_weight, TSP_path


def los_start_node(lista_wierzcholkow, nodes):
    return lista_wierzcholkow[randint(0, nodes - 1)]


def first_next_node(current, odwiedzony, Matrix, nodes, lista_wierzcholkow):                        # pierwszy nieodwiedzony jako najblizszy
    for node1 in range(0,nodes):
        for node2 in range(0,nodes):
            if lista_wierzcholkow[node1] == current and odwiedzony[lista_wierzcholkow[node2]] == False:
                return (Matrix[node1][node2], lista_wierzcholkow[node2])                            # return (weight, node2)
    return (-1, (-1, -1))                                                                           # wszystkie odwiedzone juz

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