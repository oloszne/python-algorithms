from typing import List, Tuple

class BitmaskIterator:
    """
    Iterador de vectores de dígitos en base 'base' con longitud 'num_digits'.
    Aquí se usa con base=2 para generar todos los subconjuntos (0/1) de n elementos
    como si recorriéramos un contador binario desde 0...0 hasta 1...1.

    Ejemplo:num_digits = 3, base = 2
    Secuencia generada (en orden):
        [0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1],
        [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]
    """

    def __init__(self, num_digits: int, base: int):
        self.num_counters = num_digits
        self.base = base