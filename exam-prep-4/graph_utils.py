# graph_utils.py — utilidades para construir grafos con Minigraph
from typing import List, Dict, Set
import minigraph as nx


def build_graph(lines: List[str]) -> nx.DiGraph:
    it = iter(lines)
    _, E = map(int, next(it).split())
    edges = []
    nodes: Set[str] = set()
    for _ in range(E):
        u, v = next(it).split()
        edges.append((u, v))
        nodes.add(u)
        nodes.add(v)
    # optional states
    states: Dict[str, str] = {}
    for rest in it:
        rest = rest.strip()
        if not rest:
            continue
        if '=' in rest:
            k, v = rest.split('=', 1)
            states[k.strip()] = v.strip().upper()
    # default: any SW* not declared is ON
    def is_switch(n: str) -> bool:
        return n.upper().startswith("SW")
    for n in nodes:
        if is_switch(n) and n not in states:
            states[n] = "ON"
    # construir grafo dirigido con Minigraph usando SOLO fuentes activas
    G = nx.DiGraph()
    for n in nodes:
        G.add_node(n)
    for u, v in edges:
        on = (states.get(u, "ON") == "ON")  # non-SW default ON
        if on:
            G.add_edge(u, v)
    return G
