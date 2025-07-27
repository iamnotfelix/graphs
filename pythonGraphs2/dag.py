
import queue
import string
from graph import Graph
import tabulate

def read_activities(filename: string)->tuple:
    with open(filename, "r") as f:
        n = int(f.readline())
        duration = [0 for _ in range(n)]
        graph = Graph(n)
        for _ in range(0, n):
            line = f.readline().split()
            to_vertex = int(line[0])
            duration[to_vertex] =int(line[1])
            line = line[2:]
            for from_vertex in line:
                graph.add_edge(int(from_vertex), to_vertex)
    return graph, duration


def topological_sort(graph: Graph, duration: list)->list:
    sorted_list = list()
    free = queue.Queue()

    count = [0 for _ in range(graph.get_number_of_vertices())]
    earliest = [0 for _ in range(graph.get_number_of_vertices())]

    for vertex in graph.get_vertices():
        count[vertex] = graph.get_in_degree(vertex)
        if count[vertex] == 0:
            earliest[vertex] = 0
            free.put(vertex)

    while not free.empty():
        x = free.get()

        sorted_list.append(x)

        for vertex in graph.get_out_bound_edges(x):
            count[vertex] -= 1
            earliest[vertex] = max(earliest[vertex], earliest[x] + duration[x])
            if count[vertex] == 0:
                free.put(vertex)

    if len(sorted_list) < graph.get_number_of_vertices():
        sorted_list = []
    
    return sorted_list, earliest


def solve_schedule(filename: string)->None:
    graph, duration = read_activities(filename)
    sorted_list, earliest = topological_sort(graph, duration)

    if len(sorted_list) > 0:
        latest = [9999999 for _ in range(graph.get_number_of_vertices())]
        the_latest = -1
        for i, val in enumerate(earliest):
            the_latest = max(the_latest, val + duration[i])

        for x in sorted_list:
            if graph.get_out_degree(x) == 0:
                latest[x] = the_latest
            for vertex in graph.get_out_bound_edges(x):
                latest[x] = min(latest[x], earliest[vertex])
        
        table = [["Action", "Duration", "Earliest", "Latest", "Is critical"]]
        for i in range(0, len(sorted_list)):
            early_string = f"{earliest[sorted_list[i]]}-{earliest[sorted_list[i]] + duration[sorted_list[i]]}"
            late_string = f"{latest[sorted_list[i]] - duration[sorted_list[i]]}-{latest[sorted_list[i]]}"
            is_critical = (early_string == late_string)
            arr = [sorted_list[i], duration[sorted_list[i]], early_string, late_string, is_critical]
            table.append(arr)

        print(f"Total time: {the_latest}")
        print(tabulate.tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
 
    else:
        print("The graph contains cycles!")

# problem 6