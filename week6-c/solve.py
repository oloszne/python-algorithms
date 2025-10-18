# solve_vpl.py — ESQUELETO (alumnos)
# Entrada:
#   Línea 1: N B
#     - N: número de productos
#     - B: presupuesto (euros enteros)
#   Líneas 2..N+1: nombre precio cantidad
#     - nombre: cadena sin espacios
#     - precio: euros redondeados al alza a entero
#     - cantidad: entero (unidades compradas)
#
# Objetivo:
#   Elegir un subconjunto de productos comprando su cantidad completa, 
#   maximizando la suma de cantidades sin superar B. 
#   Coste de un producto = ceil(precio) * cantidad.

from typing import List, Tuple
from mask_iter import BitmaskIterator

    

def solve(budget: int, items: List[Tuple[str, int, int, int]]) -> Tuple[int, List[str]]:
    best_qty = 0
    best_cost = 0
    best_set = []

    def backtrack(i, total_cost, total_qty, chosen):
        nonlocal best_qty, best_cost, best_set

        if i == len(items):
            chosen_sorted = sorted(chosen)
            if (total_qty > best_qty) or \
               (total_qty == best_qty and total_cost < best_cost) or \
               (total_qty == best_qty and total_cost == best_cost and chosen_sorted < best_set):
                best_qty = total_qty
                best_cost = total_cost
                best_set = chosen_sorted
            return

        name, price, qty, cost = items[i]

        if total_cost + cost <= budget:
            backtrack(i + 1, total_cost + cost, total_qty + qty, chosen + [name])

        backtrack(i + 1, total_cost, total_qty, chosen)

    backtrack(0, 0, 0, [])

    return best_qty, best_set

