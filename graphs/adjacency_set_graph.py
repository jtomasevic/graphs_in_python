"""
Represents a graph as an adjacency set. Graph is represent as list of Nodes.
Each node has set of adjacent vertices.
This implementation covers only unweighted edges.
"""
from graphs.graph import Graph
from graphs.node import Node

class AdjacenecySetGraph(Graph):
    """ Represent a graph as an adjacency set. """
    matrix = None
    vertex_list = []
    def __init__(self, num_vertices, directed=False):
        """ first call base constructor, and then set..."""
        super(AdjacenecySetGraph, self).__init__(num_vertices, directed)
        self.vertex_list = []
        for i in range(num_vertices):
            self.vertex_list.append(Node(i))
    def add_edge(self, vertex_a, vertex_b, weight=1):
        """ add conection between vertices v1 and v2 with  provided weight  """
        # check constrains
        if (vertex_a >= self.num_vertices or vertex_b >= self.num_vertices
                or vertex_a < 0 or vertex_b < 0):
            raise ValueError("Vertices %d and %d are out of bounds" % (vertex_a, vertex_b))
        if weight != 1:
            raise ValueError("This graph implmentation doesn't support wighted edges")
        # add vertex b to set adjacency set of vertex a
        self.vertex_list[vertex_a].add_edge(vertex_b)
        # if graph is not directed then we need to add edge from b to a also
        if not self.directed:
            self.vertex_list[vertex_b].add_edge(vertex_a)
    def get_adjacent_vertices(self, vertex):
        """ return vertices connected with vertex """
        # check constrains
        if vertex < 0 or vertex >= self.num_vertices:
            raise ValueError("Cannot access vertex %d" % vertex)
        # just refer to provided vertex and return its adjacent vertices set
        return self.vertex_list[vertex].get_adjacent_vertices()
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
        # how many nodes has edge to the provided node
        for i in range(self.num_vertices):
            if vertex in self.get_adjacent_vertices(i):
                indegree = indegree + 1
        return indegree
    def get_edge_weight(self, v_1, v_2):
        """ return wieght between vertices v1 and v2 """
        return 1
    def display(self):
        for i in range(self.num_vertices):
            for vertex in self.get_adjacent_vertices(i):
                print(i, "-->", vertex)
