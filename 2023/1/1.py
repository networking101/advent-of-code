with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

count = 0

for l in lines:
    a = 0
    b = 0
    for i in l:
        if i.isnumeric():
            a = i
            break
    for i in l[::-1]:
        if i.isnumeric():
            b = i
            break

    count += int(a+b)

print(count)

numbers = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

count = 0

for l in lines:
    found = []
    last = 0
    for i, x in enumerate(l):
        if x.isnumeric():
            found.append(x)
            last = i
            continue
        for n in numbers:
            if n in l[last:i+1]:
                last = i
                found.append(numbers[n])

    print(found)
    if len(found) >= 2:
        count += int(found[0] + found[-1])
    elif len(found) == 1:
        count += int(found[0] + found[0])

print(count)