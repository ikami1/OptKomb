# Reprezentacja grafu

from random import randint
from math import sqrt, inf
from greedy import greedy, greedyWithFirst
from SimulatedAnnealing import SimulatedAnnealing


def main():
    # nodes = int(input('Podaj liczbe wierzcholkow: '))
    # rozmiar = int(input('Podaj maksymalny rozmiar wspolrzednej: '))
    # losuj(nodes, rozmiar)

    plik = open('dane.txt','r')
    nodes = int(plik.readline())

    graph = [[i for i in range(nodes)] for _ in range(nodes)]
    coordinates = list(range(nodes))
    odwiedzony = list(range(nodes))

    for i in range(1, nodes+1):
        linia = plik.readline()
        dane = linia.split()
        wsp_x = int(dane[1])
        wsp_y = int(dane[2])
        coordinates[i-1] = (wsp_x, wsp_y)

    for i in range(nodes):                             # dodawanie krawedzi
        for j in range(i+1):
            add_edge(graph, coordinates, i, j)

    for i in range(nodes):                              # ustawiamy wszystkie wierzcholki na nieodwiedzone
        odwiedzony[i] = False

    naj = inf
    rozw = []
    for i in range(nodes):                              # naj - najlepszy wynik greedy przy startowaniu z wszystkich wierzcholkow
        wynik, rozwGreedy = greedyWithFirst(graph, nodes, odwiedzony, i)
        if wynik < naj:
            naj = wynik
            rozw = rozwGreedy


    r = 0.999
    T = 100.0
    Tmin = 1.0
    print(naj, rozw)
    wynik, rozwAnnealing = SimulatedAnnealing(graph, nodes, naj, rozw, T, Tmin, r)
        if wynik < naj:
            naj = wynik
            rozw = rozwAnnealing

    zapis_do_pliku(coordinates, nodes, rozw)
    print()


def zapis_do_pliku(coordinates, nodes, rozw):
    f = open('dane1.txt', 'w')
    f.write(str(nodes))
    for i in rozw:
        (x, y) = coordinates[i - 1]
        f.write(str(i - 1) + ' ' + str(x) + ' ' + str(y) + '\n')

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
            ile += 1
            f.write(str(ile)+' '+str(wsp_x)+' '+str(wsp_y)+'\n')


def add_edge(graph, coordinates, i, j):                     # i,j numery wierzcholkow
    if i == j:
        graph[i][j] = inf                                   # inf - infinity
        return
    (x1, y1) = coordinates[i]
    (x2, y2) = coordinates[j]

    weight = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))

    graph[i][j] = graph[j][i] = weight

main()
