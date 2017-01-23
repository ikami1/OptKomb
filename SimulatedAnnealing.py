# simulated annealing

from random import randint, random
from math import exp
"""
rozw - najlepsze rozwiazanie greedy algorytmu
T - temp poczatkowa
Tmin - temperatura przy ktorej konczymy wykonywanie programu
r - wspolczynnik o jaki zmniejszamy T
"""


def SimulatedAnnealing(graph, nodes, wynik, rozw, T, Tmin, r):
    i = 0
    naj_wynik = wynik
    naj_rozw = rozw
    while(i<100000):
        i+=1
        nowy_wynik, a, b = losujRozw(graph, nodes, rozw, wynik)
        roznica = nowy_wynik - wynik

        if wynik > nowy_wynik:
            rozw = noweRozw(nodes, rozw, a, b)
            wynik = nowy_wynik
            if nowy_wynik < naj_wynik:
                print("wynik: ", nowy_wynik, "iteracja: ", i)
                naj_rozw = rozw
                naj_wynik = nowy_wynik
        elif random() < exp(-roznica/T):
            rozw = noweRozw(nodes, rozw, a, b)
            wynik = nowy_wynik

        if T > 0.00001:
            T = T * r
        if i%10000==0:
            zapis_do_plikux(wynik,i,r)
    return naj_wynik, naj_rozw





def zapis_do_plikux(wynik, i, r):
    f = open('rozw.txt', 'a')
    f.write(str(r) + " " + str(i) + " " + str(wynik) + "\n")


def losujRozw(graph, nodes, rozw, wynik):                                          # nowe rozwiazanie, zamieniamy miejscami wierzcholki na miejscach x i x+1 w rozw
    x = randint(0, nodes-1)
    y = randint(0, nodes-1)
    while ( x == y):                                                                # losujemy 2 miasta do zamiany
        y = randint(0, nodes - 1)

    stara_dlugosc = graph[rozw[x] - 1][rozw[(x-1) % nodes] - 1] + graph[rozw[y] - 1][rozw[(y+1) % nodes] - 1]
    nowa_dlugosc = graph[rozw[x] - 1][rozw[(y+1) % nodes] - 1] + graph[rozw[y] - 1][rozw[(x-1) % nodes] - 1]
    dlugosc = wynik - stara_dlugosc + nowa_dlugosc

    return dlugosc, x, y


def noweRozw(nodes, rozw1, x, y):
    rozw = rozw1[:]                                 # normalnie wskaznik ale dzieki [:] tworzy nowa liste
    i = x
    j = y
    while (i != j and i != j + 1 and i != j - 1):  # odwracamy kolejnosc miast pomiedzy
        temp = rozw[i]
        rozw[i] = rozw[j]
        rozw[j] = temp
        i = (i + 1) % nodes
        j = (j - 1) % nodes
    if i == j + 1 or i == j - 1:
        temp = rozw[i]
        rozw[i] = rozw[j]
        rozw[j] = temp

    return rozw
