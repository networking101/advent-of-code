with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

times = []
distances = []

time2 = 0
distance2 = 0

for line in lines:
    if line[:5] == "Time:":
        times += [int(z) for z in line[5:].split()]
        time2 = int(''.join(line[5:].split()))
    if line[:9] == "Distance:":
        distances += [int(z) for z in line[9:].split()]
        distance2 = int(''.join(line[9:].split()))

count1 = 1
for i, v in enumerate(times):
    max_dist = distances[i]
    curr_count = 0
    for j in range(v):
        curr_dist = j * (v-j)
        if curr_dist > max_dist:
            curr_count += 1
    if curr_count > 0:
        count1 *= curr_count
print(count1)

count2 = 0
for j in range(time2):
    curr_dist = j * (time2 - j)
    if curr_dist > distance2:
        count2 += 1

print(count2)