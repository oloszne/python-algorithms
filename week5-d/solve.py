
def solve(num_queens):
    """
    Using backtracking compute all the solutions to place the
    given number of queens in a square board.

    :param num_queens: number of queens to place in the board
    :return: list of lists containing all the solutions

    For example, if num_queens = 4 there are two solutions,
    and it returns:
       solutions_list = [ [1, 3, 0, 2], [2, 0, 3, 1] ]

    """

    solutions_list = []
    res = []
    
    def backtrack(i):
        if i in res:
            return
        res.append(i)
        col = len(res) - 1
        for prev_col in range(col):
            if abs(res[prev_col] - res[col]) == abs(prev_col - col):
                res.pop()
                return
        if len(res) == num_queens:
            solutions_list.append(res[:])
        else:
            for j in range(num_queens):
                backtrack(j)
        res.pop()
        
    for i in range(num_queens):
        backtrack(i)
       
    return solutions_list