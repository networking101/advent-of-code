import copy
import sys

minim = float("inf")

def print_graph(g, x, y, d):
    for i in range(len(g)):
        for j in range(len(g[i])):
            if i==y and j==x:
                if d == 1:
                    sys.stdout.write('>')
                elif d == 2:
                    sys.stdout.write('v')
                elif d == 3:
                    sys.stdout.write('<')
                elif d == 4:
                    sys.stdout.write('^')
                elif d == 0:
                    sys.stdout.write('0')
            else:
                sys.stdout.write(str(g[i][j]))
        print ''
    print ''


def recurse(g, s, gl, kl, x, y, d, kc):

    global minim

    if s >= minim:
        return float("inf")

    if len(kl) >= kc:
        print "FInished Step: " + str(s)
        print kl
        minim = s
        print_graph(g, x, y, d)
        return s
    
    g2 = copy.deepcopy(g)
    gl2 = copy.deepcopy(gl)
    kl2 = copy.deepcopy(kl)
    count = 0

    raw_input()
    print_graph(g, x, y, d)

    vals = [float("inf")]

    t = g[y][x-1]
    if t != '#':# and t != 1:
        if t == '.' or t == 2 or t == 3 or t == 4:
            g2[y][x] = 3
            vals.append(recurse(g2, s+1, gl2, kl2, x-1, y, 3, kc))
        elif t == 1:
            if d == 1:
                vals.append(float("inf"))
            else:
                g2[y][x] = 3
                vals.append(recurse(g2, s+1, gl2, kl2, x-1, y, 3, kc))
        elif t in gl2:
            if t.lower() in kl2:
                g2[y][x] = 3
                vals.append(recurse(g2, s+1, gl2, kl2, x-1, y, 3, kc))
            else:
                vals.append(float("inf"))
        elif ord(t) >= 97 and ord(t) <= 122:
            kl2.append(t)
            g2[y][x] = 3
            g2[y][x-1] = 3
            vals.append(recurse(g2, s+1, gl2, kl2, x-1, y, 3, kc))
            g2[y][x] = 1
            g2[y][x-1] = 1
            vals.append(recurse(g2, s+2, gl2, kl2, x, y, 1, kc))
    else:
        vals.append(float("inf"))

    t = g[y][x+1]
    if t != '#':
        if t == '.' or t == 1 or t == 2 or t == 4:
            g2[y][x] = 1
            vals.append(recurse(g2, s+1, gl2, kl2, x+1, y, 1, kc))
        elif t == 3:
            if d == 3:
                vals.append(float("inf"))
            else:
                g2[y][x] = 1
                vals.append(recurse(g2, s+1, gl2, kl2, x+1, y, 1, kc))
        elif t in gl2:
            if t.lower() in kl2:
                g2[y][x] = 1
                vals.append(recurse(g2, s+1, gl2, kl2, x+1, y, 1, kc))
            else:
                vals.append(float("inf"))
        elif ord(t) >= 97 and ord(t) <= 122:
            kl2.append(t)
            g2[y][x] = 1
            g2[y][x+1] = 1
            vals.append(recurse(g2, s+1, gl2, kl2, x+1, y, 1, kc))
            g2[y][x] = 3
            g2[y][x+1] = 3
            vals.append(recurse(g2, s+2, gl2, kl2, x, y, 3, kc))
    else:
        vals.append(float("inf"))
    
    t = g[y-1][x]
    if t != '#':
        if t == '.' or t == 1 or t == 3 or t == 4:
            g2[y][x] = 4
            vals.append(recurse(g2, s+1, gl2, kl2, x, y-1, 4, kc))
        elif t == 2:
            if d == 2:
                vals.append(float("inf"))
            else:
                g2[y][x] = 4
                vals.append(recurse(g2, s+1, gl2, kl2, x, y-1, 4, kc))
        elif t in gl2:
            if t.lower() in kl2:
                g2[y][x] = 4
                vals.append(recurse(g2, s+1, gl2, kl2, x, y-1, 4, kc))
            else:
                vals.append(float("inf"))
        elif ord(t) >= 97 and ord(t) <= 122:
            kl2.append(t)
            g2[y][x] = 4
            g2[y-1][x] = 4
            vals.append(recurse(g2, s+1, gl2, kl2, x, y-1, 4, kc))
            g2[y][x] = 2
            g2[y-1][x] = 2
            vals.append(recurse(g2, s+2, gl2, kl2, x, y, 2, kc))
    else:
        vals.append(float("inf"))

    t = g[y+1][x]
    if t != '#':
        if t == '.' or t == 1 or t == 2 or t == 3:
            g2[y][x] = 2
            vals.append(recurse(g2, s+1, gl2, kl2, x, y+1, 2, kc))
        elif t == 4:
            if d == 4:
                vals.append(float("inf"))
            else:
                g2[y][x] = 2
                vals.append(recurse(g2, s+1, gl2, kl2, x, y+1, 2, kc))
        elif t in gl2:
            if t.lower() in kl2:
                g2[y][x] = 2
                vals.append(recurse(g2, s+1, gl2, kl2, x, y+1, 2, kc))
            else:
                vals.append(float("inf"))
        elif ord(t) >= 97 and ord(t) <=122:
            kl2.append(t)
            g2[y][x] = 2
            g2[y+1][x] = 2
            vals.append(recurse(g2, s+1, gl2, kl2, x, y+1, 2, kc))
            g2[y][x] = 4
            g2[y+1][x] = 4
            vals.append(recurse(g2, s+2, gl2, kl2, x, y, 4, kc))
    else:
        vals.append(float("inf"))


    return min(vals)


def main():

    my_map = []
    with open("smallinput.txt") as fp:
        line = fp.readline()
        while line:
            row = [i for i in line.rstrip()]
            my_map.append(row)
            line = fp.readline()

    print_graph(my_map, 0, 0, 1)

    x = 0
    y = 0

    gate_list = []
    key_count = 0
    for i in range(len(my_map)):
        for j in range(len(my_map[i])):
            if ord(my_map[i][j]) >= 65 and ord(my_map[i][j]) <= 90:
                gate_list.append(my_map[i][j])
            if ord(my_map[i][j]) >= 97 and ord(my_map[i][j]) <= 122:
                key_count += 1
            if my_map[i][j] == '@':
                y = i
                print "Y: " + str(i)
                x = j
                print "X: " + str(j)

    step = 0
    key_list = []
    direction = 0
    print recurse(my_map, step, gate_list, key_list, x, y, direction, key_count)

main()
