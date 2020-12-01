import sys

with open('input.txt') as fp:
    line = fp.readline()

i = 0
z = 0
layers = []
while i < len(line)-1:
    verts = []
    for j in range(6):
        horiz = []
        for k in range(25):
            horiz.append(line[i])
            i += 1
        verts.append(horiz)
    layers.append(verts)

#Part 1
"""
minim = 1000000
ret = 0

for i in layers:
    num0 = 0
    num1 = 0
    num2 = 0
    for j in i:
        for k in j:
            if k == '0':
                num0 += 1
            if k == '1':
                num1 += 1
            if k == '2':
                num2 += 1
    print "Num of 0: " + str(num0)
    if num0 < minim:
        ret = num1*num2
        minim = num0

print ret
"""


#Part 2

layers = layers[::-1]

final_layer = layers.pop(0)
#print final_layer

for i in range(len(layers)):
    for j in range(len(layers[i])):
        for k in range(len(layers[i][j])):
            pixel = layers[i][j][k]
            if pixel != '2':
                final_layer[j][k] = pixel

#print picture
for j in final_layer:
    for k in j:
        if k == '0':
            sys.stdout.write(' ')
        if k == '1':
            sys.stdout.write('8')
        if k == '2':
            sys.stdout.write('-')
    sys.stdout.write('\n')
