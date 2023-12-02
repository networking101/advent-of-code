with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

bots = [0] * 1000
instructions = []

for line in lines:
    if line[:5] == "value":
        _, v, _, _, _, b = line.split()
        v, b = [int(z) for z in [v, b]]
    
    if line[:3] == "bot":
        instructions.append(line)