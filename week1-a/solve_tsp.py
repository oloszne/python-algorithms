def order_crossover(parent1, parent2, lower_bound, upper_bound):
    
    child1 = [None] * len(parent1)
    
    
    child1[lower_bound:upper_bound] = parent1[lower_bound:upper_bound]
    
    index = upper_bound
    
    for i in range(len(parent2)):
        pos = (upper_bound + i) % len(parent2)
        n = parent2[pos]
        
        if n not in child1:
            if index >= len(child1):
                index = 0
            child1[index] = n
            index += 1
            
    
    
    return child1
