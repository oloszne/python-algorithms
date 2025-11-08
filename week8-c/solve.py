# MergeSort estable para ordenar canciones por BPM (asc), y opcionalmente por energy (desc).
# Devuelve únicamente la lista de títulos ordenados (list[str]).

def sort_playlist_by_flow(tracks, use_energy):
    """
    Ordena una playlist aplicando MergeSort estable por BPM ascendente y, si
    `use_energy` es True, desempatando por energía descendente. Devuelve
    exclusivamente los títulos en el orden final.

    Parámetros:
      - tracks: lista de tuplas (title:str, bpm:int [, energy:int])
      - use_energy: bool → si True, en empates de BPM se usa energy descendente

    Devuelve:
      - list[str]: títulos en el orden final

    Detalles del comparador y estabilidad:
      - Siempre prioriza menor BPM (ascendente).
      - Si `use_energy` es True y el BPM empata, mayor energía primero
        (descendente).
      - Si vuelve a haber empate, se preserva orden de llegada (estabilidad),
        seleccionando el elemento del subarray izquierdo.
    """
    n = len(tracks)
    if n > 1:
        a = tracks[:n//2]
        b = tracks[n//2:]
        
        #recursion
        sort_playlist_by_flow(a, use_energy)
        sort_playlist_by_flow(b, use_energy)
        
        #merge
        i = 0
        j = 0
        k = 0
        while i < len(a) and j < len(b):
            if a[i][1] < b[j][1]:
                tracks[k] = a[i]
                i += 1
            elif a[i][1] > b[j][1]:
                tracks[k] = b[j]
                j += 1
            else:
                if use_energy:
                    if a[i][2] >= b[j][2]:
                        tracks[k] = a[i]
                        i += 1
                    else:
                        tracks[k] = b[j]
                        j += 1 
                else:
                    tracks[k] = a[i]
                    i += 1                    
            k += 1
            
        while i < len(a):
            tracks[k] = a[i]
            i += 1
            k += 1
            
        while j < len(b):
            tracks[k] = b[j]
            j += 1
            k += 1
        
        if n == len(tracks):  # top-level call
            return [t[0] for t in tracks]        