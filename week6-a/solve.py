from minigraph import Graph as MiniGraph
from collections import defaultdict
from simple_stack import Stack

def kruskal_mst_dfs(G: MiniGraph):
    edges = []
    complete_cost = 0
    for u, v, w in G.edges(data=True):
        edges.append((u, v, w.get("weight")))
        complete_cost += w.get("weight")
    sorted_edges = sorted(edges, key=lambda edge: (edge[2], edge[0], edge[1]))
    mst = []
    mst_cost = 0
    mst_graph = MiniGraph()
    for node in G.nodes():
        mst_graph.add_node(node)
    for edge in sorted_edges:
        if not dfs(mst_graph, edge):
            u, v, w = edge
            mst.append((u, v, w))
            mst_cost += w
            mst_graph.add_edge(u, v, weight=w)
            if len(mst) == len(G.nodes()) - 1:
                break
    if len(mst) < len(G.nodes()) - 1:
        return None
    return mst, mst_cost, complete_cost

def dfs(graph, edge):
    u, v, _ = edge
    stack = Stack()
    visited = set()
    stack.push(u)
    while not stack.isEmpty():
        current_node = stack.pop()
        if current_node == v:
            return True
        if current_node not in visited:
            visited.add(current_node)
            for neighbor in graph.neighbors(current_node):
                if neighbor not in visited:
                    stack.push(neighbor)
    return False
