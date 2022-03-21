
import copy
import random


class Graph:

    def __init__(self, nr_vertices = 0, nr_edges = 0) -> None:
        self.__vertices = set()
        self.__in = dict()
        self.__out = dict()
        self.__cost = dict()

        self.__initialize_graph(nr_vertices, nr_edges)


    def __initialize_graph(self, nr_vertices, nr_edges):
        for i in range(nr_vertices):
            self.add_vertex(i)

        for i in range(nr_edges):
            x = random.randint(0, nr_vertices-1)
            y = random.randint(0, nr_vertices-1)
            while self.is_edge(x, y):
                x = random.randint(0, nr_vertices-1)
                y = random.randint(0, nr_vertices-1)
            self.add_edge(x, y, random.randint(0, 1000))


    def add_edge(self, x, y, c=0):
        if self.is_edge(x, y):
            raise Exception("Edge already exists!")

        if not self.is_vertex(x) or not self.is_vertex(y):
            raise Exception("These vertices do not exist!")

        self.__out[x].add(y)
        self.__in[y].add(x)
        self.__cost[(x, y)] = c


    def remove_edge(self, x, y):
        if not self.is_vertex(x) or not self.is_vertex(y):
            raise Exception("These vertices do not exist!")

        if not self.is_edge(x, y):
            raise Exception("Edge does not exist!")

        self.__cost.pop((x,y))
        self.__out[x].remove(y)
        self.__in[y].remove(x)


    def add_vertex(self, x):
        if self.is_vertex(x):
            raise Exception("The vertex already exists!")

        self.__vertices.add(x)
        self.__out[x] = set()
        self.__in[x] = set()


    def remove_vertex(self, x):
        if  not self.is_vertex(x):
            raise Exception("The vertex does not exist!")
        
        left_vertices = copy.deepcopy(self.__out[x])
        for vertex in left_vertices:
            self.remove_edge(x, vertex)

        left_vertices = copy.deepcopy(self.__in[x])
        for vertex in left_vertices:
            self.remove_edge(vertex, x)

        self.__vertices.remove(x)
        self.__out.pop(x)
        self.__in.pop(x)


    def get_number_of_vertices(self):
        return len(self.__vertices)
    

    def get_number_of_edges(self):
        return len(self.__cost)


    def get_vertices(self):
        for vertice in self.__vertices:
            yield vertice


    def is_edge(self, x, y):
        return y in self.__out[x]


    def is_vertex(self, x):
        return x in self.__vertices


    def get_out_degree(self, x):
        if not self.is_vertex(x):
            raise Exception("The vertex does not exist!")
        
        return len(self.__out[x])


    def get_in_degree(self, x):
        if not self.is_vertex(x):
            raise Exception("The vertex does not exist!")
        
        return len(self.__in[x])


    def get_out_bound_edges(self, x):
        if not self.is_vertex(x):
            raise Exception("The vertex does not exist!")
        
        for vertex in self.__out[x]:
            yield vertex


    def get_in_bound_edges(self, x):
        if not self.is_vertex(x):
            raise Exception("The vertex does not exist!")

        for vertex in self.__in[x]:
            yield vertex


    def get_cost(self, x, y):
        if not self.is_vertex(x) or not self.is_vertex(y):
            raise Exception("These vertices do not exist!")

        if not self.is_edge(x, y):
            raise Exception("Edge does not exist!")

        return self.__cost[(x, y)]


    def update_cost(self, x, y, newCost):
        if not self.is_vertex(x) or not self.is_vertex(y):
            raise Exception("These vertices do not exist!")

        if not self.is_edge(x, y):
            raise Exception("Edge does not exist!")

        self.__cost[(x, y)] = newCost


    def copy(self):
        return copy.deepcopy(self)
