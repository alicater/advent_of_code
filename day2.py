def check_safe(report):
    levels = list(map(int, report.split()))

    increase = True
    for i in range(len(levels)-1):
        if not (1 <= levels [i+1] - levels[i] <= 3):
            increase = False
            break

    decrease = True
    for i in range(len(levels) - 1):
        if not (1 <= levels[i] - levels[i+1] <= 3):
            decrease = False
            break

    return increase or decrease

def check_dampener(report):
    levels = list(map(int, report.split()))

    for i in range(len(levels)):
        new_report = levels[:i] + levels[i+1:]
        if check_safe(" ".join(map(str, new_report))):
            return True
    return False


def count_report(input_file):
    with open(input_file, 'r') as file:
        reports = file.readlines()

    safe_amnt = 0
    for report in reports:
        report = report.strip()
        if check_safe(report) or check_dampener(report):
            safe_amnt+=1
    
    return safe_amnt

input_file = "day2.txt"
safe_amnt = count_report(input_file)
print(f"number of safe reports: {safe_amnt}")