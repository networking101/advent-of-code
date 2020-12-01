import math

def compute_lcm(x,y,z):
    lcm = x
    temp = math.gcd(lcm,y)
    lcm = int(lcm*y/temp)
    temp = math.gcd(lcm,z)
    lcm = int(lcm*z/temp)
    return lcm

a = [[4,12,13],[0,0,0]]
b = [[-9,14,-3],[0,0,0]]
c = [[-7,-1,2],[0,0,0]]
d = [[-11,17,-1],[0,0,0]]

A = [[4,12,13],[0,0,0]]
B = [[-9,14,-3],[0,0,0]]
C = [[-7,-1,2],[0,0,0]]
D = [[-11,17,-1],[0,0,0]]

#a = [[-8,-10,0],[0,0,0]]
#b = [[5,5,10],[0,0,0]]
#c = [[2,-7,3],[0,0,0]]
#d = [[9,-8,-3],[0,0,0]]

l = []
ol = []

l.append(a)
l.append(b)
l.append(c)
l.append(d)

ol.append(A)
ol.append(B)
ol.append(C)
ol.append(D)

for i in l:
    print(i)
print('\n')

# Part 1
"""
for i in range(1000):
    for j in l:
        nl = list(l)
        nl.remove(j)
        for k in nl:
            #print "k: " + str(k)
            #print "j: " + str(j)
            for m in range(3):
                if k[0][m] < j[0][m]:
                    j[1][m] -= 1
                elif k[0][m] > j[0][m]:
                    j[1][m] += 1

    for j in l:
        for k in range(3):
            j[0][k] = j[0][k] + j[1][k]

    for j in l:
        print j
    print '\n'

tenergy = 0
for i in l:
    penergy = 0
    kenergy = 0
    for j in range(3):
        penergy += abs(i[0][j])
        kenergy += abs(i[1][j])
    tenergy += penergy * kenergy

print "TOTAL ENERGY: " + str(tenergy)
"""

# Part 2
"""
count = 0
timer = 0
failed = 0
while True:
    failed = 0
    for j in l:
        nl = list(l)
        nl.remove(j)
        for k in nl:
            for m in range(3):
                if k[0][m] < j[0][m]:
                    j[1][m] -= 1
                elif k[0][m] > j[0][m]:
                    j[1][m] += 1

    for j in range(4):
        for k in range(3):
            temp = l[j][0][k] + l[j][1][k]
            l[j][0][k] = temp
            #print "TEMP: " + str(temp)
            #print "OL  : " + str(ol[j][0][k])
            if failed == 0:
                if temp != ol[j][0][k]:
                    failed = 1
    if failed == 0:
        print timer
        exit()
    if timer%100000 == 0:
        print "TIME: " + str(timer)
    timer += 1
"""

xp = [4,-9,-7,-11]
#xp = [-8,5,2,9]
oxp = list(xp)
xv = [0,0,0,0]
oxv = list(xv)

yp = [12,14,-1,17]
#yp = [-10,5,-7,-8]
oyp = list(yp)
yv = [0,0,0,0]
oyv = list(yv)

zp = [13,-3,2,-1]
#zp = [0,10,3,-3]
ozp = list(zp)
zv = [0,0,0,0]
ozv = list(zv)

print(xp)
print(xv)
print('\n')
print(yp)
print(yv)
print('\n')
print(zp)
print(zv)
print('\n')

xcount = 0
while True:
#for k in range(10):
    for i in range(4):
        for j in range(1,4):
            if xp[i] < xp[(i+j)%4]:
                xv[i] += 1
            if xp[i] > xp[(i+j)%4]:
                xv[i] -= 1
    for i in range(4):
        xp[i] += xv[i]
    xcount += 1
    if oxp == xp and oxv == xv:
        print("X Count: " + str(xcount))
        print(xp)
        print(xv)
        break

ycount = 0
while True:
    for i in range(4):
        for j in range(1,4):
            if yp[i] < yp[(i+j)%4]:
                yv[i] += 1
            if yp[i] > yp[(i+j)%4]:
                yv[i] -= 1
    for i in range(4):
        yp[i] += yv[i]
    ycount += 1
    if oyp == yp and oyv == yv:
        print("Y Count: " + str(ycount))
        print(yp)
        print(yv)
        break

zcount = 0
while True:
    for i in range(4):
        for j in range(1,4):
            if zp[i] < zp[(i+j)%4]:
                zv[i] += 1
            if zp[i] > zp[(i+j)%4]:
                zv[i] -= 1
    for i in range(4):
        zp[i] += zv[i]
    zcount += 1
    if ozp == zp and ozv == zv:
        print("Z Count: " + str(zcount))
        print(zp)
        print(zv)
        break

total = compute_lcm(xcount,ycount,zcount)
print(total)































