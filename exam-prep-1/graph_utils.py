from typing import List, Tuple
import minigraph as nx


def build_graph(edges: List[Tuple[str, str]]) -> nx.DiGraph:
    """
    Construye y devuelve un grafo dirigido (MiniGraph DiGraph) a partir
    de la lista de aristas (u, v).
    """
    G = nx.DiGraph()
    for u, v in edges:
        G.add_edge(u, v)
    return G
