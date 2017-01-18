# greedy algorytm

from random import randint


def greedy(graph, nodes, odwiedzony):               # greedy z losowym miejscem startu

    first = randint(0, nodes-1)
    odwiedzony[first] = True
    current = first                                 # aktualny wierzcholek, od niego szukamy nastepnego

    whole_weight = 0                                # koszt przejscia grafu
    TSP_path = [first]                              # kolejne odwiedzone wierzcholki

    while True:
        min_weight, next = first_next_node(current, odwiedzony, nodes, graph)    # pierwszy nieodwiedzony jako najblizszy
        if min_weight == -1:                        # wszystkie wierzcholki juz odwiedzone
            break

        for i in range(nodes):                          # sprawdzamy czy jest jakis blizszy current niz next
            if (odwiedzony[i] == False) and (min_weight > graph[current][i]):
                min_weight = graph[current][i]
                next = i

        odwiedzony[next] = True                     # idziemy do nastepnego
        whole_weight += graph[current][next]
        TSP_path.append(next+1)
        current = next

    whole_weight += graph[current][first]          # zamykamy cykl
    # TSP_path.append(first+1)                       idziemy do pierwszego ale nie pokazujemy tego

    return whole_weight, TSP_path


def greedyWithFirst(graph, nodes, odwiedzony, first):        # greedy z wybranum miejscem startu

    odwiedzony[first] = True
    current = first                                 # aktualny wierzcholek, od niego szukamy nastepnego

    whole_weight = 0                                # koszt przejscia grafu
    TSP_path = [first+1]                              # kolejne odwiedzone wierzcholki

    while True:
        min_weight, next = first_next_node(current, odwiedzony, nodes, graph)    # pierwszy nieodwiedzony jako najblizszy
        if min_weight == -1:                        # wszystkie wierzcholki juz odwiedzone
            break

        for i in range(nodes):                          # sprawdzamy czy jest jakis blizszy current niz next
            if (odwiedzony[i] == False) and (min_weight > graph[current][i]):
                min_weight = graph[current][i]
                next = i

        odwiedzony[next] = True                     # idziemy do nastepnego
        whole_weight += graph[current][next]
        TSP_path.append(next+1)
        current = next

    whole_weight += graph[current][first]          # zamykamy cykl
    # TSP_path.append(first+1)                      idziemy do pierwszego ale nie pokazujemy tego

    return whole_weight, TSP_path


def first_next_node(current, odwiedzony, nodes, graph):      # pierwszy nieodwiedzony jako najblizszy
    for i in range(nodes):
        if odwiedzony[i] == False:
            return (graph[current][i], i)                     # return (weight, node_next)
    return (-1, -1)                                           # wszystkie odwiedzone juz
