# solve_vpl.py — Esqueleto para alumnos

def solve(total: int, max10: int, max20: int, max50: int) -> str:
    if total % 10 != 0 or total < 0:
        return "ERROR"
    
    for b50 in range(min(max50, total // 50), -1, -1):
        rem1 = total - (b50 * 50)
        if rem1 == 0:
            return f"0 0 {b50}"
        for b20 in range(min(max20, rem1 // 20), -1, -1):
            rem2 = rem1 - (b20 * 20)
            if rem2 % 10 == 0:
                b10 = rem2 // 10
            if b10 <= max10:
                return f"{b10} {b20} {b50}"
            

    # retornando error por defecto
    return "ERROR"
