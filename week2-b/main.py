# -----------------------------------------------------------------
# Para redireccionar la entrada en Wing 101 crea un fichero con
# los datos de entrada en la misma carpeta donde tienes el fichero
# main.py de este ejercicio y añade aquí una string con el nombre
# del fichero.
#    Ejemplo:
#    test_file = "test1.txt"

test_file = "test1.txt"

if test_file is not None:
    input_source = open(test_file, 'r', newline='')
else:
    import sys
    input_source = sys.stdin
# ----------------------------------------------------------------

import minigraph as nx
from solve import *

first_line = input_source.readline().split()
num_nodes  = int(first_line[0])
num_edges  = int(first_line[1])

edges_list = []
for j in range(1, num_edges+1):
    edges_list.append(input_source.readline())

graph = build_graph(edges_list, num_nodes, num_edges);

print("Number of nodes: " + str(graph.number_of_nodes()))
print("Nodes: ", graph.nodes())
print("Number of edges: " + str(graph.number_of_edges()))
print("Edges: ", graph.edges())

# --------------------------------------------------------------------
# Cerramos el fichero (si lo utilizamos para redireccionar la entrada)
if test_file is not None:
    input_source.close()