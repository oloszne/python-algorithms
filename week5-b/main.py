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
num_digits = int(first_line[0])
base       = int(first_line[1])

obj = My_Iterator(num_digits, base)
for c in obj.next():
     print(c)

# ----------------------------------------------------------------
# Cerramos el fichero (si lo utilizamos para redireccionar la entrada)

close_test_file(test_file, input_source)
