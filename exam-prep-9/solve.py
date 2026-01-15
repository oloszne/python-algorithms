
def solve_greedy_coloring(graph, order_nodes):    
    """
    Implementa el algoritmo greedy de coloreado de grafos.

    Args:
        - order_nodes: lista de vértices en el orden en que deben colorearse 
          (p.ej. [1,3,5,...] o ['v1','v3',...])
        - graph: grafo de adyacencias con mismas etiquetas que en order_nodes
    Returns:
        - lista de colores en el mismo orden de order_nodes
          (se asigna a cada vértice el menor color entero >= 0 
          no usado por sus vecinos ya coloreados)
    """
    
    node_colors = [-1] * len(order_nodes)
    for i in range(len(order_nodes)):
        curr_node = order_nodes[i]
        neighbors_colors = set()
        
        for neighbor in graph.neighbors(curr_node):
            # Find the index of the neighbor
            neigh_index = order_nodes.index(neighbor)
            # Find if color was already assigned to the neighbor
            if node_colors[neigh_index] != -1:
                neighbors_colors.add(node_colors[neigh_index])
                
        # Find the lowest possible integer (color)
        color = 0
        while color in neighbors_colors:
            color += 1
        node_colors[i] = color
                
            
    return node_colors