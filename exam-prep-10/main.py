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
from solve  import *


first_line = get_line(input_source).split()
item_count = int(first_line[0])

items = []
for i in range(1, item_count+1):
    parts = get_line(input_source).split()
    items.append(int(parts[0]))

value, taken = solve_tabulation(items)

print(value)
print(taken)


# ----------------------------------------------------------------
# Cerramos fichero (si se utiliza para redireccionar entrada)

close_test_file(test_file, input_source)
