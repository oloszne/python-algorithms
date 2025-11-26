
def solve_memoization(items, capacity):
    taken = []
    mem={}

    def t(n,w):
        nonlocal mem
        
        if (n, w) in mem:
            return mem[(n, w)]
        
        if n < 0 or w == 0:
            return 0  
        
        if items[n].weight > w:
            r = t(n-1, w)
        else:
            r = max(t(n-1, w), t(n-1, w - items[n].weight) + items[n].value)
        
        mem[(n, w)] = r
        return r

    def fill_taken():
        nonlocal taken
        nonlocal n
        w = capacity
        
        while n >= 0 and w > 0:
            if t(n, w) != t(n-1, w):
                taken.append(n + 1)
                w -= items[n].weight
            n -= 1
        taken.reverse()
        
    n = len(items)-1

    max_benefit = t(n,capacity)
    fill_taken()

    return max_benefit, taken
    