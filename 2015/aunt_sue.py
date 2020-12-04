with open("text.txt", "r") as fp:
    lines = [line.strip() for line in fp]

mem = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0, "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1}

print(mem)

pos = []

for line in lines:
    l = line.split()
    name = l[0]

    case = True
    for i in range(2, len(l)):
        if i%2 == 0:
            val = l[i].strip(":")
            if val == "pomeranians" or val == "goldfish":
                if mem[val] <= int(l[i+1].strip(",")):
                    case = False
            if val == "cats" or val == "trees":
                if mem[val] >= int(l[i+1].strip(",")):
                    case = False
            if val != "cats" and val != "trees" and val != "pomeranians" and val != "goldfish":
                if mem[val] != int(l[i+1].strip(",")):
                    case = False

    if case == True:
        pos.append(line)

for i in pos:
    print(i)
