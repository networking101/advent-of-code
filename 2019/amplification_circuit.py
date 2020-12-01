import itertools
import os

def addition(tl, inst):
    params = inst[1:]
    opcode = int(inst[0]/100)
    for i in range(3):
        if opcode%10 == 0:
            params[i] = tl[params[i]]
        opcode = int(opcode/10)
    return params[0] + params[1]

def multiplication(tl, inst):
    params = inst[1:]
    opcode = int(inst[0]/100)
    for i in range(3):
        if opcode%10 == 0:
            params[i] = tl[params[i]]
        opcode = int(opcode/10)

    return params[0] * params[1]

def reading(tl, inst):
    params = inst[1:]
    opcode = int(inst[0]/100)
    if opcode%10 == 0:
        params[0] = tl[params[0]]

    return params[0]

def jift(tl, inst, ip):
    params = inst[1:]
    opcode = int(inst[0]/100)
    for i in range(2):
        if opcode%10 == 0:
            params[i] = tl[params[i]]
        opcode = int(opcode/10)

    if params[0] == 0:
        return ip + 3
    return params[1]

def jiff(tl, inst, ip):
    params = inst[1:]
    opcode = int(inst[0]/100)
    for i in range(2):
        if opcode%10 == 0:
            params[i] = tl[params[i]]
        opcode = int(opcode/10)

    if params[0] == 0:
        return params[1]
    return ip + 3

def lessthan(tl, inst):
    params = inst[1:]
    opcode = int(inst[0]/100)
    for i in range(3):
        if opcode %10 == 0:
            params[i] = tl[params[i]]
        opcode = int(opcode/10)

    if params[0] < params[1]:
        return 1
    return 0

def equals(tl, inst):
    params = inst[1:]
    opcode = int(inst[0]/100)
    for i in range(3):
        if opcode%10 == 0:
            params[i] = tl[params[i]]
        opcode = int(opcode/10)
    
    if params[0] == params[1]:
        return 1
    return 0

def computer(input_sigs, orig_list, ip):

    int_param = input_sigs[0]

    while ip <= len(orig_list):
        if orig_list[ip]%100 == 1:
            orig_list[orig_list[ip+3]] = addition(orig_list, orig_list[ip:ip+4])
            ip += 4

        elif orig_list[ip]%100 == 2:
            orig_list[orig_list[ip+3]] = multiplication(orig_list, orig_list[ip:ip+4])
            ip += 4

        elif orig_list[ip]%100 == 3:
            try:
                int_param = input_sigs.pop(0)
            except:
                print "Could not pop"
                exit()
            orig_list[orig_list[ip+1]] = int_param
            ip += 2

        elif orig_list[ip]%100 == 4:
            int_param = reading(orig_list, orig_list[ip:ip+2])
            ip += 2
            return int_param,orig_list,ip

        elif orig_list[ip]%100 == 5:
            ip = jift(orig_list, orig_list[ip:ip+3], ip)

        elif orig_list[ip]%100 == 6:
            ip = jiff(orig_list, orig_list[ip:ip+3], ip)

        elif orig_list[ip]%100 == 7:
            orig_list[orig_list[ip+3]] = lessthan(orig_list, orig_list[ip:ip+4])
            ip += 4

        elif orig_list[ip]%100 == 8:
            orig_list[orig_list[ip+3]] = equals(orig_list, orig_list[ip:ip+4])
            ip += 4

        elif orig_list[ip]%100 == 99:
            return int_param, orig_list, -1

        else:
            print "Failed, Did not match opcode!"
            exit()
    
    return

def main():
    phases = list(itertools.permutations([5,6,7,8,9], 5))

    with open('input.txt') as fp:
        line = fp.readline()
        mylist = line.split(',')
        orig_list = [int(i) for i in mylist]

    maxes = []

    for phase in phases:
        ip = []
        lists = []
        for i in range(5):
            ip.append(0)
            new_list = list(orig_list)
            lists.append(new_list)

        input_signal = 0

        for j in range(5):
            input_signal,lists[j],ip[j] = computer([phase[j], input_signal], lists[j], ip[j])

        while ip[4] >=0:
            for i in range(5):
                input_signal,lists[i],ip[i] = computer([input_signal], lists[i], ip[i])

        maxes.append(input_signal)

    print max(maxes)



main()


