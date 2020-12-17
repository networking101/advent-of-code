with open("input.txt", "r") as fp:
    lines = [line.strip() for line in fp]

fields = []
for i in range(len(lines)):
    if not lines[i]:
        break
    left, b = lines[i].split(" or ")
    a = left.split()[-1]
    a1, a2 = [int(x) for x in a.split('-')]
    b1, b2 = [int(x) for x in b.split('-')]
    fields.append([range(a1, a2+1), range(b1, b2+1)])

yt = [int(x) for x in lines[i+2].split(",")]

nt = []
for i in range(i+5, len(lines)):
    nt.append([int(x) for x in lines[i].split(",")])

tser = 0
validnt = []
for ticket in nt:
    caset = True
    for number in ticket:
        case = False
        for field in fields:
            if number in field[0] or number in field[1]:
                case = True

        if case == False:
            caset = False
            tser += number

    if caset == True:
        validnt.append(ticket)

print("Silver:  " + str(tser))

validfields = []
for i in yt:
    t = []
    for j in range(len(fields)):
        t.append(j)
    validfields.append(t)

for ticket in validnt:
    for numberindex in range(len(ticket)):
        for fieldindex in range(len(fields)):
            if ticket[numberindex] not in fields[fieldindex][0] and ticket[numberindex] not in fields[fieldindex][1]:
                if fieldindex in validfields[numberindex]:
                    validfields[numberindex].remove(fieldindex)

positions = [-1] * len(yt)

while any(validfields):
    for positionindex in range(len(validfields)):
        if len(validfields[positionindex]) == 1:
            t = validfields[positionindex].pop(0)
            x = positionindex
            positions[x] = t
            for j in validfields:
                if t in j:
                    j.remove(t)

dsum = 1
index = 0
for i in positions:
    if i <= 5:
        dsum *= yt[index]
    index += 1

print("Gold:  " + str(dsum))