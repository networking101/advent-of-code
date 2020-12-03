with open("input.txt", "r") as fp:
    lines = [line.strip() for line in fp]

answer = "gold"
#answer = "silver"

count = 0
for line in lines:
    left, right = line.split(": ")
    a, b = left.split()
    begin, end = a.split("-")
    tempcount = 0
    
    if answer == "gold":
        if right[int(begin)-1] == b:
            tempcount += 1
        if right[int(end)-1] == b:
            tempcount += 1
        if tempcount == 1:
            count += 1


    if answer == "silver":
        for i in right:
            if b == i:
                tempcount += 1
        if tempcount >= int(begin) and tempcount <= int(end):
            count += 1


print(count)

