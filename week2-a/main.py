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

from solve import *

first_line = input_source.readline().split()
num_lines  = int(first_line[0])

input_list = []
for j in range(num_lines):
    input_list.append(input_source.readline())

solution = solve(input_list)

print(solution)

# --------------------------------------------------------------------
# Cerramos el fichero (si lo utilizamos para redireccionar la entrada)
if test_file is not None:
    input_source.close()
    