# solve.py — Solución de referencia (NO subir al VPL del alumno)
from typing import Iterator, Iterable, List


class RollsIterator:
    
    """
    Iterador que expone un método generador `next()`
    que produce las tiradas válidas como strings
    con valores separados por espacios.

    Requisitos:
    - Implementa backtracking con poda determinista.
    - Genera en orden lexicográfico (caras en orden 1..s).
    - No construyas toda la lista en memoria; 
      usa `yield` para producir resultados.
    """

    def __init__(self, d: int, s: int, T: int):
        self.d = d
        self.s = s
        self.T = T

    
    # Ejemplo:
    # Parámetros: d = 2, s = 3, T = 4
    # Tiradas válidas (en orden):
    # 1 1
    # 1 2
    # 1 3
    # 2 1
    # 2 2
    # 3 1
    def next(self):
        """
        Generador que debe producir strings con los `d` valores 
        separados por espacios, en orden lexicográfico.
        """
        def roll_dice(dice_left, curr_roll, curr_sum):
            # Prune
            if curr_sum > self.T:
                return
            # Prune if the next min roll exceeds the threshold
            if curr_sum + dice_left * 1 > self.T:
                return
            # If there are no dice left, yield
            if dice_left == 0:
                yield " ".join(map(str, curr_roll))
            
            # Roll the die
            for face in range(1, self.s + 1):
                curr_roll.append(face)
                
                # Recurse
                for result in roll_dice(dice_left - 1, curr_roll, curr_sum + face):
                    yield result
                    
                # Backtrack
                curr_roll.pop()
        # Generate result
        for roll in roll_dice(self.d, [], 0):
            yield roll
