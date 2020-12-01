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

    print "Params[0]: " + str(params[0])
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

def main():

    int_param = 5

    with open('input.txt') as fp:
        line = fp.readline()
        mylist = line.split(',')
        orig_list = [int(i) for i in mylist]

    print orig_list

    for i in range(len(orig_list)):
        if orig_list[i] == 99:
            print("I: " + str(i) + "     orig_list[i]: " + str(orig_list[i]))


    ip = 0
    while ip <= len(orig_list):
        print "\n"
        print "IP: " + str(ip)
        if orig_list[ip]%100 == 1:
            print "ADD"
            orig_list[orig_list[ip+3]] = addition(orig_list, orig_list[ip:ip+4])
            ip += 4

        elif orig_list[ip]%100 == 2:
            print "MULT"
            orig_list[orig_list[ip+3]] = multiplication(orig_list, orig_list[ip:ip+4])
            ip += 4

        elif orig_list[ip]%100 == 3:
            print "WRITE"
            orig_list[orig_list[ip+1]] = int_param
            ip += 2

        elif orig_list[ip]%100 == 4:
            print "READ"
            int_param = reading(orig_list, orig_list[ip:ip+2])
            ip += 2

        elif orig_list[ip]%100 == 5:
            print "JUMP-IF-TRUE"
            ip = jift(orig_list, orig_list[ip:ip+3], ip)

        elif orig_list[ip]%100 == 6:
            print "JUMP-IF-FALSE"
            ip = jiff(orig_list, orig_list[ip:ip+3], ip)

        elif orig_list[ip]%100 == 7:
            print "LESS-THAN"
            orig_list[orig_list[ip+3]] = lessthan(orig_list, orig_list[ip:ip+4])
            ip += 4

        elif orig_list[ip]%100 == 8:
            print "EQUALS"
            orig_list[orig_list[ip+3]] = equals(orig_list, orig_list[ip:ip+4])
            ip += 4

        elif orig_list[ip]%100 == 99:
            print "Complete!: " + str(int_param)
            return

        else:
            print "Failed, Did not match opcode!"
            exit()

main()

