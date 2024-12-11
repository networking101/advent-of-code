with open("input", "r") as fp:
    line = [line.strip() for line in fp][0]

arrangement = [int(x) for x in line.split()]

DP = {}

def recurse(stone, itter):

    if itter == 0:
        return 1

    ret_val = 0

    if (itter, stone) in DP:
        ret_val = DP[(itter, stone)]

    else:
        stone_str = str(stone)

        if stone == 0:
            ret_val = recurse(1, itter - 1)

        elif len(stone_str) % 2 == 0:
            ret_val = recurse(int(stone_str[:int(len(stone_str) / 2)]), itter - 1)
            ret_val +=  recurse(int(stone_str[int(len(stone_str) / 2):]), itter - 1)

        else:
            ret_val = recurse(stone * 2024, itter - 1)

    DP[(itter, stone)] = ret_val
    return ret_val

silver = 0
gold = 0
for i in arrangement:
    silver += recurse(i, 25)
    gold += recurse(i, 75)

print(silver)
print(gold)