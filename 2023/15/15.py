with open("input", "r") as fp:
    lines = [line.strip() for line in fp][0]

line = lines.split(',')

def hash_func(string):
    h = 0
    for c in string:
        h = ((ord(c) + h) * 17) % 256
    return h

boxes = [[] for _ in range(256)]

count1 = 0
count2 = 0
for l in line:
    h = hash_func(l)
    count1 += h

    for i, c in enumerate(l):
        if c == '=' or c == '-':
            label = l[:i]
            op = c
            fl = l[i+1:]
    h = hash_func(label)
    changed = False
    curr_box = boxes[h]
    for i, lens in enumerate(curr_box):
        if label == lens[0]:
            if op == '=':
                curr_box[i] = [label, fl]
                changed = True
            if op == '-':
                curr_box.pop(i)
            break
    if not changed and op == '=':
        curr_box.append([label, fl])
    
for i, box in enumerate(boxes):
    for j, lens in enumerate(box):
        tmp = (i+1) * (j+1) * int(lens[1])
        count2 += tmp

print(count1)
print(count2)