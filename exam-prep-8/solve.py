# solve.py — Lógica a implementar por el alumno

from typing import List, Tuple


def sort_hotels_by_rating(hotels: List[Tuple[str, int, int]]) -> List[Tuple[str, int, int]]:
    if len(hotels) <= 1:
        return hotels
    pivot = hotels.pop()
    lower = []
    greater = []
    
    for h in hotels:
        # Sorting keys
        h_key = (h[1], h[2], [-ord(c) for c in h[0]])
        p_key = (pivot[1], pivot[2], [-ord(c) for c in pivot[0]])        
        if h_key > p_key:
            greater.append(h)
        else:
            lower.append(h)
    return sort_hotels_by_rating(greater) + [pivot] + sort_hotels_by_rating(lower)
    
    
    """
    Devuelve una nueva lista con los hoteles ordenados con QuickSort usando:
    - rating descendente
    - reviews descendente (en empates de rating)
    - name ascendente (desempate final)

    Nota: Cada hotel se representa como (name: str, rating: int, reviews: int).
    """
