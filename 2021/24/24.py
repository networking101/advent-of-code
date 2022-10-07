with open("input", "r") as fp:
    instructions = [line.strip() for line in fp]

def solve(modelNumber, instructions):
    v = {
        'w':0,
        'x':0,
        'y':0,
        'z':0
    }

    for i in instructions:
        # inp
        if i[:3] == "inp":
            v[i[4]] = int(modelNumber[0])
            modelNumber = modelNumber[1:]

        # add
        if i[:3] == "add":
            if i[6:].lstrip("-").isdigit():
                v[i[4]] = v[i[4]] + int(i[6:])
            else:
                v[i[4]] = v[i[4]] + v[i[6]]

        # mul
        if i[:3] == "mul":
            if i[6:].lstrip("-").isdigit():
                v[i[4]] = v[i[4]] * int(i[6:])
            else:
                v[i[4]] = v[i[4]] * v[i[6]]

        # div
        if i[:3] == "div":
            try:
                if i[6:].lstrip("-").isdigit():
                    v[i[4]] = v[i[4]] // int(i[6:])
                else:
                    v[i[4]] = v[i[4]] // v[i[6]]
            except:
                return False

        # mod
        if i[:3] == "mod":
            try:
                if i[6:].lstrip("-").isdigit():
                    v[i[4]] = v[i[4]] % int(i[6:])
                else:
                    v[i[4]] = v[i[4]] % v[i[6]]
            except:
                return False

        # eql
        if i[:3] == "eql":
            if i[6:].lstrip("-").isdigit():
                if v[i[4]] == int(i[6:]):
                    v[i[4]] = 1
                else:
                    v[i[4]] = 0
            else:
                if v[i[4]] == v[i[6]]:
                    v[i[4]] = 1
                else:
                    v[i[4]] = 0
    
    if v['z'] == 0:
        return True
    return False


solve(str(92967699949891), instructions)