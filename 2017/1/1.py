with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

line = [int(i) for i in lines[0]]

silver = 0
gold = 0

i = 0
while i < len(line):
    multiples = 0
    start = line[i]
    while i+1 < len(line) and start == line[i+1]:
        multiples += start
        i += 1
    
    if multiples == 0:
        i += 1

    silver += multiples

if line[-1] == line[0]:
    silver += line[0]

for i, v in enumerate(line):
    j = int(i + len(line)/2) % len(line)
    if v == line[j]:
        gold += v

print(silver)
print(gold)

# 995 too low