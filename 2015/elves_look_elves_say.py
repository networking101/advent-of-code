start = "3113322113"

for i in range(50):
    newstart = ""
    index = start[0]
    count = 0
    for j in start:
        if j == index:
            count += 1
        else:
            newstart += str(count) + str(index)
            index = j
            count = 1
    newstart += str(count) + str(index)
    start = newstart

print(len(start))
