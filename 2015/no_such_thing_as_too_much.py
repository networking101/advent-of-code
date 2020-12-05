from copy import deepcopy

with open("text.txt", "r") as fp:
    lines = [int(line.strip()) for line in fp]

count = 0
target = 150

shortest = []

def recurse(l, s, j):
    global count
    global target
    for i in range(j, len(l)):
        nl = deepcopy(l)
        temp = nl.pop(i)
        if s + temp == target:
            if (len(lines) - len(nl)) == 4:
                count += 1
            shortest.append(len(lines) - len(nl))
            continue
        if s + temp >= target:
            continue
        
        recurse(nl, s + temp, i)


s = 0
recurse(lines, s, 0)

print(min(shortest))
print("Answer  " + str(count))
