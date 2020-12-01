import copy

nl1 = []
g1 = []
with open('input.txt') as fp:
    line = fp.readline()
    while line:
        n1 = []
        n,g = line.rstrip().split(" => ")
        nl1.append(n)
        g1.append(g)
        line = fp.readline()


wl = []
need = []
for i in nl1:
    i = i.split(", ")
    nl2 = []
    for j in i:
        j = j.split(" ")
        wl.append(j[1])
        nl2.append(j)
    need.append(nl2)

nded = {'ORE':0}
get = []
for i in g1:
    i = i.split(" ")
    get.append(i)
    if i[1] == 'FUEL':
        nded[i[1]] = 1
    else:
        nded[i[1]] = 0

    #for i in needed:
    #    print i + "  " + str(needed[i])


def cost(fuel):
    needed = copy.deepcopy(nded)
    whats_left = copy.deepcopy(wl)
    needed['FUEL'] = fuel
    queue = ['FUEL']
    while queue:
    #for a in range(3):
        cur = queue.pop(0)
        #print "First cur: " + cur
        if cur in whats_left:
            queue.append(cur)
            continue            
        if cur == 'ORE':
            continue
        #print "Second cur: " + cur
        for i in range(len(get)):
            if get[i][1] == cur:
                quant = 0
                temp = needed[cur] + int(get[i][0])
                if temp > 0:
                    if needed[cur]<0:
                        quant = 1
                    else:
                        quant = int(needed[cur]/int(get[i][0]))
                        if needed[cur]%int(get[i][0]) > 0:
                            quant += 1
                needed[cur] -= quant * int(get[i][0])
                for j in need[i]:
                    whats_left.remove(j[1])
                    temp = quant * int(j[0])
                    needed[j[1]] += temp
                    if j[1] not in queue:
                        queue.append(j[1])

    print "NEEDED: " + str(needed['ORE'])
    return needed['ORE']

def main():

    """
    lo = 2100000
    hi = 2300000
    while lo < hi:
        mid = (lo+hi)//2
        print "MID: " + str(mid)
        if cost(mid) <= int(1e12):
            print "LOW"
            lo = mid
        else:
            print "HIGH"
            hi = mid-1
    print hi
    """

    print cost(2144702)
    print cost(2144703)
    

main()

















