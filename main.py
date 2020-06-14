from _graph.GraphPro import GraphPro as g
from time import time
import os
from Metodo import *

#Desarrolla los puntos para mirar los profesores y ordenarlos, junto a que no cruce sus clases
Comparacion()

os.system('clear')
print("<--------Test Floyd-Warshall------->\n")

weights = [1, 2, 3, 4, 5]
#graph = g.creategraph(6, .75, weights, directed=False)
sources = [0, 1, 0, 2, 0, 3, 0, 5, 1, 2, 1, 3, 1, 4, 1, 5, 2, 3, 2, 4, 3, 4, 3, 5, 4, 5]
targets = [1, 0, 2, 0, 3, 0, 5, 0, 2, 1, 3, 1, 4, 1, 5, 1, 3, 2, 4, 2, 4, 3, 5, 3, 5, 4]
weights = [2, 2, 2, 2, 4, 4, 1, 1, 3, 3, 2, 2, 4, 4, 4, 4, 2, 2, 1, 1, 3, 3, 5, 5, 1, 1]
graph = g(sources, targets, weights)

graph.print_r()
print('.........................')
t = time()
print(graph.floyd_warshall())
elapsed = time() - t
print("Time: ", elapsed)

materias,objeto,idProfesor = Materias()
print(materias)
print(idProfesor)
graph.draw()

def create_network(self, source, target, weight):

    self.graph = nx.DiGraph()
    count = len(source)

    edges = []

    for i in range(0, count):
        edges.append( (source[i], target[i], weight[i]) )

    self.graph.add_weighted_edges_from(edges)
    return self.graph

def print_distances(self):
    printt = ""
    for i in self.distances:
        printt = printt + str(i) + ": \t"
        for j in self.distances[i]:
            printt = printt + str(self.distances[i][j]) + "\t"
        printt = printt + "\n"
    print("\n------------------------------------")
    print(printt)
    return
