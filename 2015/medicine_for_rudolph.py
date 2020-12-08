with open("text2.txt", "r") as fp:
    lines = [line.strip() for line in fp]

mol = lines[-1]

lines.pop()
lines.pop()

conv = {}
for line in lines:
    a, b = [x.strip() for x in line.split("=>")]
    if a not in conv:
        conv[a] = [b]
    else:
        conv[a].append(b)

for x in conv:
    print(x, end="  ")
    print(conv[x])

endmol = []

for j in conv:
    ti = 0
    while True:
        ti = mol.find(j, ti)
        if ti == -1:
            break

        for i in conv[j]:
            ts = ""
            if ti > 0:
                ts += mol[:ti]
            ts += i
            if ti < len(mol)-1:
                ts += mol[ti+1:]
            endmol.append(ts)
        ti += 1


res = set(endmol)

print(len(res))
