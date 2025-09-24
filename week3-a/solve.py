import minigraph  as nx
from sys          import maxsize as infinite
from simple_queue import *

def bfs_path_length(graph, first_node):
    """
    Compute the shortest path length of the non-directed graph G
    starting from node first_node. Return a dictionary with the
    distance (in number of steps) from first_node to all the nodes.
    """

    distance = {} 
    queue = Queue()
    queue.enqueue(first_node)
    done = []
    
    for node in graph.nodes():
        distance[node] = infinite
        
    distance[first_node] = 0
    done.append(first_node)
    
    while not queue.isEmpty():
        visited_node = queue.dequeue()
        for neighbor in graph.neighbors(visited_node):
            if neighbor not in done:
                done.append(neighbor)
                queue.enqueue(neighbor)
                distance[neighbor] = distance[visited_node] + 1
        

    return distance
