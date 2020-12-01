with open("text.txt", "r") as fp:
    lines = [line.strip() for line in fp]

print(lines)

# count total characters
tot = 0
for line in lines:
    tot += len(line)

for i in range(0):
    print("DEBUG")
    lines.pop(0)


counter = 0

# count actual characters
actual = 0
"""
for line in lines:
    temp = len(line) - 2
    #print("DEBUG")
    #print(len(line))
    for i in range(1, len(line)-1):
        if counter > 0:
            counter -= 1
            continue
        #print(str(i-1), end="  ")
        #print(line[i-1])
        if line[i-1] == "\\":
            if line[i] == "x":
                temp -= 3
                counter += 3
            else:
                temp -= 1
                counter += 1
    actual += temp
    print("")
    print(line)
    print(temp)
    print("")
    #exit(0)
"""

for line in lines:
    temp = len(line) + 2
    for i in range(len(line)):
        if line[i] == "\"":
            temp += 1
        if line[i] == "\\":
            temp += 1
    actual += temp
    print("")
    print(line)
    print(temp)
    print("")


print(actual-tot)

