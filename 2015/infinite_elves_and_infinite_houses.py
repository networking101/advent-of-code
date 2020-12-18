pi = 34000000

t = 0
i = 1
while t < pi:
    t += i * 10
    i *= 2

currmin = t
currhouse = int(i/2)
currsteps = [2]

"""
def checkpresents(testmin):
    tot = 0
    for i in range(1,testmin+1):
        if testmin % i == 0:
            tot += i * 10

    return(tot)

# This wasn't as complete as I intended but it works to get the answer.  I was trying to
# find the multiples of i and update "currsteps" to test all multiples, hence the j for
# loop
for i in range(3, 1000):
    for j in currsteps:
        t = j
        while t < i:
            t += t
        testhouse = int(currhouse/t) * i
        testmin = checkpresents(testhouse)
        if testmin > pi:
            print(i, j)
            print(testhouse)
            print(testmin)
            print("")
            currhouse = testhouse
            currmin = testmin

print("Silver:  " + str(currhouse))
"""

t = 0
i = 1
while t < pi:
    t += i * 11
    i *= 2

    raw_input(t)