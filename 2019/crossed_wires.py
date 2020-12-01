one = [0,0,0]
two = [0,0,0]

placement1 = []
placement2 = []
placement1.append(list(one))
placement2.append(list(two))

count = 0

with open("input1.txt") as fp1:
    line1 = fp1.readline()
    list1 = line1.split(',')

    for i in list1:
        direction = i[:1]
        magnitude = i[1:]

        one[2] = count
        count += int(magnitude)

        if direction == 'R':
            one[0] += int(magnitude)
            placement1.append(list(one))
        if direction == 'L':
            one[0] -= int(magnitude)
            placement1.append(list(one))
        if direction == 'U':
            one[1] += int(magnitude)
            placement1.append(list(one))
        if direction == 'D':
            one[1] -= int(magnitude)
            placement1.append(list(one))
print(placement1)
count = 0

with open("input2.txt") as fp2:
    line2 = fp2.readline()
    list2 = line2.split(',')

    for i in list2:
        direction = i[:1]
        magnitude = i[1:]

        two[2] = count
        count += int(magnitude)

        if direction == 'R':
            two[0] += int(magnitude)
            placement2.append(list(two))
        if direction == 'L':
            two[0] -= int(magnitude)
            placement2.append(list(two))
        if direction == 'U':
            two[1] += int(magnitude)
            placement2.append(list(two))
        if direction == 'D':
            two[1] -= int(magnitude)
            placement2.append(list(two))

#print len(placement1)
#print len(placement2)

for i in range(len(placement1)):
    for j in range(len(placement2))[1:]:
        if ((i%2 == 1) and (j%2 == 0)):
            #print("One: " + str(placement1[i]) + "   Two: " + str(placement2[j]))
            first = placement1[i]
            first_prev = placement1[i-1]
            second = placement2[j]
            second_prev = placement2[j-1]
            if min(first[0],first_prev[0]) <= second[0] <= max(first[0],first_prev[0]):
                if min(second[1],second_prev[1]) <= first[1] <= max(second[1],second_prev[1]):
                    #if abs(first[1]) + abs(second[0]) == 709:
                    #    print first_prev
                    #    print first
                    #    print second_prev
                    #    print second
                    print(first[2] + abs(second[0]-first_prev[0]) + second[2] + abs(first[1]-second_prev[1]))

print("\n")

for i in range(len(placement1))[1:]:
    for j in range(len(placement2)):
        if ((i%2 == 0) and (j%2 == 1)):
            first = placement1[i]
            first_prev = placement1[i-1]
            second = placement2[j]
            second_prev = placement2[j-1]
            if min(second[0],second_prev[0]) <= first[0] <= max(second[0],second_prev[0]):
                if min(first[1],first_prev[1]) < second[1] <= max(first[1],first_prev[1]):
                    #print(abs(first[1]) + abs(second[0]))
                    print(second[2] + abs(first[0]-second_prev[0]) + first[2] + abs(second[1]-first_prev[1]))
                    

#for i in placement1[2::2]:
    #for j in placement2[2::]:

