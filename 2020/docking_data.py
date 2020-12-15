with open("input.txt", "r") as fp:
    lines = [line.strip() for line in fp]

htsize = 0x10001
ht = [0] * 0x10001

data = {}

temp = []
for line in lines:
    if line[:4] == "mask":
        data[line[7:]] = []
        temp = data[line[7:]]
        continue
    temp.append(line)

#ans = "silver"
ans = "gold"

if ans == "silver":
    for i in data:
        band = int(i.replace('X', '1'), 2)
        bor = int(i.replace('X', '0'), 2)
        for j in data[i]:
            left, right = j.split(" = ")
            right = int(right)
            left = int(left.strip("mem[").strip("]"))
            right = (right & band) | bor

            ht[left] = right

    print("Silver:  " + (str(sum(ht))))


if ans == "gold":
    found = {}
    def recurse(addr, r):
        global ht
        if 'X' not in addr:
            found[addr] = r
            return
        recurse(addr.replace('X', '0', 1), r)
        recurse(addr.replace('X', '1', 1), r)

    for i in data:
        for j in data[i]:
            left, right = j.split(" = ")
            right = int(right)
            left = int(left.strip("mem[").strip("]"))

            addr = bin(left)[2:].zfill(36)
            mask = ""
            for k in range(len(i)):
                if i[k] == 'X':
                    mask += 'X'
                if i[k] == '1':
                    mask += '1'
                if i[k] == '0':
                    mask += addr[k]
            
            recurse(mask, right)

    s = 0
    for i in found:
        s += found[i]

    print("Gold  " + str(s))