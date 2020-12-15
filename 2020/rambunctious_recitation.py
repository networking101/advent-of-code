with open("input.txt", "r") as fp:
    lines = [line.strip() for line in fp]

data = lines[0].split(",")
print(data)

#ans = "silver"
ans = "gold"

if ans == "silver":
    ending = 2020
if ans == "gold":
    ending = 30000000

last = []
for i in range(ending):
    last.append([])

for i in range(len(data[:-1])):
    last[int(data[i])].append(i)

la = data[-1]
i = len(data)
while len(data) < ending:
    index = int(data[i-1])
    last[index].append(i-1)
    if len(last[int(la)]) == 2:
        diff = last[index][1] - last[index][0]
        last[index].pop(0)
        data.append(diff)
    else:
        data.append(0)
    
    la = data[-1]
    i += 1

print(data[i-1])