#        ABCDEFGHIJKLMN
silver = "92967699949891"
gold   = "91411143612181"

w = 0
x = 0
y = 0
z = 0

#          0   1   2   3   4   5   6    7   8    9  10  11  12   13
first =  [ 1,  1,  1, 26,  1,  1, 26,  26,  1,  26,  1, 26, 26,  26]
second = [11, 14, 13, -4, 11, 10, -4, -12, 10, -11, 12, -1,  0, -11]
third =  [ 3,  7,  1,  6, 14,  7,  9,   9,  6,   4,  0,  7, 12,   1]

start = gold

for i in range(14):
    w = int(start[i])
    x = z
    x = x % 26
    z = z // first[i]
    x += second[i]
    if x == w:
        x = 1
    else:
        x = 0
    y = 25
    y += 1
    z = z * y
    y = w
    y += third[i]
    y = y * x
    z += y

print(z)

"""
for i in range(14):
    w = int(start[i])
    x = (z % 26) + second[i]
    z = z // first[i]
    if x != w:
        z *= 26
        x = 0
    else:
        x = 1
    z += (w + third[i]) * x

print(z)
"""