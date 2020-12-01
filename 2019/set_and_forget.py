import itertools
import os
import time
import sys
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
            #print "DEBUG WRITE"
            try:
                int_param = input_sigs.pop(0)
            except:
                print "Could not pop"
                exit()
            writes = writing(orig_list, orig_list[ip:ip+2], rb, int_param)
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
            print "DEBUG COMPLETE"
            return int_param, orig_list, -1, rb

        else:
            print "Failed, Did not match opcode!"
            exit()
    
    return

def print_grid(grid, y, x):
    sys.stdout.write("  ")
    for i in range(len(grid[0])):
        sys.stdout.write(str((i)/10))
    sys.stdout.write("\n  ")
    for i in range(len(grid[0])):
        sys.stdout.write(str((i)%10))
    print ""
    for i in range(len(grid)):
        print("%02d"%(i)),
        for j in range(len(grid[i])):
            if i == y and j == x:
                sys.stdout.write('X')
            else:
                sys.stdout.write(grid[i][j])
        print ""

def gen_map(grid, input_signal, orig_list, ip, rb):
    x = 0
    y = 0
    count = 0
    row = []
    insig, orig_list, ip, rb = computer([input_signal], orig_list, ip, rb)
    while ip != -1:
        #print "INSIG: " + str(insig)
        if count == 1 and insig == 10:
            print "RETURN"
            return insig, orig_list, ip, rb
        count = 0
        if insig == 46:
            row.append('.')
            x += 1
        elif insig == 35:
            row.append('#')
            x += 1
        elif insig == 10:
            count += 1
            grid.append(row)
            row = []
            x = 0
            y += 1
        elif insig == 94:
            row.append('^')
            x += 1
        elif insig == 60:
            row.append('<')
            x += 1
        elif insig == 118:
            row.append('v')
            x += 1
        elif insig == 62:
            row.append('>')
            x += 1
        elif insig == 58:
            print "DEBUG :\n\n\n"
            insig = [65,44,65,44,66,10]
        else:
            try:
                print "Unknown: " + str(chr(insig)) + " " + str(insig)
                return
            except:
                print "TOO BIG: " + str(insig)
            
        insig, orig_list, ip, rb = computer([insig], orig_list, ip, rb)

def main():

    with open('input.txt') as fp:
        line = fp.readline()
        mylist = line.split(',')
        orig_list = [int(i) for i in mylist]

    ol = copy.deepcopy(orig_list)
    ol[0] = 2
    input_signal = 0
    ip = 0
    rb = 0

    #     A  ,  B  ,  A  ,  B  ,  A  ,  C  ,  B  ,  C  ,  A  ,  C  \n
    mr = [65,44,66,44,65,44,66,44,65,44,67,44,66,44,67,44,65,44,67,10]
    #     L  ,  6  ,  R  ,  1  2  ,  L  ,  6  \n
    fa = [76,44,54,44,82,44,49,50,44,76,44,54,10]
    #     R  ,  1  2  ,  L  ,  1  0  ,  L  ,  4  ,  L  ,  6  \n
    fb = [82,44,49,50,44,76,44,49,48,44,76,44,52,44,76,44,54,10]
    #     L  ,  1  0  ,  L  ,  1  0  ,  L  ,  4  ,  L  ,  6  \n
    fc = [76,44,49,48,44,76,44,49,48,44,76,44,52,44,76,44,54,10]

    grid = []
    insig, ol, ip, rb = gen_map(grid, input_signal, ol, ip, rb)
    print_grid(grid, 0, 0)

    templ = []

    while ip != -1:
        insig, ol, ip, rb = computer([insig], ol, ip, rb)
        templ.append(chr(insig))
        print "INSIG: " + str(chr(insig)) + "   " + str(insig)

        if insig == 10:
            print templ
            if templ == list("Main:\n"):
                print "DEBUG MAIN"
                insig, ol, ip, rb = computer(mr, ol, ip, rb)
            if templ == list("Function A:\n"):
                print "DEBUG FUNA"
                insig, ol, ip, rb = computer(fa, ol, ip, rb)
            if templ == list("Function B:\n"):
                print "DEBUG FUNB"
                insig, ol, ip, rb = computer(fb, ol, ip, rb)
            if templ == list("Function C:\n"):
                print "DEBUG FUNC"
                insig, ol, ip, rb = computer(fc, ol, ip, rb)
            if templ == list("Continuous video feed?\n"):
                print "DEBUG VIDEO"
                insig, ol, ip, rb = computer([121,10], ol, ip, rb)
                print insig
                while True:
                    grid = []
                    insig, ol, ip, rb = gen_map(grid, insig, ol, ip, rb)
                    print_grid(grid, 0, 0)
                    time.sleep(.2)
                return
            templ = []
            print "INSIG: " + str(chr(insig)) + "   " + str(insig)
            templ.append(chr(insig))


main()


























