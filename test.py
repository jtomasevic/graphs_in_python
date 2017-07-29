""" demo examples """
from graphs.adjacency_matrix_graph import AdjacenecyMatrixGraph
from graphs.adjacency_set_graph import AdjacenecySetGraph
from graphs.traversals import *
from graphs.topological_sort import topological_sort
from graphs.shortest_paths import shortest_path, shortest_path_dijkstra

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
print "depth_first representation:"
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
print "breath_first representation, directed graph:"
breath_first(graph)
print "depth_first representation, direceted graph:"
depth_first(graph, np.zeros(graph.num_vertices))


graph = AdjacenecySetGraph(9, directed=True)
graph.add_edge(0,1)
graph.add_edge(1,2)
graph.add_edge(2,7)
graph.add_edge(2,4)
graph.add_edge(2,3)
graph.add_edge(1,5)
graph.add_edge(5,6)
graph.add_edge(3,6)
graph.add_edge(3,4)
graph.add_edge(6,8)

print "topological sort example:"
topological_sort(graph)


graph = AdjacenecySetGraph(9, directed=True)
graph.add_edge(0,1)
graph.add_edge(1,2)
graph.add_edge(1,3)
graph.add_edge(2,3)
graph.add_edge(1,4)
graph.add_edge(3,5)
graph.add_edge(5,4)
graph.add_edge(3,6)
graph.add_edge(6,7)
graph.add_edge(0,7)

shortest_path(graph, 0, 5)
shortest_path(graph, 0, 6)
shortest_path(graph, 7, 4)

graph = AdjacenecyMatrixGraph(8, directed=False)
graph.add_edge(0,1, 1)
graph.add_edge(1,2, 2)
graph.add_edge(1,3, 6)
graph.add_edge(2,3, 2)
graph.add_edge(1,4, 3)
graph.add_edge(3,5, 1)
graph.add_edge(5,4, 5)
graph.add_edge(3,6, 1)
graph.add_edge(6,7, 1)
graph.add_edge(0,7, 8)

shortest_path_dijkstra(graph, 0, 6)
shortest_path_dijkstra(graph, 4, 7)
shortest_path_dijkstra(graph, 7, 0)

graph = AdjacenecyMatrixGraph(8, directed=True)
graph.add_edge(0,1, 1)
graph.add_edge(1,2, 2)
graph.add_edge(1,3, 6)
graph.add_edge(2,3, 2)
graph.add_edge(1,4, 3)
graph.add_edge(3,5, 1)
graph.add_edge(5,4, 5)
graph.add_edge(3,6, 1)
graph.add_edge(6,7, 1)
graph.add_edge(0,7, 8)

shortest_path_dijkstra(graph, 0, 6)
shortest_path_dijkstra(graph, 4, 7)
shortest_path_dijkstra(graph, 7, 0)