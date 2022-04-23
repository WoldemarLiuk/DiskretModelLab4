import numpy as np

# Цей клас представляє орієнтований граф, записаний у матричній формі
class Graph:

    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(graph)


    #Повертає true якщор є шлях з витоку до стоку в залишковому графі
    #Заповнює parent[] для збереження маршруту
    def BFS(self, s, t, parent):

        # Позначає всі вершини як невідвідані
        visited = [False] * (self.ROW)

        # Черга для пошуку
        queue = []

        # Позначає вершину витоку як відвідану і додає її в чергу
        queue.append(s)
        visited[s] = True

        while queue:
            # виклачає вершину з черги
            u = queue.pop(0)

            # Отримує всі суміжні вершини до виведеної з черги вершини u
            # Якщо сусідня вершина не відвідана, позначає її як відвідувану та ставить в чергу
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    # Якщо знайдено зв'язок зі стоком,
                    # пошук припиняється
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
                    if ind == t:
                        return True

        # Якщо стоку не досягнуто, то повертає false
        return False

    # Повертає максимальний потік від витоку до стоку в даному графі
    def FordFulkerson(self, source, sink):

        # Цей масив зберігає пройдений шлях
        parent = [-1] * (self.ROW)

        max_flow = 0  # В початковий момент потік відсутній

        # Потік збільшується, поки є шлях від витоку до стоку
        while self.BFS(source, sink, parent):

            # Знаходить максимальний потік для знайденого шляху.
            path_flow = float("Inf")
            s = sink
            while (s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Додати потік шляху до загального потоку
            max_flow += path_flow

            # Оновлює залишкові ємності ребер вздовж шляху
            v = sink
            while (v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow

graph = np.loadtxt('D:\l4-1.txt', dtype='i', delimiter=' ', skiprows=1)
print('Матриця графа:')
print(graph)

g = Graph(graph)

source = 0
sink = 7

print("\nВершина витоку: %d " % source)
print("Вершина стоку: %d " % sink)

print("Максимальний потік для даного графа: %d " % g.FordFulkerson(source, sink))