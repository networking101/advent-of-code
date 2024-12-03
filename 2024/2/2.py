from copy import deepcopy

with open("input", "r") as fp:
    lines = [[int(x) for x in line.strip().split()] for line in fp]

silver = 0
gold = 0

def check_report(report, iteration):
    tolerate = False
    for i, v in enumerate(report):
        if i == 0:
            continue
        if v <= report[i-1] or v > report[i-1] + 3:
            if iteration == 0 and (check_report(report[:i] + report[i+1:], 1) or check_report(report[:i-1] + report[i:], 1)):
                return True
            return False
    return True


for line in lines:
    if check_report(line, 1) or check_report(line[::-1], 1):
        silver += 1
    if check_report(line, 0) or check_report(line[::-1], 0):
        gold += 1

print(silver)
print(gold)