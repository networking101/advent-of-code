with open("input", "r") as fp:
    line = [line.strip() for line in fp][0]

found = False
for i in range(len(line)):
    if len(set(line[i:i+4])) == 4 and not found:
        print(i+4)
        found = True

    if len(set(line[i:i+14])) == 14:
        print(i+14)
        break
