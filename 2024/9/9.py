from copy import deepcopy

with open("input", "r") as fp:
    line = [line.strip() for line in fp][0]

disk = []

flag = 1
index = 0
for c in line:
    if flag:
        disk += [str(index)] * int(c)
        index += 1
    else:
        disk += ["."] * int(c)
    flag = (flag + 1) % 2

orig_disk = deepcopy(disk)

start = 0
end = len(disk) - 1
while start < end:
    if disk[start] == '.':
        while disk[end] == '.':
            end -= 1

        disk[start] = disk[end]
        disk[end] = '.'
    start += 1

silver = 0
for i, c in enumerate(disk):
    if c != '.':
        silver += i * int(c)
print(silver)

disk = orig_disk
back_end = len(disk) - 1
while back_end > 0:
    # get last file
    while disk[back_end] == '.':
        back_end -= 1
    
    front_end = back_end - 1
    while disk[front_end] == disk[back_end]:
        front_end -= 1
    front_end += 1
    back_end += 1

    # find space big enough starting from front
    front_start = 0
    flag_done = 0
    while front_start < len(disk):
        while disk[front_start] != '.':
            front_start += 1

        if front_start >= front_end:
            break
        
        back_start = front_start + 1
        while disk[back_start] == '.':
            back_start += 1

        if back_end - front_end <= back_start - front_start:
            for i in range(front_end, back_end):
                disk[front_start] = disk[i]
                front_start += 1
                disk[i] = '.'
            break
        else:
            front_start = back_start
    back_end = front_end - 1

gold = 0
for i, c in enumerate(disk):
    if c != '.':
        gold += i * int(c)
print(gold)