from utils import open_test_file, close_test_file, get_line
from solve import *

# cambiar a "test1.txt" para depurar localmente
TEST_FILE = "test1.txt"
inp = open_test_file(TEST_FILE)
line = get_line(inp)
n = int(line.strip())
values_line = get_line(inp).strip()
values = list(map(int, values_line.split()))

max_benefit, houses = solve_house_robber(values)


print(f"max_benefit={max_benefit}")
print("houses=[" + ",".join(map(str, houses)) + "]")

close_test_file(TEST_FILE, inp)

