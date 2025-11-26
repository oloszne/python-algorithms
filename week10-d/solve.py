import networkx as nx


def solve_dsat_coloring(graph, order_nodes):
    
    # Implementación del algoritmo DSatur
    nodes_colors = {}
    for node in order_nodes:
        nodes_colors[node] = None

    # Escribir el código a partir de aquí
    # _____________________________________________________________________
    
    # Dict of numbers of distinct colors of neighboring nodes
    saturation = {node: 0 for node in order_nodes}
    
    # List of degrees of each node
    degrees = graph.degree(order_nodes)
    
    # First node, max degree
    first_node = max(degrees, key=lambda x: (x[1], -x[0]))[0]
    print(first_node)
    
    # Initial saturation 
    nodes_colors[first_node] = 0
    
    # Calculate saturation of each neighbor of the first node
    for neigh1 in graph.neighbors(first_node):
        distinct_neigh_satur = set()
        for neigh2 in graph.neighbors(neigh1):
            if nodes_colors[neigh2] != None and nodes_colors[neigh2] not in distinct_neigh_satur:
                distinct_neigh_satur.add(nodes_colors[neigh2])
        saturation[neigh1] = len(distinct_neigh_satur)
    
    # While any node has no color assigned    
    while any(color is None for color in nodes_colors.values()):
        
        # Find all nodes with no color assigned
        candidates = [ n for n in order_nodes if nodes_colors[n] is None ]
        
        # Determine next node out of all candidates by Saturation, Degree and Lex Order
        next_node = max(candidates, key=lambda n: (saturation[n], degrees[n], -n))
        
        # Store every neighboring color
        neigh_colors = [nodes_colors[n] for n in graph.neighbors(next_node) if nodes_colors[n] is not None]
        
        # Find minimum positive integer missing
        i = 0
        while i in neigh_colors:
            i += 1
        
        # Assign color
        nodes_colors[next_node] = i
        
        # Update saturation of neighbors
        for neigh1 in graph.neighbors(next_node):
            distinct_neigh_satur = set()
            for neigh2 in graph.neighbors(neigh1):
                if nodes_colors[neigh2] != None and nodes_colors[neigh2] not in distinct_neigh_satur:
                    distinct_neigh_satur.add(nodes_colors[neigh2])
            saturation[neigh1] = len(distinct_neigh_satur)        
        
    # _____________________________________________________________________

    return [nodes_colors[node] for node in order_nodes]

