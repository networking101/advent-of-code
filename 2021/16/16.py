with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

line = lines.pop()

bline = ""

for i in range(0, len(line), 2):
    bline += bin(int(line[i: i+2], 16))[2:].zfill(8)

def expressions(tID, v):
    if tID == 0:
        return sum(v)
    if tID == 1:
        r = 1
        for x in v:
            r *= x
        return r
    if tID == 2:
        return min(v)
    if tID == 3:
        return max(v)
    if tID == 5:
        if v[0] > v[1]:
            return 1
        else:
            return 0
    if tID == 6:
        if v[0] < v[1]:
            return 1
        else:
            return 0
    if tID == 7:
        if v[0] == v[1]:
            return 1
        else:
            return 0

    return

def parseBits(bl):
    ver = 0
    vals = []
    i = 0
    while i < len(bl)-1:
        version, typeID, i = checkHeader(bl, i)
        ver += version

        if typeID == 4:
            l, i = getLiteral(bl, i)
            vals.append(l)
        else:
            o, v, i = getOperator(bl, i, typeID)
            vals.append(o)
            ver += v

    return (vals, ver)

def parsePackets(bl, pLen):
    ver = 0
    vals = []
    i = 0
    for _ in range(pLen):
        version, typeID, i = checkHeader(bl, i)
        ver += version

        if typeID == 4:
            l, i = getLiteral(bl, i)
            vals.append(l)
        else:
            o, v, i = getOperator(bl, i, typeID)
            vals.append(o)
            ver += v

    return (vals, ver, i)

def getOperator(bl, i, tID):
    ver = 0
    lenTypeID = bl[i]
    i += 1

    if lenTypeID == '0':
        bitLength = int(bl[i:i+15], 2)
        i += 15
        vals, v = parseBits(bl[i: i+bitLength])
        ver += v
        i += bitLength
    else:
        pktLength = int(bl[i:i+11], 2)
        i += 11
        vals, v, i2 = parsePackets(bl[i:], pktLength)
        ver += v
        i += i2

    gold = expressions(tID, vals)

    return (gold, ver, i)

def getLiteral(bl, i):
    val = ""
    while True:
        prefix = bl[i]
        val += bl[i+1: i+5]
        tmp = bl[i+1: i+5]
        i += 5
        if prefix == '0':
            break

    return (int(val, 2), i)

def checkHeader(bl, i):
    v = int(bl[i:i+3], 2)
    tID = int(bl[i+3:i+6], 2)
    return (v, tID, i+6)

ver = 0
i = 0
while i < len(bline)-1:
    version, typeID, i = checkHeader(bline, i)
    ver += version

    if typeID == 4:
        val, i = getLiteral(bline, i)
    else:
        val, v, i = getOperator(bline, i, typeID)
        ver += v
    
    if "1" not in bline[i:]:
        break


print(ver)
print(val)