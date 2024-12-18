from copy import deepcopy

with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

A = 0
B = 0
C = 0
instructions = []

for line in lines:
    if line[:len("Register A")] == "Register A":
        A = int(line.split(": ")[1])
    if line[:len("Register B")] == "Register B":
        B = int(line.split(": ")[1])
    if line[:len("Register C")] == "Register C":
        C = int(line.split(": ")[1])
    if line[:len("Program")] == "Program":
        instructions = [int(x) for x in line.split(": ")[1].split(",")]

def get_combo(x, a, b, c):
    assert(0 <= x <= 6)
    if x <= 3:
        return x
    if x == 4:
        return a
    if x == 5:
        return b
    if x == 6:
        return c

def program(a, b, c, instructions):
    output = []
    PC = 0
    while PC < len(instructions):
        instruction = instructions[PC]
        operand = instructions[PC + 1]

        # adv (division)
        if instruction == 0:
            a = int(a / (2**get_combo(operand, a, b, c)))
            PC += 2

        # bxl (bitwise xor)
        if instruction == 1:
            b = b ^ operand
            PC += 2

        # bst (modulo)
        if instruction == 2:
            b = get_combo(operand, a, b, c) % 8
            PC += 2

        # jnz (jump)
        if instruction == 3:
            PC += 2
            if a != 0:
                PC = operand

        # bxc (bitwise xor)
        if instruction == 4:
            b = b ^ c
            PC += 2

        # out (print)
        if instruction == 5:
            output.append(get_combo(operand, a, b, c) % 8)
            PC += 2

        # bdv (division)
        if instruction == 6:
            b = int(a / (2**get_combo(operand, a, b, c)))
            PC += 2

        # cdv (division)
        if instruction == 7:
            c = int(a / (2**get_combo(operand, a, b, c)))
            PC += 2

    return ",".join([str(x) for x in output])

print(program(A, B, C, instructions))

golds = []
def recurse(num, instruct):
    if len(instruct) == 0:
        golds.append(num)
        return

    curr = instruct.pop()
    # 2,4,1,5,7,5,1,6,4,2,5,5,0,3,3,0
    for i in range(8):
        aa = (num << 3) + i
        bb = aa % 8
        bb = bb ^ 5
        cc = aa >> bb
        bb = bb ^ 6
        bb = bb ^ cc
        bb = bb % 8

        if bb == curr:
            recurse(aa, deepcopy(instruct))

for i in range(2**7):
    recurse(i, deepcopy(instructions))

print(min(golds))