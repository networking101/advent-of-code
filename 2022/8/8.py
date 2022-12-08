with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

rows = []
cols = []
for l in lines[0]:
    cols.append([])

for i in range(len(lines)):
    rows.append([int(x) for x in lines[i]])
    for j in range(len(lines[i])):
        cols[j].append(int(lines[i][j]))

# Part 1
tot = 2 * len(rows) + 2 * len(cols) - 4
for y in range(1, len(lines)-1):
    for x in range(1, len(lines[y])-1):
        curr = rows[y][x]
        # check top
        if max(cols[x][:y]) < curr:
            tot += 1
            continue
        # check bottom
        if max(cols[x][y+1:]) < curr:
            tot += 1
            continue

        # check left
        if max(rows[y][:x]) < curr:
            tot += 1
            continue

        # check right
        if max(rows[y][x+1:]) < curr:
            tot += 1
            continue
print(tot)

# Part 2
# Need to make all the edges max height to fix counting
for r in range(len(rows)):
    rows[r][0] = 9
    rows[r][-1] = 9

for c in range(len(cols)):
    cols[c][0] = 9
    cols[c][-1] = 9

max_score = 0
for y in range(1, len(lines)-1):
    for x in range(1, len(lines[y])-1):
        curr_score = [1,1,1,1]

        # check top
        curr_val = rows[y][x]
        for z in cols[x][:y][::-1]:
            if z < curr_val:
                curr_score[0] += 1
            else:
                break

        # check bottom
        curr_val = int(lines[y][x])
        for z in cols[x][y+1:]:
            if z < curr_val:
                curr_score[1] += 1
            else:
                break

        # check left
        curr_val = int(lines[y][x])
        for z in rows[y][:x][::-1]:
            if z < curr_val:
                curr_score[2] += 1
            else:
                break

        # check right
        curr_val = int(lines[y][x])
        for z in rows[y][x+1:]:
            if z < curr_val:
                curr_score[3] += 1
            else:
                break

        new_score = curr_score[0] * curr_score[1] * curr_score[2] * curr_score[3]
        if max_score < new_score:
            max_score = new_score

print(max_score)