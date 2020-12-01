with open("text.txt", "r") as fp:
    lines = [line.strip() for line in fp]

skip = 0

def checkVal(x):
    global skip
    left = [i.strip() for i in x.split(" ")]
    a = left[0]
    b = left[2]
    if not a.isnumeric():
        if values[a][0] == 0:
            skip = 1
            return (0,0)
        a = values[a][1]

    if not b.isnumeric():
        if values[b][0] == 0:
            skip = 1
            return (0,0)
        b = values[b][1]

    return (a, b)

def myAnd(x):
    a, b = checkVal(x)

    return int(a) & int(b)

def myOr(x):
    a, b = checkVal(x)
    if x == "c LSHIFT 1" and skip == 0:
        print(a)
        print(b)
        exit(0)
    return int(a) | int(b)

def myLshift(x):
    a, b = checkVal(x)
    

    return int(a) << int(b)

def myRshift(x):
    a, b = checkVal(x)

    return int(a) >> int(b)

def myNot(x):
    global skip
    left = [i.strip() for i in x.split(" ")]
    a = left[1]

    if not a.isnumeric():
        if values[a][0] == 0:
            skip = 1
        a = values[a][1]

    b = int(a)

    return ~b

def update(right, x, line):
    #global newLines
    values[right][0] = 1
    values[right][1] = x
    newLines.remove(line)

newLines = []
values = {}

for line in lines:
    left, right = [i.strip() for i in line.split("->")]
    newLines.append([left, right])

    values[right] = [0,0]

values["b"] = [1, 956]
count = 0
loops = 0
print(values)
while newLines:
    loops += 1
    count += 1
    print("")
    for line in newLines:
        skip = 0
        left = line[0]
        right = line[1]
        
        #print(left)

        if "AND" in left:
            #print("DEBUG AND\t\t  " + str(left))
            x = myAnd(left)
            if skip == 0:
                print(line)
                update(right, x, line)
                count += 1
        elif "OR" in left:
            #print("DEBUG OR\t\t  " + str(left))
            x = myOr(left)
            if skip == 0:
                print(line)
                update(right, x, line)
                count += 1
        elif "LSHIFT" in left:
            #print("DEBUG LSHIFT\t\t  " + str(left))
            x = myLshift(left)
            if skip == 0:
                print(line)
                update(right, x, line)
                count += 1
        elif "RSHIFT" in left:
            x = myRshift(left)
            if skip == 0:
                print(line)
                update(right, x, line)
                count += 1
        elif "NOT" in left:
            #print("DEBUG NOT\t\t  " + str(left))
            x = myNot(left)
            if skip == 0:
                print(line)
                update(right, x, line)
                count += 1
        else:
            if left.isnumeric():
                print(line)
                update(right, left, line)
                count += 1
            elif values[left][0] ==1:
                if right == 'a':
                    print(values)
                    print(values["lx"])
                    exit(0)
                a = values[left][0]
                print(line)
                update(right, a, line)
                count += 1
    #print("DEBUG  " + str(len(newLines)) + "\n")
    print("DEBUG loops  " + str(loops))
    print(len(newLines))
    #if loops == 5:
        #exit(0)

print(values)
print(values["a"])



