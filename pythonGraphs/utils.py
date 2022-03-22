
import random
from graph import Graph


def read_graph(file_name):
    with open(file_name, "r") as f:
        n, m = f.readline().split()
        graph = Graph(int(n))
        for i in range(int(m)):
            x, y, c = f.readline().split()
            graph.add_edge(int(x), int(y), int(c))
    return graph

def write_graph(graph, file_name):
    with open(file_name, "w+") as f:
        f.write(f"{graph.get_number_of_vertices()} {graph.get_number_of_edges()}\n")
        for x in graph.get_vertices():
            for y in graph.get_out_bound_edges(x):
                f.write(f"{x} {y} {graph.get_cost(x, y)}\n")
