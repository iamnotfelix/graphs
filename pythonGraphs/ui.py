
from graph import Graph
from utils import *


class UI:

    def __init__(self) -> None:
        self.graph = None

    def print_menu(self):
        print("Menu:")
        print("1\tCreate new graph.")
        print("2\tRead graph from file.")
        print("3\tWrite graph to file.")

        print("4\tAdd vertex.")
        print("5\tAdd edge.")
        print("6\tRemove vertex.")
        print("7\tRemove edge.")

        print("8\tGet the number of vertices.")
        print("9\tParse the vertices.")
        print("10\tCheck if edge.")
        print("11\tGet degree out.")
        print("12\tGet degree in.")
        print("13\tParse outbound edges.")
        print("14\tParse inbound edges.")
        print("15\tGet cost.")
        print("16\tUpdate cost.")

        print("exit\tExit the application.")


    def create_graph(self):
        nr_vertices = int(input("Number of vertices: "))
        nr_edges = int(input("Number of edges: "))

        self.graph = Graph(nr_vertices, nr_edges)


    def read_file_graph(self):
        file_name = input("Enter path of file: ")

        self.graph = read_graph(file_name)


    def write_file_graph(self):
        file_name = input("Enter path of file: ")

        write_graph(self.graph, file_name)


    def add_vertex(self):
        x = int(input("Vertex: "))
        self.graph.add_vertex(x)


    def add_edge(self):
        x = int(input("Vertex 1: "))
        y = int(input("Vertex 2: "))
        c = int(input("Cost: "))
        self.graph.add_edge(x, y, c)


    def remove_vertex(self):
        x = int(input("Vertex: "))
        self.graph.remove_vertex(x)
        

    def remove_edge(self):
        x = int(input("Vertex 1: "))
        y = int(input("Vertex 2: "))
        self.graph.remove_edge(x, y)


    def get_nr_vertices(self):
        print(self.graph.get_number_of_vertices())


    def parse_vertices(self):
        vertices = ""
        for vertex in self.graph.get_vertices():
            vertices += str(vertex) + " "
        
        print(vertices)


    def check_edge(self):
        x = int(input("Vertex 1: "))
        y = int(input("Vertex 2: "))
        print(self.graph.is_edge(x, y))


    def get_degree_out(self):
        x = int(input("Vertex: "))
        print(self.graph.get_out_degree(x))

    def get_degree_in(self):
        x = int(input("Vertex: "))
        print(self.graph.get_in_degree(x))

    def get_out_edges(self):
        x = int(input("Vertex: "))
        edges = f"{x}: "

        for vertex in self.graph.get_out_bound_edges(x):
            edges += str(vertex) + " "
        
        print(edges)

    def get_in_edges(self):
        x = int(input("Vertex: "))
        edges = f"{x}: "

        for vertex in self.graph.get_in_bound_edges(x):
            edges += str(vertex) + " "
        
        print(edges)

    def get_cost(self):
        x = int(input("Vertex 1: "))
        y = int(input("Vertex 2: "))

        print(self.graph.get_cost(x, y))

    def update_cost(self):
        x = int(input("Vertex 1: "))
        y = int(input("Vertex 2: "))
        c = int(input("New cost: "))

        self.graph.update_cost(x, y, c)

    def command_handler(self):
        commands = {
            "1": self.create_graph,
            "2": self.read_file_graph,
            "3": self.write_file_graph,
            "4": self.add_vertex,
            "5": self.add_edge,
            "6": self.remove_vertex,
            "7": self.remove_edge,
            "8": self.get_nr_vertices,
            "9": self.parse_vertices,
            "10": self.check_edge,
            "11": self.get_degree_out,
            "12": self.get_degree_in,
            "13": self.get_out_edges,
            "14": self.get_in_edges,
            "15": self.get_cost,
            "16": self.update_cost,
            "0": exit
        }

        while True:
            command = input(">>>")
            try:    
                if command in commands:
                    if int(command) > 2 and not self.graph:
                        raise Exception("Create or read a graph first!")
                    commands[command]()
                else:
                    raise Exception("Invalid command!")
            except Exception as ex:
                print(str(ex))


    def start(self):
        self.print_menu()
        self.command_handler()