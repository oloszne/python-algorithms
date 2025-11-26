import networkx  as nx

from solve import *

first_line = input().split()
num_nodes  = int(first_line[0])
num_edges  = int(first_line[1])
    
graph = nx.Graph()
graph.add_nodes_from(range(1,num_nodes+1))


for j in range(1, num_edges+1):
        parts = input().split()

        u = int(parts[0])
        v = int(parts[1])

        graph.add_edge(u, v)


order_nodes = graph.nodes()
colores_nodos = solve_dsat_coloring(graph, order_nodes)
    
print(colores_nodos)