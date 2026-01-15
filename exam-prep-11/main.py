import minigraph as nx

from utils import open_test_file, close_test_file, get_line
from solve import *

# set to a filename like "test1.txt" for local redirection
test_file = "test1.txt"
input_source = open_test_file(test_file)

first_line = get_line(input_source).split()
num_nodes  = int(first_line[0])
num_edges  = int(first_line[1])

graph = nx.Graph()
for i in range(1, num_nodes+1):
    graph.add_node(i)


for j in range(1, num_edges+1):
    parts = get_line(input_source).split()

    u = int(parts[0])
    v = int(parts[1])

    graph.add_edge(u, v)

colors = solve_rlf_graph_coloring(graph)
print(colors)

close_test_file(test_file, input_source)
