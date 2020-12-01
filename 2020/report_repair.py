with open("input.txt", "r") as fp:
    lines = [int(line.strip()) for line in fp]

# silver
for i in lines:
    for j in lines:
        k = i + j
        if k == 2020:
            print(i * j)

print("")

# gold
for i in lines:
    for j in lines:
        for k in lines:
            l = i + j + k
            if l == 2020:
                print(i * j * k)

