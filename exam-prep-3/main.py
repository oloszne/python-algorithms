from utils import open_test_file, close_test_file, get_line
from solve import solve_knapsack
#from solve_alt import solve_knapsack

TEST_FILE = "test1.txt"  # Cambiar a "test1.txt" para pruebas locales

inp = open_test_file(TEST_FILE)

# Leer N y BUDGET (se asume formato correcto)
parts = get_line(inp).split()
n = int(parts[0])
budget = int(parts[1])

# Leer N líneas: NAME COST
# Guardamos NAME para imprimirlo en Best=[...]
costs = []
names = []
for _ in range(n):
    _name, c_str = get_line(inp).split()
    names.append(_name)
    costs.append(int(c_str))

# Resolver y formatear salida exacta
best_indices, best_cost = solve_knapsack(costs, budget)
names_text = ",".join(names[i-1] for i in best_indices)
print(f"Best=[{names_text}]")
print(f"Cost={best_cost}")

close_test_file(TEST_FILE, inp)
