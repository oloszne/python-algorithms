import minigraph as nx
from simple_stack import *
from simple_queue import *

def solve(input_list):
    #Create the graph
    graph = nx.Graph()
    for n in input_list:
        n_strip = n.strip()
        n_split = n_strip.split('-')
        u = n_split[0]
        v = n_split[1]
        graph.add_edge(u, v)
        
    
    num_solutions = 0
    all_paths = []
    small_caves_visited = []
    path = Stack()
    
    def dfs(node, path, small_caves_visited):
        path.push(node)
        if node == "end":
            all_paths.append(path.items.copy())
            
        else:
            for neighbor in graph.neighbors(node):
                if neighbor == "start":
                    continue
                if neighbor.islower():
                    if neighbor in small_caves_visited:
                        continue
                    small_caves_visited.append(neighbor)
                    dfs(neighbor, path, small_caves_visited)
                    small_caves_visited.remove(neighbor)
                else:
                    dfs(neighbor, path, small_caves_visited)
        path.pop()
                        
    dfs("start", path, small_caves_visited)
    num_solutions = len(all_paths)
    
    return num_solutions, all_paths
