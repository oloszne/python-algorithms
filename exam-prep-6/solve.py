from simple_queue import Queue

def friends_on_social_network(net, src, dst):
    """
    BFS en grafo no dirigido para calcular:
      - la distancia mínima (en aristas) entre 'src' y 'dst'
      - y un camino mínimo (cualquiera de los posibles).

    Parámetros
    ----------
    net : Graph (MiniGraph)
        Grafo no dirigido con usuarios como nodos y amistades como aristas.
    src, dst : str
        Nombres de 
    --------
    (int | None, liorigen y destino.

    Devuelvest[str] | None)
        (número de saltos, camino). Si no existe camino: (None, None).
        Si existen varios caminos mínimos, se aceptará cualquiera de ellos.
    """
    # Dict to store parent nodes
    visited = {}
    
    # FIFO queue
    queue = Queue()
    
    # Base cases
    if src == dst:
        return 0, [src]
    
    if net.neighbors(src) is None or net.neighbors(dst) is None:
        return None, None
    # Source node
    queue.enqueue(src)
    visited[src] = None
    
    while queue.size() > 0:
        node = queue.dequeue()
        
        # If destination found
        if node == dst:
            path = []
            # While visited nodes have a parent (Until src)
            while node:
                path.append(node)
                node = visited[node]
            # Reverse the path
            path.reverse()
            return len(path) - 1, path      
        
        # Enqueue all neighbors if not visited
        for n in net.neighbors(node):
            if n not in visited:
                visited[n] = node
                queue.enqueue(n)
        
    return None, None
