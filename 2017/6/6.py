with open("input", "r") as fp:
    line = [[int(x) for x in line.strip().split()] for line in fp][0]

saved = [str(line)]

gold_check = ""
count = 0
while True:
    # find max
    max_index = 0
    for i, x in enumerate(line):
        if x > line[max_index]:
            max_index = i

    # redistribute
    max_val = line[max_index]
    line[max_index] = 0
    for i in range(0, max_val):
        line[(i + 1 + max_index) % len(line)] += 1

    if len(gold_check) and str(line) == gold_check:
        print(count)
        break

    if len(gold_check) == 0:
        if str(line) in saved:
            print(len(saved))
            gold_check = str(line)
            count = 0
        saved.append(str(line))

    count += 1
