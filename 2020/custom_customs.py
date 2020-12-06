with open("input.txt", "r") as fp:
    lines = [line.strip() for line in fp]

cnt = 0
tl = []

lines.append("")

#ans = "silver"
ans = "gold"

for line in lines:

    if ans == "silver":
        if not line:
            cnt += len(tl)
            tl = []
            continue

        for i in line:
            if i not in tl:
                tl.append(i)

    if ans == "gold":
        if not line:
            for i in tl[0]:
                cond = True
                for j in tl:
                    if i not in j:
                        cond = False
                if cond == True:
                    cnt += 1
            tl = []
            continue

        tl.append(line)

print(cnt)
