with open("input.txt", "r") as fp:
    lines = [int(line.strip()) for line in fp]

lines.sort()

onejd = 0
threejd = 0
prev = 0
for i in range(len(lines)):
    nls = lines[i:i+3]
    for j in nls:
        if j - prev == 1:
            onejd += 1
        if j - prev == 3:
            threejd += 1

        prev = j
        break
threejd += 1

print("Silver  " + str(threejd * onejd))

lines.append(max(lines)+3)

data = {}
found = []
tot = 1
def recurse(p, l):
    cnt = 0
    nl = l[:3]
    for j in range(len(nl)):
        if nl[j] - p <= 3:
            if len(l[j+1:]) == 1:
                cnt += 1
                break
            cnt += recurse(nl[j], l[j+1:])

    return cnt

low = 0
tot = 1
lines.insert(0, 0)
for i in range(1,len(lines)-1):
    if lines[i+1] - lines[i-1] > 3:
        nl = lines[low:i+1]
        if len(nl) == 2:
            low = i
            continue
        tot *= recurse(lines[low], nl)
        low = i


print("Gold  " + str(tot))
