import re 

def parse_calc(input_file):
    with open(input_file, 'r') as file:
        data = file.read()

    mul = r'mul\((\d+),\s*(\d+)\)'
    do = r"do\(\)"
    dont = r"don't\(\)"
    pattern = f'{mul}|{do}|{dont}'

    enabled = True
    total = 0

    for match in re.finditer(pattern, data):
        # print(match.groups())
        if match.group() == 'do()':
            enabled = True
        elif match.group() == "don't()":
            enabled = False
        elif match.group(1) and enabled:
            x, y = int(match.group(1)), int(match.group(2))
            total += x * y

    print(total)
    return total


input_file = "day3.txt"
parse_calc(input_file)
