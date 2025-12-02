with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

position = 50
silver = 0
gold = 0
for line in lines:
    dir = line[0]
    dist = int(line[1:])
    
    for i in range(dist):
        if dir == 'R':
            position = (position + 1) % 100
        else:
            position = (position - 1) % 100
        
        if not position:
            gold += 1

    if not position:
        silver += 1

print(silver)
print(gold)