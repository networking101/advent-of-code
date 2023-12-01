with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

vals = []

count = 0

for l in lines:
    vals.append([int(x) for x in l.split()])

for v in vals:
    if (v[0] + v[1]) > v[2] and (v[1] + v[2]) > v[0] and (v[2] + v[0]) > v[1]:
        count += 1

print(count)


count = 0
j = 0
while j < len(vals):
    a = vals[j]
    b = vals[j+1]
    c = vals[j+2]
    
    for i in range(3):
        if (a[i] + b[i]) > c[i] and (b[i] + c[i]) > a[i] and (c[i] + a[i]) > b[i]:
            count += 1
    
    j += 3

print(count)
    