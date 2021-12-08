from copy import deepcopy

with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

line = [int(x) for x in lines[0].split(",")]

minval = min(line)
maxval = max(line)

def fuel(l, c):
    ret_val = 0
    for i in l:
        ret_val += abs(c - i)
    return ret_val

curr = minval
curr_val = fuel(line, curr)
ncurr_val = fuel(line, curr+1)
while (ncurr_val < curr_val):
    curr += 1
    curr_val = ncurr_val
    ncurr_val = fuel(line, curr+1)

print(curr_val)

# Gold

def fuel2(l, c):
    ret_val = 0
    for i in l:
        for j in range(abs(c-i)):
            ret_val += j+1
    return ret_val

curr = minval
curr_val = fuel2(line, curr)
ncurr_val = fuel2(line, curr+1)
while (ncurr_val < curr_val):
    curr += 1
    curr_val = ncurr_val
    ncurr_val = fuel2(line, curr+1)

print(curr_val)