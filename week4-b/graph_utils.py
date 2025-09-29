import minigraph as nx

def build_digraph_with_weights(edges_list, num_nodes, num_edges):
    G = nx.DiGraph()
    
    for n in range(1, num_nodes + 1):
        G.add_node(str(n))
    
    for edge in edges_list:
        split_edge = edge.split()
        u = split_edge[0]
        v = split_edge[1]
        w = split_edge[2]
        G.add_edge(u, v, weight=w)
    
    return G
