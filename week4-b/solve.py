import minigraph as nx
from simple_stack import Stack

def dfs_topological_sort(graph):
    """
    Compute one topological sort of the given graph.
    """
    
    # La solucion que retorna esta función es un diccionario de Python.
    #   * La clave del diccionario es el número del nodo
    #   * El valor es el orden topologico asignado a ese nodo
    # 
    # Por ejemplo, si tenemos el siguiente grafo dirigido con 3 vertices:
    #                    3 ---> 2 ---> 1
    # ... el orden topologico es:
    #                El vértice 3 va en la primera posición
    #                El vértice 2 en la segunda posición
    #                El vértice 1 en la tercera posición
    # Con lo que debemos devolver un diccionario con este contenido:
    #     {1: 3, 2: 2, 3: 1}

    N = graph.number_of_nodes()
    
    visibleNodes = set()  # En este ejercicio utilizamos un set
    # para recordar los nodos visibles
    order = {}

    # solve it here! ------------------------------------------------
    stack = Stack() 

    def dfs(u):
        nonlocal N
        visibleNodes.add(u)
        for v in graph.neighbors(u):
            if v not in visibleNodes:
                dfs(v)
        stack.push(u)
        
    for node in graph.nodes():
        if node not in visibleNodes:
            dfs(node)         
    
    pos = 1
    while not stack.isEmpty():
        node = stack.pop()
        order[node] = pos
        pos += 1       

    return order
