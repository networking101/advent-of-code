with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

tot = 0
for line in lines:
    curr_line = list(line)
    val = 0
    index = 1
    while curr_line:
        digit = curr_line.pop()
        if digit.isnumeric():
            val += index * int(digit)
        if digit == '-':
            val -= index
        if digit == '=':
            val -= index * 2

        index *= 5
    tot += val

check = 1
index = 0
ret_val = ''
while True:
    if tot < check * 3:
        break
    check *= 5
    index += 1

tmp = tot - 5**index

if tmp > int((5**index)/2):
    ret_val += '2'
    tot -= (2 * int(5**(index)))
else:
    ret_val += '1'
    tot -= int(5**(index))
index -= 1

while tot != 0:
    tmp = int(5**(index+1) / 2) * -1
    if tot < tmp + 5**index:
        ret_val += '='
        tot += 2 * 5**index
    elif tot < tmp + (2 * 5**index):
        ret_val += '-'
        tot += 5**(index)
    elif tot < tmp + (3 * 5**index):
        ret_val += '0'
    elif tot < tmp + (4 * 5**index):
        ret_val += '1'
        tot -= 5**index
    else:
        ret_val += '2'
        tot -= 2 * 5**index
    index -= 1

if tot == 2:
    ret_val += '2'
if tot == 1:
    ret_val += '1'
if tot == 0:
    ret_val += '0'
if tot == -1:
    ret_val += '-'
if tot == -2:
    ret_val += '='
print(ret_val)