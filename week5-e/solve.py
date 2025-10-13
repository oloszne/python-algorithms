import minigraph as nx
from simple_queue import *
from simple_stack import *

def solve(input_list, voltage):
    solutions_list = []
    G = nx.DiGraph()
    queue = Queue()
    queue.enqueue((0, []))
    min_len = None

    for edge in input_list:
        u, v = map(int, edge.split())
        G.add_edge(u, v)

    while not queue.isEmpty():
        current, path = queue.dequeue()

        if min_len is not None and len(path) > min_len:
            break

        if current == voltage:
            if min_len is None:
                min_len = len(path)
            if len(path) == min_len:
                solutions_list.append(path)
            continue

        for neighbor in G.neighbors(current):
            new_edge = (current, neighbor)
            new_path = path + [new_edge]
            queue.enqueue((neighbor, new_path))

    return solutions_list

