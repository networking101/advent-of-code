with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

silver = 0
for line in lines:
    max_val = 0
    for i, x in enumerate(line):
        for j in range(i + 1, len(line)):
            if int(x + line[j]) > max_val:
                max_val = int(x + line[j])
    silver += max_val

print(silver)

gold = 0
for line in lines:
    line = line + "A"
    max_val = ""
    tmp_max_index = 0
    for j in range(12):
        tmp_max = 0
        saved_i = 0
        for i, x in enumerate(line[tmp_max_index:j - 12]):
            if int(max_val + x) > tmp_max:
                print(int(max_val + x), tmp_max, i)
                tmp_max = int(max_val + x)
                saved_i = i
        tmp_max_index = tmp_max_index + saved_i + 1
        
        max_val = str(tmp_max)

    gold += int(max_val)

print(gold)