#
#
#
#############
from graphs.graph import Graph
import numpy as np

class AdjacenecySetGraph(Graph):
    """ Represent a graph as an adjacency set. """
    matrix = None
    def __init__(self, num_vertices, directed=False):
        """ first call base constructor, and then set..."""
        super(AdjacenecySetGraph, self).__init__(num_vertices, directed)
    def add_edge(self, v_1, v_2, weight=1):
        """ add conection between vertices v1 and v2 with  provided weight  """
        if v_1 >= self.num_vertices or v_2 >= self.num_vertices or v_1 < 0 or v_2 < 0:
            raise ValueError("Vertices %d and %d are out of bounds" % (v_1, v_2))
        if weight < 1:
            raise ValueError("An edge cannot have wwight less than one")
    def get_adjacent_vertices(self, vertex):
        """ return vertices connected with vertex """
        if vertex < 0 or vertex >= self.num_vertices:
            raise ValueError("Cannot access vertex %d" % vertex)
    def get_indegree(self, vertex):
        """ return number of incoming edges """
        if vertex < 0 or vertex >= self.num_vertices:
            raise ValueError("Cannot access vertex %d" % vertex)
    def get_edge_weight(self, v_1, v_2):
        """ return wieght between vertices v1 and v2 """
        return 1
    def display(self):
        print "A"
