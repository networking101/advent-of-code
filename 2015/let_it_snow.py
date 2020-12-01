row = 3010
column = 3019


maxrow = row + column - 1

count = 1
tot = 1
for i in range(1, maxrow):
    tot += count
    count += 1


tot += column - 1

print(tot)

code = 20151125
multiple = 252533
modulus = 33554393

print("")
print(code)
for j in range(1, tot):
    #if j == 5:
    #    exit(0)
    code = (code * multiple) % modulus

print("")
print(code)
