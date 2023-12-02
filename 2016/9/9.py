import numpy as np

with open("input", "r") as fp:
    compressed = [line.strip() for line in fp][0]

decompressed = ''

index = 0

while index < len(compressed):
    if compressed[index] == '(':
        end = compressed[index:].find(')') + index
        a, b = [int(z) for z in compressed[index+1:end].split('x')]
        index = end+1
        for i in range(b):
            decompressed += compressed[index:index+a]
        index += a
    else:
        decompressed += compressed[index]
        index += 1

print(len(decompressed))

stored = {}

def recurse(comp):
    if comp in stored:
        return stored[comp]
    
    index = 0
    tot = 0
    while index < len(comp):

        nxt = comp[index:].find('(') + index
        if nxt == -1:
            tot += len(comp) - index
            break
        tot += nxt - index

        start_mark = nxt
        end_mark = comp[start_mark:].find(')') + start_mark
        a, b = [int(z) for z in comp[start_mark+1:end_mark].split('x')]
        start_substring = end_mark + 1
        substr = comp[start_substring:start_substring + a]
        index = start_substring + a
        tot += recurse(substr) * b

    stored[comp] = tot

    return tot

print(recurse(compressed))
