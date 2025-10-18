#!/usr/bin/env python3
# main.py — Entrada/salida del VPL (NO modificar salvo test_file para pruebas locales)
from utils import open_test_file, close_test_file, get_line
from solve import solve

# Para redirigir entrada en local, asigna un nombre de fichero.
# test_file = "test1.txt"
test_file = "test1.txt"
input_source = open_test_file(test_file)

# Leer exactamente 2 líneas:
# 1) total, 2) "max10 max20 max50"
total_str = get_line(input_source).strip()
stock_line = get_line(input_source).strip()

total = int(total_str)
max10_str, max20_str, max50_str = stock_line.split()
max10, max20, max50 = int(max10_str), int(max20_str), int(max50_str)

result = solve(total, max10, max20, max50)
print(result)

close_test_file(test_file, input_source)
