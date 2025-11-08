# Esqueleto para ejercicio del VPL
from typing import List

def solve_mfd_feasible(exams: List[int], rooms: List[int]):
    """    

    Objetivo propuesto: 
    Implementar la estrategia MFD (Max-Fit Decreasing)
    para asignar exámenes a aulas con formato de salida esperado:

    "rooms_used=<k> waste=<w>\nassign=[cap1, cap2, ...]"

    donde 'assign[i]' -> capacidad del aula asignada al examen 'exams[i]'.

    Parámetros:
      - exams: lista de enteros con los tamaños/necesidades de cada examen.
      - rooms: lista de enteros con las capacidades de las aulas disponibles.

    Devuelve:
      - (rooms_used, waste, assign_cap) si es factible
      - None si no hay asignación posible

    Implementación de estrategia MFD:
      - Ordenar exámenes de mayor a menor.
      - Ordenar aulas de mayor a menor.
      - Asignar secuencialmente la primera aula suficientemente grande a cada examen.
      - Calcular rooms_used, waste y la lista assign en el orden original de exams.
    """
    if len(exams) > len(rooms):
        return None
    rooms_used = 0
    assign = []
    waste = 0
    
    # Sort the input
    exams.sort(reverse=True)
    rooms.sort(reverse=True)
    
    # Assign rooms
    for i in range(len(exams)):
        if exams[i] <= rooms[i]:
            assign.append(rooms[i])
            rooms_used += 1
            waste += rooms[i] - exams[i]
        else:
            return None

    return rooms_used, waste, assign

