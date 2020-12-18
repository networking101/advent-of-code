with open("input.txt", "r") as fp:
    lines = [line.strip() for line in fp]


def solve(l, s, i):
    nl = l[s:i].split()
    #res = int(nl.pop(0))
    while '+' in nl:
        ind = 0
        while ind <= len(nl) - 1:
            if nl[ind] == "+":
                nl.pop(ind)
                t = int(nl.pop(ind-1)) + int(nl.pop(ind-1))
                nl.insert(ind-1, str(t))
                continue
            ind += 1
    ind = 0
    while len(nl) != 1:
        if nl[ind] == '*':
            nl.pop(ind)
            t = int(nl.pop(ind-1)) * int(nl.pop(ind-1))
            nl.insert(ind-1, str(t))
            continue
        ind += 1
        
    return int(nl[0])

tot = 0
for line in lines:
    i = 0
    start = 0
    while i < len(line):
        if line[i] == '(':
            start = i
        if line[i] == ')':
            res = solve(line, start+1, i)
            line = line[:start] + str(res) + line[i+1:]
            start = 0
            i = 0
            continue

        if start == 0 and i == len(line)-1:
            res = solve(line, start, i +1)
            break

        i += 1
    tot += res

print(str(tot))