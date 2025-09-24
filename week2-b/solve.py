import minigraph as nx

def build_graph(edges_list, num_nodes, num_edges):
    
    graph = nx.Graph()
    
    for node in range(num_nodes):
        graph.add_node(node + 1)
    
    for line in edges_list:
        print(line.split())
        graph.add_edge(int(line.split()[0]), int(line.split()[1]))   
    return graph