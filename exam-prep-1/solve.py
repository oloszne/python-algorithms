import minigraph as nx
from simple_queue import Queue


def topo_sort_dfs(G: nx.DiGraph):
    """
    Calcula un orden topológico mediante DFS con detección de ciclos.

    Retorna:
      (order: List[str], is_dag: bool)
    """

    order = []
    is_dag = True
    visiting = set() # for cycle detection
    visited = set()
    
    def dfs(node):
        nonlocal is_dag
        
        if node in visiting:
            is_dag = False
            return
        if node in visited:
            return
        
        visiting.add(node)
        
        for next_node in G.successors(node):
            dfs(next_node)
            
        visiting.remove(node)
        visited.add(node)
        order.append(node)
    
    for node in G.nodes():
        if node not in visited:
            dfs(node)
    
    order.reverse()
    print(order)
    return order, is_dag # (order: List[str], is_dag: bool)
