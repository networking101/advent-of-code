class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def main():

    mylist = []

    with open('input.txt') as fp:
        line = fp.readline()
        while line:
            mylist.append(line.rstrip())
            line = fp.readline()

    fl = []
    
    for i in mylist:
        a, b = i.split(')')
        test_list_set = set(fl)
        if a not in test_list_set:
            fl.append(a)
        if b not in test_list_set:
            fl.append(b)

    ol = []

    for i in fl:
        node = Node(i)
        ol.append(node)

    for i in mylist:
        com = i[:3]
        orbiter = i[4:]
        for j in ol:
            if j.val == orbiter:
                for k in ol:
                    if k.val == com:
                        j.next = k

    count = 0
    youcount = 0
    santacount = 0
    setlist = []
    you = []
    santa = []

    for i in ol:
        current = i
        while current.next:
            current = current.next
            count += 1
        if i.val == "YOU":
            current = i
            while current.next:
                current = current.next
                setlist.append(current.val)
                you.append(current.val)
                if current.val != 'TZF':
                    youcount += 1
                else:
                    break
        if i.val == "SAN":
            current = i
            while current.next:
                current = current.next
                setlist.append(current.val)
                santa.append(current.val)
                if current.val != 'TZF':
                    santacount += 1
                else:
                    break

    print "\nDistance to Santa: " + str(youcount+santacount)

    my_set = set(setlist)

    print "Count: " + str(count)


main()
