with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

colors = {"red":12, "green":13, "blue":14}

stuff = []

count1 = 0
count2 = 0

for line in lines:
    status = True
    possible = {"red":0, "green":0, "blue":0}
    game, rest = line.split(":")
    game = int(game[5:])
    rounds = rest.split(";")
    for r in rounds:
        cubes = [z.strip() for z in r.split(',')]
        for c in cubes:
            num, color = c.split()
            if colors[color] < int(num):
                status = False
            if possible[color] < int(num):
                possible[color] = int(num)

    if status:
        count1 += game

    int_score = 1
    for k, v in possible.items():
        int_score *= v
    count2 += int_score
            

print(count1)
print(count2)