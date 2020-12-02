import json

dicttype = type({})
listtype = type([])

with open("text.txt", "r") as fp:
    data = json.load(fp)

def recurse(data):
    for i in data:
        itype = type(i)
        if itype == listtype:
            print("list")
        if itype == dicttype:
            print("dict")
    return 0

tot = recurse(data)

print(tot)
