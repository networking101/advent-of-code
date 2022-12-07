#with open("input", "r") as fp:
with open("input2", "r") as fp:
    lines = [line.strip() for line in fp]

dirs = {}

curr_dir = []
for line in lines:
    if line[:5] == "$ cd ":
        if line[5:] == "..":
            curr_dir.pop()
        else:
            curr_dir.append(line[5:])
    elif line[:4] != "$ ls":
        if curr_dir[-1] not in dirs:
            dirs[curr_dir[-1]] = [line]
        else:
            dirs[curr_dir[-1]].append(line)

for d in dirs:
    print(d, dirs[d])

print()

sizes = {}
def recurse(d):
    if d not in sizes:
        sizes[d] = 0
    for y in dirs[d]:
        if y[:4] == "dir ":
            n = y[4:]
            if n not in sizes:
                recurse(n)
            sizes[d] += sizes[n]
        else:
            sizes[d] += int(y.split()[0])
    print(d + "  :  " + str(sizes[d]))

recurse('/')

tot = 0
for s in sizes:
    if sizes[s] <= 100000:
        tot += sizes[s]

print(tot)

# incorrect guesses
# 1098082