""" module description """
from abc import ABCMeta, abstractmethod


class Graph:
    """ Abstract class to represent Graph """
    __metaclass__ = ABCMeta
    def __init__(self, num_vertices, directed=False):
        """ constructor """
        self.num_vertices = num_vertices
        self.directed = directed
    @abstractmethod
    def add_edge(self, v_1, v_2, weight):
        """ add conection between vertices v1 and v2 with  provided weight  """
        pass
    @abstractmethod
    def get_adjacent_vertices(self, vertex):
        """ return vertices connected with vertex """
        pass
    @abstractmethod
    def get_indegree(self, vertex):
        """ return number of edges """
        pass
    @abstractmethod
    def get_edge_weight(self, v_1, v_2):
        """ return wieght between vertices v1 and v2 """
        pass
    @abstractmethod
    def display(self):
        """ show graph in some way """
        pass
