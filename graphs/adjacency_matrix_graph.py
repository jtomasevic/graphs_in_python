#
#
#
#############
from graphs.graph import Graph
import numpy as np

class AdjacenecyMatrixGraph(Graph):
    """ Represent a graph as an adjacency matrix. """
    matrix = None
    def __init__(self, num_vertices, directed=False):
        """ first call base constructor, and then set matrix"""
        super(AdjacenecyMatrixGraph, self).__init__(num_vertices, directed)
        self.matrix = np.zeros((num_vertices, num_vertices))
    def add_edge(self, v_1, v_2, weight=1):
        """ add conection between vertices v1 and v2 with  provided weight  """
        if v_1 >= self.num_vertices or v_2 >= self.num_vertices or v_1 < 0 or v_2 < 0:
            raise ValueError("Vertices %d and %d are out of bounds" % (v_1, v_2))
        if weight < 1:
            raise ValueError("An edge cannot have wwight less than one")
        self.matrix[v_1][v_2] = weight
        if not self.directed:
            self.matrix[v_2][v_1] = weight
    def get_adjacent_vertices(self, vertex):
        """ return vertices connected with vertex """
        if vertex < 0 or vertex >= self.num_vertices:
            raise ValueError("Cannot access vertex %d" % vertex)
        adjacent_vertices = []
        for i in range(self.num_vertices):
            if self.matrix[vertex][i] > 0:
                adjacent_vertices.append(i)
        return adjacent_vertices
    def get_indegree(self, vertex):
        """ In short: number of incoming edges.
            Number of edges that flow into provided node:vertex
            In the case of direceted graph definition would be:
            Number of directed edges that directly flow into the node.
            Which means on how many nodes this node depends on. This is important
            for topological sort
        """
        if vertex < 0 or vertex >= self.num_vertices:
            raise ValueError("Cannot access vertex %d" % vertex)
        indegree = 0
        for i in range(self.num_vertices):
            if self.matrix[i][vertex] > 0:
                indegree = indegree + 1
        return indegree
    def get_edge_weight(self, v_1, v_2):
        """ return wieght between vertices v1 and v2 """
        return self.matrix[v_1][v_2]
    def display(self):
        for i in range(self.num_vertices):
            for v in self.get_adjacent_vertices(i):
                print(i, "-->", v)
