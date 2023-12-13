with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

conditions = []

for line in lines:
    first, second = line.split(' ')
    second = [int(z) for z in second.split(',')]
    conditions.append([first, second])

DP = {}

def recursive(f, s):

    if str((f, s)) in DP:
        return DP[str((f, s))]

    if len(s) == 0:
        if '#' in f:
            return 0
        return 1
    if len(f) < sum(s) + len(s) - 1:
        return 0
        
    count = 0
    s0 = s[0]

    decoded = ''
    if len(s) > 1:
        test = '#' * s0 + '.'
        substring = f[:s0+1]
        for i in substring[:-1]:
            if i == '?':
                decoded += '#'
            else:
                decoded += i
        if substring[-1] == '?':
            decoded += '.'
        else:
            decoded += substring[-1]
    else:
        test = '#' * s0
        substring = f[:s0]
        for i in substring:
            if i == '?':
                decoded += '#'
            else:
                decoded += i

    if decoded == test:
        count += recursive(f[len(decoded):], s[1:])
    if f[0] != '#':
        count += recursive(f[1:], s)

    DP[str((f, s))] = count

    return count


count1 = 0

for con in conditions:
    first, second = con
    count1 += recursive(first, second)

print(count1)

conditions = []
for line in lines:
    first, second = line.split(' ')
    second = [int(z) for z in second.split(',')]
    conditions.append([first + "?" + first + "?" + first + "?" + first + "?" + first, second*5])

DP = {}
count2 = 0
for i, con in enumerate(conditions):
    first, second = con
    count2 += recursive(first, second)

print(count2)