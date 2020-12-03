import json


with open("text.txt", "r") as fp:
    data = json.load(fp)

def recurse(data):
    temptot = 0
    itype = type(data)
    if itype is list:
        for i in data:
            temptot += recurse(i)
        return temptot
    if itype is dict:
        for i in data:
            if data[i] == "red":
                return 0
        for i in data:
            temptot += recurse(data[i])
        return temptot
    if itype is int:
        return data
    if itype is str:
        return 0
    else:
        print(itype)
        print(data)
        exit(0)
    return temptot

tot = 0

for i in data:
    tot += recurse(i)

print(tot)
