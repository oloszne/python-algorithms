
def solve(input_list):
    
    #hashmap
    string_to_digit = {
        "one": "1", "two": "2", "three": "3",
        "four": "4", "five": "5", "six": "6",
        "seven": "7", "eight": "8", "nine": "9"
    }
    
    sum = 0
    for line in input_list:
        digits = []
        i = 0
        while i < len(line):
            if line[i].isdigit():
                digits.append(line[i])
                i += 1
            else:
                matched = False
                for word, digit in string_to_digit.items():
                    if line.startswith(word, i):
                        digits.append(digit)
                        i += 1
                        matched = True
                        break
                if not matched:
                    i += 1
        number = int(digits[0] + digits[-1])
        sum += number
    
    return sum