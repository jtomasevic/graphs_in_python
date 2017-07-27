""" Define abstract class to represent graph """
from abc import ABCMeta, abstractmethod

class Graph:
    """ Abstract class to represent Graph """
    __metaclass__ = ABCMeta
    def __init__(self, num_vertices, directed=False):
        """ constructor """
        self.num_vertices = num_vertices
        self.directed = directed
    @abstractmethod
    def add_edge(self, vertex_a, vertex_b, weight):
        """ add conection between vertices v1 and v2 with  provided weight  """
        pass
    @abstractmethod
    def get_adjacent_vertices(self, vertex):
        """ return vertices connected with vertex """
        pass
    @abstractmethod
    def get_indegree(self, vertex):
        """ In short: number of incoming edges.
            Number of edges that flow into provided node:vertex
            In the case of direceted graph definition would be:
            Number of directed edges that directly flow into the node.
            Which means on how many nodes this node depends on. This is important
            for topological sort
        """
        pass
    @abstractmethod
    def get_edge_weight(self, v_1, v_2):
        """ return wieght between vertices v1 and v2 """
        pass
    @abstractmethod
    def display(self):
        """ show graph in some way """
        pass
