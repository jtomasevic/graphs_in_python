""" node in graph """

class Node(object):
    """ node in graph """
    adjacency_set = None
    def __init__(self, vertex_id):
        """  constructor """
        self.vertex_id = vertex_id
        self.adjacency_set = set()
    def add_edge(self, vertex):
        """ add edge """
        if self.vertex_id == vertex:
            raise ValueError("The vertex %d cannot be adjacent to itself" % d)
        self.adjacency_set.add(vertex)
    def get_adjacent_vertices(self):
        """ get connections """
        return sorted(self.adjacency_set)
