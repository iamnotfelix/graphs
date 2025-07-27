
from graph import Graph


def shortest_walk(graph: Graph, src: int, des: int) -> int:
    """
        Computes the shortest walk from a vertex to another vertex.
            graph: Graph - the initial graph
            src: int - the source vertex
            des: int - the destination vertex
        Returns the shortest walk from the source vertex to the destination vertex.
        Raises exception if the graph contains negative cost cycles.
    """
    if not graph.is_vertex(src) or not graph.is_vertex(des):
        raise Exception("Cannot find these vertices!")

    max_int = 100000000
    d = [ [max_int for _ in range(graph.get_number_of_vertices() - 1)] for _ in range(graph.get_number_of_vertices())]
    #print(d)
    
    for i in range(graph.get_number_of_vertices() - 1):
        d[src][i] = 0

    for k in range(graph.get_number_of_vertices() - 1):
        for edge in graph.get_edges():
            x = edge[0]
            y = edge[1]
            cost = graph.get_cost(x, y)
            if (d[x][k] != max_int and d[y][k] > d[x][k] + cost):
                d[y][k] = d[x][k] + cost
                if k != graph.get_number_of_vertices() - 2:
                    d[y][k+1] = d[y][k]

    k = graph.get_number_of_vertices() - 2
    for edge in graph.get_edges():
            x = edge[0]
            y = edge[1]
            cost = graph.get_cost(x, y)
            if (d[x][k] != max_int and d[y][k] > d[x][k] + cost):
                raise Exception("Graph contains negative cycles!")
    
    return d[des][k]
