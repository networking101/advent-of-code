with open("text.txt", "r") as fp:
    lines = [line.strip() for line in fp]

# silver
for i in lines:
    for j in lines:
        k = int(i) + int(j)
        if k == 2020:
            print(int(i) * int(j))

print("")

# gold
for i in lines:
    for j in lines:
        for k in lines:
            l = int(i) + int(j) + int(k)
            if l == 2020:
                print(int(i) * int(j) * int(k))

