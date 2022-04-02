
from graph import Graph

def dfs(graph: Graph, current ,visited, components) -> None:
        visited[current] = True
        components.append(current)

        for vertex in graph.get_out_bound_edges(current):
            if not visited[vertex]:
                dfs(graph, vertex, visited, components)


def create_graph(graph: Graph, component: list) -> Graph:
    graph_component = Graph()

    for vertex in component:
        graph_component.add_vertex(vertex)

    for vertex in component:
        for out in graph.get_out_bound_edges(vertex):
            graph_component.add_edge(vertex, out, graph.get_cost(vertex, out))
    
    return graph_component


def get_connected_components(graph: Graph) -> list:
    if graph.get_number_of_vertices() == 0:
        raise Exception("The graph is empty!")

    components = list()
    visited = [False for _ in range(graph.get_number_of_vertices())]

    for vertex in graph.get_vertices():
        if not visited[vertex]:
            component = list()
            dfs(graph, vertex, visited, component)
            graph_component = create_graph(graph, component)
            components.append(graph_component)

    return components
