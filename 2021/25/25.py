with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

grid = []
for line in lines:
    row = []
    for c in line:
        row.append(c)
    grid.append(row)