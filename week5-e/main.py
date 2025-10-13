# -----------------------------------------------------------------
# Para redireccionar la entrada en Wing 101 crea un fichero con
# los datos de entrada en la misma carpeta donde tienes el fichero
# main.py de este ejercicio y añade aquí una string con el nombre
# del fichero.
#    Ejemplo:
#    test_file = "test1.txt"

from utils import *

test_file    = "test1.txt"
input_source = open_test_file (test_file)

# ----------------------------------------------------------------
from solve import *

first_line = get_line(input_source).split()
num_lines  = int(first_line[0])
voltage    = int(first_line[1])
input_list = get_n_lines(input_source, num_lines)

solutions_list = solve(input_list, voltage)

# VPL output

for sublist in solutions_list:
    print(sublist)

print(len (solutions_list), "solutions")

# ----------------------------------------------------------------
# Close the file if it was opened

close_test_file(test_file, input_source)
