
def funkcja():
    graph = {}
    for i in range(10):
        graph[i] = [(i,i)]

    for node in graph:
        print(graph[node])

funkcja()