"""
Skeleton for SubsetIterator

Implementa un iterador que genere SOLO los subconjuntos factibles (por presupuesto)
de índices 0-based usando Backtracking con poda, en orden DFS: para cada índice i
en [0..n-1], primero sin i y luego con i, pero la rama de inclusión solo se explora
si el coste acumulado + coste[i] no supera el presupuesto.

La clase debe exponer un método `next()` que devuelva un iterador de listas de int.
No reordenes los índices dentro de cada subconjunto y evita enumerar subconjuntos
inviables (poda por presupuesto en la generación).
"""

from typing import Iterator, List


class SubsetIterator:
    
    def __init__(self, costs: List[int], budget: int):
        """Recibe la lista de costes y el presupuesto total."""
        self.costs = costs
        self.budget = budget
        self.n = len(costs)

    def next(self):
        def dfs(i, current_cost, current_subset):
            # Base case: All items have been considered
            if i == self.n:
                # Yield a copy to avoid modification issues during backtracking
                yield list(current_subset)
                return

            # 1. Branch: WITHOUT index i
            # We iterate through the generator returned by the recursive call
            for subset in dfs(i + 1, current_cost, current_subset):
                yield subset

            # 2. Branch: WITH index i (Pruning: only if budget allows)
            if current_cost + self.costs[i] <= self.budget:
                current_subset.append(i)
                for subset in dfs(i + 1, current_cost + self.costs[i], current_subset):
                    yield subset
                # Backtrack: remove the item before returning to the previous state
                current_subset.pop()

        # Start the recursion from index 0, cost 0, and an empty subset
        return dfs(0, 0, [])