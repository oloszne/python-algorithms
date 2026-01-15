#!/usr/bin/env python3
# main.py — VPL runner (NO modificar)
from utils import open_test_file, close_test_file, get_line
from solve import check_circuit_connectivity
import sys
from graph_utils import build_graph

# Verifica si un nodo es un componente (no es Vcc, GND ni SW*)
def is_component(name: str) -> bool:
    return name not in {"Vcc", "GND"} and not name.startswith("SW")

test_file = "test1.txt"  # Cambia a "test1.txt" para pruebas locales
src = open_test_file(test_file)

# Construir la lista de líneas de entrada asumiendo entrada válida
first = get_line(src)
V_str, E_str = first.split()
E = int(E_str)

data = [first]
# Leer exactamente E líneas de aristas
for _ in range(E):
    data.append(get_line(src))
# Leer el resto de líneas opcionales hasta EOF
data.extend(ln.rstrip("\n") for ln in src)

G = build_graph(data)

reachable_list, disconnected_list = check_circuit_connectivity(G)
ok = (len(disconnected_list) == 0)

reachable = [n for n in reachable_list if is_component(n)]
disconnected = [n for n in disconnected_list if is_component(n)]

lines = [
    f"Componentes conectados: {sorted(reachable)}",
    f"Componentes desconectados: {sorted(disconnected)}",
]
sys.stdout.write("\n".join(lines))

# Cerrar el origen de entrada si aplica
close_test_file(test_file, src)