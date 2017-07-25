from graphs.adjacency_matrix_graph import AdjacenecyMatrixGraph
from graphs.adjacency_list_graph import AdjacenecyListGraph
from graphs.adjacency_set_graph import AdjacenecySetGraph

g = AdjacenecyMatrixGraph(4, directed=True)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(2,3)
g.display()

g = AdjacenecyListGraph(4, directed=True)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(2,3)
g.display()

g = AdjacenecySetGraph(4, directed=True)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(2,3)
g.display()
