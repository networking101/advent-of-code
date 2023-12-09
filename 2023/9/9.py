with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

lines = [[int(x) for x in y.split()] for y in lines]

count1 = 0
count2 = 0

for line in lines:
    all_seq = [line]

    old_seq = line
    while old_seq != [0]*len(old_seq):
        new_seq = []
        for i, x in enumerate(old_seq[:-1]):
            new_seq.append(old_seq[i+1] - x)
        all_seq.insert(0, new_seq)
        old_seq = new_seq

    # print(all_seq)
    

    for i, x in enumerate(all_seq[1:]):
        x.append(x[-1] + all_seq[i][-1])
        x.insert(0, x[0] - all_seq[i][0])
    
    count1 += all_seq[-1][-1]
    count2 += all_seq[-1][0]

print(count1)
print(count2)