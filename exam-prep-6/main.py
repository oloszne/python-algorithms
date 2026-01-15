from utils import open_test_file, close_test_file, get_line
from minigraph import Graph
from solve import friends_on_social_network

TEST_FILE = "test1.txt"  # Cambiar a "test1.txt" para pruebas locales


inp = open_test_file(TEST_FILE)
    
# U F
_, F = map(int, get_line(inp).split())

# nombres (U)
users = get_line(inp).split()

# amistades (F líneas)
edges = [tuple(get_line(inp).split()) for _ in range(F)]

# SRC DST
src, dst = get_line(inp).split()

# Construir grafo no dirigido con MiniGraph
net = Graph()
for u in users:
    net.add_node(u)
for a, b in edges:
    net.add_edge(a, b)

dist, path = friends_on_social_network(net, src, dst)

# Salida estandarizada:
# distancia_social(SRC, DST) = K saltos | inf si no hay camino
steps = dist if dist is not None else "inf"
print(f"distancia_social({src}, {dst}) = {steps} saltos")

# Si hay camino, imprimir también el camino (mínimo en número de saltos)
if dist is not None and path:
    print("camino: " + " -> ".join(path))

close_test_file(TEST_FILE, inp)

