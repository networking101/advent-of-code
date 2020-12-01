import itertools
import os
import time
import sys

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

def main():

    with open('input.txt') as fp:
        line = fp.readline()
        mylist = line.split(',')
        orig_list = [int(i) for i in mylist]

    input_signal = 2
    ip = 0
    rb = 0
    opcode = 0

    while ip != -1:
        input_signal,orig_list,ip,rb = computer([input_signal], orig_list, ip, rb)
        print input_signal



main()


