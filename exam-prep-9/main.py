import networkx as nx
from utils import open_test_file, close_test_file, get_line
from solve import solve_greedy_coloring

# Crear un grafo bipartito
B = nx.Graph()
left_nodes = ['v1','v3', 'v5','v7','v9']
right_nodes = ['v2','v4', 'v6','v8','v10']
B.add_nodes_from(left_nodes, bipartite=0)
B.add_nodes_from(right_nodes, bipartite=1)

# Agregar aristas según la condición dada
for i in range(len(left_nodes)):
    for j in range(len(right_nodes)):
        if i!=j:
            B.add_edge(left_nodes[i], right_nodes[j])

nodes = B.nodes()

# Para redirigir entrada en local, asigna un nombre de fichero.
# test_file = "test1.txt"
test_file = "test1.txt"
input_source = open_test_file(test_file)

#cambiamos el orden
order_list = get_line(input_source).split()
# Creamos un diccionario que mapea cada valor a su índice
order_dict = {v: i for i, v in enumerate(order_list)}  

nodes = sorted(nodes, key=lambda x: order_dict[x[1:]])

color_map = solve_greedy_coloring(B, order_nodes=nodes)

print(color_map)

close_test_file(test_file, input_source)
