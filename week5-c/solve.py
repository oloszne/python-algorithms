from my_iterator import *

def solve(num_queens):
    """
    Using your brute force iterator compute all the
    solutions to place the given number of queens in
    a square board.

    :param num_queens: number of queens to place in the board
    :return: list of lists containing all the solutions

    For example, if num_queens = 4 there are two solutions,
    and it returns:
       solutions_list = [ [1, 3, 0, 2], [2, 0, 3, 1] ]

    """

    solutions_list = []
    iterator = My_Iterator(num_queens, num_queens)
    for pos in iterator.next():         
        valid = True      
        for i in range(len(pos)):
            for j in range(i + 1, len(pos)):
                if pos[i] == pos[j] or abs(i - j) == abs(pos[i] - pos[j]):
                    valid = False
                    break
            if not valid:
                break
        if valid:
            solutions_list.append(pos)    

    return solutions_list
