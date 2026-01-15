# solve_vpl.py
# Esqueleto de la función de tabulación para implementar por los alumnos.


def solve_tabulation(items):
    """
    Calcula el beneficio máximo y las casas robadas.

    Parámetros
    ----------
    items : list[int]
        Lista de valores de las casas en orden, donde items[i] es el valor
        de la casa i+1 (índice 1-based).

    Devuelve
    --------
    (max_benefit, taken) : (int, list[int])
        max_benefit es el beneficio máximo alcanzable respetando las
        restricciones del enunciado.
        taken es la lista de índices 1-based de las casas robadas,
        en orden creciente.
    """
    # Remove all odd-numbered houses, since they are of no use. Indexes are reversed (index 0 is house 1 so it has to be removed)
    items = items[1::2]
    n = len(items)
    dp = []
    taken = []
    max_benefit = 0 
    
    # Base cases
    if n == 0:
        return 0, []
    if n > 0:
        dp.append(items[0])
        if n > 1:
            dp.append(max(dp[0], items[1]))
    
    def fill_dp():
        nonlocal dp
        for i in range(2, n):
            dp.append(max(dp[i-1], dp[i-2] + items[i]))
            
    def fill_taken():
        nonlocal taken
        nonlocal max_benefit
        i = n - 1
        while i >= 0:
            if i == 0 or dp[i] != dp[i-1]:
                taken.append(2 * (i + 1)) # Reconstruct original index
                max_benefit += items[i]                
                i -= 2
            else:
                i -= 1
        taken.reverse()
    
    if n > 2:
        fill_dp()
    fill_taken()
    
    return max_benefit, taken
