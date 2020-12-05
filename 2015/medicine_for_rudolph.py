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

endmol = [""]

def whatever(x):
    global endmol
    global cnt
    for j in range(len(endmol)):
        k = endmol.pop(0)
        for i in conv[x]:
            endmol.append(k + i)

for i in range(len(mol)):
    x = mol[i]
    if x in conv:
        whatever(x)
    y = mol[i:i+2]
    if y in conv:
        whatever(y)

for i in endmol:
    print(i)
print(len(endmol))
