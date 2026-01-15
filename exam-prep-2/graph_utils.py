from typing import List, Dict, Set
import minigraph as nx


def build_active_graph(lines: List[str]):
    """
    Parsea las líneas y construye el grafo dirigido activo (MiniGraph) SIN pesos.

    Entrada:
    - 1ª línea: "V E" (V no se usa después),
    - E líneas: aristas "u v w" para u->v (la tercera columna se ignora),
    - Resto (opcional): estados "SWx=ON|OFF".

    Reglas:
    - SW* ON por defecto si no se especifica.
    - Se activan solo aristas cuyo ORIGEN esté ON 
      (si u es SW y está OFF, se bloquean sus salidas).

    Devuelve:
    - G (minigraph.DiGraph) con nodos y aristas activas, sin atributos de peso.
    """
    it = iter(lines)
    _, E = map(int, next(it).split())
    edges = []
    nodes_all: Set[str] = set()
    for _ in range(E):
        # La tercera columna (w) se admite por compatibilidad pero se ignora
        parts = next(it).split()
        if len(parts) < 2:
            raise ValueError("Cada arista debe tener al menos dos columnas: u v [w]")
        u, v = parts[0], parts[1]
        edges.append((u, v))
        nodes_all.add(u)
        nodes_all.add(v)
    # estados opcionales
    states: Dict[str, str] = {}
    for rest in it:
        rest = rest.strip()
        if not rest:
            continue
        if '=' in rest:
            k, v = rest.split('=', 1)
            states[k.strip()] = v.strip().upper()

    def is_sw(n: str) -> bool:
        return n.upper().startswith("SW")

    for n in nodes_all:
        if is_sw(n) and n not in states:
            states[n] = "ON"

    # Construir grafo dirigido activo con MiniGraph
    G = nx.DiGraph()
    for n in nodes_all:
        G.add_node(n)
    for u, v in edges:
        on = (states.get(u, "ON") == "ON")
        if on:
            # Grafo sin pesos: no incluimos atributo 'weight'
            G.add_edge(u, v)
    return G
