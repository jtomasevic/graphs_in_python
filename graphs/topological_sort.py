""" Topological sort can be applyed on DAGs graphs.
    DAGs grpah means Directed acyclic graphs.
    Any ordering of all nodes that satisfy all relationships is:
    topological sort. It means we start from one node and visit all only once, 
    and we visited them all in one path.
"""

from Queue import Queue

def topological_sort(graph):
    """ Topological sort algorithm, applicaple on DAG:
        Directed acyclic graphs. This algorithm find one of path.
    """
    queue = Queue()
    indegree_map = {}
    for i in range(graph.num_vertices):
        indegree_map[i] = graph.get_indegree(i)
        # Queue all nodes without dependencies, which means
        # they don't have incoming edges, which means
        # indegree is 0
        if indegree_map[i] == 0:
            queue.put(i)
    sorted_list = []
    while not queue.empty():
        vertex = queue.get()
        sorted_list.append(vertex)
        for v in graph.get_adjacent_vertices(vertex):
            indegree_map[v] = indegree_map[v] - 1
            if indegree_map[v] == 0:
                queue.put(v)
    if len(sorted_list) != graph.num_vertices:
        raise ValueError("This graph has a cycle!")
    print(sorted_list)
