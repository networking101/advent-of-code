with open("text.txt", "r") as fp:
    lines = [line.strip() for line in fp]

count = 0

# Part 1
"""
for line in lines:
    # Case 1
    num_vowels = 0
    for i in line:
        if i in "aeiou":
            num_vowels += 1
    if num_vowels < 3:
        continue

    # Case 2
    case2 = False
    for i in range(1, len(line)):
        if line[i] == line[i-1]:
            case2 = True
    if not case2:
        continue

    # Case 3
    case3 = True
    for i in range(1, len(line)):
        if line[i-1:i+1] == "ab":
            case3 = False
        if line[i-1:i+1] == "cd":
            case3 = False
        if line[i-1:i+1] == "pq":
            case3 = False
        if line[i-1:i+1] == "xy":
            case3 = False

    if case3:
        count += 1
"""

# Part 2
for line in lines:
    # Case 1
    case1 = False

    for i in range(1, len(line)):
        a = line[i-1:i+1]
        for j in range(i+2, len(line)):
            b = line[j-1:j+1]
            if a == b:
                case1 = True
    if not case1:
        continue

    # Case 2
    case2 = False
    for i in range(2, len(line)):
        if line[i] == line[i-2]:
            case2 = True
    if not case2:
        continue

    count += 1
    

print(count)

