from collections import namedtuple

from node import *
from solve import *
from utils import open_test_file, close_test_file, get_line

# set to a filename like "test1.txt" for local redirection
test_file = "test1.txt"
input_source = open_test_file(test_file)

first_line = get_line(input_source).split()
item_count = int(first_line[0])
capacity = int(first_line[1])
    
items = []
for i in range(1, item_count+1):
    line = get_line(input_source)
    parts = line.split()
    items.append(Item(i, int(parts[0]), int(parts[1])))

value, taken, visiting_order = \
    solve_branch_and_bound_LDS(capacity, items, True)

print(visiting_order)
print(value)
print(taken)

close_test_file(test_file, input_source)
