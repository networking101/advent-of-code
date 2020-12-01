import sys
import math

mylist = []


with open("input.txt") as fp:
    line = fp.readline()
    while line:
        mylist.append(line)
        line = fp.readline()

outlist = []

for i in range(len(mylist)):
    for j in range(len(mylist[i])):
        if mylist[i][j] == '#':
            outlist.append([i,j])

#print mylist[0][5]
#print mylist[5][0]

# Part 1
"""
finallist = []
coords = []
count = 0
for i in list(outlist):
    vert = [0,0]
    horiz = [0,0]
    poslist = []
    neglist = []
    coords.append([i[0],i[1]])
    for j in list(outlist):
        y = j[0]-i[0]
        x = j[1]-i[1]
        if x == 0:
            if y > 0:
                vert[0] = 1
            if y < 0:
                vert[1] = 1
            continue
        if y == 0:
            if x > 0:
                horiz[0] = 1
            if x < 0:
                horiz[1] = 1
            continue
        result = float(y)/float(x)
        if y>0 and result not in poslist:
            poslist.append(result)
        if y<0 and result not in neglist:
            neglist.append(result)
    finallist.append(len(poslist)+len(neglist)+vert[0]+vert[1]+horiz[0]+horiz[1])
    count += 1

print "COUNT: " + str(count)

print '\n'
print max(finallist)

maxim = 0
for i in range(len(finallist)):
    if finallist[i]>finallist[maxim]:
        maxim = i
print coords[maxim]
"""

# Part 2
lazer = [28,26] 


half1 = []
half2 = []
for j in outlist:
    y = j[0]-lazer[0]
    x = j[1]-lazer[1]
    if x>0:
        half1.append(j)
    #if x>0 and y>0:
    #    quad2.append(j)
    if x<0:
        half2.append(j)
    #if x<0 and y<0:
    #    quad4.append(j)

count = 0

#print half2

yy=0
xx=1
MAX = 1000000
rem = 0
lowerbound = -1000000
answer = []
while count < 198:
    # half 1
    if xx==1:
        changed = 0
        upperbound = [1000000,MAX]
        f = [0,0]
        for i in half1:
            y = i[0]-lazer[0]
            x = i[1]-lazer[1]
            f[0] = float(y)/float(x)
            f[1] = abs(y) + abs(x)
            if f[0] > lowerbound:
                if f[0] < upperbound[0]:
                    upperbound = [f[0],f[1]]
                    rem = i
                    changed = 1
                elif f[0] == upperbound[0]:
                    if f[1] < upperbound[1]:
                        upperbound = [f[0],f[1]]
                        changed = 1
                        rem = i
        if changed == 1:
            lowerbound = upperbound[0]
            print str(rem) + "  " + str(lowerbound)
            half1.remove(rem)
            outlist.remove(rem)
            answer = rem
            count += 1
        else:
            xx = -1
            yy = 0
            lowerbound = -1000000
            print "DEBUG, FINISH FIRST HALF"

    # positive vertical
    if yy == 1:
        break

    # half 2
    if xx == -1:
        changed == 0
        upperbound = [1000000,MAX]
        f = [0,0]
        for i in half2:
            y = i[0]-lazer[0]
            x = i[1]-lazer[1]
            f[0] = float(y)/float(x)
            f[1] = abs(y) + abs(x)
            if f[0] > lowerbound:
                if f[0] < upperbound[0]:
                    upperbound = [f[0],f[1]]
                    rem = i
                    changed = 1
                elif f[0] == upperbound[0]:
                    if f[1] < upperbound[1]:
                        upperbound = [f[0],f[1]]
                        changed = 1
                        rem = i
        if changed == 1:
            lowerbound = upperbound[0]
            print str(rem) + "  " + str(lowerbound)
            half2.remove(rem)
            outlist.remove(rem)
            count += 1
            answer = rem
        else:
            xx = 0
            yy = -1
            lowerbound = -1000000
            print "DEBUG, FINISH SECOND HALF"

    if yy == -1:
        break

print answer
#print half2






