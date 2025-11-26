# Recurrencia del problema del ladrón
# -----------------------------------
#    t(n) = max (t(n-2) + v[n], t(n-1))
#    t(n) = 0		               : si n<0

def solve_tabulation(items):
    table = []
    taken = []
    
    def fill_table():
        nonlocal table
        
        n = len(items)
        
        # Handle base cases
        table.append(items[0])
        table.append(max(items[0], items[1]))
        
        for i in range(2, n):
            table.append(max(table[i-2] + items[i], table[i-1]))
            
        return
        
    def fill_taken():
        nonlocal table
        nonlocal taken
        
        # Select the last index (last house)
        n = len(items) - 1
        
        # Iterate down the 'table' list
        while n > 0:
            # Compare if the value has changed (if the house was robbed)
            if table[n] != table[n - 1]:
                taken.append(n)
                # Adjacent houses can't be robbed so we skip the previous house
                n -= 2
            else:
                # We didn't rob this house so the one before it must be checked
                n -= 1
        
        # Reverse the list
        taken.reverse()
        
    fill_table()
    fill_taken()
    if table:
        return table[-1], taken
    else:
        return 0, []
