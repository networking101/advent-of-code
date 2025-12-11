with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

devices = {}

for line in lines:
    l, r = line.split(': ')
    r = r.split()
    
    devices[l] = r

def recurse(curr_dev):
    if curr_dev == "out":
        return 1
    
    tmp = 0
    for d in devices[curr_dev]:
        tmp += recurse(d)

    return tmp


silver = recurse("you")
print(silver)


DP = {}
def recurse_gold(curr_dev, dac, fft):
    if curr_dev == "out":
        if dac and fft:
            return 1
        return 0
    
    if (curr_dev, dac, fft) in DP:
        return DP[(curr_dev, dac, fft)]
    
    tmp = 0
    for d in devices[curr_dev]:
        if d == "dac":
            dac = 1
        if d == "fft":
            fft = 1
        tmp += recurse_gold(d, dac, fft)
        
    DP[(curr_dev, dac, fft)] = tmp
    return tmp

gold = recurse_gold("svr", 0, 0)

print(gold)