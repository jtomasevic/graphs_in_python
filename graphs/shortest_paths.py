"""
Shortes path alfoteithms are looking for the most efficient route
between a pair of nodes. Edges weight determine cost of a particular path
- if all edges are equal we are using unweight shortest path algorithm
- if edges are unequal we are using Dijkstra's algorithm
"""
from Queue import Queue
from graphs.graph import Graph
from pqdict import minpq

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


def build_distance_table_dijkstra(graph, source):
    """ build distance table for dijkstra algorithm. """
    # A dictionary mapping from the vertex number to a tuple
    # (distancefrom source, last vertex on path from source)
    distance_table = {}
    for i in range(graph.num_vertices):
        distance_table[i] = (None, None)
    # Distance from source itself is 0
    distance_table[source] = (0, source)
    # Hold mapping of vertex id to distance from source
    # Access to highest priority (lowest distance) item first
    priority_queue = minpq()
    priority_queue[source] = 0
    while len(priority_queue.keys())>0:
        current_vertex = priority_queue.pop()
        # Distance of the current node from the source
        curren_distance = distance_table[current_vertex][0]
        for neighbor in graph.get_adjacent_vertices(current_vertex):
            distance = curren_distance + graph.get_edge_weight(current_vertex, neighbor)
            # last recorded distance of the neighbor from the soruce
            neighbor_distance = distance_table[neighbor][0]
            # if there is recoreded distance from source and disance is grater of new path, 
            # update the current disance from the source in distance tble 
            if neighbor_distance is None or neighbor_distance > distance:
                distance_table[neighbor] = (distance, current_vertex)
                priority_queue[neighbor] = distance
    return distance_table

def shortest_path_dijkstra(graph, source, destination):
    """ if edges are unequal we are using Dijkstra's algorithm """
    distance_table = build_distance_table_dijkstra(graph, source)
    path = [destination]
    previous_vertex = distance_table[destination][1]
    while previous_vertex is not None and previous_vertex is not source:
        path = [previous_vertex] + path
        previous_vertex = distance_table[previous_vertex][1]
    if previous_vertex is None:
        print ("There is not path from %d to %d", source, destination)
    else:
        path = [source] + path
        print ("Shortest djk path is: ", path)
