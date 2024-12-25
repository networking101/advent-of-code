with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

secrets = [int(x) for x in lines]

def process(s):
    s = ((s * 64) ^ s) % 16777216
    s = (int(s / 32) ^ s) % 16777216
    s = ((s * 2048) ^ s) % 16777216

    return s

silver = 0
for s in secrets:
    for i in range(2000):
        s = process(s)
    # print(s)
    silver += s

print(silver)