""" trasversals of graph """
from Queue import Queue
import numpy as np


def breath_first(graph, start=0):
    """ visit first childs and then other """
    queue = Queue()
    queue.put(start)
    visited = np.zeros(graph.num_vertices)
    while not queue.empty():
        node = queue.get()
        if visited[node] == 1:
            continue
        print("visit: ", node)
        visited[node] = 1
        for c_node in graph.get_adjacent_vertices(node):
            if visited[c_node] != 1:
                queue.put(c_node)
