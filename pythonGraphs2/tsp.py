from graph import Graph
import copy

def TSP(graph: Graph, current: int, visited: list, start_node: int, children: list)->int:
    visited[current] = 1
    if sum(visited) == graph.get_number_of_vertices() and graph.is_edge(current, start_node):
        # children[start_node] = current
        return graph.get_cost(current, start_node), children
    else:
        cost = 1000000000
        survived_branch = list()
        for vertex in graph.get_out_bound_edges(current):
            if visited[vertex] == 0 and vertex != start_node:
                branch_cost, branch_children = TSP(graph, vertex, copy.deepcopy(visited), start_node, copy.deepcopy(children))
                branch_children[current] = vertex 
                if cost > branch_cost + graph.get_cost(current, vertex):
                    cost = graph.get_cost(current, vertex) + branch_cost
                    survived_branch = copy.deepcopy(branch_children)
        children = copy.deepcopy(survived_branch)
        return cost, children