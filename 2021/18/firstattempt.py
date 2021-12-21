from copy import deepcopy

with open("input", "r") as fp:
    lines = [line.strip() for line in fp]


def addition(currLine, nextLine):
    currLine = '[' + currLine + ',' + nextLine + ']'
    return currLine


def explode(currLine, pos):
    # search left
    tpos = pos-1
    innerLeftNumber = -1
    leftNumber = -1
    leftBracket = -1
    if currLine[tpos] == ',' and currLine[tpos-1].isnumeric():
        innerLeftNumber = int(currLine[tpos-1])
    while tpos >=0:
        tmp = currLine[tpos]
        if tmp == '[' and leftBracket == -1:
            leftBracket = tpos
        if tmp.isnumeric():
            leftNumber = tpos
        if leftNumber != -1 and leftBracket != -1:
            break
        tpos -= 1

    # search right
    foundLeftBracket = False
    tpos = pos +1
    innerRightNumber = -1
    rightNumber = -1
    rightBracket = -1
    while currLine[tpos] != ']':
        tpos += 1
    tpos += 1
    if currLine[tpos] == ',' and currLine[tpos+1].isnumeric():
        innerRightNumber = int(currLine[tpos+1])
    while tpos < len(currLine):
        tmp = currLine[tpos]
        if tmp == '[' and rightBracket == -1:
            foundLeftBracket = True
            rightNumber = tpos + 1
            break
        if tmp == ']' and rightBracket == -1:
            rightBracket = tpos
        if tmp.isnumeric():
            rightNumber = tpos
        if rightNumber != -1 and rightBracket != -1:
            break
        tpos += 1


    newlineleft = currLine[:leftBracket+1]
    if leftNumber != -1 and leftNumber < leftBracket:
        newNum = str(int(newlineleft[leftNumber]) + int(currLine[pos+1]))
        newlineleft = newlineleft[:leftNumber] + newNum + newlineleft[leftNumber+1:]

    newline = newlineleft
    if innerLeftNumber == -1:
        newline += "0"
    else:
        newline += str(innerLeftNumber + int(currLine[pos+1]))
    newline += ','

    if foundLeftBracket:
        newlineright = "[" + str(int(currLine[pos+3]) + int(currLine[rightNumber]))
        newlineright += currLine[rightNumber+1:]
        return newline + newlineright
    else:
        newlineright = currLine[rightBracket:]
        if rightNumber != -1 and rightNumber > rightBracket:
            newNum = str(int(newlineright[rightNumber-rightBracket]) + int(currLine[pos+3]))
            newlineright = newlineright[:rightNumber-rightBracket] + newNum + newlineright[rightNumber-rightBracket + 1:]
        if innerRightNumber == -1:
            newline += "0"
        else:
            newline += str(innerRightNumber + int(currLine[pos+3]))
    newline += newlineright

    return newline


def split(currLine, pos):
    newLine = currLine[:pos] + '['
    number = int(currLine[pos: pos+2])
    newLine += str(number//2) + ',' + str(number - (number//2))
    newLine += ']' + currLine[pos+2:]
    return newLine

# test
#test = "[[[[0,[3,2]],[3,3]],[4,4]],[5,5]]"
#test = "[[[[[1,1],[2,2]],[3,3]],[4,4]],[5,5]]"
#result = explode(test, 4)
#test = "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"
#result = explode(test, 24)

# Silver
result = 0
currLine = lines.pop(0)
while lines:
    currLine = addition(currLine, lines.pop(0))
    countBrackets = 0
    pos = 0
    while pos < len(currLine):
        if currLine[pos] == '[':
            countBrackets += 1
            if countBrackets == 5:
                nextPos = pos - 1
                oldCurrLine = deepcopy(currLine)
                currLine = explode(currLine, pos)
                countBrackets = 0
                pos = 0
                continue
        if currLine[pos] == ']':
            countBrackets -= 1
        if currLine[pos].isnumeric() and currLine[pos+1].isnumeric():
            nextPos = pos - 1
            currLine = split(currLine, pos)
            countBrackets = 0
            pos = 0
            continue
        pos += 1

print(currLine)
exit(0)

left = 0
while not currLine[left].isnumeric():
    left += 1

right = len(currLine)-1
while not currLine[right].isnumeric():
    right -= 1

magnitude = int(currLine[left]) * 3 + int(currLine[right]) * 2
print(magnitude)