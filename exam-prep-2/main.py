#!/usr/bin/env python3
# main.py — VPL runner
import sys
from utils import open_test_file, close_test_file, get_line, get_n_lines
from solve import find_lit_leds
from graph_utils import build_active_graph

test_file = "test1.txt"  # Cambia a "test1.txt" para pruebas locales
src = open_test_file(test_file)

# Leer primera línea "V E" y luego E líneas de aristas
first_line = get_line(src)
_, E_str = first_line.split()
E = int(E_str)
edge_lines = get_n_lines(src, E)

# Leer el resto (opcional) hasta EOF como estados de switches
rest_lines = src.read().splitlines()

# Componer todas las líneas para el parser del grafo
lines = [first_line] + edge_lines + rest_lines

# Construir grafo activo con aristas donde SWx=ON
G = build_active_graph(lines)

# Devuelve un string determinista con la lista ordenada, 
# por ejemplo: "['LED1', 'LED2', ...]"
sorted_leds = sorted(find_lit_leds(G))
leds = str(sorted_leds)

# Imprime solo la lista de LEDs encendidos
sys.stdout.write(f"LEDs: {leds}\n")

# Cerrar el origen de entrada si procede
close_test_file(test_file, src)