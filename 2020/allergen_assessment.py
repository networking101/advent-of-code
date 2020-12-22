from copy import deepcopy

with open("input.txt", "r") as fp:
    lines = [line.strip() for line in fp]

ingredients = set()
allergens = {}

notin = set()

# populate ingredients and allergens lists
for i in range(len(lines)):
    left, right = lines[i].split(" (")
    left = left.split()
    right = right[9:-1].split(", ")

    for j in left:
        ingredients.add(j)

    for j in right:
        if j not in allergens:
            allergens[j] = []
        for k in left:
            if k not in allergens[j]:
                allergens[j].append(k)

# if an ingreedient is not in an allergen, remove it
for i in range(len(lines)):
    left, right = lines[i].split(" (")
    left = left.split()
    right = right[9:-1].split(", ")

    for j in right:
        remlist = []
        for k in allergens[j]:
            if k not in left:
                remlist.append(k)
        for k in remlist:
            allergens[j].remove(k)

# find ingredients that aren't present at all
for i in ingredients:
    found = False
    for j in allergens:
        if i in allergens[j]:
            found = True
    if found == False:
        notin.add(i)

# count number of times non-allergens appear
cnt = 0
for i in range(len(lines)):
    left, right = lines[i].split(" (")
    left = left.split()
    for j in notin:
        if j in left:
            #input(j)
            cnt += 1

print("Silver:  " + str(cnt))

gold = {}
a = []
cont = False
while True:
    for i in allergens:
        if len(allergens[i]) == 1:
            cont = True
            t = allergens[i].pop(0)
            a.append(i)
            gold[i] = t

            ac = deepcopy(allergens)

            for j in allergens:
                if t in allergens[j]:
                    ac[j].remove(t)

            allergens = ac

            break
    if cont == False:
        break
    cont = False

a = sorted(a)

answer = ""
for i in a:
    answer += gold[i]
    answer += ","

print("Gold:  " + answer[:-1])