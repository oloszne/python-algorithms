# Recurrencia del problema del ladrón
# -----------------------------------
#    t(n) = max (t(n-2) + v[n], t(n-1))
#    t(n) = 0		               : si n<0

def solve_memoization(items):
    mem = {}
    taken = []

    def t(n):
        nonlocal mem
        if n < 0:
            return 0
        
        if n not in mem:
            r = max(t(n-2) + items[n], t(n-1))
            mem[n] = r
            
        return mem[n]

    def fill_taken():
        nonlocal mem, taken
        
        i = len(items) - 1
        
        while i >= 0:
            if t(i-2) + items[i] > t(i-1):
                taken.append(i + 1)
                i -= 2
            else:
                i -= 1
        taken.reverse()

    n = len(items) - 1    
    
    max_benefit = t(n)
    fill_taken()
    
    return max_benefit, taken
