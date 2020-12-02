pinput = "cqjxxyzz"


def nextString(string):
    index = len(string) - 1
    while True:
        if string[index] != "z":
            string = string[:index] + chr(ord(string[index]) + 1) + string[index+1:]
            return string
        string = string[:index] + "a" + string[index+1:]
        index -= 1
        

while True:
    pinput = nextString(pinput)
    # first check
    first = False
    for i in range(2,len(pinput)):
        a = ord(pinput[i-2])
        b = ord(pinput[i-1])
        c = ord(pinput[i])
        if b == a+1 and c == b+1:
            first = True
            break
    if not first:
        continue

    #second check
    second = True
    for i in pinput:
        if i == "i" or i == "o" or i == "l":
            second = False
            break
    if not second:
        continue

    #third check
    first_pair = "A"
    third = 0
    for i in range(1, len(pinput)):
        if pinput[i-1] == pinput[i]:
            if first_pair != pinput[i]:
                third += 1
                first_pair = pinput[i]
            if third == 2:
                break
    if third < 2:
        continue
    print(pinput)
    exit(0)


