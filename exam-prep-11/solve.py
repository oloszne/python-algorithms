import minigraph as nx

def solve_rlf_graph_coloring(graph):

    nodes = set(graph.nodes())
    colors = {} # Dicciónario key= nodo, value= color
    color = 0 # Empezamos por el color 0

    #Escribe el código a partir de aquí
    #------------------------------------
    while nodes:
        max_deg = max(nodes, key=lambda n: graph.degree(n))
        colors[max_deg] = color
        nodes.remove(max_deg)
        colored_this_round = {max_deg}
        for node in list(nodes):
            if not any(node in graph.neighbors(colored_node) for colored_node in colored_this_round):
                colors[node] = color
                colored_this_round.add(node)
                nodes.remove(node)
        color += 1
    #------------------------------------
        
    # Ordenamos el diccionario de colores por número de nodo
    sorted_dict = {k: colors[k] for k in sorted(colors)}
    
    # Devolvemos los valores del diccionario ordenado en una lista
    return list(sorted_dict.values())
