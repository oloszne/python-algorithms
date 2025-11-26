import numpy as np

def solve_tabulation(items, capacity):
    n_items = len(items)
    table = np.zeros((n_items + 1, capacity + 1), dtype=int)
    taken = []

    def fill_table():
        # Iterate through each combination of the DP table
        for i in range(1, n_items + 1):
            item = items[i - 1]
            w = item.weight
            v = item.value
            for j in range(capacity + 1):
                # Initialize first row with zeroes
                #if i <= 0:
                #    table[i][j] = 0
                #    continue
                # If the item doesn't fit, copy the value above it
                if w > j:
                    table[i][j] = table[i-1][j]
                    continue
                
                # Decide whether it's better to add the item or not
                table[i][j] = max(table[i-1][j], table[i-1][j - w] + v)
                    
                
        return

    def fill_taken():
        i = n_items
        j = capacity
        # Calculate what items make the best solution (table[i][j])
        while j > 0 and i > 0:
            # If the value is equal to the one above it, it means the item was not taken, so we just decrement by the item index and capacity stays the same
            if table[i][j] == table[i-1][j]:
                i -= 1
            # If not, we take the item and decrement j by its weight and i by one.
            else:
                taken.append(i)
                j -= items[i - 1].weight
                i -= 1
                
        # Reverse for correct taking order
        taken.reverse()
       
            
    
    fill_table()
    fill_taken()
    # Last item is the best solution
    max_benefit = table[n_items, capacity]

    return max_benefit, taken