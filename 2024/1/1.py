with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

silver = 0
gold = 0
left = []
right = []

for line in lines:
    l, r = [int(x) for x in line.split()]
    left.append(l)
    right.append(r)

for i, l in enumerate(left):
    count = 0
    for j, r in enumerate(right):
        if l == r:
            count += 1
    gold += l * count

left.sort()
right.sort()

for l, r in zip(left, right):
    silver += abs(l - r)

print(silver)
print(gold)