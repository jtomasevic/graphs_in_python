""" demo examples """
from graphs.adjacency_matrix_graph import AdjacenecyMatrixGraph
from graphs.adjacency_set_graph import AdjacenecySetGraph

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