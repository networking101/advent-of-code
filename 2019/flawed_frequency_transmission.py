with open("input.txt") as f:
    inp = list(map(int, f.read()[::].rstrip()))

def do_phase(lst):
    return [do_comp(lst, i) for i in range(len(lst))]

def get_mult(n, m):
    m += 1
    m %= 4 * n
    if m < n:
        return 0
    elif m < 2 * n:
        return 1
    elif m < 3 * n:
        return 0
    elif m < 4 * n:
        return -1

def do_comp(lst, idx):
    idx += 1
    out = 0
    for i in range(len(lst)):
        out += lst[i] * get_mult(idx, i)
    return int(str(out)[-1:])

def do_phase2(inp):
    s = sum(inp)
    out = []
    for i in range(len(inp)):
        out += [((s % 10) + 10) % 10]
        s -= inp[i]
    return out

part_1 = inp[:]

for i in range(100):
    part_1 = do_phase(part_1)

print("part 1:", "".join(map(str, part_1[:8])))

part_2 = inp[:]
offset = int("".join(map(str, part_2[:7])))
part_2 = part_2 * 10000
part_2 = part_2[offset:]

for i in range(100):
    part_2 = do_phase2(part_2)

print("part2:", "".join(map(str, part_2[:8])))
