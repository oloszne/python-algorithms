from node import *

def solve_branch_and_bound_DFS(capacity, items, record_visiting_order = False):
    """"
    :param capacity: capacidad de la mochila
    :param items: items de la mochila
    :param record_visiting_order: activa/desactiva el registro de nodos visitados
    :return: Por ahora sólo devuelve la lista de nodos visitados
    """

    alive = []
    
    visiting_order = []
    
    max_value = 0
    taken = []
    
    root = Node(0, [], 0, capacity)

    alive.append(root)
    
    while alive:
        current = alive.pop()
        
        if record_visiting_order:
            visiting_order.append(current.index)
        
        #pruning conditions
        if current.estimate(items) <= max_value or current.room < 0:
            continue
                       
        if current.value > max_value:
            max_value = current.value
            taken = current.taken
            
        #branching
        if current.index < len(items):
            right_child = Node(current.index + 1, current.taken, current.value, current.room)
            alive.append(right_child)
            
            item = items[current.index]

            left_child = Node(current.index + 1, current.taken + [item.index], current.value + item.value, current.room - item.weight)
            alive.append(left_child)

    return max_value, taken, visiting_order