with open ("text.txt", "r") as fp:
    lines = [line.strip() for line in fp]

sum = 0

for line in lines:
    dim = line.split("x")

    a = int(dim[0]) * int(dim[1])
    b = int(dim[1]) * int(dim[2])
    c = int(dim[2]) * int(dim[0])

    minimum = min(a, b, c)

    sum += minimum + 2*a + 2*b + 2*c

ribbon = 0

for line in lines:
    dim = [int(y) for y in line.split("x")]

    print(dim)

    bow = dim[0] * dim[1] * dim[2]

    a = min(dim)
    dim.remove(a)
    b = min(dim)

    wrap = 2*a + 2*b

    print(wrap)
    print(bow)
    print("")

    ribbon += bow + wrap

print(ribbon)
