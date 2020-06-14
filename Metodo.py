import csv
from Profesor import *

def create_network(self, source, target, weight):

    self.graph = nx.DiGraph()
    count = len(source)

    edges = []

    for i in range(0, count):
        edges.append( (source[i], target[i], weight[i]) )

    self.graph.add_weighted_edges_from(edges)
    return self.graph


def floyd_warshall(self):
    nodes = list(self.graph.nodes)

    for i in nodes:
        dict_i = {}
        for j in nodes:
            if i == j:
                dict_i[j] = 0
                continue
            try:
                dict_i[j] = self.graph[i][j]['weight']
            except:
                dict_i[j] = float("inf")

        self.distances[i] = dict_i

    for i in nodes:
        for j in nodes:
            for k in nodes:
                ij = self.distances[i][j]
                ik = self.distances[i][k]
                kj = self.distances[k][j]

                if ij > ik + kj:
                    self.distances[i][j] = ik + kj

    return self.distances

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

def Materias():
  lista = []
  lista2 = []
  id1 = []
  c=open('pa20192.csv','r')
  with c:
    lector=csv.reader(c,delimiter=',')

    for lineas in lector:
      materia = lineas[0]
      idP = int(lineas[2])
      dia = lineas[3]
      horaI = lineas[4]
      horaF = lineas[5]
      Inver = Profesor(materia,idP,dia,horaI,horaF)
      lista2.append(Inver)
      lista.append(materia)
      id1.append(idP)
  id1 = list(map(int, id1))
  id2 = set(id1)
  id3 = sorted(id2)
  listaSinRepetidos = set(lista)
  lista4 = sorted(listaSinRepetidos)
  return lista4,lista2,id3

def Comparacion():
    materia,profesor,idP = Materias()
    profesor.sort(key=lambda x: x.id)
    profesor2 = profesor
    cont2 = 0
    for a in idP:
        cont = 0
        #print(a)
        for b in profesor:
            if cont < len(profesor):
                if a != profesor[cont].getId():
                    break;                
                else:
                    if profesor[cont].getDia() == profesor[cont+1].getDia():
                        if profesor[cont].getHoraI() == profesor[cont+1].getHoraI():
                            if profesor[cont].getMateria() != profesor[cont+1].getMateria():
                                profesor2.pop(cont2)
                                print("Hay un problema con un profesor")
                                print(str(profesor[cont].getId())+ " " + profesor[cont].getDia() + " " + profesor[cont].getMateria() + " " + profesor[cont].getHoraI())
                                print(str(profesor[cont+1].getId())+ " " + profesor[cont].getDia() + " " + profesor[cont+1].getMateria() + " " + profesor[cont+1].getHoraI())
                        else:
                            if profesor[cont].getHoraF() == profesor[cont+1].getHoraF():
                                if profesor[cont].getMateria() != profesor[cont+1].getMateria():
                                    profesor2.pop(cont2)
                                    print("Hay un problema con un profesor")
                                    print(str(profesor[cont].getId())+ " " + profesor[cont].getDia()+ " " + profesor[cont].getMateria() + " " + profesor[cont].getHoraF())
                                    print(str(profesor[cont+1].getId())+ " " + profesor[cont].getDia() + " " + profesor[cont+1].getMateria() + " " + profesor[cont+1].getHoraF())
            profesor.pop(cont)
            cont = cont + 1
            cont2 = cont2 + 1
    print("Todos los profesores fueron ordenados y clasificados")

