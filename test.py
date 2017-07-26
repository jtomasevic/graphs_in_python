""" demo examples """
from graphs.adjacency_matrix_graph import AdjacenecyMatrixGraph
from graphs.adjacency_set_graph import AdjacenecySetGraph
from graphs.traversals import *

graph = AdjacenecyMatrixGraph(4, directed=True)
graph.add_edge(0,1)
graph.add_edge(0,2)
graph.add_edge(2,3)
print "AdjacenecyMatrixGraph representation:"
graph.display()

graph = AdjacenecySetGraph(4, directed=False)
graph.add_edge(0,1)
graph.add_edge(0,2)
graph.add_edge(2,3)
print "AdjacenecySetGraph representation:"
graph.display()

graph = AdjacenecyMatrixGraph(9)
graph.add_edge(0,1)
graph.add_edge(1,2)
graph.add_edge(2,7)
graph.add_edge(2,4)
graph.add_edge(2,3)
graph.add_edge(1,5)
graph.add_edge(5,6)
graph.add_edge(6,3)
graph.add_edge(3,4)
graph.add_edge(6,8)
print "breath_first representation:"

breath_first(graph)
print "breath_first representation:"
depth_first(graph, np.zeros(graph.num_vertices))

graph = AdjacenecySetGraph(9, directed=True)
graph.add_edge(0,1)
graph.add_edge(1,2)
graph.add_edge(2,7)
graph.add_edge(2,4)
graph.add_edge(2,3)
graph.add_edge(1,5)
graph.add_edge(5,6)
graph.add_edge(6,3)
graph.add_edge(3,4)
graph.add_edge(6,8)
breath_first(graph)
breath_first(graph)
print "breath_first representation, directed graph:"
breath_first(graph)
print "breath_first representation, direceted graph:"
depth_first(graph, np.zeros(graph.num_vertices))
