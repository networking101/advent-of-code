total = 0

def calc_fuel(fuel):
    a = int(fuel/3) - 2
    if (a<=0):
        return 0
    else:
        return a + calc_fuel(a)

with open("input.txt") as fp:
    line = fp.readline()
    while line:
        total += calc_fuel(int(line))
        line = fp.readline()

print total
