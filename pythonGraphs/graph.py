
import copy
import random


class Graph:

    def __init__(self, nr_vertices = 0, nr_edges = 0) -> None:
        self.__vertices = set()
        self.__in = dict()
        self.__out = dict()
        self.__cost = dict()

        if nr_edges != 0:
            if (nr_vertices * (nr_vertices + 1) / 2) < nr_edges:
                raise Exception("Graph is not possible!")

        self.__initialize_graph(nr_vertices, nr_edges)

    def __initialize_graph(self, nr_vertices, nr_edges):
        """
            Initializes the graph with random edges.
                nr_veritces: int - number of vertices
                nr_edges: int - number of edges
        """
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
        """
            Adds an edge to the graph.
                x: int - start vertex
                y: int - end vertex
                c: int - cost of the edge
            Raises error if vertices do not exist or if the edge already exists. 
        """
        if not self.is_vertex(x) or not self.is_vertex(y):
            raise Exception("These vertices do not exist!")

        if self.is_edge(x, y):
            raise Exception("Edge already exists!")

        self.__out[x].add(y)
        self.__in[y].add(x)
        self.__cost[(x, y)] = c


    def remove_edge(self, x, y):
        """
            Removes an edge from the graph.
                x: int - start vertex
                y: int - end vertex
            Raises error if vertices do not exist or if the edge already exists. 
        """
        if not self.is_vertex(x) or not self.is_vertex(y):
            raise Exception("These vertices do not exist!")

        if not self.is_edge(x, y):
            raise Exception("Edge does not exist!")

        self.__cost.pop((x,y))
        self.__out[x].remove(y)
        self.__in[y].remove(x)


    def add_vertex(self, x):
        """
            Adds vertex to the graph.
                x: int - vertex
            Raises error if the vertex already exists.
        """
        if self.is_vertex(x):
            raise Exception("The vertex already exists!")

        self.__vertices.add(x)
        self.__out[x] = set()
        self.__in[x] = set()


    def remove_vertex(self, x):
        """
            Removes a vertex, and all in bound and out bound edges of that vertex, from the graph.
                x: int - vertex
            Raises error if vertex does not exist.
        """
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
        """
            Returns the number of vertices.
        """
        return len(self.__vertices)
    

    def get_number_of_edges(self):
        """
            Returns the number of edges.
        """
        return len(self.__cost)


    def get_vertices(self):
        """
            Vertex interator, yields all the vertices from the graph.
        """
        for vertice in self.__vertices:
            yield vertice


    def is_edge(self, x, y):
        """
            Checks if an edge exists.
                x: int - start vertex
                y: int - end vertex
            Returns true if exists and false otherwise.
        """
        return y in self.__out[x]


    def is_vertex(self, x):
        """
            Checks if a vertex exists.
                x: int - vertex
            Returns true if exists and false otherwise.
        """
        return x in self.__vertices


    def get_out_degree(self, x):
        """
            Returns the out degree of a vertex.
                x: int - vertex
            Raises an error if the vertex does not exist.
        """
        if not self.is_vertex(x):
            raise Exception("The vertex does not exist!")
        
        return len(self.__out[x])


    def get_in_degree(self, x):
        """
            Returns the in degree of a vertex.
                x: int - vertex
            Raises an error if the vertex does not exist.
        """
        if not self.is_vertex(x):
            raise Exception("The vertex does not exist!")
        
        return len(self.__in[x])


    def get_out_bound_edges(self, x):
        """
            Out bound edges iterator, yields all the out bound edges of a vertex.
                x: int - vertex
             Raises an error if the vertex does not exist.
        """
        if not self.is_vertex(x):
            raise Exception("The vertex does not exist!")
        
        for vertex in self.__out[x]:
            yield vertex


    def get_in_bound_edges(self, x):
        """
            In bound edges iterator, yields all the in bound edges of a vertex.
                x: int - vertex
             Raises an error if the vertex does not exist.
        """
        if not self.is_vertex(x):
            raise Exception("The vertex does not exist!")

        for vertex in self.__in[x]:
            yield vertex


    def get_cost(self, x, y):
        """
            Returns the cost of an edge.
                x: int - start vertex
                y: int - end vertex
            Raises error if vertices do not exist or if the edge does not exist. 
        """
        if not self.is_vertex(x) or not self.is_vertex(y):
            raise Exception("These vertices do not exist!")

        if not self.is_edge(x, y):
            raise Exception("Edge does not exist!")

        return self.__cost[(x, y)]


    def update_cost(self, x, y, newCost):
        """
            Updates the cost of an edge.
                x: int - start vertex
                y: int - end vertex
                newCost: int - new cost of the edge
            Raises error if vertices do not exist or if the edge does not exist. 
        """
        if not self.is_vertex(x) or not self.is_vertex(y):
            raise Exception("These vertices do not exist!")

        if not self.is_edge(x, y):
            raise Exception("Edge does not exist!")

        self.__cost[(x, y)] = newCost


    def copy(self):
        """
            Returns a deepcopy of the graph.
        """
        return copy.deepcopy(self)
