#!/usr/bin/env python3
# main.py -- entrada/salida del VPL (NO modificar)
# Para redireccionar la entrada en local: cambia `test_file` a "test1.txt"
from utils import open_test_file, close_test_file, get_line
from solve import RollsIterator
import sys

# Para redirigir entrada en local, asigna un nombre de fichero.
# test_file = "test1.txt"
test_file = "test1.txt"
src = open_test_file(test_file)

# Leer exactamente una línea: "d s T"
line = get_line(src).strip()
d_str, s_str, T_str = line.split()
d, s, T = int(d_str), int(s_str), int(T_str)

# Generar todas las líneas resultado con RollsIterator
lines = list(RollsIterator(d, s, T).next())

if lines:
    #sys.stdout.write("\n".join(lines))
    print("\n".join(lines))

close_test_file(test_file, src)

