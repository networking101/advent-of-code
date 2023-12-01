with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

count = 0

for line in lines:
    found = []
    for c in line:
        if c.isnumeric():
            found.append(c)

    count += int(found[0] + found[-1])

print(count)

numbers = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
count = 0

for line in lines:
    found = []
    start = 0
    for i, c in enumerate(line):
        if c.isnumeric():
            found.append(c)
            start = i
            continue
        for k, v in numbers.items():
            if k in line[start:i+1]:
                start = i
                found.append(v)

    count += int(found[0] + found[-1])

print(count)