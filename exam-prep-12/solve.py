from node import *

def solve_branch_and_bound_LDS(capacity, items, record_visiting_order = False):
    """"
    :param capacity: capacidad de la mochila
    :param items: items de la mochila
    :param record_visiting_order: activa/desactiva el registro de nodos visitados
    :return: best_value, taken, visiting_order
    """
    alive = []
    visiting_order = []
    # ...
    best_value = 0
    taken = []
    
    # Initilize root node
    root_node = Node(0, [], 0, capacity)
    alive.append(root_node)
    
    while alive:
        current = alive.pop()
        if record_visiting_order:
            visiting_order.append(current.index)
        
        # Pruning
        if current.estimate(items) <= best_value or current.room < 0:
            continue
        
        # Compare best value
        if current.value > best_value:
            best_value = current.value
            taken = current.taken
            
        # Branch
        if current.index < len(items):
            not_take = Node(current.index + 1, current.taken, current.value, current.room)
            alive.append(not_take)
            if current.room >= items[current.index][1]:
                take = Node(current.index + 1, current.taken + [items[current.index][0]], current.value + items[current.index][2], current.room - items[current.index][1])
                alive.append(take)
            

    return best_value, taken, visiting_order