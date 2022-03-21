
import unittest

from graph import Graph
from utils import *

class TestGraph(unittest.TestCase):

    def test_add_edge(self):
        graph = Graph(3)
        self.assertTrue(graph.get_number_of_vertices() == 3)


        self.assertTrue(graph.get_number_of_edges() == 0)
        graph.add_edge(0, 2, 1)
        self.assertTrue(graph.get_number_of_edges() == 1)
        self.assertTrue(graph.get_cost(0, 2) == 1)
        graph.add_edge(1, 2)
        self.assertTrue(graph.get_number_of_edges() == 2)
        self.assertTrue(graph.get_cost(1, 2) == 0)

        with self.assertRaises(Exception) as ex:
            graph.add_edge(1, 2, 1)
        self.assertTrue(str(ex.exception) == "Edge already exists!\n")

        with self.assertRaises(Exception) as ex:
            graph.add_edge(1, 3, 4)
        self.assertTrue(str(ex.exception) == "These vertices do not exist!\n")


    def test_remove_edge(self):
        graph = Graph(10)
        self.assertTrue(graph.get_number_of_vertices() == 10)

        graph.add_edge(1, 2, 3)
        graph.add_edge(2, 3, 4)
        graph.add_edge(3, 4, 5)
        self.assertTrue(graph.get_number_of_edges() == 3)

        with self.assertRaises(Exception) as ex:
            graph.remove_edge(10, 11)
        self.assertTrue(str(ex.exception) == "These vertices do not exist!\n")

        with self.assertRaises(Exception) as ex:
            graph.remove_edge(4, 5)
        self.assertTrue(str(ex.exception) == "Edge does not exist!\n")

        graph.remove_edge(3, 4)
        self.assertTrue(graph.get_number_of_edges() == 2)
        graph.remove_edge(2, 3)
        self.assertTrue(graph.get_number_of_edges() == 1)
        graph.remove_edge(1, 2)
        self.assertTrue(graph.get_number_of_edges() == 0)


    def test_add_vertex(self):
        graph = Graph(10)
        self.assertTrue(graph.get_number_of_vertices() == 10)

        graph.add_vertex(10)
        self.assertTrue(graph.get_number_of_vertices() == 11)
        
        graph.add_vertex(11)
        self.assertTrue(graph.get_number_of_vertices() == 12)
        
        graph.add_vertex(12)
        self.assertTrue(graph.get_number_of_vertices() == 13)

        with self.assertRaises(Exception) as ex:
            graph.add_vertex(0)
        self.assertTrue(str(ex.exception) == "The vertex already exists!\n")


    
    def test_remove_vertex(self):
        graph = Graph(10)
        self.assertTrue(graph.get_number_of_vertices() == 10)
        graph.add_edge(0, 1)
        graph.add_edge(1, 2)

        graph.remove_vertex(0)
        self.assertTrue(graph.get_number_of_vertices() == 9)
        self.assertTrue(graph.get_number_of_edges() == 1)
        
        graph.remove_vertex(1)
        self.assertTrue(graph.get_number_of_vertices() == 8)
        self.assertTrue(graph.get_number_of_edges() == 0)
        
        graph.remove_vertex(2)
        self.assertTrue(graph.get_number_of_vertices() == 7)

        with self.assertRaises(Exception) as ex:
            graph.remove_vertex(0)
        self.assertTrue(str(ex.exception) == "The vertex does not exist!\n")


    def test_get_vertices(self):
        graph = Graph(10)

        x = 0
        for vertex in graph.get_vertices():
            self.assertTrue(x == vertex)
            x += 1


    def test_get_out_bound_edges(self):
        graph = Graph(5)

        graph.add_edge(0, 1)
        graph.add_edge(0, 2)
        graph.add_edge(0, 3)
        graph.add_edge(0, 4)
        graph.remove_edge(0, 1)

        x = 2
        for vertex in graph.get_out_bound_edges(0):
            self.assertTrue(x == vertex)
            x += 1


    def test_get_in_bound_edges(self):
        graph = Graph(5)

        graph.add_edge(1, 0)
        graph.add_edge(2, 0)
        graph.add_edge(3, 0)
        graph.add_edge(4, 0)
        graph.remove_edge(1, 0)

        x = 2
        for vertex in graph.get_in_bound_edges(0):
            self.assertTrue(x == vertex)
            x += 1

    
    def test_update_cost(self):
        graph = Graph(5)

        graph.add_edge(0, 1, 4)
        self.assertTrue(graph.get_cost(0, 1) == 4)
        
        graph.update_cost(0, 1, 5)
        self.assertTrue(graph.get_cost(0, 1) == 5)


if __name__ == "__main__":
    unittest.main()