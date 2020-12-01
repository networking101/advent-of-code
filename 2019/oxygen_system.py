import itertools
import os
import sys
import time
import copy

def expand_read(tl, params, i, rb):
    trigger = 0
    while trigger == 0:
        try:
            params[i] = tl[rb + params[i]]
            trigger = 1
        except:
            tl.append(0)

    return params[i]

def expand_write(tl, param, sol):
    trigger = 0
    while trigger == 0:
        try:
            tl[param] = sol
            trigger = 1
        except:
            tl.append(0)

def addition(tl, inst, rb):
    params = inst[1:]
    opcode = int(inst[0]/100)
    for i in range(2):
        if opcode%10 == 0:
            params[i] = expand_read(tl, params, i, 0)
        if opcode%10 == 2:
            params[i] = expand_read(tl, params, i, rb)
        opcode = int(opcode/10)
    sol = params[0] + params[1]

    if opcode%10 == 0:
        expand_write(tl, params[2], sol)
    if opcode%10 == 2:
        expand_write(tl, rb + params[2], sol)

def multiplication(tl, inst, rb):
    params = inst[1:]
    opcode = int(inst[0]/100)
    for i in range(2):
        if opcode%10 == 0:
            params[i] = expand_read(tl, params, i, 0)
        if opcode%10 == 2:
            params[i] = expand_read(tl, params, i, rb)
        opcode = int(opcode/10)

    sol = params[0] * params[1]

    if opcode %10 == 0:
        expand_write(tl, params[2], sol)
    if opcode%10 == 2:
        expand_write(tl, rb + params[2], sol)

def writing(tl, inst, rb, iparam):
    params = inst[1:]
    opcode = int(inst[0]/100)
    if opcode%10 == 0:
        expand_write(tl, params[0], iparam)
    if opcode%10 == 2:
        expand_write(tl, rb + params[0], iparam)

def reading(tl, inst, rb):
    params = inst[1:]
    opcode = int(inst[0]/100)
    if opcode%10 == 0:
        return tl[params[0]]
    if opcode%10 == 1:
        return params[0]
    if opcode%10 == 2:
        return tl[rb + params[0]]

def jift(tl, inst, ip, rb):
    params = inst[1:]
    opcode = int(inst[0]/100)
    for i in range(2):
        if opcode%10 == 0:
            params[i] = tl[params[i]]
        if opcode%10 == 2:
            params[i] = tl[rb + params[i]]
        opcode = int(opcode/10)

    if params[0] == 0:
        return ip + 3
    return params[1]

def jiff(tl, inst, ip, rb):
    params = inst[1:]
    opcode = int(inst[0]/100)
    for i in range(2):
        if opcode%10 == 0:
            params[i] = tl[params[i]]
        if opcode%10 == 2:
            params[i] = tl[rb + params[i]]
        opcode = int(opcode/10)

    if params[0] == 0:
        return params[1]
    return ip + 3

def lessthan(tl, inst, rb):
    params = inst[1:]
    opcode = int(inst[0]/100)
    for i in range(2):
        if opcode%10 == 0:
            params[i] = expand_read(tl, params, i, 0)
        if opcode%10 == 2:
            params[i] = expand_read(tl, params, i, rb)
        opcode = int(opcode/10)

    if params[0] < params[1]:
        sol = 1
    else:
        sol = 0

    if opcode%10 == 0:
        expand_write(tl, params[2], sol)
    if opcode%10 == 2:
        expand_write(tl, rb + params[2], sol)

def equals(tl, inst, rb):
    params = inst[1:]
    opcode = int(inst[0]/100)
    for i in range(2):
        if opcode%10 == 0:
            params[i] = expand_read(tl, params, i, 0)
        if opcode%10 == 2:
            params[i] = expand_read(tl, params, i, rb)
        opcode = int(opcode/10)
    
    if params[0] == params[1]:
        sol = 1
    else:
        sol = 0

    if opcode%10 == 0:
        expand_write(tl, params[2], sol)
    if opcode%10 == 2:
        expand_write(tl, rb + params[2], sol)

def relative_base(tl, inst, rb):
    params = inst[1:]
    opcode = int(inst[0]/100)
    if opcode%10 == 0:
        return rb + tl[params[0]]
    if opcode%10 == 1:
        return rb + params[0]
    if opcode%10 == 2:
        return rb + tl[rb + params[0]]

def computer(input_sigs, orig_list, ip, rb):

    int_param = input_sigs[0]

    while ip <= len(orig_list):
        #print "IP:" + str(ip)
        #print orig_list[ip:ip+4]
        #print "RB: " + str(rb)
        if orig_list[ip]%100 == 1:
            #print "DEBUG ADD"
            addition(orig_list, orig_list[ip:ip+4], rb)
            ip += 4

        elif orig_list[ip]%100 == 2:
            #print "DEBUG MULT"
            multiplication(orig_list, orig_list[ip:ip+4], rb)
            ip += 4

        elif orig_list[ip]%100 == 3:
            try:
                int_param = input_sigs.pop(0)
            except:
                print "Could not pop"
                exit()
            writing(orig_list, orig_list[ip:ip+2], rb, int_param)
            ip += 2

        elif orig_list[ip]%100 == 4:
            #print "DEBUG READ"
            int_param = reading(orig_list, orig_list[ip:ip+2], rb)
            ip += 2
            return int_param, orig_list, ip, rb

        elif orig_list[ip]%100 == 5:
            #print "DEBUG TRUE"
            ip = jift(orig_list, orig_list[ip:ip+3], ip, rb)

        elif orig_list[ip]%100 == 6:
            #print "DEBUG FALSE"
            ip = jiff(orig_list, orig_list[ip:ip+3], ip, rb)

        elif orig_list[ip]%100 == 7:
            #print "DEBUG LESSTHAN"
            lessthan(orig_list, orig_list[ip:ip+4], rb)
            ip += 4

        elif orig_list[ip]%100 == 8:
            #print "DEBUG EQUALS"
            equals(orig_list, orig_list[ip:ip+4], rb)
            ip += 4

        elif orig_list[ip]%100 == 9:
            #print "DEBUG RELATIVE POINTER"
            rb = relative_base(orig_list, orig_list[ip:ip+2], rb)
            ip += 2

        elif orig_list[ip]%100 == 99:
            print "COMPLETE"
            return int_param, orig_list, -1, rb

        else:
            print "Failed, Did not match opcode!"
            exit()
    
    return

def print_grid(grid, size, x, y, direction):
    sys.stdout.write("  ")
    for i in range(size):
        sys.stdout.write(str(int(i/10)))
    print ""
    sys.stdout.write("  ")
    for i in range(size):
        sys.stdout.write(str(i%10))
    print ""
    for i in range(size):
        print("%02d"%i),
        for j in range(size):
            if i == y and j == x:
                if direction == 1:
                    sys.stdout.write('^')
                if direction == 4:
                    sys.stdout.write('>')
                if direction == 2:
                    sys.stdout.write('v')
                if direction == 3:
                    sys.stdout.write('<')
            elif i == int(size/2) and j == int(size/2):
                sys.stdout.write('+')
            else:
                sys.stdout.write(grid[j][i])
        print ""

    print "\n"


def recurse(steps, grid, xo, yo, size):
    #print_grid(grid, size, 0, 0, 0)
    if grid[xo][yo] == 'X':
        return steps+1
    grid[xo][yo] = '*'
    mylist = []
    if grid[xo-1][yo] == ' ' or grid[xo-1][yo] == 'X':
        mylist.append(recurse(steps+1, grid, xo-1, yo, size))
    if grid[xo+1][yo] == ' ' or grid[xo+1][yo] == 'X':
        mylist.append(recurse(steps+1, grid, xo+1, yo, size))
    if grid[xo][yo-1] == ' ' or grid[xo][yo-1] == 'X':
        mylist.append(recurse(steps+1, grid, xo, yo-1, size))
    if grid[xo][yo+1] == ' ' or grid[xo][yo+1] == 'X':
        mylist.append(recurse(steps+1, grid, xo, yo+1, size))

    try:
        return min(mylist)
    except:
        return float("inf")

def bfs(steps, grid, xo, yo, size):
    queue = [[xo,yo,steps]]
    maxim = 0
    while queue:
        #print_grid(grid,size, 0, 0, 0)
        cur = queue.pop(0)
        xo = cur[0]
        yo = cur[1]
        step = cur[2]
        if step > maxim:
            maxim = step
        grid[xo][yo] = '*'
        if grid[xo-1][yo] == ' ' or grid[xo-1][yo] == 'X':
            queue.append([xo-1,yo,step+1])
        if grid[xo+1][yo] == ' ' or grid[xo+1][yo] == 'X':
            queue.append([xo+1,yo,step+1])
        if grid[xo][yo-1] == ' ' or grid[xo][yo-1] == 'X':
            queue.append([xo,yo-1,step+1])
        if grid[xo][yo+1] == ' ' or grid[xo][yo+1] == 'X':
            queue.append([xo,yo+1,step+1])
        
    return maxim+1
        

def main():

    size = 46

    with open('input.txt') as fp:
        line = fp.readline()
        mylist = line.split(',')
        orig_list = [int(i) for i in mylist]

    insig = 0
    ip = 0
    rb = 0

    grid = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(".")
        grid.append(row)

    x = size/2
    y = size/2
    direction = 1

    xx = 0
    yy = 0
    xo = x
    yo = y
    #while True:
    for i in range(3200):
        #print_grid(grid, size, x, y, direction)
        #time.sleep(.2)
        insig = direction
        outsig, orig_list, ip, rb = computer([insig], orig_list, ip, rb)
        if outsig == 0:
            if direction == 1:
                grid[x][y-1] = '0'
                direction = 4
            elif direction == 4:
                grid[x+1][y] = '0'
                direction = 2
            elif direction == 2:
                grid[x][y+1] = '0'
                direction = 3
            elif direction == 3:
                grid[x-1][y] = '0'
                direction = 1
        elif outsig == 1 or outsig == 2:
            if outsig == 1:
                if x != xx or y != yy:
                    grid[x][y] = ' '
            if outsig == 2:
                grid[x][y] = 'X'
                xx = x
                yy = y
            if direction == 1:
                y -= 1
                direction = 3
            elif direction == 4:
                x += 1
                direction = 1
            elif direction == 2:
                y += 1
                direction = 4
            elif direction == 3:
                x -= 1
                direction = 2

    print_grid(grid, size, 0, 0, direction)

    print recurse(0, copy.deepcopy(grid), xo, yo, size)

    print bfs(0, copy.deepcopy(grid), xx, yy, size)


main()
