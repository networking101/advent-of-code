with open("input.txt", "r") as fp:
    lines = [line.strip() for line in fp]


def check(vals):
    for i in vals:
        t = vals[i]
        if i == "byr":
            if int(t) < 1920 or int(t) > 2002 or len(t) != 4:
                return False
        if i == "iyr":
            if int(t) < 2010 or int(t) > 2020 or len(t) != 4:
                return False
        if i  == "eyr":
            if int(t) < 2020 or int(t) > 2030 or len(t) != 4:
                return False
        if i == "hgt":
            if t[-2:] == "cm":
                if int(t[:-2]) < 150 or int(t[:-2]) > 193:
                    return False
            if t[-2:] == "in":
                if int(t[:-2]) < 59 or int(t[:-2]) > 76:
                    return False
        if i == "hcl":
            try:
                if t[0] != '#':
                    return False
            except:
                return False
            if len(t) != 7:
                return False
            try:
                int(t[1:], 16)
            except:
                return False
        if i == "ecl":
            a = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            if t not in a:
                return False
        if i == "pid":
            try:
                int(t)
                if len(t) != 9 :
                    return False
            except:
                return False

    return True



found = 0
vals = {}
for line in lines:

    if line == "":
        ch = False
        if len(vals) == 8:
            ch = True
        elif len(vals) == 7 and "cid" not in vals:
            ch = True
        """ Part of part 1 (I'm not cleaning this up)
        print(found)
        print(vals)
        print("")
        vals = {}    
        """
        if not ch:
            vals = {}
            continue
        res = check(vals)
        if res:
            found += 1
        vals = {}

        continue

    a = line.split()
    for z in a:
        b, c = z.split(":")
        vals[b] = c

print("Answer:  " + str(found))
