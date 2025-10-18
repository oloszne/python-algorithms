
import sys
from solve import kruskal_mst_dfs
from minigraph import Graph as MiniGraph
from utils import open_test_file, close_test_file, get_line


# Entrada: permitir redirección a fichero para pruebas locales
test_file = "test1.txt"  # e.g. "test1.txt"
input_source = open_test_file(test_file)

# Leer N M
first = get_line(input_source).strip()
p = first.split()
_, M = int(p[0]), int(p[1])

# Leer nombres de nodos
names_line = get_line(input_source).strip()
nodes = names_line.split()

# Leer M aristas
edges = []
for _ in range(M):
    line = get_line(input_source).strip()
    u, v, w = line.split()
    edges.append((u, v, int(w)))

# Normalizar aristas no dirigidas manteniendo menor peso por par
norm = {}
for u, v, w in edges:
    a, b = (u, v) if u <= v else (v, u)
    key = (a, b)
    if key not in norm or w < norm[key]:
        norm[key] = w

edges_unique = [(a, b, w) for (a, b), w in norm.items()]

G = MiniGraph()
for n in nodes:
    G.add_node(n)
for u, v, w in edges_unique:
    G.add_edge(u, v, weight=w)

# Usa el algoritmo de Kruskal para obtener:
# - mst: lista de aristas del árbol de expansión mínima, 
#   normalizadas como (u, v, w) con u <= v.
# - mst_cost: suma de pesos del MST.
# - complete_cost: suma de pesos del grafo original.
result = kruskal_mst_dfs(G)

if result is None:
    # Permitir que se devuelva un único 'None' de no haber MST
    mst, mst_cost, complete_cost = [], None, None
else:
    mst, mst_cost, complete_cost = result

# Canonizar salida: 
# normalizar (a<=b) y ordenar por (w,u,v)
mst_norm = []
for (u, v, w) in mst:
    a, b = (u, v) if u <= v else (v, u)
    mst_norm.append((a, b, w))
mst_norm.sort(key=lambda e: (e[2], e[0], e[1]))

energy_loss_mw = mst_cost # 1mW/cm
mst_lines = [f"{u} {v} {w}" for (u, v, w) in mst_norm]

out = []
out.append("MST:")
out.extend(mst_lines)
out.append(f"MST_cost={mst_cost}")
out.append(f"Complete_cost={complete_cost}")
out.append(f"Energy_loss_mW={energy_loss_mw}")
print("\n".join(out))

close_test_file(test_file, input_source)
