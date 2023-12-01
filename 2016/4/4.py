import collections

with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

count = 0

for l in lines:
    rest, check = l.split('[')
    check = check[:-1]

    rest = rest.split('-')
    sid = int(rest[-1])
    text = " ".join(rest[:-1])
    name = sorted(''.join(rest[:-1]))

    d = collections.defaultdict(int)
    for c in name:
        d[c] += 1

    index = 1
    ordered = []
    while d:
        for i, v in enumerate(name[::-1]):
            if v in d and d[v] == index:
                ordered.insert(0, v)
                d.pop(v)

        index += 1

    s = ''.join(ordered[:5])
    if s == check:
        count += sid
        plain = ""
        for t in text:
            if t == " ":
                plain += t
            else:
                c = chr((((ord(t) - 97) + sid) % 26) + 97)
                plain += c
        if plain == "northpole object storage":
            print(sid)

print(count)   
    