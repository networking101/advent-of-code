with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

# Silver
gamma_rate = 0
epsilon_rate = 0
bitsize = len(lines[0])
index = [int(line, 2) for line in lines]
for x in range(bitsize):
    gamma_rate = gamma_rate << 1
    epsilon_rate = epsilon_rate << 1
    most_common = 0
    for l in index:
        l = l >> (bitsize - 1 - x)
        tmp = l & 1
        most_common += tmp
    if most_common > len(lines)/2:
        gamma_rate += 1
    else:
        epsilon_rate += 1

print(epsilon_rate * gamma_rate)

# Gold
bitsize = len(lines[0])
index = [int(line, 2) for line in lines]
for x in range(bitsize):
    most_common = 0
    big = []
    small = []
    for l in index:
        l1 = l >> (bitsize - 1 - x)
        tmp = l1 & 1
        most_common += tmp
        if tmp:
            big.append(l)
        else: 
            small.append(l)
    if most_common >= len(index)/2:
        index = big
    else:
        index = small
    if len(index) == 1:
        break

oxygen = index[0]

index = [int(line, 2) for line in lines]
for x in range(bitsize):
    most_common = 0
    big = []
    small = []
    for l in index:
        l1 = l >> (bitsize - 1 - x)
        tmp = l1 & 1
        most_common += tmp
        if tmp:
            big.append(l)
        else: 
            small.append(l)
    if most_common < len(index)/2:
        index = big
    else:
        index = small
    if len(index) == 1:
        break

c02 = index[0]

print(oxygen * c02)