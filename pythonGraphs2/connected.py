
from graph import Graph

def dfs(graph: Graph, current ,visited, components) -> None:
    """
        Traverses the graph recursively in depth.
            graph: Graph - the graph to be traversed
            current: int - the starting node
            visited: list - list that keeps track of the visited nodes
            components: list - list that will store the vertices from one component
    """
    visited[current] = True
    components.append(current)

    for vertex in graph.get_out_bound_edges(current):
        if not visited[vertex]:
            dfs(graph, vertex, visited, components)


def create_graph(graph: Graph, component: list) -> Graph:
    """
        Creates a graph from a given set of vertices and the initial graph.
            graph: Graph - initial graph
            component: list - list of vertices
        Returns a Graph object.
    """
    graph_component = Graph()

    for vertex in component:
        graph_component.add_vertex(vertex)

    for vertex in component:
        for out in graph.get_out_bound_edges(vertex):
            graph_component.add_edge(vertex, out, graph.get_cost(vertex, out))
    
    return graph_component


def get_connected_components(graph: Graph) -> list:
    """
        Gets all the connected components, of an undirected graph, as Graph objects.
            graph: Graph - the initial graph
        Returns a list containing the connected components as Graph objects.
    """
    if graph.get_number_of_vertices() == 0:
        raise Exception("The graph is empty!")

    # Initializing the needed lists
    components = list()
    visited = [False for _ in range(graph.get_number_of_vertices())]

    for vertex in graph.get_vertices():
        # If there is a node that was not visited, a DFS is started from that node
        # and the visited list will be updated correspondingly.
        if not visited[vertex]:
            component = list()
            dfs(graph, vertex, visited, component)
            graph_component = create_graph(graph, component)
            components.append(graph_component)

    return components
