# 1. Copia aqui tu solución del primer ejercicio de esta semana

def next_number(digits, base):
    next_digits = digits.copy()
    n = len(next_digits)
    x = 1
    
    for i in range (n - 1, -1, -1):
        sum_val = next_digits[i] + x
        next_digits[i] = sum_val % base
        x = sum_val // base
        if x == 0:
            break
    return next_digits
    
# ----------------------------------------------------------

class My_Iterator:
    def __init__(self, num_digits, base):
        self.num_digits = num_digits
        self.base = base
        self.digits = [0] * num_digits

    def next(self):
        current = self.digits
        max_value = [self.base - 1] * self.num_digits

        while True:
            yield current

            if current == max_value:
                return

            current = next_number(current, self.base)
