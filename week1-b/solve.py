
def solve(input_list):
    sum = 0
    for line in input_list:
        digits = [char for char in line if char.isdigit()]
        if digits:
            number = int(digits[0] + digits[-1])
            sum += number
    
    return sum