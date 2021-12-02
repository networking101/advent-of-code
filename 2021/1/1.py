with open("input", "r") as fp:
    lines = [int(line.strip()) for line in fp]

print(sum(x < y for x, y in zip(lines, lines[1:])))
print(sum(x < y for x, y in zip(lines, lines[3:])))
