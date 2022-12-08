with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

dirs = {}

curr_dir = ""
for line in lines:
    if line[:5] == "$ cd ":
        if line[5:] == "..":
            tmp = curr_dir.split("/")
            if len(tmp) == 2:
                curr_dir = "/"
            else:
                curr_dir = "/".join(curr_dir.split("/")[:-1])
        else:
            if len(curr_dir) > 1:
                curr_dir += "/" + line[5:]
            else:
                curr_dir += line[5:]
    elif line[:4] != "$ ls":
        if curr_dir not in dirs:
            dirs[curr_dir] = [line]
        else:
            dirs[curr_dir].append(line)

sizes = {}
def recurse(d):
    if d not in sizes:
        sizes[d] = 0
    for y in dirs[d]:
        if y[:4] == "dir ":
            n = y[4:]
            if d+n not in sizes:
                if d == "/":
                    recurse(d+n)
                    sizes[d] += sizes[d+n]
                else:
                    recurse(d+"/"+n)
                    sizes[d] += sizes[d+"/"+n]
        else:
            sizes[d] += int(y.split()[0])

recurse('/')

tot = 0
for s in sizes:
    if sizes[s] <= 100000:
        tot += sizes[s]

print(tot)

max_size = 70000000
for s in sizes:
    if (30000000 - 70000000 + sizes["/"]) < sizes[s] < max_size:
        max_size = sizes[s]

print(max_size)