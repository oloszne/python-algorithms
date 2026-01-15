from typing import List, Tuple

def solve_house_robber(values: List[int]) -> Tuple[int, List[int]]:
    """
    Variante del ladrón de casas con salto por alarma:
    Si robas la casa i, debes saltarte las dos siguientes (i-1 e i-2), 
    es decir, solo puedes sumar lo mejor de i-3.

    Recibe la lista `values` con los valores de las casas.
    Devuelve: (max_benefit, houses_1_based)
    """

    max_benefit = 0 # mejor beneficio
    houses = [] # lista de casas robadas 
    dp = []
    n = len(values)
    
    # Base cases
    if n == 0:
        return 0, []
    if n > 0:
        dp.append(values[0])
        if n > 1:
            dp.append(max(values[0], values[1]))
            if n > 2:
                dp.append(max(dp[1], values[2]))
            
    
    def fill_dp():
        nonlocal dp
        for i in range(3, n):
            dp.append(max(dp[i-1], dp[i-3] + values[i]))
    
    # Reverse search
    def fill_houses():
        nonlocal houses
        nonlocal max_benefit
        
        i = n - 1
        
        while i >= 0:
            if i > 0 and dp[i] == dp[i-1]:
                i -= 1
            else:
                max_benefit += values[i]
                houses.append(i + 1)
                i -= 3
        houses.reverse()
                
    if n > 3:
        fill_dp()
        
    fill_houses()
    
    return max_benefit, houses
