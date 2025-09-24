
def solve(input_list):
    x, y = 0, 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dir_index = 0
    for instr in input_list:
        turn = instr[0]
        steps = int(instr[1:])
        if turn == "R":
            dir_index = (dir_index + 1) % 4
        else:
            dir_index = (dir_index - 1) % 4
        dx, dy = directions[dir_index]
        x += dx * steps
        y += dy * steps
    return abs(x) + abs(y)
