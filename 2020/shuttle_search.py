with open("input.txt", "r") as fp:
    lines = [line.strip() for line in fp]

#ans = "silver"
ans = "gold"

depart = int(lines.pop(0))

if ans == "silver":
    schedule = [x.strip() for x in lines[0].split(',')]
    schedule = list(filter(lambda x: x != 'x', schedule))
    schedule = [int(x) for x in schedule]

    i = depart
    bid = 0
    found = False
    while True:
        for x in schedule:
            if i%x == 0:
                bid = x
                found = True
                break
        
        if found == True:
            break 
        i += 1

    print("Silver:  " + str((i-depart) * bid))

if ans == "gold":
    data = {}
    sch = [x.strip() for x in lines[0].split(',')]
    for i in range(len(sch)):
        if sch[i] != 'x':
            data[sch[i]] = i

    keys = list(data.keys())
    offset = []
    multi = 1
    j = 1
    for i in range(len(data)-1):
        a = int(keys[i])
        b = int(keys[i+1])
        diff = data[keys[i+1]] - data[keys[i]]
        cnt = 0
        y = 0
        z = 0
        while True:
            if (a*j + diff) % b == 0:
                k = int((a*j + diff) / b)
                if cnt == 1:
                    multi = int((b*k - z) / b)
                    break
                cnt += 1
                y = a*j
                z = b*k

            j = j + multi

        j = k - multi
    print("Gold:  " + str(z - len(sch) + 1))