"""
Shortes path alfoteithms are looking for the most efficient route
between a pair of nodes. Edges weight determine cost of a particular path
- if all edges are equal we are using unweight shortest path algorithm
- if edges are unequal we are using Dijkstra's algorithm
"""
from Queue import Queue
from graphs.graph import Graph

def build_distance_table(graph, source):
    """ build distance tree """
    # Dictinary mapp vertex number to the tuple:
    # (distance from source, last vertex on path from source)
    distance_table = {}
    # set default values
    for i in range(graph.num_vertices):
        distance_table[i] = (None, None)
    distance_table[source] = (0, source)
    queue = Queue()
    queue.put(source)
    while not queue.empty():
        current_node = queue.get()
        # get current distance
        current_distance = distance_table[current_node][0]
        for c_node in graph.get_adjacent_vertices(current_node):
            if distance_table[c_node][0] is None:
                distance_table[c_node] = (1+ current_distance, current_node)
                # enqueue only if sub node has other adjacent vertices to explore.
                if len(graph.get_adjacent_vertices(c_node)) > 0:
                    queue.put(c_node)
    return distance_table

def shortest_path(graph, source, destination):
    """ find shortest path """
    distance_table = build_distance_table(graph, source)
    path = [destination]
    previous_vertex = distance_table[destination][1]
    while previous_vertex is not None and previous_vertex is not source:
        path = [previous_vertex] + path
        previous_vertex = distance_table[previous_vertex][1]
    if previous_vertex is None:
        print ("There is not path from %d to %d", source, destination)
    else:
        path = [source] + path
        print ("Shortest path is: ", path)
