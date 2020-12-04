with open("text.txt", "r") as fp:
    lines = [line.strip() for line in fp]

data = {}
for line in lines:
    t = line.split()
    data[t[0]] = [int(x) for x in [t[3], t[6], t[13]]]
    data[t[0]].append(0)
    data[t[0]].append(0)


for i in range(2503):

    for r in data:
        a = i % (data[r][1] + data[r][2])
        if a < data[r][1]:
            data[r][3] += data[r][0]
    
    rein = []
    rmax = 0
    for r in data:
        if data[r][3] > rmax:
            rmax = data[r][3]
            rein = [r]
        elif data[r][3] == rmax:
            rein.append(r)
    for r in rein:
        data[r][4] += 1
    

tot = []
for r in data:
    tot.append(data[r][4])
print(max(tot))
