from copy import deepcopy
from typing import Mapping

with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

count = 0
for line in lines:
    left, right = line.split(" | ")
    for r in right.split(" "):
        if len(r) == 2 or len(r) == 3 or len(r) == 4 or len(r) == 7:
            count += 1
    

print(count)

# Gold
alphabet = "abcdefg"
mapped = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9
}

total = 0

def transpose(input, keys):
    output = ""
    for i in input:
        for j in keys:
            if i == keys[j]:
                output += j

    return output

for line in lines:
    solved = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, }
    left, right = line.split(" | ")

    cf = 0
    bd = 0

    while True:

        # break if we've found every value
        f = True
        for i in solved:
            if solved[i] == 0:
                f = False
                break

        if f == True:
            break

        for l in left.split(" "):
            t = 0

            if len(l) == 2:
                cf = l
                continue
            
            if not cf:
                continue
            
            if len(l) == 4:
                try:
                    temp = cf
                except:
                    continue
                bd = ""
                for i in l:
                    if i not in cf:
                        bd += i

            # find a using 7
            if len(l) == 3 and solved['a'] == 0:
                try:
                    tmp = cf
                except:
                    continue
                for i in l:
                    if i not in cf:
                        solved['a'] = i
                        break
                continue

            # find d using 0
            if len(l) == 6 and solved['d'] == 0:
                try:
                    temp = cf + bd
                except:
                    continue
                if not all(elem in l for elem in bd):
                    for i in alphabet:
                        if i not in l:
                            solved['d'] = i
                            break
            
            # find b using 4
            if len(l) == 4 and solved['b'] == 0:
                try:
                    tmp = cf + solved['d']
                except:
                    continue
                for i in l:
                    if i not in tmp:
                        solved['b'] = i
                        break
                continue

            # find g using 9
            if len(l) == 6 and solved['g'] == 0:
                try:
                    tmp = cf + solved['d'] + solved['b'] + solved['a']
                except:
                    continue
                found = True
                for i in tmp:
                    if i not in l:
                        found = False
                        break
                if found == True:
                    for j in l:
                        if j not in tmp:
                            solved['g'] = j
                            break

            # find e using 8
            if len(l) == 7 and solved['e'] == 0:
                try:
                    tmp = cf + solved['d'] + solved['b'] + solved['a'] + solved['g']
                except:
                    continue
                for i in l:
                    if i not in tmp and i not in cf:
                        solved['e'] = i
                        break
                continue

            # find c and f using 6
            if len(l) == 6 and solved['f'] == 0:
                try:
                    temp = solved['a'] + solved['b'] + solved['d'] + solved['e'] + solved['g']
                except:
                    continue
                if all (elem in l for elem in temp):
                    for i in l:
                        if i not in temp:
                            solved['f'] = i
                            # fill in f
                            alph = deepcopy(alphabet)
                            for j in alph:
                                if solved[j] != 0:
                                    alph = alph.replace(solved[j], "")
                            solved['c'] = alph
                            break

    tmpTotal = 0
    for oldr in right.split(" "):
        r = transpose(oldr, solved)
        for i in mapped:
            if sorted(r) == sorted(i):
                tmpTotal += mapped[i]
                tmpTotal *= 10
                break
    tmpTotal = int(tmpTotal/10)
    total += tmpTotal

print(total)