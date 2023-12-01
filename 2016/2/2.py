with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

keypad = [[1, 2, 3],\
          [4, 5, 6],\
          [7, 8, 9]]

for l in lines:

    pos = [1,1]
    for c in l:
        if c == 'U':
            if pos[0] != 0:
                pos[0] -= 1
        if c == 'D':
            if pos[0] != 2:
                pos[0] += 1
        if c == 'L':
            if pos[1] != 0:
                pos[1] -= 1
        if c == 'R':
            if pos[1] != 2:
                pos[1] += 1
    
    y, x = pos
    print(keypad[y][x], end="")
print()

keypad = [["0", "0", "0", "0", "0", "0", "0"],\
          ["0", "0", "0", "1", "0", "0", "0"],\
          ["0", "0", "2", "3", "4", "0", "0"],\
          ["0", "5", "6", "7", "8", "9", "0"],\
          ["0", "0", "A", "B", "C", "0", "0"],\
          ["0", "0", "0", "D", "0", "0", "0"],\
          ["0", "0", "0", "0", "0", "0", "0"]]

for l in lines:

    pos = [3, 1]
    for c in l:
        y, x = pos
        if c == 'U':
            if keypad[y - 1][x] != "0":
                pos[0] -= 1
        if c == 'D':
            if keypad[y + 1][x] != "0":
                pos[0] += 1
        if c == 'L':
            if keypad[y][x - 1] != "0":
                pos[1] -= 1
        if c == 'R':
            if keypad[y][x + 1] != "0":
                pos[1] += 1

    y, x = pos
    print(keypad[y][x], end="")
print()