from typing import List
from utils import open_test_file, close_test_file, get_line, get_n_lines
from solve import *

def parse_products(lines: List[str]):
    items = []
    for ln in lines:
        parts = ln.split()
        name = parts[0]
        # Precio en euros enteros, redondeado hacia arriba
        price_eur = int(parts[1])
        #price_eur = int(-(-float(parts[1]) // 1)) 
        qty = int(parts[2])
        cost_eur = price_eur * qty
        items.append((name, price_eur, qty, cost_eur))
        
    return items

test_file = "test1.txt"
input_source = open_test_file(test_file)

first_line = get_line(input_source).split()
num_items = int(first_line[0])
budget = int(first_line[1])

input_list = get_n_lines(input_source, num_items)

items = parse_products(input_list)
best_qty, solution = solve(budget, items)

solution.sort()
print(f"{best_qty} {solution}", end="")

close_test_file(test_file, input_source)