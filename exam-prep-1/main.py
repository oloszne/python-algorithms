from typing import List, Tuple
import heapq
from utils import open_test_file, close_test_file, get_line, get_n_lines
from graph_utils import build_graph
from solve import topo_sort_dfs


def parse_edges_from_input(input_source) -> List[Tuple[str, str]]:
    """
    Lee E y las siguientes E líneas ("U V") desde input_source y devuelve
    la lista de aristas [(U, V), ...]. Asume entrada válida (tests controlados).
    """

    # Leer primera línea (E)
    first = get_line(input_source).strip()
    E = int(first)
    # Leer exactamente E líneas
    edge_lines = get_n_lines(input_source, E)
    edges: List[Tuple[str, str]] = []
    for ln in edge_lines:
        u, v = ln.split()
        edges.append((u, v))
    return edges


def is_valid_topo_order(G, order: List[str]) -> bool:
    nodes = list(G.nodes())
    if len(order) != len(nodes):
        return False
    if set(order) != set(nodes):
        return False
    pos = {u: i for i, u in enumerate(order)}
    for u in nodes:
        for v in G.successors(u):
            if pos[u] >= pos[v]:
                return False
    return True


def canonical_topo_order(G):
    nodes = sorted(G.nodes())
    indeg = {u: G.in_degree(u) for u in nodes}
    adj = {u: sorted(G.successors(u)) for u in nodes}
    h: List[str] = []
    for u in nodes:
        if indeg[u] == 0:
            heapq.heappush(h, u)
    order: List[str] = []
    while h:
        u = heapq.heappop(h)
        order.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                heapq.heappush(h, v)
    if len(order) != len(nodes):
        return [], False
    return order, True


# Para redirigir entrada en local, asigna un nombre de fichero.
test_file = "test1.txt"  # p.ej.: "test1.txt"
input_source = open_test_file(test_file)

edges = parse_edges_from_input(input_source)
G = build_graph(edges)
order, is_dag = topo_sort_dfs(G)
if not is_dag:
    print("CYCLE")
else:
    if is_valid_topo_order(G, order):
        canon_order, ok = canonical_topo_order(G)
        if ok:
            print(", ".join(canon_order))
        else:
            print("CYCLE")
    else:
        print("CYCLE")

close_test_file(test_file, input_source)
